import discord
import os
import asyncio
import json
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot

colors = []

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

with open("Colors.0","r",encoding="utf-8") as color_file:
    lines = color_file.readLines()
    for line in lines:
        line = line.rstrip("\n")
        if line != "":
            colors.append(line)

@bot.tree.command(name="color", description="color")
@app_commands.describe(color_code="設定したい色のカラーコード")
async def color(interaction: discord.Interaction, color_code:str):
    if color_code not in colors:
        colors.append(color_code)
        await interaction.guild.createRole(name=color_code,colour=discord.Colour.from_str(color_code))
        
    await interaction.user.addRole(color_code)
    await interaction.response.send_message("色を付与しました")

@bot.event
async def on_close():
    with open("Colors.0", "w",encoding="utf-8") as color_file:
        for color in colors:
            color_file.write(color + "\n")
            print ("Colors saved.")
bot.run(bottoken)
