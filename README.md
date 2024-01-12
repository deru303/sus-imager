# sus-imager
[![ci](https://github.com/deru303/sus-imager/actions/workflows/ci.yml/badge.svg)](https://github.com/deru303/sus-imager/actions/workflows/ci.yml)
![license](https://img.shields.io/github/license/deru303/sus-imager)
![last commit](https://img.shields.io/github/last-commit/deru303/sus-imager)
> Anime image bot for Discord.

## Project summary
**sus-imager** provides a Discord bot which allows to send random anime images
on a Discord server.
![susbot](https://github.com/deru303/sus-imager/assets/82843647/e310b063-df55-4791-a100-02b576f6a381)

**sus-imager** uses **danrog303/dc-imager** repo as its base. While **danrog303/dc-imager** provides bot functionality and its core features, **sus-imager** provides thousands of anime pictures that can be used by the bot.

## How to invite?
You can use this link in order to invite this bot to your Discord server:  
https://discord.com/api/oauth2/authorize?client_id=835439136709672961&permissions=2147534912&scope=bot

## Project structure
- **bot/** - contains source code of Discord bot
- **tests/** - contains some basic unit tests
- **images/** - contains image library; 
  bot will automatically detect changes in this directory
  and will send images that are present here

## How to deploy?
1. **Directly by using Python intepreter**
   ```shell
   python3 -m pip install requirements.txt
   export DC_IMAGER_TOKEN="YOUR-DISCORD-BOT-TOKEN-HERE"
   python3 main.py
   ```

2. **By using Docker** (image has around 86 MB excluding pictures)
   ```shell
   docker build -t dc-imager .
   docker run -e "DC_IMAGER_TOKEN=YOUR-BOT-TOKEN-HERE" dc-imager
   ```

## How to run tests?
You can run Python unit tests by calling this command:
```shell
python3 -m unittest discover tests/
```

## Available Discord commands
| Command             | Description  |
|---------------------|--------------|
| **/img _xyz_**      | send random image from the given category |
| **/img-categories** | send list of available categories |

## Possible improvements
1. Add **/img-bind** command, which will allow to automatically send 
   images to a Discord channel (e.g. every day at 12:00).

