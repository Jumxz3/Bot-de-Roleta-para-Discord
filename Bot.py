import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        if message.content == "?roleta":  
            pessoa1 = "Nome 1"
            pessoa2 = "Nome 2"
            pessoa3 = "Nome 3"
            pessoas = [pessoa1, pessoa2, pessoa3]

            resultado = random.choice(pessoas)

            
            await message.channel.send(f"O escolhido é: {resultado}")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

client.run('Seu Token')
