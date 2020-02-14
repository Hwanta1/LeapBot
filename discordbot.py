import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("즐거운 봇만들기")
    await client.change_presence(status=discord.Status.online, activity=game)


    @client.event
    async def on_message(message):
        if message.content.startswith("리프야 안녕"):
            await message.channel.send("난 안반갑지롱~ 아냐 장난이야 안녕!")

        if message.content.startswith("리프야 잘자"):
            await message.channel.send("너도 잘자~ 좋은꿈꿔~")

        if message.content.startswith("리프야 크드는?"):
            await message.channel.send("바보멍청이다!")




client.run("Njc3NDg3MDQyMTAzNjA3Mjk2.XkU9pQ.i85JcUBjE_0oWOoFvI3PiXWZXAE")
