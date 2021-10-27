# from keep_alive import keep_alive
import discord
import random
import os
import asyncio


client = discord.Client()

verbose = True


@client.event
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
async def on_voice_state_update(member, before, after):
    user = member
    voice_channel = user.voice.channel
    
    if (voice_channel != None and before.channel != after.channel):
        try:
            vc = await voice_channel.connect()
            await asyncio.sleep(0.2)
            audio_source = discord.FFmpegPCMAudio('voice_2.mp3')
            vc.play(audio_source,after=None)
            vc.source.volume = 10.0
            await asyncio.sleep(2)
            await vc.disconnect()
        except:
            print('erroR')
    return


@client.event
async def on_message(message):
    global verbose
    mentions = message.mentions
    if message.author == client.user:
        return

    if message.content == '!阿致嘴閉閉':
        if verbose:
            await message.channel.send('好啊都這樣')
            verbose = False
        else:
            await message.channel.send('到底想怎樣')
        return
    
    if message.content == '!阿致回來':
        if not verbose:
            await message.channel.send('想不到吧')
            verbose = True
        else:
            await message.channel.send('回你媽')
        return

    for member in mentions:
        if member.id == 429658144042516480:
            await message.channel.send('閉嘴啦魂爆')
            return

    # if client.get_user(429658144042516480) in mentions:
    #     await message.channel.send('閉嘴啦魂爆')
    #     return

    if 'chi' in message.content.lower() and verbose:
        await message.channel.send('閉嘴啦魂爆')
        return
    
    if message.content.startswith('!把') and message.content.endswith('關廁所'):
        for member in mentions:
            await member.move_to(client.get_channel(876115972325507072))
            await message.channel.send('<@'+str(member.id)+'> 下去')
        return

    if message.content == '!阿致吸奶':
        user = message.author
        voice_channel = user.voice.channel
        if voice_channel != None:
            try:
                vc = await voice_channel.connect()
                await asyncio.sleep(0.5)
                audio_source = discord.FFmpegPCMAudio('voice_1.mp3')
                vc.play(audio_source,after=None)
                vc.source.volume = 10.0
                # while not player.is_done():
                #     await asyncio.sleep(1)
                # player.stop()
                await asyncio.sleep(2)
                await vc.disconnect()
            except:
                print('erroR')
        return
    
    if message.content == '!垃圾遊戲':
        user = message.author
        voice_channel = user.voice.channel
        if voice_channel != None:
            try:
                vc = await voice_channel.connect()
                await asyncio.sleep(0.5)
                audio_source = discord.FFmpegPCMAudio('voice_2.mp3')
                vc.play(audio_source,after=None)
                vc.source.volume = 10.0
                # while not player.is_done():
                #     await asyncio.sleep(1)
                # player.stop()
                await asyncio.sleep(2)
                await vc.disconnect()
            except:
                print('erroR')
        return

    a_msg = ['哭啊', '不是誒老哥', '誒你剛有看到嗎 我剛很強吧', '外掛啦外掛', '這對面很有水準誒','我要吐了']

    if random.choice([1, 2, 3]) == 1 and verbose:
        await message.channel.send(random.choice(a_msg))

client.run(os.environ['BOT_TOKEN'])

