# Discord Bot Template

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![License](https://img.shields.io/github/license/lucasw0908/Discord-Bot-Template.svg)](https://github.com/lucasw0908/Discord-Bot-Template/blob/master/LICENSE)

# 說明📖

* **自動根據設定的前綴改變狀態**
* **cog自動載入系統**
* **好看的報錯系統**
* **方便的機器人物件建立**
* **幫助指令設為自動讀取的指令列表及說明(前綴指令說明請寫在data.py)**
* **log系統**
* **使用者版本偵測系統**

****

# 預設指令⚙️

### **help**
***顯示指令列表***

![help](https://imgur.com/QklpRs3.png)

### **ping**
***測試機器人延遲***

![ping](https://imgur.com/QYwWpnT.png)

### **register**
***重新註冊所有指令***

![register](https://imgur.com/L90vY6K.png)

### **reload**
***重新載入所有指令***

![reload](https://imgur.com/hji5neY.png)

****

# 小工具📦

### Emoji
```python=
from bot.utils.emoji import EmojiManager
...
text = EmojiManager("haha:kekw:!")
await ctx.send(text)
```
_**可將`:emoji:`轉換為可被bot發送的形式**_
### Embed
```python=
from bot.utils.embed import EmbedMaker
...
await ctx.send(embed=EmbedMaker(status=True, description="Hello World!"))
```
_**可快速建立Embed物件**_

****