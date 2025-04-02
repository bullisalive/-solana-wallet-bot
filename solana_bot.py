from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from solana.rpc.api import Client
from solana.publickey import PublicKey
import os
import logging

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Solana RPC Endpoint
solana_client = Client("https://api.mainnet-beta.solana.com")

async def search_wallet(update: Update, context: CallbackContext):
    """Fetches and displays the SOL balance of a given wallet."""
    if context.args:
        wallet_address = context.args[0]
        try:
            public_key = PublicKey(wallet_address)
            balance = solana_client.get_balance(public_key)['result']['value'] / 1e9  # Convert lamports to SOL
            await update.message.reply_text(f"🔹 Wallet: `{wallet_address}`\n💰 Balance: `{balance} SOL`")
        except Exception as e:
            logger.error(f"Error fetching wallet balance: {e}")
            await update.message.reply_text("❌ Invalid Solana wallet address or error fetching balance.")
    else:
        await update.message.reply_text("⚠️ Please provide a Solana wallet address.\nExample: `/search WALLET_ADDRESS`")

async def create_bot():
    """Creates and returns the Telegram bot application."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")  # Load token from environment variable
    if not bot_token:
        raise ValueError("🚨 TELEGRAM_BOT_TOKEN is not set!")

    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler("search", search_wallet))

    logger.info("✅ Bot initialized successfully!")
    return app

