import discord
import random
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!!')

staff=["587146787807166485","336180549192515585","323289739505696768", "348397583783297024","553039764723466290","445972271828303873","685792823416455188","595235685024399360","607222952114651148"]

@bot.event
async def on_ready():
    print("FELIXER ONLINE")

@bot.event
async def on_message(ctx):
    if ctx.channel.id == 705475626592895007:
        if ctx.content.upper() == ('AGREE'):
            roles = [role.name for role in ctx.author.roles]
            if "Accepted Rules" in roles :
                await ctx.delete()
            else :
                msg = await ctx.channel.send("YOU ARE QUALIFIED, YOU HAVE NOW ACCESS TO THE SERVER, ENJOY!:heart: {}".format(ctx.author.mention))
                print ("QUALIFIED MEMBER")
                await asyncio.sleep(5)
                await msg.delete()
        mod_roles = [role.name for role in ctx.author.roles]
        if "ᵕ̈♡˳೫˚∗ admins" in mod_roles:
            pass
        elif "⋆¸*ೃ☼ mods" in mod_roles :
            pass
        elif ctx.author.id == 698691257828114443:
            pass
        else :
            await ctx.delete()


bot.run("TOKEN")
