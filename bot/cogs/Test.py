import discord
from discord.ext import commands
from ..utils.embed import EmbedMaker

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="test", description="範例指令")
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond(embed=EmbedMaker(status=True, description="**Hello world!!!**"))
        
              
def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))