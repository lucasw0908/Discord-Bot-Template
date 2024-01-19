from bot.__init__ import DiscordBotSync

bot = DiscordBotSync("?")   
    
if __name__ == "__main__":
    bot.run(debug=True)