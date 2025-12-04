# web.py - Render webhook server

from flask import Flask, request
from threading import Thread
import barber_bot
import os
import json

app = Flask(__name__)

# Render root page
@app.route("/")
def home():
    return "Barber Bot is running!", 200


# Telegram webhook receiver
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = request.get_json()

        if update:
            # Pass update to bot
            barber_bot.application.update_queue.put_nowait(update)

        return "OK", 200

    except Exception as e:
        print("Webhook error:", e)
        return "Error", 500


def run_bot():
    """Start the Telegram bot (without polling)."""
    barber_bot.main_webhook()   # You MUST add this function inside barber_bot.py


if __name__ == "__main__":
    # Start bot thread
    Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
