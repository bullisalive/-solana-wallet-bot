import asyncio
import logging
from solana_bot import create_bot

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """Starts the bot and runs polling."""
    app = await create_bot()
    logger.info("🚀 Bot is now running!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
