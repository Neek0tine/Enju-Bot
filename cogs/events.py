import discord
import asyncio
import random
from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        greet = "Umm, hi? So you're the new guy? I- Um.. the server's president. Nice to meet you.\n \n Before doing some fun things together in our server, I need you to know some of our rules!\n 1. Don't annoy me. Or someone else."
        await member.send(greet)
        print(f'[!] New member joined the guild: {member}\n ')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        farewell = 'Hey umm.. I dont know what happened, and I dont really want to be nosey and all, but if you had unsolved problems, make sure you- Wait, who am i to lecture you?'
        try:
            await member.send(farewell)
        except discord.Forbidden:
            print(f'[!] Member left the guild: {member}')
            print(f'[-] Failed to send farewell message to {member}. Do they even deserve it?\n ')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        try:
            print(message.author.name, "#", message.channel.name, " : ", message.content, )
        except AttributeError:
            print("Direct Message received!")
            print(message.author.name, "[#] Direct Channel: ", message.content)
        trigger = ["nju"]
        easter = ['cum']
        author = message.author.name
        responses = ['Hi',
                     f'Stop calling me {author} ',
                     'are you into me or something?!',
                     f'I have a beautiful name, I know {author}',
                     f'I have a beautiful name, I know {author}',
                     f'What do you want {author}?',
                     f'I don\'t feel like talking, especially with you {author}',
                     f'Um, how can i help you {author}',
                     f'I wont let you copy my homework, {author}',
                     f'How many times have i told you, {author}, stop calling me!',
                     f'I dont need your help, and im hoping you don\'t need mine',
                     f'Go away, hentai!'
                     f'I have something to do. Go call @Ayana#8911 instead'
                     ]
        altresponses = ['Umm, Hi Niko-kun! :3',
                        'How can I help you Niko-kun?',
                        'How are you? Oh I\'m fine, no need to worry about me!',
                        'Hey, stop teasing me already!',
                        'Can\'t talk with you right now. Um, well, maybe later? In the Cafe?',
                        'Hey~',
                        'Heya!',
                        'I\'m okay, Niko-kun. No need to worry me :).',
                        'Do you need something, Niko-kun?', ]

        cumresponses = ['Father of lies',
                        'Cum in disguise',
                        'Your cum won\'t last',
                        'There\'s a snake in my ass',
                        'The cum-fathers secret stash',
                        'Cum-stomp me flat',
                        'I\'m going to fuck your dad',
                        'Cumming high into the morning sky',
                        'Vape cum from my bum til I die',
                        'Watching Arthur with a cock in my ass',
                        'Riding hard',
                        'Eating ass master-class',
                        'Sacred cum blade',
                        'A fuckling crusade',
                        'Fatal cum--theft',
                        'Give me cum or give me death',
                        'Elon\'s Musk',
                        'Jesus Crust',
                        'Stealing donations from the Cum-Czar\'s trust',
                        'A cum smoothie gulped smoothly',
                        'Consume the cum chalice',
                        'Fuck everyone named Alex',
                        'David Hayter',
                        'Cum Crusador',
                        'The Holy Cum Wars',
                        'Razor-blade Masturbator',
                        'Margret Thatcher',
                        'The Cum Snatcher',
                        'Father drowned',
                        'Going down on the cum clown',
                        'Prolapse pounding',
                        'Toothpick sounding',
                        'Cum baking',
                        'My nipple-pussy is aching',
                        'Cum fooler',
                        'Semen drooler',
                        'Forbidden cum-spice',
                        'Your shit-box looks nice!',
                        'Life is a cage, and death is the key',
                        'All your cum are belong to me',
                        'Normalize crying over spilt cum',
                        'Making cum-angels with my son',
                        'I fucked a fairy in half',
                        'How many holes does a human have?',
                        'My butt and cunny are in agony',
                        'Castration in the sky',
                        'Your penis will fly',
                        'Scrotal chambers',
                        'Semen sailors',
                        'Mommy\'s cum tax',
                        'Grind my balls on an axe!',
                        'Cum-scented candle',
                        'Cum-broiled eggs',
                        'Cum-Christ consciousness',
                        'Third-eye, cum spy',
                        'Cum-scrote sailboat',
                        'Semen speed racer',
                        'Off-road cum chode',
                        'My uterus came out!',
                        'Cum treasurer',
                        'Dick measurer',
                        'Irresponsible Manager of Cum',
                        'A cum-slave, back from the grave',
                        'The price for breaking a cum-oath',
                        'James Hector',
                        'Cum key-lector (or collector, vote in comments)',
                        'I tripped in the cum-keeper\'s crypt',
                        'Cum feeder',
                        'Moist meter',
                        'Sans Undertale, the cum reaper',
                        'Fucking a skeleton, right in the pussy',
                        'The Dark Souls of cum',
                        'Cum-framed, and cum-blamed',
                        'Cum-drowning awareness day',
                        'Brewing cum-fuel after school',
                        'Your nipples are crunchy',
                        'The tragic cum-sponge',
                        'Your cum is fading...',
                        'Sweep up the cum flakes, Joan']
        msg = message.content
        msg = msg.casefold()
        msg = msg.replace(" ", "")
        for item in trigger:
            if item in msg:
                print(f'[+]Trigger word detected by {message.author.name} : {message.content}')
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                if message.author.id != 256713166149386240:
                    await message.channel.send(random.choice(responses))
                elif message.author.id == 256713166149386240:
                    await message.channel.send(random.choice(altresponses))
        for item in easter:
            if item in msg:
                print(f'[+]C U M word detected by {message.author.name} : {message.content}')
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                if message.author.id != 256713166149386240:
                    await message.channel.send(random.choice(cumresponses))


def setup(bot):
    bot.add_cog(EventsCog(bot))
