import discord
from discord.ext import commands
import logging

from bot.config import LOGNAME
from bot.utils.embed import EmbedMaker

log = logging.getLogger(f"{LOGNAME}.cogs.test")

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="test", description="範例指令")
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond(embed=EmbedMaker(status=True, description="**Hello world!!!**"))
        
        log.debug(f"{ctx.author.name}[{ctx.author.id}] used {ctx.command.name}.")
        print(__name__)
        
              
def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))