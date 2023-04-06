# telegram-gpt

A self-hosted telegram bot to use the different openai APIs.

## Features

- GPT-3.5 chatbot.
- Handle voice messages
- (Option) Response on mentions, for a better integration in group chats.

## Usage 

1. Set your environment variables

   You have multiple options:

   1. create a `.env` file in the `/src` folder with the following content:
   
       ```bash
      TELEGRAM_TOKEN="your_telegram_token"
      OPENAI_API_KEY="your_openai_api_key" 
      ALLOWED_USERS="allowed_user1,allowed_user2"
       ```

      You can also fill the `.env.example` file and rename it to `.env`.

   2. set the environment variables in your shell:

       ```bash
      export OPENAI_API_KEY="your_telegram_token"
      export TELEGRAM_TOKEN="your_openai_api_key"
      export ALLOWED_USERS="allowed_user1,allowed_user2"
       ```

2. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

3. Run the bot

    ```bash
    python src/bot.py
    ```

## Deployment

You have multiple solutions to deploy this bot. The simplest solution is to run it on a bare metal server. Since this application run on very low resources, you can run it on a raspberry pi or a small vps (e.g: Digital Ocean 4$/month droplet).
