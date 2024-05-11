import re
import discord

class EmojiManager:
    
    emojis: dict[str:discord.Emoji] = None
    
    def __new__(self, massage: str):
        return self.translation_emoji_string(massage)
    
    @classmethod
    def translation_emoji_string(cls, message: str) -> str:
        """Translate the message including emojis"""
        pattern = re.compile(r':[^:]+:')
        
        for t in re.findall(pattern, message):
            t: str
            if t.strip(":") in cls.emojis:
                message = message.replace(t, cls.emojis[t.strip(":")])
                
        return message
        
    @classmethod
    def set_emojis(cls, emojis: dict[str:discord.Emoji]) -> None:
        cls.emojis = emojis
        
    @classmethod
    def get_emojis(cls) -> dict[str:discord.Emoji] | None:
        return cls.emojis