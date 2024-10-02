import os
import asyncio
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

from src.cogs.greet import startup

intents = Intents.all()
prefix = "!"

class lyn_main():
    def __init__(self):
        load_dotenv()

    async def load_cogs(self):
        await bot.load_extension("src.cogs.greet")

    def run(self):
        asyncio.run(self.load_cogs())
        token = os.getenv("key")
        bot.run(token)

if __name__ == "__main__":
    bot = commands.Bot(command_prefix = prefix, intents=intents)
    lyn_main().run()
