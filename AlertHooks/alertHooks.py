from platformdirs import user_config_path
from discord_webhook import DiscordWebhook
from requests import Response
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import json
import sys

APP_NAME="alertHooks"
APP_AUTHOR="MycoG"

class AlertHooks():
    def __init__(self):
        self.config_dir = user_config_path(APP_NAME, APP_AUTHOR)
        self.config_path = self.config_dir / "config.json"

        pw = os.environ.get("AHOOKS_PW")
        if pw is None:
            print("No Password provided. Please set AHOOKS_PW env variable!", file=sys.stderr)
            quit(1)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"alertHooks",
            iterations=10_000
        )
        key = base64.urlsafe_b64encode(kdf.derive(pw.encode()))
        self._f = Fernet(key)
        self.config = {}

        if not self.config_dir.exists():
            self.config_dir.mkdir()
        elif not self.config_path.exists():
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
        print(list(self.config.keys()))

    def add_alias(self, alias:str, url:str):
        """Add alias to config"""
        hashed:bytes = self._f.encrypt(url.encode())
        self.config[alias] = hashed.decode()
        self._save_config()

    def rm_alias(self, alias:str):
        """Remove alias from config"""
        if self._check_alias(alias):
            self.config.pop(alias)
            self._save_config()
        else:
            print(f"error: alias \"{alias}\" is not a present alias!", file=sys.stderr)
            quit(1)

    def send(self, alias:str, msg:str):
        """Send msg to alias"""
        if self._check_alias(alias):
            url:str = self.config[alias]

            try:
                unhashed = self._f.decrypt(url.encode())
            except InvalidToken:
                print("Invalid AHOOKS_PW env variable! please check!", file=sys.stderr)
                quit(1)

            webhook = DiscordWebhook(url=unhashed, content=msg)
            response:Response = webhook.execute()
            if response.ok:
                quit(0)
            else:
                print(f"error: response status code {response.status_code}", file=sys.stderr)
                quit(1)
        else:
            print(f"error: alias \"{alias}\" is not a present alias!", file=sys.stderr)
            quit(1)