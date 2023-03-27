from pathlib import Path

import yaml

config_dir = Path(__file__).parent.parent / "config"

with open(config_dir / "config.yaml", "r") as f:
    config = yaml.safe_load(f)

telegram_token = config["telegram_token"]
openai_api_key = config["openai_api_key"]
