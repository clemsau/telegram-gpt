# telegram-gpt

Implementation of a telegram bot to use with the different openai APIs

## Deployment

You have multiple options to deploy your bot:
- Run the application on your own server
- Run the application on a PaaS

### Running the application on a PaaS

#### Using Render (free)

1. Login to [Render](https://render.com) and create a new Web Service using this repository
2. Use the following options:
   - branch: `main`
   - runtime: `Python 3`
   - build command: `pip install -r requirements.txt`
   - start command: `python src/bot.py`
3. Click on the `Advanced` Option to add the following environment variables:
   - `TELEGRAM_TOKEN`
   - `OPENAI_API_KEY`
   - `ALLOWED_USERS`
   - `PYTHON_VERSION` use `3.10.10`