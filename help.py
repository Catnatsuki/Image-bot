import discord, datetime
from discord.ext import commands

# custom help that neatly packs all commands into categories and sends them in an embed
class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color=0xfcba03)
            emby.title = "Help"
            await destination.send(embed=emby)

