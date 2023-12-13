import os
import re
import csv
import git
import json
import time
import psutil
import shutil
import base64
import hashlib
import jsonschema
import importlib_resources

from os import linesep
from pathlib import Path
from datetime import datetime

from .config import config

################################## hash ###################################


def compute_sha256_hash(file_path):
    """
    Computes the SHA-256 hash of a file.
    """
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


################################## ssh ####################################


def check_ssh_key_pair():
    """
    Checks the existence of SSH key pairs in the user's SSH directory.

    Returns:
        str or None: The type of the existing key pair ('id_ed25519' or 'id_rsa') if found,
        or None if no key pair is found.
    """
    ssh_dir = Path("~/.ssh").expanduser()

    if (
        Path(ssh_dir, "citros_ed25519").exists()
        and Path(ssh_dir, "citros_ed25519.pub").exists()
    ):
        return "citros_ed25519"
    elif (
        Path(ssh_dir, "citros_rsa").exists()
        and Path(ssh_dir, "citros_rsa.pub").exists()
    ):
        return "citros_rsa"
    else:
        return None


############################## Network ####################################


def suppress_ros_lan_traffic():
    """
    avoid seeing ros traffic from other simulations on the same LAN.
    """
    if "ROS_DOMAIN_ID" not in os.environ:
        # anything between 0 and 101
        os.environ["ROS_DOMAIN_ID"] = str(config.ROS_DOMAIN_ID)


########################### file and format utils #########################


def is_valid_file_name(name: str, log):
    # check for empty name, invalid characters and trailing periods or spaces.
    if (
        not name
        or re.search(r'[\\/*?:,;"\'<>|(){}\t\r\n]', name)
        or name[-1] == "."
        or name[-1] == " "
    ):
        log.warning(f"invalid file or folder name: {name}")
        return False

    return True


def get_foramtted_datetime():
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d-%H-%M-%S")

    # Use only the last two digits of the year
    formatted = formatted[2:]

    return formatted


def str_to_bool(s):
    if s == "True":
        return True
    elif s == "False":
        return False
    else:
        raise ValueError(f"Cannot convert {s} to a bool")


# files
def get_data_file_path(data_package, filename):
    if data_package not in [
        "schemas",
        "defaults",
        "scripts",
        "sample_code",
        "markdown",
        "misc",
    ]:
        raise ValueError(f"data package '{data_package}' is unsupported.")

    return importlib_resources.files(f"data.{data_package}").joinpath(filename)


def copy_files(file_paths, target_directory, log, create_dir=False):
    if create_dir:
        # Create the target directory if it does not exist
        os.makedirs(target_directory, exist_ok=True)

    for file_path in file_paths:
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_directory)
        else:
            log.error(f"copy_files: File does not exist: {file_path}")


def copy_subdir_files(source_directory, target_directory, log):
    """
    Copies files from the source to the target, if and only if the target has the
    same directory structure as the source, for any specific file.
    """
    if not os.path.exists(source_directory):
        log.error(f"Source directory does not exist: {source_directory}")
        return

    # Iterate through the subdirectories in the source directory
    for root, subdirs, files in os.walk(source_directory):
        relative_path = os.path.relpath(root, source_directory)
        target_subdir = os.path.join(target_directory, relative_path)

        # Check if the subdirectory exists in the target directory
        if os.path.exists(target_subdir):
            # List of file paths in the current subdirectory
            file_paths = [os.path.join(root, file) for file in files]
            copy_files(file_paths, target_subdir)
        else:
            log.error(f"Target subdirectory does not exist: {target_subdir}")


def get_last_created_file(folder_path, dirs=False):
    folder = Path(folder_path)
    items = []

    if dirs:
        items = [f for f in folder.iterdir() if f.is_dir()]
    else:
        items = [f for f in folder.iterdir() if f.is_file()]

    if not items:
        return None

    # Sort files by creation time
    items.sort(key=lambda x: x.stat().st_ctime)

    # The last item in the list is the most recently created file
    return items[-1]


def rename_file(file_path, new_name):
    file = Path(file_path)

    # Construct the new path
    new_file_path = file.parent / new_name

    # Rename the file
    file.rename(new_file_path)


def find_ancestor_with_name(path, name):
    """
    Checks all ancestors of the given path to see if one of them has the specified name.

    :param path: The path to start from.
    :param name: The name of the ancestor directory to find.
    :return: The Path of the ancestor directory if found, else None.
    """
    path = Path(path)
    for ancestor in path.parents:
        if ancestor.name == name:
            return ancestor
    return None


########################### git #########################


def update_git_exclude(repo_path, pattern, log):
    gitexclude_path = Path(repo_path, ".git/info/exclude")
    if not gitexclude_path.exists():
        log.warning(f"Could not find git exclude in repo {repo_path}")
        return

    def normalize_pattern(pattern: str):
        # Remove any trailing slash or asterisk
        return pattern.rstrip("*/")

    normalized_pattern = normalize_pattern(pattern)

    with open(gitexclude_path, "r+") as gitexclude:
        lines = gitexclude.readlines()
        for line in lines:
            if normalize_pattern(line.strip()) == normalized_pattern:
                # pattern already exists.
                return

        # Pattern not found, append it
        gitexclude.write(linesep + pattern + linesep)
        print(f"Pattern `{pattern}` appended to {gitexclude_path}")


def get_git_info(self, repo_path="."):
    try:
        repo = git.Repo(repo_path)
    except:
        return None, None

    try:
        latest_commit_hash = repo.head.commit.hexsha
    except:
        # empty repo (https://github.com/lulav/citros_cli/issues/51)
        latest_commit_hash = None

    current_branch_name = repo.active_branch.name

    return latest_commit_hash, current_branch_name


def get_user_git_info(self, dir):
    commit, branch = self.get_git_info(dir)
    return commit, branch


########################### Validation #########################


def _has_files(dir: Path):
    return any(p.is_file() for p in dir.iterdir())


def _validate_json_file(json_filepath, schema_filepath, log):
    with open(json_filepath, "r") as file:
        data = json.load(file)

    with open(schema_filepath, "r") as file:
        schema = json.load(file)

    try:
        # in order to support future changes in schemas (i.e. additional fields),
        # we merge with the default, so any new fields will be added to the user's
        # file and the validation will succeed.
        merged_dict = data  # {**default, **data}
        jsonschema.validate(instance=merged_dict, schema=schema)
        # print(f"{json_filepath} is valid.")

        if merged_dict != data:
            with open(json_filepath, "w") as file:
                file.write(json.dumps(merged_dict, indent=4))

        return True
    except jsonschema.exceptions.ValidationError as ve:
        log.error(f"{json_filepath} is not valid:{linesep}{ve}")
        return False


def validate_file(file_path: Path, schema_file, log):
    if file_path.is_file():
        with get_data_file_path("schemas", schema_file) as schema_path:
            return _validate_json_file(str(file_path), schema_path, log)
    else:
        return False


def validate_dir(path: Path, schema_file, log):
    if path.is_dir() and _has_files(path):
        with get_data_file_path("schemas", schema_file) as schema_path:
            for file in path.iterdir():
                if str(file).endswith("json"):
                    if not _validate_json_file(file, schema_path, log):
                        return False
            return True
    else:
        # empty folder is valid
        return True
