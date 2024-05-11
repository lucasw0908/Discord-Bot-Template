import discord
from discord.ext import commands
from .embed import EmbedMaker
from .description import prefix_commands_description


def need_help(command_name: str, error: discord.ApplicationCommandError) -> discord.Embed:
    return EmbedMaker(status=False, description=f'**在執行{command_name}時發生錯誤，錯誤報告如下:**``` * {error}```')

class HelpCommandSettings:
    
    command_list = None
    prefix = None
    
    @classmethod
    def set_command_list(cls, command_list: list[discord.ApplicationCommand]) -> None:
        cls.command_list = command_list
        
    @classmethod
    def set_prefix(cls, prefix: str) -> None:
        cls.prefix = prefix
        
    @classmethod
    def help(cls) -> discord.Embed:
        
        embed = discord.Embed(title=f'指令列表⚙️', color=discord.Color.purple())
        
        if cls.command_list is None: 
            embed.add_field(name=f"_**無法取得指令資訊**_", inline=False)
            
        for cmd in cls.command_list:
            
            if isinstance(cmd, discord.SlashCommand):
                description = cmd.description_localizations if cmd.description_localizations else cmd.description
                embed.add_field(name="", value=f"{cmd.mention}\n _{description}_", inline=False)
                
            elif cls.prefix is not None: 
                
                if cmd.name in prefix_commands_description:
                    description = prefix_commands_description[cmd.name]
                    
                else:
                    description = "No description provided"
                    
                embed.add_field(name="", value=f"**{cls.prefix}{cmd.name}**\n _{description}_", inline=False)
            
        return embed