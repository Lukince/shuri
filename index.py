import discord
client = discord.Client()
import random
from captcha. image import ImageCaptcha
import os

#Answer = 0

def Record_Content(content, author, channel):
    var channels = client.get_channel(667756919129112586)
    await channels.send(author+"님이 "+channel+"에서 "+content+"라고 하였습니다.")

@client.event

async def on_ready():
    print("Shuri is Ready!")
    game = discord.Game("채팅 검열중 :face_with_monocle:")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event

async def on_message(message):
    if (message.content.find('시발련아') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('닥쳐') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('니얼굴이민철') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('이민철') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('니애미') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('섹스') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('세에엑스') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    elif (message.content.find('개새끼') > -1):
        Record_Content(message.content, message.author.username, message.channel.name)
    """
    if message.content.startswith("=인증"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("시간 초과")
            return

        if msg.content == a:
            await message.channel.send("인증되었습니다.")
            if message.guild.id == '453949981502472203':
                await message.guild.get_member(message.author.id).add_roles(discord.utils.get(message.guild.roles, name="user"))
        else:
            await message.channel.send("인증에 실패하였습니다. 다시 시도해 주세요.")
'''
        if message.content[4:6] == '문제':
            msg = ""
            await message.channel.send('자 문제 나갑니다!')
            FirstN = random.randint(0, 100)
            SecondN = random.randint(1, 100)
            Calc = random.randint(0, 3)
            if message.content[7:] == '/':
                Calc = 3
            if Calc == 0:
                Answer = FirstN + SecondN
                await message.channel.send(str(FirstN) + '+' + str(SecondN))
            if Calc == 1:
                Answer = FirstN - SecondN
                await message.channel.send(str(FirstN) + '-' + str(SecondN))
            if Calc == 2:
                Answer = FirstN * SecondN
                await message.channel.send(str(FirstN) + '×' + str(SecondN))
            if Calc == 3:
                Answer = int((FirstN / SecondN) * 100) / 100
                await message.channel.send(str(FirstN) + '÷' + str(SecondN))
            await message.channel.send('정답은?')
            def claculate(msg):
                return msg.author == message.author and msg.channel == message.channel

            try:
                msg = await client.wait_for("message", timeout=30, check=claculate)
            except:
                await message.channel.send("시간 초과! 답은 " + str(Answer) + " 이였습니다!")
                return

            if msg.content == str(Answer):
                await message.channel.send("정답입니다! :white_check_mark:")
            else:
                await message.channel.send("틀렸습니다! :x: 정답은 " + str(Answer) + " 입니다!")
'''
"""
BOT_TOKEN = os.environ("BOT_TOKEN")
client.run(BOT_TOKEN)
