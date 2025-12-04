from threading import Thread
from flask import Flask
import os
import barber_bot   # this imports your main Telegram bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_bot():
    barber_bot.main()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
