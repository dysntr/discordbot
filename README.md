## A Simple Python Discord Bot
This is a simple Discord bot written in python.

### Requirements:

1. To use this bot. You need to create a new application and bot in discord. You will need to invite your bot to the sever. Here is a ref link that provides some details on how to do this [Create new Discord App and Bot](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/). 

2. Store your API token key in `.env` file. Make sure you don't upload this file as it contains a secret. This is how your .env file may look like:

    ```
    # .env file
    DISCORD_TOKEN=### REPLACE WITH SECRET TOKEN ###
    DISCORD_GUILD=Dysan's server
    ```

3. Install the discord.py library using:

    `python3 -m pip install -U discord.py`

    or

    `py -3 -m pip install -U discord.py`

    If you need to install pip use the following commands:

    ``` bash
    sudo apt update
    sudo apt install python3-pip
    pip3 --version
    ```
4. If you don't have dotenv library use command `pip3 install python-dotenv` to install dotenv. This is required so your script can load the .env file and read the Discord Token.
 

### Run Discord bot:
Once you have installed the requirements, you can run the discord bot by running `python3 bot.py`.

### Questions/Comments
If you have any questions or Comments feel free to reach me on discord.

Discord: Dysan#6547