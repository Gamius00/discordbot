import asyncio
import os
import discord
from convex import ConvexClient
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
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)
name = None
did_ask_for_name = False
names = []
random = randint(0, 3)
list = ["✅", "💻", "🔒", "🔐"]

load_dotenv(".env")

@client.event
async def on_ready():
    print("Gamius (1069597015899643944) ist jetzt startklar.")
    sync = await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=ActivityType.listening, name="Creative Programmers"))


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
    guild = client.get_guild(1086939783374315530)
    modrole = discord.utils.get(guild.roles, name="🛡️ | Moderator")
    adminrole = discord.utils.get(guild.roles, name="🎓 | Admin")
    members = modrole.members
    admin = adminrole.members
    moderatoren = [modmember.id for modmember in members]
    admin = [adminmember.id for adminmember in admin]
    team = moderatoren + admin

    async def test():

        if interaction.user == member:
            await member.edit(nick=nick)
            await interaction.response.send_message(content=f'Nickname from user {member} was changed to {member.mention}', ephemeral=True)

        elif interaction.user != member and interaction.user.id in team:
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

        elif interaction.user != member and interaction.user.id in team:
            await member.edit(nick=None)
            await interaction.response.send_message(content=f'Nickname from user {member} was reseted', ephemeral=True)

        else:
            await interaction.response.send_message(content="Du hast leider nicht die nötigen Rechte um den Nickname von " + str(member) + " zu ändern!", ephemeral=True)
    else:
        await test()

@client.tree.command(name="report", description="report command")
async def report(interaction: discord.Interaction, member: discord.Member,description: str, proof: str ):
    nutzer = interaction.user

    if proof.startswith("https://"):
        zeit = date.today()
        await interaction.response.send_message(content=f'You have report {member.mention} on ' + str(zeit) + ' because of: ' + '"' + description + '". \nOur Team check that!', ephemeral=True)
        channel = client.get_channel(1094744985175347260) #ID des jeweiligen Channels
        embedVar2 = discord.Embed(title="Report", description=str(nutzer.name) + " (" + str(nutzer.id) + ")" + " have reported " + member.mention , color=797979)
        embedVar2.add_field(name="Reason", value=description, inline=False)
        embedVar2.add_field(name="Proof", value=proof, inline=False)
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
                                                          description="The report by " + str(user.name) + " (" + str(
                                                              user.id) + ") " + "was cancelled on " + str(zeit),
                                                          color=189018)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar4)

            elif user != message.author and str(reaction.emoji) == '❌' and reaction.message.id == message.id:
                            embedVar3 = discord.Embed(title="Edited by " + str(user),
                                                          description="The report by " + str(user.name) + " (" + str(
                                                              user.id) + ") " + "was adopted on " + str(
                                                              zeit) + ". Has been reported: " + str(member) + " because of " + description,
                                                          color=990001)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar3)
                            await member.send("You was reported at " + str(guild.name) + " because " + description)

    else:
        await interaction.response.send_message(content="Please provide a link to the message. If this message no longer exists, please enter the channel in which the event happened!", ephemeral=True)

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(1086939783374315530)
    modrole = discord.utils.get(guild.roles, name="🛡️ | Moderator")
    adminrole = discord.utils.get(guild.roles, name="🎓 | Admin")
    members = modrole.members
    admin = adminrole.members
    moderatoren = [modmember.id for modmember in members]
    admin = [adminmember.id for adminmember in admin]
    team = moderatoren + admin

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

                        elif close == False and user.id not in team:
                            await message.remove_reaction("🔒", user)
                            await user.send("**Please wait until this ticket has been claimed or a moderator closes this ticket. \nYou can't close the ticket because we don't want one person to open too many tickets!**")

                        elif close == False and user.id in team:
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

@client.command()
async def start(message):
    user = client.get_user(726409024894926869)
    if message.author.id == 779381502311137301:
        while True:
            await user.send("Du kannst jetzt Bumpen")
            await asyncio.sleep(7200)




@client.tree.command(name="help", description="This ist the Help command!")
async def help(interaction: discord.Interaction):
    embedVar = discord.Embed(title="Help Command",
                             description="")
    embedVar.add_field(name="/report {user} proof(link) reason", value="",
                       inline=False)
    embedVar.add_field(name="/changenick {member} {new nick}", value="", inline=False)
    embedVar.add_field(name="/userinfo", value="", inline=False)
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
async def createpoll(interaction: discord.Interaction, question: str, option1: str, option2: str, anonymous: str=None, option3: str=None, max_select: int=None):
    option1count = 0
    option2count = 0
    option3count = 0
    maxcount = 0
    polllist = []
    member = interaction.user
    channel = client.get_channel(1095786723872608337)
    await interaction.response.send_message(content="Poll created successful!", ephemeral=True)

    if option3 == None:
        message = await channel.send("<@&" + str(1096397761865334864) + ">")
        await message.delete()
        embed = discord.Embed(title=question, description="",
                              color=discord.Color.blue())
        embed.add_field(name="1️⃣ " + option1, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • 0 0%", inline=False)
        embed.add_field(name="2️⃣ " + option2, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • 0 0%", inline=False)
        if max_select == None or max_select == 1:
            embed.add_field(name="Select one", value="", inline=False)
        elif max_select == 2:
            embed.add_field(name="Select two", value="", inline=False)
        elif max_select == 3:
            embed.add_field(name="Select three", value="", inline=False)
        embed.add_field(name="`📊` Votes 0", value="", inline=False)
        embed.set_footer(text="Created by " + str(interaction.user))
        message = await channel.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        channel = client.get_channel(1098303576276733972)
        cembed = discord.Embed(title="Cancel", description="",
                               color=discord.Color.red())
        cembed.add_field(name="Press \❌ for Cancel", value="", inline=False)
        cembed.add_field(name="Pollquestion", value=question, inline=False)
        cembed.add_field(name="Created by", value=interaction.user, inline=False)
        cembedmessage = await channel.send(embed=cembed)
        await cembedmessage.add_reaction("❌")

        while True:
            reaction, user = await client.wait_for("reaction_add")
            if reaction.emoji == "❌" and reaction.message.id == cembedmessage.id:
                await cembedmessage.clear_reactions()
                embed = discord.Embed(title=question, description="Poll was cancelled",
                                       color=discord.Color.red())

                highest_count = max(option1count, option2count, option3count)

                if highest_count == option1count:
                    embed.add_field(name="The most votes had " + option1, value="Votes " + str(option1count), inline=False)
                elif highest_count == option2count:
                    embed.add_field(name="The most votes had " + option2, value="Votes " + str(option2count), inline=False)
                else:
                    embed.add_field(name="The most votes had " + option3, value="Votes " + str(option3count), inline=False)

                embed = await message.edit(embed=embed)
                await message.clear_reactions()
            if user.id not in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                if reaction.emoji == "1️⃣":
                    option1count = option1count + 1
                if reaction.emoji == "2️⃣":
                    option2count = option2count + 1

                ergebnis = option1count + option2count
                a = option1count/ergebnis
                b = option2count/ergebnis

                polllist.append(user.id)
                if max_select == 2 and maxcount == 0:
                    maxcount = 2
                    polllist.remove(user.id)
                embed2 = discord.Embed(title=question, description="",
                                      color=discord.Color.blue())
                if a == 0:
                    embed2.add_field(name="1️⃣ " + option1,value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 5 and round(a * 100) < 15:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 15 and round(a * 100) < 25:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 25 and round(a * 100) < 35:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 35 and round(a * 100) < 45:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛`  • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 45 and round(a * 100) < 55:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 55 and round(a * 100) < 65:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 65 and round(a * 100) < 75:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 75 and round(a * 100) < 85:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 85 and round(a * 100) < 95:
                    embed2.add_field(name="1️⃣ " + option1, value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 95 and round(a * 100) <= 100:
                    embed2.add_field(name="1️⃣ " + option1,value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)

                if b == 0:
                    embed2.add_field(name="2️⃣ " + option2,value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 5 and round(b * 100) < 15:
                    embed2.add_field(name="1️2️⃣ " + option2,value="`🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 15 and round(b * 100) < 25:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 25 and round(b * 100) < 35:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 35 and round(b * 100) < 45:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛`  • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 45 and round(b * 100) < 55:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 55 and round(b * 100) < 65:
                    embed2.add_field(name="1️2️⃣ " + option2,value="`🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 65 and round(b * 100) < 75:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 75 and round(b * 100) < 85:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 85 and round(b * 100) < 95:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 95 and round(b * 100) <= 100:
                    embed2.add_field(name="2️⃣ " + option2,value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦` • " + str(option2count) + " " + str(round(b * 100)) + "%", inline=False)

                if max_select == None or max_select == 1:
                    embed2.add_field(name="Select one", value="", inline=False)
                elif max_select == 2:
                    embed2.add_field(name="Select two", value="", inline=False)
                embed2.add_field(name="`📊` Votes " + str(ergebnis), value="", inline=False)
                embed2.set_footer(text="Created by " + str(interaction.user))
                message = await message.edit(embed=embed2)
                if anonymous == None or anonymous == "on":
                    pass
                elif anonymous == "off" or anonymous == "no" or anonymous == "No" or anonymous == "Off":
                    channel = client.get_channel(1095792970315333652)
                    await channel.send(str(user) + " have votet for " + reaction.emoji + " The poll question is: " + question)

            elif user.id in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                await user.send(content="You have already voted.")

    else:
        message = await channel.send("<@&" + str(1096397761865334864) + ">")
        await message.delete()
        embed = discord.Embed(title=question, description="",
                              color=discord.Color.blue())
        embed.add_field(name="1️⃣ " + option1, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • 0 0%", inline=False)
        embed.add_field(name="2️⃣ " + option2, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • 0 0%", inline=False)
        embed.add_field(name="3️⃣ " + option3, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • 0 0%", inline=False)
        if max_select == None or max_select == 1:
            embed.add_field(name="Select one", value="", inline=False)
        elif max_select == 2:
            embed.add_field(name="Select two", value="", inline=False)
        elif max_select == 3:
            embed.add_field(name="Select three", value="", inline=False)
        embed.add_field(name="`📊` Votes 0", value="", inline=False)
        embed.set_footer(text="Created by " + str(interaction.user))
        message = await channel.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        channel = client.get_channel(1098303576276733972)
        cembed = discord.Embed(title="Cancel", description="",
                              color=discord.Color.red())
        cembed.add_field(name="Press \❌ for Cancel", value="", inline=False)
        cembed.add_field(name="Pollquestion", value=question, inline=False)
        cembed.add_field(name="Created by", value=interaction.user, inline=False)
        cembedmessage = await channel.send(embed=cembed)
        await cembedmessage.add_reaction("❌")

        while True:
            reaction, user = await client.wait_for("reaction_add")
            if reaction.emoji == "❌" and reaction.message.id == cembedmessage.id:
                await cembedmessage.clear_reactions()
                embed = discord.Embed(title=question, description="Poll was cancelled",
                                       color=discord.Color.red())

                highest_count = max(option1count, option2count, option3count)

                if highest_count == option1count:
                    embed.add_field(name="The most votes had " + option1, value="Votes " + str(option1count), inline=False)
                elif highest_count == option2count:
                    embed.add_field(name="The most votes had " + option2, value="Votes " + str(option2count), inline=False)
                else:
                    embed.add_field(name="The most votes had " + option3, value="Votes " + str(option3count), inline=False)

                embed = await message.edit(embed=embed)
                await message.clear_reactions()

            if user.id not in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                if reaction.emoji == "1️⃣":
                  option1count = option1count + 1
                if reaction.emoji == "2️⃣":
                    option2count = option2count + 1
                if reaction.emoji == "3️⃣":
                    option3count = option3count + 1

                ergebnis = option1count + option2count + option3count
                a = option1count / ergebnis
                b = option2count / ergebnis
                c = option3count / ergebnis

                polllist.append(user.id)
                if max_select == 2 and maxcount == 0:
                    maxcount = 2
                    polllist.remove(user.id)
                elif max_select == 3 and maxcount != 2:
                    polllist.remove(user.id)
                    maxcount = maxcount + 1

                embed2 = discord.Embed(title=question, description="",
                                      color=discord.Color.blue())
                if a == 0:
                    embed2.add_field(name="1️⃣ " + option1, value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 5 and round(a * 100) <= 15:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 15 and round(a * 100) < 25:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 25 and round(a * 100) < 35:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 35 and round(a * 100) < 45:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛`  • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 45 and round(a * 100) < 55:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 55 and round(a * 100) < 65:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 65 and round(a * 100) < 75:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 75 and round(a * 100) < 85:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 85 and round(a * 100) < 95:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)
                elif round(a * 100) >= 95 and round(a * 100) <= 100:
                    embed2.add_field(name="1️⃣ " + option1,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦` • " + str(option1count) + " " + str(
                                         round(a * 100)) + "%", inline=False)

                if b == 0:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 5 and round(b * 100) < 15:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 15 and round(b * 100) < 25:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 25 and round(b * 100) < 35:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 35 and round(b * 100) < 45:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛`  • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 45 and round(b * 100) < 55:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 55 and round(b * 100) < 65:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 65 and round(b * 100) < 75:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 75 and round(b * 100) < 85:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 85 and round(b * 100) < 95:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)
                elif round(b * 100) >= 95 and round(b * 100) <= 100:
                    embed2.add_field(name="2️⃣ " + option2,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦` • " + str(option2count) + " " + str(
                                         round(b * 100)) + "%", inline=False)

                if c == 0:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 5 and round(c * 100) < 15:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 15 and round(c * 100) < 25:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 25 and round(c * 100) < 35:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 35 and round(c * 100) < 45:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛`  • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 45 and round(c * 100) < 55:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 55 and round(c * 100) < 65:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 65 and round(c * 100) < 75:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 75 and round(c * 100) < 85:
                    embed2.add_field(name="2️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 85 and round(c * 100) < 95:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)
                elif round(c * 100) >= 95 and round(c * 100) <= 100:
                    embed2.add_field(name="3️⃣ " + option3,
                                     value="`🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛` • " + str(option3count) + " " + str(
                                         round(c * 100)) + "%", inline=False)

                if max_select == None or max_select == 1:
                    embed2.add_field(name="Select one", value="", inline=False)
                elif max_select == 2:
                    embed2.add_field(name="Select two", value="", inline=False)
                elif max_select == 3:
                    embed2.add_field(name="Select three", value="", inline=False)
                embed2.add_field(name="`📊` Votes " + str(ergebnis), value="", inline=False)
                embed2.set_footer(text="Created by " + str(interaction.user))
                message = await message.edit(embed=embed2)
                if anonymous == None or anonymous == "on":
                    pass
                elif anonymous == "off" or anonymous == "no" or anonymous == "No" or anonymous == "Off":
                    channel = client.get_channel(1095792970315333652)
                    await channel.send(str(user) + " have votet for " + reaction.emoji + " The question is: " + question)

            elif user.id in polllist and reaction.message.id == message.id:
                await message.remove_reaction(reaction, user)
                await user.send(content="You have already voted.")

@client.tree.command(name="echo", description="The Bot say that you write")
async def echo(interaction: discord.Interaction, message: str, channel: discord.TextChannel= None):
    if channel == None:
        channel = interaction.channel
    else:
        channel = channel
    await interaction.response.send_message(content="Message sended succesful!", ephemeral=True)
    await channel.send(message)

@client.tree.command(name="test", description="This is a DataBase Test")
async def test(interaction: discord.Interaction, channel: discord.TextChannel= None):
    load_dotenv(".env.local")
    CONVEX_URL = os.getenv("CONVEX_URL")
    data = str(ConvexClient(CONVEX_URL).query("getData:get"))
    
    if channel == None:
        channel = interaction.channel
    else:
        channel = channel
    await channel.send(data)

client.run(os.getenv("DISCORD_TOKEN"))

