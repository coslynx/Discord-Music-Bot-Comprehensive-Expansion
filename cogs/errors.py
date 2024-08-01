import discord
from discord.ext import commands

class InvalidVoiceChannel(commands.CommandError):
    """Custom exception for invalid voice channels."""
    def __init__(self, message="Please join a valid voice channel first."):
        super().__init__(message)

class TrackNotFound(commands.CommandError):
    """Custom exception for when a track cannot be found."""
    def __init__(self, message="Track not found. Please try a different search query."):
        super().__init__(message)

class AlreadyConnected(commands.CommandError):
    """Custom exception for when the bot is already connected to a voice channel."""
    def __init__(self, message="I am already connected to a voice channel."):
        super().__init__(message)

class NotInVoice(commands.CommandError):
    """Custom exception for when the user is not in a voice channel."""
    def __init__(self, message="You need to be in a voice channel to use this command."):
        super().__init__(message)

class NoPermissions(commands.CommandError):
    """Custom exception for when the bot lacks permissions to perform an action."""
    def __init__(self, message="I do not have the permissions to do that."):
        super().__init__(message)

class NotConnected(commands.CommandError):
    """Custom exception for when the bot is not connected to a voice channel."""
    def __init__(self, message="I am not connected to a voice channel."):
        super().__init__(message)

class PlaylistNotFound(commands.CommandError):
    """Custom exception for when a playlist cannot be found."""
    def __init__(self, message="Playlist not found. Please check the playlist name."):
        super().__init__(message)

class PlaylistError(commands.CommandError):
    """Custom exception for errors during playlist management."""
    def __init__(self, message="An error occurred while managing the playlist."):
        super().__init__(message)