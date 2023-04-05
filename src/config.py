import os

from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN", "")
openai_api_key = os.getenv("OPENAI_API_KEY", "")
allowed_telegram_users = os.getenv("ALLOWED_USERS", "").split(",")
if allowed_telegram_users != [""]:
    allowed_telegram_users = list(map(int, allowed_telegram_users))
answer_on_mention = False
