import asyncio
from solana_bot import create_bot

async def main():
    app = await create_bot()
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
