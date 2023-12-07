
import threading
import base64
import os
import stat
import psutil
import subprocess
import re
import shutil
import threading
import time
import csv
import hashlib
import platform
import requests
import importlib_resources
from pathlib import Path
from datetime import datetime

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ed25519
from cryptography.hazmat.backends import default_backend as crypto_default_backend


class citros_utils():
    def __init__(self, citros):
        self.citros = citros      
        self.log = citros.log

        self.stop_flag = threading.Event()
        self.thread = None

    ########################## encode/decode base64 ###########################
    
    def encode64(self, original_string : str):
        """
        Encodes a given string into base64.
        """
        encoded_string = base64.b64encode(original_string.encode()).decode()
        return encoded_string
    

    def decode64(self, encoded_string : str):
        """
        Decodes a given base64 string back to its original form.
        """
        decoded_string = base64.b64decode(encoded_string).decode()
        return decoded_string

    ################################## hash ###################################

    def compute_sha256_hash(self, file_path):
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
    
    def check_ssh_key_pair(self):
        """
        Checks the existence of SSH key pairs in the user's SSH directory.

        Returns:
            str or None: The type of the existing key pair ('id_ed25519' or 'id_rsa') if found, 
            or None if no key pair is found.
        """
        ssh_dir = Path('~/.ssh').expanduser()

        if Path(ssh_dir, 'citros_ed25519').exists() and \
           Path(ssh_dir, 'citros_ed25519.pub').exists():
            return 'citros_ed25519'
        elif Path(ssh_dir, 'citros_rsa').exists() and \
             Path(ssh_dir, 'citros_rsa.pub').exists():
            return 'citros_rsa'
        else:
            return None


    def create_ssh_key_pair(self, key_type='ed25519', key_comment=""):
        """
        Creates an SSH key pair of either RSA or Ed25519 type.
        Creates or updates ssh config file accordingly.
        Args:
            key_type (str, optional): The type of SSH key pair to create, either 'rsa' or 'ed25519'. 
                Defaults to 'ed25519'.
            key_comment (str, optional): Comment to append to the public key. If not provided, 
                the Citros user's email is used. Defaults to an empty string.

        Returns:
            str: The public key in OpenSSH format with the comment appended.

        Raises:
            ValueError: If an unsupported key_type is provided.
        """
        if not key_comment:
            key_comment = self.citros.get_username_and_hostname()

        rsa_name = 'citros_rsa'
        ed_name = 'citros_ed25519'

        if key_type == 'rsa':
            key = rsa.generate_private_key(
                backend=crypto_default_backend(),
                public_exponent=65537,
                key_size=2048
            )
            private_key_path = Path('~/.ssh', rsa_name).expanduser()
            public_key_path = Path('~/.ssh', f'{rsa_name}.pub').expanduser()
        elif key_type == 'ed25519':
            key = ed25519.Ed25519PrivateKey.generate()
            private_key_path = Path('~/.ssh', ed_name).expanduser()
            public_key_path = Path('~/.ssh', f'{ed_name}.pub').expanduser()
        else:
            raise ValueError("Invalid key_type! Choose either 'rsa' or 'ed25519'.")

        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.OpenSSH,
            crypto_serialization.NoEncryption()
        )

        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )

        ssh_dir = os.path.expanduser('~/.ssh')
        os.makedirs(ssh_dir, exist_ok=True)

        # Write the private key to a file
        with open(private_key_path, 'wb') as priv_file:
            priv_file.write(private_key)

        os.chmod(private_key_path, stat.S_IRUSR | stat.S_IWUSR)

        # Write the public key to a file
        with open(public_key_path, 'wb') as pub_file:
            pub_file.write(public_key + f' {key_comment}'.encode())

        # Create or update ssh config file
        file_name = ed_name if key_type == 'ed25519' else rsa_name
        self.setup_ssh_config(self.citros.CITROS_GIT_DOMAIN, file_name)

        return public_key.decode() + f' {key_comment}'
    

    def setup_ssh_config(self, host_name, file_name):
        """
        Creates a `config` file under the user's .ssh dir (if it doesn't already exit),
        and appends the Host/IdentityFile lines with the given host and key file names
        (or overwrites if the Host exists but the IdentityFile is different).
        """
        config_file_path = os.path.expanduser("~/.ssh/config")
        
        # Check if config file exists, create if not
        if not os.path.exists(config_file_path):
            open(config_file_path, 'w').close()
        
        # Read content of the config file
        with open(config_file_path, 'r') as file:
            lines = file.readlines()

        # Construct the strings to match
        host_string = f"Host {host_name}\n"
        identity_string = f"\tIdentityFile ~/.ssh/{file_name}\n"

        # Check if the hostname exists in the file
        if host_string in lines:
            host_index = lines.index(host_string)
            # Check if the next line has the correct filename
            if lines[host_index+1] != identity_string:
                # Overwrite filename if different
                lines[host_index+1] = identity_string
        else:
            # Append host and filename if hostname not in file
            lines.extend([host_string, identity_string])

        # Write back to the config file
        with open(config_file_path, 'w') as file:
            file.writelines(lines)
    

    def check_ssh_key_uploaded(self, key_file_name="", try_all_keys=False):
        """
        Checks if an SSH key has been uploaded to the 'git.citros.io' server.
        
        Args:
            key_file_name (str): The file name of the private key in the user's SSH directory.

        Returns:
            bool: True if the SSH key has been uploaded, False otherwise.

        Raises:
            ValueError: If the key file does not exist in the SSH directory or the file name 
            does not include 'ed25519' or 'rsa'.
        """
        hostname = self.citros.CITROS_GIT_DOMAIN
        username = self.citros.CITROS_GIT_USER

        private_key_path = ""

        if key_file_name == "":
            if try_all_keys:
                # no need for a specific key - just try all existing keys.
                pass
            else:
                raise ValueError(f"empty key file name")
        else:
            ssh_dir = os.path.expanduser('~/.ssh')
            private_key_path = os.path.join(ssh_dir, key_file_name)

            if not os.path.exists(private_key_path):
                self.log.error(f"ssh key file {key_file_name} does not exist in {ssh_dir}.")
                raise ValueError(f"{key_file_name}")

            if 'ed25519' not in key_file_name and 'rsa' not in key_file_name:
                self.log.error(f"ssh key file name must include `ed25519` or `rsa`. The name {key_file_name} is invalid.")
                raise ValueError(f"{key_file_name}")

        ssh_command = ""
        if private_key_path != "":
            self.log.debug(f"using key {private_key_path}")
            ssh_command = ['ssh', '-i', private_key_path, '-o', 'StrictHostKeyChecking=no', f'{username}@{hostname}', 'info']
        else:
            self.log.debug("no key given, trying all keys.")
            ssh_command = ['ssh', '-o', 'StrictHostKeyChecking=no', f'{username}@{hostname}', 'info']

        try:
            output = subprocess.check_output(ssh_command, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output

        self.log.debug(f"ssh output = {output}")

        if 'Permission denied' in output: 
            return False    # The key has not been uploaded yet
        else:
            return True
        

    def is_repo_ready(self, slug, proj_name):
        hostname = self.citros.CITROS_GIT_DOMAIN
        username = self.citros.CITROS_GIT_USER

        ssh_command = ['ssh', '-o', 'StrictHostKeyChecking=no', f'{username}@{hostname}', 'info']
        
        try:
            output = subprocess.check_output(ssh_command, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output

        expected = f"{slug}/{proj_name}"

        self.log.debug(f"SSH info output:\n[{output}]\n")

        return expected in output
    

    def is_ssh_agent_running(self):
        plat = platform.system()
        if plat == 'Windows':
            try:
                subprocess.run(['Get-Service', 'ssh-agent'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return True
            except subprocess.CalledProcessError:
                return False
        elif plat == 'Linux' or plat == 'Darwin':
            # Note: The gnome-keyring-daemon process (GNOME keyring daemon) runs by default on modern Linux 
            # distributions (e.g. Ubuntu). This daemon provides several services, including acting 
            # as an SSH agent. While gnome-keyring-daemon can provide SSH agent functionality,
            # it is a separate process from `ssh-agent`. Thus, `pgrep ssh-agent` will only return a PID if the
            # actual `ssh-agent` process is running, regardless of the status of gnome-keyring-daemon.
            ssh_agent_result = subprocess.run(['pgrep', 'ssh-agent'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Check for gnome-keyring-daemon process
            gnome_keyring_result = subprocess.run(['pgrep', '-f', 'gnome-keyring-daemon'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # If either process is running, return True
            return ssh_agent_result.returncode == 0 or gnome_keyring_result.returncode == 0

        else:
            raise ValueError(f"Unsupported operating system: [{plat}]")


    def start_ssh_agent(self):
        try:
            plat = platform.system()
            if plat == 'Windows':
                if not os.geteuid() == 0:
                    raise ValueError("Please run the command as administrator.")
                
                subprocess.run(['Set-Service', 'ssh-agent', '-StartupType', 'Automatic'], check=True)
                subprocess.run(['Start-Service', 'ssh-agent'], check=True)
                subprocess.run(['Get-Service', 'ssh-agent'], check=True)
            
            elif plat == 'Linux' or plat == 'Darwin':
                # start the service for this session
                os.system('eval "$(ssh-agent -s)"')
                
                # edit the user's profile so next time it will start automatically
                script_text = ""
                with self.get_data_file_path('scripts', 'ssh_agent_on_login.sh') as script:
                    script_text = script.read_text()

                profiles = ['~/.bashrc' , '~/.bash_profile', '~/.zprofile']
                at_least_one = False

                for profile in profiles:
                    profile_path = Path(profile).expanduser()
                    if profile_path.exists():
                        at_least_one = True
                        with open(profile_path, 'a') as f:
                            f.write(script_text)

                if not at_least_one:
                    self.log.error(f"Non of the following shell profiles were found: {profiles} ")
                    self.citros.print("Failed setting up the user's profile for ssh-agent. See logfile for details.", color='red')

        except Exception as ex:
            self.log.error(f"Failed to start ssh agent.")
            raise ex
            

    def add_ssh_key_and_agent(self, key_path):
        try:
            if not self.is_ssh_agent_running():
                self.start_ssh_agent()
            
            # Try adding the SSH key
            subprocess.run(['ssh-add', str(key_path)], check=True)
        except subprocess.CalledProcessError as ex:
            self.log.error(f"Failed adding ssh key.")
            self.citros.handle_exceptions(ex, exit=True)
    

    ############################## Network ####################################

    def suppress_ros_lan_traffic(self):
        """
        avoid seeing ros traffic from other simulations on the same LAN.
        """
        if 'ROS_DOMAIN_ID' not in os.environ:
            # anything between 0 and 101
            os.environ['ROS_DOMAIN_ID'] = '42'


    def is_connected(self):
        try:
            response = requests.get(self.citros.CITROS_NETWORK_CHECK_URL, timeout=5)
            
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        return False

    ############################# stats sampling ##############################

    def _sample_system_statistics(self):
        cpu_usage = psutil.cpu_percent()

        memory_info = psutil.virtual_memory()

        total_memory = memory_info.total
        available_memory = memory_info.available
        used_memory = memory_info.used
        memory_percent = memory_info.percent

        return cpu_usage, total_memory, available_memory, used_memory, memory_percent
    

    def _write_statistics_to_file(self, file_name):
        with open(file_name, 'a') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(self._sample_system_statistics())


    def _stats_collection_loop(self, interval, file_name):
        while not self.stop_flag.is_set():
            self._write_statistics_to_file(file_name)
            time.sleep(interval)


    def start_collecting_stats(self, interval, file_name):
        with open(file_name, 'w') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['cpu usage (%)', 'total memory', 'available memory', 'used memory', 'memory usage (%)'])

        self.stop_flag.clear()
        self.thread = threading.Thread(target=self._stats_collection_loop, args=(interval, file_name))
        self.thread.start()


    def stop_collecting_stats(self):
        if self.thread is not None:
            self.stop_flag.set()
            self.thread.join()

    ########################### file and format utils ######################### 

    def get_data_file_path(self, data_package,  filename):
        if data_package not in ['schemas', 'defaults', 'scripts', 'sample_code', 'markdown', 'misc']:
            raise ValueError(f"data package '{data_package}' is unsupported.")
        
        return importlib_resources.files(f'data.{data_package}').joinpath(filename)


    def is_valid_file_name(self, name : str):
        # check for empty name, invalid characters and trailing periods or spaces.
        if not name or \
           re.search(r'[\\/*?:,;"\'<>|(){}\t\r\n]', name) or \
           name[-1] == '.' or name[-1] == ' ':
            self.log.warning(f"invalid file or folder name: {name}")
            return False

        return True


    def get_foramtted_datetime(self):
        now = datetime.now()
        formatted = now.strftime('%Y-%m-%d-%H-%M-%S')

        # Use only the last two digits of the year
        formatted = formatted[2:]
        
        return formatted
    

    def copy_files(self, file_paths, target_directory, create_dir=False):
        if create_dir:
            # Create the target directory if it does not exist
            os.makedirs(target_directory, exist_ok=True)

        for file_path in file_paths:
            if os.path.isfile(file_path):
                shutil.copy(file_path, target_directory)
            else:
                self.log.error(f"copy_files: File does not exist: {file_path}")

    
    def copy_subdir_files(self, source_directory, target_directory):
        """
        Copies files from the source to the target, if and only if the target has the 
        same directory structure as the source, for any specific file.
        """
        if not os.path.exists(source_directory):
            self.log.error(f"Source directory does not exist: {source_directory}")
            return

        # Iterate through the subdirectories in the source directory
        for root, subdirs, files in os.walk(source_directory):
            relative_path = os.path.relpath(root, source_directory)
            target_subdir = os.path.join(target_directory, relative_path)

            # Check if the subdirectory exists in the target directory
            if os.path.exists(target_subdir):
                # List of file paths in the current subdirectory
                file_paths = [os.path.join(root, file) for file in files]
                self.copy_files(file_paths, target_subdir)
            else:
                self.log.error(f"Target subdirectory does not exist: {target_subdir}")


    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False
        else:
            raise ValueError(f"Cannot convert {s} to a bool")
        

    def get_last_created_file(self, folder_path, dirs=False):
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
    

    def rename_file(self, file_path, new_name):
        file = Path(file_path)
        
        # Construct the new path
        new_file_path = file.parent / new_name
        
        # Rename the file
        file.rename(new_file_path)


    def find_ancestor_with_name(self, path, name):
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
    
################################ misc #########################################

    def is_linux_amd64(self):
        # Check OS
        if not os.name == 'posix' or 'linux' not in platform.system().lower():
            return False
        
        # Check architecture
        machine = platform.machine()
        if machine not in ['x86_64', 'AMD64']:
            return False
        
        return True

###############################################################################

# def setInterval(interval):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             stopped = threading.Event()

#             def loop():  # executed in another thread
#                 while not stopped.wait(interval):  # until stopped
#                     function(*args, **kwargs)

#             t = threading.Thread(target=loop)
#             t.daemon = True  # stop if the program exits
#             t.start()
#             return stopped
#         return wrapper
#     return decorator
