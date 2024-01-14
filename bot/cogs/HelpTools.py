import discord
from discord.ext import commands
import datetime
import os
from pathlib import Path

from ..utils.help import HelpCommandSettings
from ..utils.embed import EmbedMaker

class HelpTools(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(name="register")
    @commands.has_permissions(administrator=True)
    async def register(self, ctx: discord.ApplicationContext):
        
        for cmd in self.bot.application_commands:
            self.bot.remove_application_command(cmd)
            
        await self.bot.sync_commands(commands=self.bot.application_commands, guild_ids=[ctx.guild.id])
        HelpCommandSettings.set_command_list(list(self.bot.all_commands.values()))
        
        await ctx.message.reply(embed=EmbedMaker(status=True, description=f"已重新註冊以下指令:\n" + "```" + ", ".join([cmd.name for cmd in self.bot.application_commands]) + "```"))
        
    @commands.command(name="ping")
    async def ping(self, ctx: discord.ApplicationContext): 
        runnung_time = datetime.datetime.utcnow().replace(tzinfo=None) - ctx.message.created_at.replace(tzinfo=None)
        await ctx.message.reply(embed=EmbedMaker(status=True, description=f"**延遲:{runnung_time.seconds}.{runnung_time.microseconds}s**"))
        
    
    @commands.command(name="reload")
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx: discord.ApplicationContext):
        
        message = []
        status = True
        
        for cog in [p.stem for p in Path(os.path.abspath(os.path.dirname(__file__))).glob("*.py")]:  
            
            if f"bot.cogs.{cog}" in self.bot.extensions:
                try:
                    self.bot.reload_extension(f"bot.cogs.{cog}")
                    print(f" * Discrod bot : Reloaded {cog}")
                    message.append(f"**成功重新載入{cog}**")
                    
                except Exception as e:
                    print(f" * Discrod bot : Reloaded {cog} fail!")
                    print(e)
                    message.append(f"**重新載入{cog}時發生了錯誤，錯誤如下:**")
                    message.append(f"``` * {e}```")
                    status = False
            else:
                try:
                    self.bot.load_extension(f"bot.cogs.{cog}")
                    print(f" * Discrod bot : Loaded {cog}")
                    message.append(f"**成功載入{cog}**")
                    
                except Exception as e:
                    print(f" * Discrod bot : Loaded {cog} fail!")
                    print(e)
                    message.append(f"**載入{cog}時發生了錯誤，錯誤如下:**")
                    message.append(f"``` * {e}```")
                    status = False
                
        print(f" * Discrod bot : Loading completed!")
        
        await ctx.message.reply(embed=EmbedMaker(status=status, description="\n".join(message)))
                


def setup(bot: commands.Bot):
    bot.add_cog(HelpTools(bot))