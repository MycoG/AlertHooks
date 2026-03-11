from platformdirs import user_config_path
from discord_webhook import DiscordWebhook
from requests import Response
import json

APP_NAME="alertHooks"
APP_AUTHOR="MycoG"

class AlertHooks():
    def __init__(self):
        self.config_dir = user_config_path(APP_NAME, APP_AUTHOR)
        self.config_path = self.config_dir / "config.json"
        self.config = {}

        if not self.config_dir.exists():
            self.config_dir.mkdir()
            self._save_config()
        else:
            self._load_config()
        return
    
    def _check_alias(self, alias:str) -> bool:
        """Check if alias is valid"""
        if alias in self.config:
            return True
        else:
            return False

    def _save_config(self):
        with open(self.config_path, 'w') as f:
            f.write(json.dumps(self.config))

    def _load_config(self):
        with open(self.config_path, 'r') as f:
            self.config = json.loads(f.read())
                
 
    def list_config(self):
        """Lists config directory and aliases"""
        print(f"config dir: {self.config_dir}")
        print("alias\turl")
        if self.config != {}:
            for k,v in self.config.items():
                print(f"\"{k}\"\t\"{v}\"")
        else:
            print("(None)\t(None)")

    def add_alias(self, alias:str, url:str):
        """Add alias to config"""
        self.config[alias] = url
        self._save_config()

    def rm_alias(self, alias:str):
        """Remove alias from config"""
        if self._check_alias(alias):
            self.config.pop(alias)
            self._save_config()
        else:
            print(f"error: alias \"{alias}\" is not a present alias!")
            quit(1)

    def send(self, alias:str, msg:str):
        """Send msg to alias"""
        if self._check_alias(alias):
            url = self.config[alias]
            webhook = DiscordWebhook(url=url, content=msg)
            response:Response = webhook.execute()
            if response.ok:
                quit(0)
            else:
                print(f"error: response status code {response.status_code}")
                quit(1)
        else:
            print(f"error: alias \"{alias}\" is not a present alias!")
            quit(1)