import asyncio
import os
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import youtube_dl
from datetime import date
from discord import ActivityType
from datetime import datetime
from random import *
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".", intents=intents)
name = None
did_ask_for_name = False
names = []
# Gamius Jabok Kip Dicilucs Aggression Kage
moderatoren = [726409024894926869, 779381502311137301, 211441083434008576, 978739541877878844, 868155018287661117, 263907031084302336]
random = randint(0, 3)
list = ["✅", "💻", "🔒", "🔐"]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=ActivityType.listening, name="Creative Programmers"))
    print("Gamius (1069597015899643944) ist jetzt startklar.")

@client.event
async def on_message(message):

        async def test():

            if client.user == message.author:
                return

            else:
                    embedVar = discord.Embed(title=str(message.author), description="User ID: " + str(message.author.id))
                    embedVar.add_field(name="Message Content", value=message.content,
                                       inline=False)
                    embedVar.add_field(name="Channel ID", value=str(message.channel.id), inline=False)
                    embedVar.add_field(name="Message ID", value=str(message.id), inline=False)
                    time = date.today()
                    embedVar.set_footer(text=time,
                                        icon_url="https://cdn.discordapp.com/attachments/1020628377243242537/1091686027598495855/logo-6062235_960_720.png")
                    channel = client.get_channel(1094923750434156554)
                    await channel.send(embed=embedVar)
                    await client.process_commands(message)

                    if message.channel.name.startswith("ticket") or message.channel.name.startswith("claim") :
                        channel = client.get_channel(1094744773279105067)
                        embedVar = discord.Embed(title="Ticket: " + str(message.channel.name),
                                                 description= "User Name: " + str(message.author.name) + "\nUser ID: " + str(message.author.id))
                        embedVar.add_field(name="Message Content", value=message.content,
                                           inline=False)
                        embedVar.add_field(name="Channel ID", value=str(message.channel.id), inline=False)
                        embedVar.add_field(name="Message ID", value=str(message.id), inline=False)
                        time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        embedVar.set_footer(text=time,
                                            icon_url="https://cdn.discordapp.com/attachments/1020628377243242537/1091686027598495855/logo-6062235_960_720.png")
                        await channel.send(embed=embedVar)

        if message.content == "?help":
            embedVar = discord.Embed(title="Help Command",
                                     description="")
            embedVar.add_field(name=".report {user} proof(link) reason", value="",
                               inline=False)
            embedVar.add_field(name=".ticket {question}", value="", inline=False)
            embedVar.add_field(name=".changenick {member} {new nick}", value="", inline=False)
            time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            embedVar.set_footer(text="© Gamius",
                                icon_url="https://cdn.discordapp.com/attachments/1020628377243242537/1091686027598495855/logo-6062235_960_720.png")
            await message.channel.send(embed=embedVar)

        await test()

@client.command()
async def changenick(ctx, nick):
    await ctx.author.edit(nick=nick)
    await ctx.send(f'Nickname was changed to {ctx.author}')

@client.command()
async def report(ctx, member: discord.Member, Nachweis, * ,discription):
    if Nachweis.startswith("https://"):
        await ctx.message.delete()
        zeit = date.today()
        await ctx.author.send(f'You have report {member.mention} on ' + str(zeit) + ' because of: ' + '"' + discription + '". \nOur Team check that!')
        channel = client.get_channel(1094744985175347260) #ID des jeweiligen Channels
        embedVar2 = discord.Embed(title="Report", description=str(client.user.name) + " (" + str(client.user.id) + ")" + " have reported " + member.mention , color=797979)
        embedVar2.add_field(name="Reason", value=discription, inline=False)
        embedVar2.add_field(name="Proof", value=Nachweis, inline=False)
        embedVar2.add_field(name="Day", value=zeit, inline=False)
        embedVar2.add_field(name="Procedure", value="Press ✅ to cancel the report or press ❌ to caution the user! ", inline=False)
        message = await channel.send(embed=embedVar2)
        guild: discord.Guild = client.get_guild(1086939783374315530)
        channel = discord.TextChannel = guild.get_channel(1020625253275275304)
        #Emoji Hinzufügen
        await message.add_reaction('✅')
        await message.add_reaction('❌')

        while True:

            reaction, user = await client.wait_for('reaction_add')
            if user != message.author and str(reaction.emoji) == '✅' and reaction.message.id == message.id:
                            embedVar4 = discord.Embed(title="Edited by " + str(user),
                                                          description="The report by " + str(client.user.name) + " (" + str(
                                                              client.user.id) + ") " + "was cancelled on " + str(zeit),
                                                          color=189018)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar4)

            elif user != message.author and str(reaction.emoji) == '❌' and reaction.message.id == message.id:
                            embedVar3 = discord.Embed(title="Edited by " + str(user),
                                                          description="The report by " + str(client.user.name) + " (" + str(
                                                              client.user.id) + ") " + "was adopted on " + str(
                                                              zeit) + ". Has been reported: " + str(member) + " because of " + discription,
                                                          color=990001)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar3)
                            await member.send("You was reported at " + str(guild.name) + " because " + discription)

    else:
        await ctx.message.delete()
        await ctx.author.send("Please provide a link to the message. If this message no longer exists, please enter the channel in which the event happened!")


@client.command()
async def ticket(ctx,*, frage):


    member = ctx.message.author
    Mod = get(member.guild.roles, name="🛡️ | Moderator")
    guild = ctx.message.guild

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True),
        Mod: discord.PermissionOverwrite(view_channel=True)
    }

    async def code():
        names.append(ctx.author.id)
        await ctx.message.delete()
        print("[Gelöscht] " + "(" + str(client.user.id) + ") " + str(ctx.message.content))
        guild = ctx.message.guild
        channel = await guild.create_text_channel('ticket-' + str(ctx.author.id), overwrites=overwrites)
        client.get_channel(channel)
        embed = discord.Embed(title="Ticket by " + str(ctx.author) + " (" + str(ctx.author.id) + ") ",
                              description="Reason: " + str(frage))
        embed.add_field(name="A team member will contact you as soon as possible!" + "", value="", inline=False)
        embed.add_field(name="Claimstatus ❌", value="", inline=False)
        embed.add_field(name="🔒 Close", value="", inline=False)
        embed.add_field(name="🖱️ Claim", value="", inline=False)
        embed.set_footer(text="© Gamius",
                         icon_url="https://cdn.discordapp.com/attachments/1072590655202791525/1072590882110455860/Profilbild_Discord.png")
        message = await channel.send(embed=embed)
        await message.add_reaction("🔒")
        await message.add_reaction("🖱️")
        close = False

        while True:

            reaction, user = await client.wait_for("reaction_add")

            if reaction.emoji == "🔒" and user != client.user and reaction.message.id == message.id:
                if close == True:
                    await channel.delete()
                    print("The Ticket of: " + str(client.user.id) + " was closed.")
                    names.remove(ctx.author.id)

                elif close == False and user.id not in moderatoren:
                    await message.remove_reaction("🔒", user)
                    await user.send(
                        "**Please wait until this ticket has been claimed or a moderator closes this ticket. \nYou can't close the ticket because we don't want one person to open too many tickets!**")

                elif close == False and user.id in moderatoren:
                    close = True
                    await channel.delete()
                    print("The Ticket of: " + str(client.user.id) + " wurde geschlossen.")
                    names.remove(ctx.author.id)

            elif reaction.emoji == "🖱️" and user != client.user and reaction.message.id == message.id:
                if user.id in moderatoren:
                    await message.clear_reaction("🖱️")
                    embed2 = discord.Embed(title="Ticket by " + str(ctx.author) + " (" + str(ctx.author.id) + ") ",
                                           description="Reason: " + str(frage))
                    embed2.add_field(name="**The Ticket was claimed by " + str(user) + "**", value="", inline=False)
                    embed2.add_field(name="Claimstatus ✅", value="", inline=False)
                    embed2.add_field(name="🔒 Close", value="", inline=False)
                    embed2.set_footer(text="© Gamius",
                                      icon_url="https://cdn.discordapp.com/attachments/1072590655202791525/1072590882110455860/Profilbild_Discord.png")
                    await message.edit(embed=embed2)
                    await channel.edit(name="claim " + str(user.name))
                    close = True

                else:
                    await message.remove_reaction("🖱️", user)
                    await user.send("**You can´t close the Ticket. Only moderators can do that.**")

    if ctx.author.id not in names:
        await code()

    else:

        for channel in ctx.guild.channels:
            if channel.name == "ticket-" + str(ctx.author.id):
                await ctx.message.delete()
                await ctx.author.send("**There is already a ticket open from you!**")
                return

        for channel in ctx.guild.channels:
            if channel.name != "ticket-" + str(ctx.author.id):
                print("test")
                await code()
                return

@client.command()
async def reset(message):
    names.clear()

@client.command()
async def join(ctx):
    # check if the user is in a voice channel
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        # join the channel
        await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send("You are not in a voice channel")


@client.command()
async def play(ctx, url):
    # check if the user is in a voice channel
    if not ctx.author.voice:
        return await ctx.send("You are not in a voice channel.")

    # get the voice channel
    vc = ctx.author.voice.channel

    # check if the bot is already connected to a voice channel
    if not ctx.voice_client:
        await vc.connect()
    else:
        if ctx.voice_client.channel != vc:
            return await ctx.send("I'm already in a voice channel.")

    # download the audio from YouTube
    ytdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        try:
            info = ytdl.extract_info(url, download=True)
            filename = ytdl.prepare_filename(info)
        except Exception as e:
            return await ctx.send(f"Error: {e}")

    # create the audio source
    source = discord.FFmpegPCMAudio(filename)

    # play the audio
    ctx.voice_client.play(source)

    # send a message to the user
    await ctx.send(f"Now playing: {info['title']}")

client.run(os.getenv("DISCORD_TOKEN"))

