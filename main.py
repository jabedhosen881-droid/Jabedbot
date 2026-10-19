import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Online: {bot.user}")

@bot.tree.command(name="ping", description="Check bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 24/7 Active!")

keep_alive()
bot.run(os.environ.get("TOKEN"))
