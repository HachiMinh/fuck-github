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


@bot.command(name='list')
async def _list(ctx, arg):
    pass

import random

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)


bot.run(TOKEN)
