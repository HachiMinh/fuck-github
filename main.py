import discord
import os
from discord.ext import commands


TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix = "?")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    
@bot.command(
    name = "say",
    aliases = ["speak"],
    description = "Make the bot say something",
)
async def _say(ctx, content):
    await ctx.send(content)


bot.run(TOKEN)
