# telegram-gpt

A self-hosted telegram bot to use the different openai APIs.

## Features

- GPT-3.5 chatbot.
- (Option) Response on mentions, for a better integration in group chats.

## Usage 

1. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

2. Run the bot

    ```bash
    python src/bot.py
    ```

## Deployment

You have multiple solutions to deploy this bot. The simplest solution is to run it on a bare metal server. Since this application run on very low resources, you can run it on a raspberry pi or a small vps (e.g: Digital Ocean 4$/month droplet).
