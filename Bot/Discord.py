import asyncio
import os
import discord
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import date
from discord import ActivityType
from datetime import datetime
from random import *
from dotenv import load_dotenv

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
    synced = await client.tree.sync()

@client.event
async def on_message(message):

        async def test():

            if client.user == message.author:
                return

            elif message.author.bot:
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
            await message.channel.send(embed=embedVar, ephemeral=True)

        await test()

@client.tree.command(name="changenick", description="With this command you can change your nick at this Server!")
async def changenick(interaction: discord.Interaction, nick: str, member: discord.Member=None):
    async def test():
        if interaction.user == member:
            await member.edit(nick=nick)
            await interaction.response.send_message(content=f'Nickname from user {member} was changed to {member.mention}', ephemeral=True)

        elif interaction.user != member and interaction.user.id in moderatoren:
            await member.edit(nick=nick)
            await interaction.response.send_message(content=f'Nickname from user {member} was changed to {member.mention}', ephemeral=True)

        else:
            await interaction.response.send_message(content="Du hast leider nicht die nötigen Rechte um den Nickname von " + str(member) + " zu ändern!", ephemeral=True)

    if member == None:
        member = interaction.user
        await member.edit(nick=nick)
        await interaction.response.send_message(content=f'Nickname from user {member} was changed to {member.mention}', ephemeral=True)

    elif nick == "reset":
        if interaction.user == member:
            await member.edit(nick=None)
            await interaction.response.send_message(content=f'Nickname from user {member} was reseted', ephemeral=True)

        elif interaction.user != member and interaction.user.id in moderatoren:
            await member.edit(nick=None)
            await interaction.response.send_message(content=f'Nickname from user {member} was reseted', ephemeral=True)

        else:
            await interaction.response.send_message(content="Du hast leider nicht die nötigen Rechte um den Nickname von " + str(member) + " zu ändern!", ephemeral=True)
    else:
        await test()

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

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    member = payload.member

    if payload.emoji.name == "✉️":
        if message_id == 1095439527516065843:
            member = member
            Mod = get(member.guild.roles, name="🛡️ | Moderator")
            guild = member.guild

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                member: discord.PermissionOverwrite(view_channel=True),
                Mod: discord.PermissionOverwrite(view_channel=True)
            }

            async def code():
                names.append(member.id)
                guild = member.guild
                channel = await guild.create_text_channel('ticket-' + str(member.id), overwrites=overwrites)
                client.get_channel(channel)
                message = await channel.send("<@" + str(member.id) + ">")
                await message.delete()
                embed = discord.Embed(title="Ticket by " + str(member) + " (" + str(member.id) + ") ", description="")
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
                            names.remove(member.id)

                        elif close == False and user.id not in moderatoren:
                            await message.remove_reaction("🔒", user)
                            await user.send("**Please wait until this ticket has been claimed or a moderator closes this ticket. \nYou can't close the ticket because we don't want one person to open too many tickets!**")

                        elif close == False and user.id in moderatoren:
                            close = True
                            await channel.delete()
                            print("The Ticket of: " + str(client.user.id) + " wurde geschlossen.")
                            names.remove(member.id)

                    elif reaction.emoji == "🖱️" and user != client.user and reaction.message.id == message.id:
                        if user.id in moderatoren:
                            await message.clear_reaction("🖱️")
                            embed2 = discord.Embed(
                                title="Ticket by " + str(member) + " (" + str(member.id) + ") ",
                                description="")
                            embed2.add_field(name="**The Ticket was claimed by " + str(user) + "**", value="",
                                             inline=False)
                            embed2.add_field(name="Claimstatus ✅", value="", inline=False)
                            embed2.add_field(name="🔒 Close", value="", inline=False)
                            embed2.set_footer(text="© Gamius",
                                              icon_url="https://cdn.discordapp.com/attachments/1072590655202791525/1072590882110455860/Profilbild_Discord.png")
                            await message.edit(embed=embed2)
                            await channel.edit(name="claim " + str(user.name))
                            close = True

                        else:
                            await message.remove_reaction("🖱️", user)
                            await user.send("**You can´t claim the Ticket. Only moderators can do that.**")

            if member.id not in names:
                await code()

            else:

                for channel in member.guild.channels:
                    if channel.name == "ticket-" + str(member.id):
                        await member.send("**There is already a ticket open from you!**")
                        return

                for channel in member.guild.channels:
                    if channel.name != "ticket-" + str(member.id):
                        await code()
                        return


@client.command()
async def reset(message):
    names.clear()

@client.tree.command(name="help", description="This ist the Help command!")
async def help(interaction: discord.Interaction):
    embedVar = discord.Embed(title="Help Command",
                             description="")
    embedVar.add_field(name=".report {user} proof(link) reason", value="",
                       inline=False)
    embedVar.add_field(name=".ticket {question}", value="", inline=False)
    embedVar.add_field(name=".changenick {member} {new nick}", value="", inline=False)
    time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    embedVar.set_footer(text="© Gamius",
                        icon_url="https://cdn.discordapp.com/attachments/1020628377243242537/1091686027598495855/logo-6062235_960_720.png")
    await interaction.response.send_message(embed=embedVar, ephemeral=True)

@client.tree.command(name="userinfo", description="Sends informations on a user")
async def unserinfo(interaction: discord.Interaction, member: discord.Member=None):
    if member == None:
        member = interaction.user

    roles = [role for role in member.roles]
    embed = discord.Embed(title="User Info", description=f"Here is the info on the user {member.mention}", color = discord.Color.green())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value= member.id)
    embed.add_field(name="Name", value=f"{member.name}#{member.discriminator}")
    embed.add_field(name="Nickname", value= member.display_name)
    embed.add_field(name="Created at", value=member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    embed.add_field(name="Joined At", value= member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    embed.add_field(name="Top Role", value=member.top_role.mention)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name="createpoll", description="Teammember can create a poll!")
async def createpoll(interaction: discord.Interaction, question: str, option1: str, option2: str, option3: str=None):
    option1count = 0
    option2count = 0
    option3count = 0
    polllist = []
    member = interaction.user
    channel = client.get_channel(1095672565281865728)
    await interaction.response.send_message(content="Poll created successful!", ephemeral=True)

    if option3 == None:
        embed = discord.Embed(title=question, description="",
                              color=discord.Color.blue())
        embed.add_field(name="1️⃣ " + option1, value="• 0")
        embed.add_field(name="2️⃣ " + option2, value="• 0")
        embed.set_footer(text="Created by " + str(interaction.user))
        message = await channel.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        while True:
            reaction, user = await client.wait_for("reaction_add")
            if user.id not in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                if reaction.emoji == "1️⃣":
                    option1count = option1count + 1
                if reaction.emoji == "2️⃣":
                    option2count = option2count + 1

                polllist.append(user.id)
                embed2 = discord.Embed(title=question, description="",
                                      color=discord.Color.blue())
                embed2.add_field(name="1️⃣ " + option1, value="• " + str(option1count))
                embed2.add_field(name="2️⃣ " + option2, value="• " + str(option2count))
                embed2.set_footer(text="Created by " + str(interaction.user))
                message = await message.edit(embed=embed2)

            elif user.id in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                await user.send(content="You have already voted.")

    else:
        embed = discord.Embed(title=question, description="",
                              color=discord.Color.blue())
        embed.add_field(name="1️⃣ " + option1, value="• 0")
        embed.add_field(name="2️⃣ " + option2, value="• 0")
        embed.add_field(name="3️⃣ " + option3, value="• 0")
        embed.set_footer(text="Created by " + str(interaction.user))
        message = await channel.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")

        while True:
            reaction, user = await client.wait_for("reaction_add")
            if user.id not in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                if reaction.emoji == "1️⃣":
                    option1count = option1count + 1
                if reaction.emoji == "2️⃣":
                    option2count = option2count + 1
                if reaction.emoji == "3️⃣":
                    option3count = option3count + 1

                polllist.append(user.id)
                embed2 = discord.Embed(title=question, description="",
                                      color=discord.Color.blue())
                embed2.add_field(name="1️⃣ " + option1, value="• " + str(option1count))
                embed2.add_field(name="2️⃣ " + option2, value="• " + str(option2count))
                embed2.add_field(name="2️⃣ " + option3, value="• " + str(option3count))
                embed2.set_footer(text="Created by " + str(interaction.user))
                message = await message.edit(embed=embed2)

            elif user.id in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                await user.send(content="You have already voted.")

client.run(os.getenv("DISCORD_TOKEN"))

