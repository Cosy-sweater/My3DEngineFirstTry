import tomli
import tomli_w
from box import Box
import paths


class Settings(Box):
    def __init__(self, *args, settings_path=paths.get_resource_path(), **kwargs):
        super().__init__(*args, **kwargs)
        self._file_path = settings_path
        self.reload_settings()

    def reload_settings(self):
        with open(self._file_path + r"\settings.toml", "rb") as f:
            data = tomli.load(f)
        super().__init__(data)

