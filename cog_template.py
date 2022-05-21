import discord
from discord.ext import commands

class ExampleCog(commands.Cog):

    def __init__(self, client):
        self.client = client
   
    @commands.command(command = 'test')
    async def test(self, ctx):
        await ctx.send("test")
    
def setup(client):
    client.add_cog(ExampleCog(client))