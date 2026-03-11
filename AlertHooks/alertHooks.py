from platformdirs import user_config_path
import json

APP_NAME="alertHooks"
APP_AUTHOR="MycoG"

class AlertHooks():
    def __init__(self):
        self.config_dir = user_config_path(APP_NAME, APP_AUTHOR)
        self.config_path = self.config_dir / "config.json"
        self.config = {}

        if not self.config_dir.exists():
            self._create_new_config()
        return
    
    def _check_alias(alias:str):
        """Check if alias is valid"""
        pass

    def _create_new_config(self):
        self.config_dir.mkdir()
        with open(self.config_path, 'w') as f:
            f.write(json.dumps(self.config))


    def list_config(self):
        """Lists config directory and aliases"""
        print(f"config dir: {self.config_dir}")
        # TODO: load json and 

    def add_alias(alias:str, url:str):
        """Add alias to config"""
        pass

    def rm_alias(alias:str):
        """Remove alias from config"""
        pass

    def send(alias:str, msg:str):
        """Send msg to alias"""
        pass

    

    