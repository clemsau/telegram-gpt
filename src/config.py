from pathlib import Path

import yaml

config_dir = Path(__file__).parent.parent / "config"

with open(config_dir / "config.yml", "r") as f:
    config = yaml.safe_load(f)

telegram_token = config["telegram_token"]
openai_api_key = config["openai_api_key"]
allowed_telegram_users = config["allowed_telegram_users"]
answer_on_mention = False
