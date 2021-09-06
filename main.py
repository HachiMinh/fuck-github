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

    
    
@bot.command(
    name = "say",
    aliases = ["speak"],
    description = "Make the bot say something",
)
async def _say(ctx, *, content):
    await ctx.send(content)

import random

class kill(commands.Converter):
    async def convert(ctx, argument):
        victim = random.choice(ctx.guild.members)
        return '{0} has been slained'.format(victim)

@bot.command()
async def kill_random(ctx, *, arg: kill):
    await ctx.send(arg)


bot.run(TOKEN)
