import discord
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guildnum = 0
        guilds = await self.bot.fetch_guilds(limit=150).flatten()
        for guild in guilds:
            guildnum = guildnum + 1
            guild = self.bot.get_guild(guild.id)
            myname = guild.me.nick
            if myname == "Enju S.":
                print(f'[+] I\'m in guild {guild.name} {guild.id} + => And my name is already sweet!')
            else:
                print(f'[+] I\'m in guild {guild.name} {guild.id} + => And of course they messed up my name!')
                await guild.me.edit(nick="Enju S.")
        print(f'Serving {guildnum} guilds')
        print(f'Logged in as: {self.bot.user.name}\n ID: {self.bot.user.id}\n API Version: {discord.__version__}\n Bot Version: 1.0.0\n Serving {guildnum} guilds')
        status = discord.Streaming(name='Lofi Hip-Hop - beats to relax/study to',
                                   url='https://www.youtube.com/watch?v=5qap5aO4i9A')
        await self.bot.change_presence(status=discord.Status.online, activity=status)
        print(f'Finally logged in! Phew.. ')
        print(
            '============================================================\n     Good morni- why am i greeting you?!\n============================================================')


def setup(bot):
    bot.add_cog(MainCog(bot))
