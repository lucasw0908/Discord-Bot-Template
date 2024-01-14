import discord
from discord.ext import commands
from pathlib import Path
import os

from .config import TOKEN

class DiscordBotSync(commands.Bot):
    """The discord bot object."""
    
    def __init__(self, command_prefix: str=None, **options) -> None:
        super().__init__(self, intents=discord.Intents.all(), **options)
        self.command_prefix = command_prefix if commands.when_mentioned_or(command_prefix) else commands.when_mentioned_or("-")
      
    def load(self) -> None:
        """Load all cogs."""

        for cog in [p.stem for p in Path(os.path.abspath(os.path.dirname(__file__))).glob("./cogs/*.py")]:
            try:
                self.load_extension(f"bot.cogs.{cog}")
                print(f" * Discrod bot : Loaded {cog}")
            except Exception as e:
                print(f" * Discrod bot : Loaded {cog} fail!")
                print(e)
            
        print(f" * Discrod bot : Loading completed!")
      
    def run(self, *args, **kwargs):
        self.load()
        if args.__len__ ()> 0:
            super().run(*args, **kwargs)
        else:
            super().run(TOKEN, **kwargs)