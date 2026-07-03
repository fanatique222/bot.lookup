import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est en ligne !")

@bot.command()
async def lookup(ctx, user: discord.User):
    embed = discord.Embed(title="Lookup Discord")
    embed.add_field(name="Pseudo", value=str(user), inline=False)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(
        name="Compte créé le",
        value=user.created_at.strftime("%d/%m/%Y %H:%M"),
        inline=False
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
