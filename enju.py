# Enju; Discord.py [rewrite] 1.3.4
from discord.ext import commands
import os
import secrets


def get_prefix(bot, message):
    prefixes = ['n ', 'nju ']
    if not message.guild:
        return 'n '
    return commands.when_mentioned_or(*prefixes)(bot, message)


client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
client.remove_command('help')

if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            client.load_extension(f'cogs.{file[:-3]}')
            print(f'Cog loaded : {file}')

client.run(secrets.BOT_TOKEN, bot=True, reconnect=True)
