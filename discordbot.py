from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import asyncio
import youtube_dl
import random
load_dotenv()


PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!play'):
        song_url = message.content[6:]
        voice_channel = message.author.voice.channel
        voice = await voice_channel.connect()
        player = await voice.create_ytdl_player(song_url)
        player.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('안녕'):
        await message.channel.send('안녕')

    if message.content.startswith('구기'):
        await message.channel.send('부르지마')

    if message.content.startswith('뭐해'):
        await message.channel.send('뭐하는지 왜 궁굼해')
    
    if message.content.startswith('그냥'):
        await message.channel.send('어쩔티비')

    if message.content.startswith('수진'):
        await message.channel.send('바보')

    if message.content.startswith('야'):
        responses = ['호', '왜 불러', '부르지 마']
        await message.channel.send(random.choice(responses))

    if message.content.startswith('구기바보'):
        responses = ['너 우수진이지', '우수진바보', '우수진바보 똥개 멍청이']
        await message.channel.send(random.choice(responses))

    if message.content.startswith('수진바보'):
        responses = ['인졍~~~', 'ㄹㅇㅋㅋ', '우수진바보 똥개 멍청이']
        await message.channel.send(random.choice(responses))

    if message.content.startswith('$dm'):
        user = message.mentions[0]
        await user.send('Private Message')
        
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server!'
    )

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(
        f'Goodbye {member.mention}. We will miss you!'
    )



try:
    client.run('MTAwODkyOTExMjU0MDMxOTgzNQ.GdrFxg.XZlXjPvoGQsvA-hhVQyAsYdhyD4UwbK1c2NAIw')
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
