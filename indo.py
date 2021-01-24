import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("켜짐")

@client.event
async def on_message(message):
    if message.content.startswith("!서버온"):
        await message.channel.send("@everyone 서버온입니다 다이렉트주소:connect cfx.re/join/oja5yy")
    if message.content.startswith("!서버오프"):
        await message.channel.send("@everyone 서버오프라인입니다")
    if message.content.startswith("!서버리붓"):
        await message.channel.send("@everyone 서버가 리붓중입니다 잠시만 기달려주세요")
    if message.content.startswith("!서버점검"):
        await message.channel.send("@everyone 서버가 점검중입니다 잠시만 기달려주세요")












access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
