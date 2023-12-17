import json
import uuid

from pathlib import Path

from .citros_obj import CitrosObj

from .utils import validate_file


class Settings(CitrosObj):
    """Object representing .citros/settings.json file."""

    ###################
    ##### private #####
    ###################

    # overriding
    def _validate(self):
        """Validate simulation.json file."""

        success = validate_file(self.path(), "schema_settings.json", self.log)

        return success

    # overriding
    def _new(self):
        path = self.path()

        # avoid overwrite
        if path.exists():
            self._load()
            # return

        Path(self.root).mkdir(parents=True, exist_ok=True)

        default = {
            "name": "default_settings",
            "force_message": "True",
            "force_batch_name": "True",
        }
        self.data = {**default, **self.data}

        self._save()
