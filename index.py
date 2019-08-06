import discord
client = discord.Client()
import random
from captcha. image import ImageCaptcha
import os

@client.event

async def on_ready():
    print("Ready")
    game = discord.Game("실험체를 생성중...")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event

async def on_message(message):
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
            await message.guild.get_member(message.author.id).add_roles(discord.utils.get(message.guild.roles, name="user"))
        else:
            await message.channel.send("인증에 실패하였습니다. 다시 시도해 주세요.")





        #각각에 print로 로그를 남겨서 작동되는지 확인하고 수정해놓기.
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
