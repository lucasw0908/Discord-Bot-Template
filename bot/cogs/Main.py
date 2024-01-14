import discord
from discord.ext import commands

from ..utils.help import Help, HelpCommandSettings, need_help
from ..utils.emoji import EmojiManager

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        
        EmojiManager.set_emojis({e.name:str(e) for e in self.bot.emojis})
        
        #set help command
        await self.bot.change_presence(activity=discord.Game(name=f"使用{self.bot.command_prefix}help以獲得幫助")) 
        HelpCommandSettings.set_prefix(self.bot.command_prefix)
        HelpCommandSettings.set_command_list(list(self.bot.all_commands.values()))
        self.bot.help_command = Help()
        
        print(" * Discord bot : Started!")
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: discord.ApplicationContext, err: discord.ApplicationCommandError):
        await ctx.message.reply(embed=need_help(command_name=ctx.message.content, error=err), mention_author=False)
            
def setup(bot: commands.Bot):
    bot.add_cog(Main(bot))