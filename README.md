# dc-imager
[![ci](https://github.com/danrog303/dc-imager/actions/workflows/ci.yml/badge.svg)](https://github.com/danrog303/dc-imager/actions/workflows/ci.yml)
![license](https://img.shields.io/github/license/danrog303/dc-imager)
![last commit](https://img.shields.io/github/last-commit/danrog303/dc-imager)
> Configurable image bot for Discord.

## Project summary
**dc-imager** provides a Discord bot which allows to send random images
on a Discord server.
![egCMD](https://github.com/danrog303/danrog303/assets/32397526/a038ca5d-ffc3-4e02-88d5-0128f16cc1d4)


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
