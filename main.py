import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Define your desired intents
intents = discord.Intents.all()
intents.typing = False  # Disable receiving typing events
intents.presences = False  # Disable receiving presence update events

# Prefix of bot
bot = commands.Bot(command_prefix='$', intents=intents)

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)