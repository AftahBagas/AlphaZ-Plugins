<h2 align="center"><b>MENAGE: <a href="https://telegram.dog/mixiologist">KOALA ░ 🐨</a></b></h2>
<br>
<p align="center">
   <a href="https://github.com/Camel07/KampangUsergay"><img src="https://media0.giphy.com/media/Hs0cX9Z3RR77c0MMA7/giphy.gif" alt="KampangUsergay" width=400px></a>
   <br>
   <br>
</p>
<h1>KampangUsergay</h1>
<b>BOT TERKAMPANG ASUU!</b>
<br>
<br>


**KampangUsergay** is a Powerful , _Pluggable_ Telegram UserBot written in _Python_ using [Pyrogram](https://github.com/pyrogram/pyrogram).
<br>
<p align="center">
    <a href="https://telegram.dog/caritemanhidop"><img src="https://telegra.ph/file/b28a3909df2e46bab6458.jpg" width=220px></a></p>

## Disclaimer
```
/**
   /** ⚠️Kang at your own risk⚠️
Akun Telegram Anda mungkin diblokir. Saya tidak bertanggung jawab atas penggunaan yang tidak benar dari bot ini Bot ini dimaksudkan untuk tujuan bersenang-senang dengan meme, serta mengelola grup secara efisien. Ini dapat membantu Anda mengelola diri sendiri juga. Anda akhirnya melakukan spamming grup, dilaporkan kiri dan kanan, dan kemudian Anda berakhir di Pertempuran Terakhir dengan Telegram dan pada akhirnya Tim Telegram menghapus akun Anda? Dan setelah itu, Anda mengarahkan jari Anda kepada kami karena akun Anda dihapus? Kami akan berguling-guling di lantai sambil menertawakan Anda. Iya! Anda tidak salah dengar. / **
/**
```
## Requirements 
* Python 3.8 or Higher
* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)
## How To Deploy 
* With Heroku:
<p align="center">
   <a href = "https://heroku.com/deploy?template=https://github.com/Camel07/UsergayKampang/tree/alpha"><img src="https://telegra.ph/file/34fa325c222a70badb02f.jpg" alt="Press to Takeoff" width="490px"></a>
</p>
<br>

> **NOTE** : your can fill other vars as your need and they are optional. (settings -> reveal config vars)
* First click The Button Above.
* Fill `API_ID`, `API_HASH`, `DATABASE_URL`, `LOG_CHANNEL_ID`, `HEROKU_APP_NAME` and `HEROKU_API_KEY` (**required**)
* Then fill Dual Mode vars : `OWNER_ID`, `BOT_TOKEN` and `HU_STRING_SESSION`
* Then fill [other **non-required** vars](https://telegra.ph/Heroku-Vars-for-USERGE-X-08-25) later
* Finally **hit deploy** button
## String Session
**VAR ->** `HU_STRING_SESSION`
#### By HEROKU
- [open your app](https://dashboard.heroku.com/apps/) then go to **more** -> **run console** and type `bash genStr` and click **run**.
#### On REPL
- [Generate on REPL Click](https://repl.it/@ManusiaRakitan/stringsession#README.md)
### Read more
<details>
  <summary><b>Details and Guides</b></summary>

## Other Ways

* With Docker 🐳 
    <a href="https://github.com/Camel07/UsergayKampang/blob/alpha/resources/readmeDocker.md"><b>See Detailed Guide</b></a>

* With Git, Python and pip 🔧
  ```bash
  # clone the repo
  git clone https://github.com/camel07/usergaykampang.git
  cd userge-x

  # create virtualenv
  virtualenv -p /usr/bin/python3 venv
  . ./venv/bin/activate

  # install requirements
  pip install -r requirements.txt

  # Create config.env as given config.env.sample and fill that
  cp config.env.sample config.env

  # get string session and add it to config.env
  bash genStr

  # finally run the UsergayKampang ;)
  bash run
  ```


<h2>Guide to Upstream Forked Repo</h2>
<a href="https://telegra.ph/Upstream-Userge-Forked-Repo-Guide-07-04"><b>Upstream Forked Repo</b></a>
<br>
<br>

<h3 align="center">Youtube Tutorial<h3>
<p align="center"><a href="https://youtu.be/M4T_BJvFqkc"><img src="https://i.imgur.com/VVgSk2m.png" width=250px></a>
</p>


## Features 

* Powerful and Very Useful **built-in** Plugins
  * gdrive [ upload / download / etc ] ( Team Drives Supported! ) 
  * zip / tar / unzip / untar / unrar
  * telegram upload / download
  * pmpermit / afk
  * notes / filters
  * split / combine
  * gadmin
  * plugin manager
  * ...and more
* Channel & Group log support
* Database support
* Build-in help support
* Easy to Setup & Use
* Easy to add / port Plugins
* Easy to write modules with the modified client

## Example Plugin 

```python
from userge import userge, Message, filters

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object

# add command handler
@userge.on_cmd("test", about="help text to this command")
async def test_cmd(message: Message):
   LOG.info("starting test command...")  # log to console
   # some other stuff
   await message.edit("testing...", del_in=5)  # this will be automatically deleted after 5 sec
   # some other stuff
   await CHANNEL.log("testing completed!")  # log to channel

# add filters handler
@userge.on_filters(filters.me & filters.private)  # filter my private messages
async def test_filter(message: Message):
   LOG.info("starting filter command...")
   # some other stuff
   await message.reply(f"you typed - {message.text}", del_in=5)
   # some other stuff
   await CHANNEL.log("filter executed!")
```

</details> 

### Project Credits 
* [Pyrogram Assistant](https://github.com/pyrogram/assistant)
* [PyroGramBot](https://github.com/SpEcHiDe/PyroGramBot)
* [PaperPlane](https://github.com/RaphielGang/Telegram-Paperplane)
* [Uniborg](https://github.com/SpEcHiDe/UniBorg)
* [UsergeTeam](https://github.com/UsergeTeam/Userge)
### Copyright & License 
[**GNU General Public License v3.0**](https://github.com/code-rgb/USERGE-X/blob/alpha/LICENSE)
