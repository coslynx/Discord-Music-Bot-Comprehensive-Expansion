import os
import discord
from discord.ext import commands

from utils.config import Config
from utils.logger import Logger
from utils.errors import (
    InvalidVoiceChannel,
    TrackNotFound,
    AlreadyConnected,
    NotInVoice,
    NoPermissions,
    NotConnected,
    PlaylistNotFound,
    PlaylistError,
)

# Load configuration settings
config = Config()

# Create a logger instance
logger = Logger(__name__)

# Define the bot instance
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    logger.info(f"Bot is ready! Logged in as {bot.user}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use `!help` to see available commands.")
    elif isinstance(error, InvalidVoiceChannel):
        await ctx.send(
            "Please join a valid voice channel first. You may need to reconnect to the voice channel."
        )
    elif isinstance(error, TrackNotFound):
        await ctx.send(f"Track not found. Please try a different search query.")
    elif isinstance(error, AlreadyConnected):
        await ctx.send("I am already connected to a voice channel.")
    elif isinstance(error, NotInVoice):
        await ctx.send("You need to be in a voice channel to use this command.")
    elif isinstance(error, NoPermissions):
        await ctx.send("You do not have the permissions to use this command.")
    elif isinstance(error, NotConnected):
        await ctx.send("I am not connected to a voice channel.")
    elif isinstance(error, PlaylistNotFound):
        await ctx.send("Playlist not found. Please check the playlist name.")
    elif isinstance(error, PlaylistError):
        await ctx.send("An error occurred while managing the playlist.")
    else:
        logger.error(f"Unhandled error: {error}")
        await ctx.send(
            "An error occurred. Please try again later or contact the bot administrator."
        )


# Run the bot
if __name__ == "__main__":
    bot.run(config.token)