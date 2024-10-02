from discord.ext import commands

class startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"logged in as {self.bot.user}")

async def setup(bot):
    await bot.add_cog(startup(bot))
