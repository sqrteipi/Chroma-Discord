import asyncio
import discord
import hkoi_tutorial
from discord.ext import commands
from dotenv import load_dotenv
import os

# Define your desired intents
intents = discord.Intents.all()
intents.typing = False  # Disable receiving typing events
intents.presences = False  # Disable receiving presence update events

# Prefix of bot
bot = commands.Bot(command_prefix='$', intents=intents)

categories = {
    'Gaming': 'Entertainment in Discord',
    'Math': 'Commands related to Math',
    'Programming': 'Commands related to Programming',
    # 'Other aspects': 'Miscellaneous Commands',
}

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

class Gaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Wordle', brief='Playing Wordle')
    async def wordle(self, ctx, word):
        await ctx.send("Start!")

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

class Programming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='task_help', brief='Provide tutorial for Competitive Programming tasks')
    async def task_help(self, ctx, task):
        if hasattr(hkoi_tutorial, task):
            await ctx.send(getattr(hkoi_tutorial, task))
        else:
            await ctx.send("Sorry, task not found / editorial is not added.")

async def main():
    # Add the cogs to the bot
    await bot.add_cog(Math(bot))
    await bot.add_cog(Programming(bot))

    # Set the command categories
    for category, description in categories.items():
        cog = bot.get_cog(category)
        if cog:
            cog.description = description

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    await bot.start(TOKEN)

asyncio.run(main())