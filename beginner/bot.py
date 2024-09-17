import discord
from dotenv import dotenv_values
import requests #make HTTP requests to any URL
import json #allows us to read JSON data

def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data["url"]

#saved the API Key in .env file --> to access the code from other file
config= dotenv_values(".env")

#will interact with the Discord API
class MyClient(discord.Client):
    async def on_ready(self): #when the Discord bot's login is successful- waiting for a message to complete action
        print("Logged on as {0}!".format(self.user))
    
    async def on_message(self, message): #when user types into discord and the bot receives the message- what to do?
        if message.author == self.user: #checks to see if the bot is sending the message in the chat (doesn't reply to its own messages)
            return
        if message.content.startswith("$hello"):
            await message.channel.send("Hello, World!")
        elif message.content.startswith("$meme"):
            await message.channel.send(get_meme())

#settings that determine what the bot has access to      
intents= discord.Intents.default()
intents.message_content= True 

#use token to authenticate access to Discord backend servers so I can function   
client = MyClient(intents=intents)
client.run(config["API_KEY"])