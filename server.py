"""
File: server.py
Author: Tanisha Banik
Date: 2024-11-08
"""


import os
import logging
import pandas as pd
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application

from utils.chatbot import ask_question
from utils.utils import find_closest_bus_station

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
df = None

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") #bhopal_bus_bot

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am Bhopal BRTS Bot. Send me your location to find the nearest bus station.')

# async def help_command(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text('Help!')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Send /location to get the nearest bus station.\nSend /clear to delete all the history.')

async def location(update: Update, context: CallbackContext) -> None:
    global df
    user_location = update.message.location

    if user_location:
        print(str(user_location))
        user_lat = round(user_location.latitude, 5)
        user_long = round(user_location.longitude, 5)
        logger.info(f"Received location: Latitude {user_lat}, Longitude {user_long}")

        closest_station = find_closest_bus_station(df, user_lat, user_long)
        if closest_station:
            message = f"The closest bus station is {closest_station['station']} which is {round(closest_station['distance'], 2)} km away. Routes: {' '.join(closest_station['all_routes'])}"
            await update.message.reply_text(message)
            await update.message.reply_text(f"Navigate using Google Map: {closest_station['dir_to_closest_point']}")
        else:
            await update.message.reply_text("Sorry, I couldn't find any nearby bus stations.")
    else:
        await update.message.reply_text("Please send your location.")

async def general_query(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    response = ask_question(query)
    await update.message.reply_text(response)

def health_check() -> None:
    global df
    logger.info("Performing health check...")

    try:
        df = pd.read_csv("assets/data/all_routes_combined.csv")

        logger.info("CSV file loaded successfully.")
    except FileNotFoundError:
        logger.error("CSV file not found.")
        raise
    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the CSV file: {e}")
        raise

    logger.info("Health check passed!")

def main() -> None:
    health_check()
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("location", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.LOCATION, location))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, general_query))

    application.run_polling()

if __name__ == '__main__':
    main()