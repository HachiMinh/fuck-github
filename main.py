import discord
import logging
import os
from discord.ext import commands


TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix = "?")
logging.basicConfig(level = logging.INFO)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    
def to_lower(argument):
    return argument.lower()
    
@bot.command(
    name = "say",
    aliases = ["speak"],
    description = "Make the bot say something",
)
async def _say(ctx: to_lower, *, content):
    await ctx.send(content)


bot.run(TOKEN)
