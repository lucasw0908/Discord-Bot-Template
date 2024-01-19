import discord
from discord.ext import commands
from pathlib import Path
import os
import logging
import logging.handlers
import discord

from bot.config import TOKEN, LOGNAME

log = logging.getLogger(LOGNAME)

class DiscordBotSync(commands.Bot):
    """The discord bot object."""
    
    def __init__(self, command_prefix: str=None, **options) -> None:
        super().__init__(self, intents=discord.Intents.all(), **options)
        self.command_prefix = command_prefix if commands.when_mentioned_or(command_prefix) else commands.when_mentioned_or("-")
        
    def init_logger(self, debug: bool=False):
        
        formatter = logging.Formatter("[{asctime}] {levelname} {name}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
        
        if debug:
            log.setLevel(logging.DEBUG)
            
        file_handler = logging.handlers.RotatingFileHandler(
            filename=f"{LOGNAME}.log",
            encoding="utf-8",
            maxBytes=8**7, 
            backupCount=8
        )
        
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console_handler)
        
      
    def load(self) -> None:
        """Load all cogs."""

        for cog in [p.stem for p in Path(os.path.abspath(os.path.dirname(__file__))).glob("./cogs/*.py")]:
            try:
                self.load_extension(f"bot.cogs.{cog}")
                log.info(f"Loaded {cog}")
            except Exception as e:
                log.error(f"Loading {cog} failed!", exc_info=True)
            
        log.info(f"Extension loading completed!")
      
    def run(self, token: str=TOKEN, debug: bool=False, **kwargs):
        
        self.init_logger(debug=debug)
        self.load()
        
        super().run(token, **kwargs)