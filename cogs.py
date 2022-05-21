import discord
from discord.ext import commands

# class for tasks like loading, unloading and restarting cogs/modules
# all commands are admin only, so they cannot be abused
class Cogs(commands.Cog):

    def __init__(self, client):
        self.client = client
   
    @commands.command(command = "loadmodule", aliases = ["lm", "load"], description = "Loads a module.")
    @commands.has_permissions(administrator = True)
    async def loadmodule (self, ctx, module):
        self.client.load_extension(f"{module}")
        await ctx.send(f"Loaded module {module}.")

    @commands.command(command = "unloadmodule", aliases = ["unload", "ulm"], description = "Unloads a module.")
    @commands.has_permissions(administrator = True)
    async def unloadmodule (self, ctx, module):
        self.client.unload_extension(f"{module}")
        await ctx.send(f"Unloaded module {module}.")

    @commands.command(command = "reloadmodule", aliases = ["reload", "rl"], description = "Reloads a module.")
    @commands.has_permissions(administrator = True)
    async def reloadmodule (self, ctx, module):
        self.client.unload_extension(f"{module}")
        self.client.load_extension(f"{module}")
        await ctx.send(f"Reloaded module {module}.")


def setup(client):
    client.add_cog(Cogs(client))