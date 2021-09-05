import discord
import os
from discord.ext import commands


TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix = "?")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(TOKEN)