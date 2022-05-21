import discord
import os
import random
from discord import file
from discord import colour
from discord import message
from discord.ext import commands
from help import MyNewHelp # import custom help command

client = commands.Bot(command_prefix="Insert a command prefix of your choice here", help_command=MyNewHelp())

@client.event
async def on_ready():
    print("Bot Online.")
    
    client.load_extension("cog_template") # load extensions
    client.load_extension("cogs")
    
    activity = discord.Activity(name="your every move!", type=discord.ActivityType.watching) # change status to something funny
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user: # if message is from the bot itself, dont process it
        return
    
    await client.process_commands(message)

@client.command(
    help = "Use {Put your chosen command here} to send a random image"
    brief = "Sends a random image to the channel"
)
async def insert_the_command_you_want_here(ctx): # Just sends an images and doesn't ping anyone
   path = "replace this witht the path where the images are located." # path where images are located
   files = os.listdir(path)
   image = random.choice(files) # returns the name of a random image from the folder
   file = discord.File(f"replace this with the path where the images are located\\{image}", filename="image.png")
   embed = discord.Embed(title="Insert a title for the embedd here", color=discord.Color.blurple())   
   embed.set_image(url="attachment://image.png")
   await ctx.send(file=file, embed=embed)
@client.command(
    help = "Use {Put your chosen command here} and mention someone to send a random image while pinging someone"
    brief = "Sends a random image to the channel and pings the mentioned user"
)
async def insert_the_command_you_want_here(ctx, target:discord.User = None): #you can mention someone in the message to make the bot ping them when sending the image
    path = "replace this witht the path where the images are located." # path where images are located
    files = os.listdir(path)
    image = random.choice(files) # returns the name of a random image from the folde
    if target == None:
        file = discord.File(f"replace this with the path where the images are located\\{image}", filename="image.png")
        embed = discord.Embed(title="Add a message here if you want", color=discord.Color.orange())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    else:
        file = discord.File(f"replace this with the path where the images are located\\{image}", filename="image.png")
        embed = discord.Embed(title=f"Insert a message for the user you are pinging here" ,color=discord.Color.orange())
        embed.set_image(url="attachment://image.png")
        await ctx.send(target.mention,file=file, embed=embed)


token = "Insert your bot token here"
client.run(token)


