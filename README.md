# telegram-voice-to-text

[@audiotranscript_bot](https://t.me/audiotranscript_bot)

Feel free to write me [@emilkayumov](https://t.me/emilkayumov)

## Introduction

A simple telegram bot to transcript voice messages.

It's my pet project which is main goal not to be something big. I'm going to learn some basic stuff: telegram bot building, docker, databases (like sqlite if I imagine how to use it), clouds, tests, ci, moninorings, logging, etc. 

You can deploy your own installation of this bot. It requires only bot token and some computation power (I test it on my Air m1 and it works without any problem with large model of Whisper).

I'm using now:
- [Faster Whisper transcription with CTranslate2](https://github.com/guillaumekln/faster-whisper)
- [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)

## How to run

You can create a virtual environment and setup it with:

```make init```

After creating a bot with [@BotFather](https://t.me/BotFather) fill `config.yaml` with token. Also you can use `allowlist_usernames` if you don't want anybody to use your bot.

And run it:

`make run`

## Plans

1. ~~Init~~
2. Run a bot on cloud
3. A docker file to easily run on server
4. Setup monitorings to see if the bot is crashed
5. Make the bot stable
6. Setup logging (no user messages only using stats)
7. Add some new functionality like summarizing messages
8. ...
