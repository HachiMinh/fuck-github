import discord
import logging
import os
from discord.ext import commands


TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix = "[",intents=discord.Intents.all())
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

@bot.command(
    name = "kill",
    description = "Kill someone",
)
async def kill(ctx, user: discord.User):
    await ctx.send(f"<@!{user.id}> was killed by <@!{ctx.author.id}>")


bot.run(TOKEN)
