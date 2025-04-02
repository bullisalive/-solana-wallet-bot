# solana_bot.py
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from solana.rpc.api import Client
from solana.publickey import PublicKey
import os

# Solana RPC Endpoint
solana_client = Client("https://api.mainnet-beta.solana.com")

# Command to search Solana wallet
async def search_wallet(update: Update, context: CallbackContext):
    if context.args:
        wallet_address = context.args[0]
        try:
            public_key = PublicKey(wallet_address)
            balance = solana_client.get_balance(public_key)['result']['value'] / 1e9  # Convert lamports to SOL
            await update.message.reply_text(f"Wallet: {wallet_address}\nBalance: {balance} SOL")
        except Exception:
            await update.message.reply_text("Invalid Solana wallet address or error fetching balance.")
    else:
        await update.message.reply_text("Please provide a Solana wallet address.")

# Telegram bot setup
async def main():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")  # Load token from environment variable
    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler("search", search_wallet))
    print("Bot is running...")
    await app.run_polling()

