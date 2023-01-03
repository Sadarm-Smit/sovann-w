import logging
import os
from telegram.ext import *

# Enable logging
logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO)

# Set the TOKEN environment variable
TOKEN = "5797761405:AAEm1zI2gnQVx4P97rH7-mhB8VMdWH7ulbY"

# Define a list of responses
responses = [
  "Hello!",
  "How are you?",
  "I'm doing well, thank you.",
  "What do you like to do?",
  "I like to chat and learn new things.",
]


# Define a function to handle the /start command
def start(update, context):
  update.message.reply_text(
    "Hi! I'm a chat bot. Type /help for a list of commands.")


# Define a function to handle the /help command
def help(update, context):
  update.message.reply_text("Here are some commands you can use:\n\n"
                            "/start - Start a conversation with me\n"
                            "/help - Show this help message\n"
                            "/auto - Toggle automatic responses\n")


# Define a function to handle the /auto command
def auto(update, context):
  # Get the current state of automatic responses
  state = context.user_data.get("auto", False)

  # Toggle the state
  context.user_data["auto"] = not state

  if state:
    update.message.reply_text("Automatic responses are now disabled.")
  else:
    update.message.reply_text("Automatic responses are now enabled.")


# Define a function to handle messages
def message(update, context):
  # Check if automatic responses are enabled
  if context.user_data.get("auto", False):
    # Choose a random response from the list
    response = responses[random.randint(0, len(responses) - 1)]

    # Send the response
    update.message.reply_text(response)


# Create the Updater and pass it the bot's TOKEN
updater = Updater(TOKEN, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("auto", auto))

# Add message handler
dispatcher.add_handler(MessageHandler(Filters.text, message))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM, or SIGABRT
updater.idle()
