import discord
import os
import asyncio
import json
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot

class button_view(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="pg!",intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game("/hello"))
    print("Online")
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)}command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello",description="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hey{interaction.user.mention}!")

with open("Token.0","r",encoding="utf-8") as f:
    bottoken = f.read()
    
bot.run(bottoken)
