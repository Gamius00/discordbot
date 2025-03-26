import asyncio
import os
import discord
from convex import ConvexClient
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import date
import schedule
from discord import ActivityType
import time
from datetime import datetime
from random import *
from dotenv import load_dotenv
from quickchart import QuickChart

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)
name = None
did_ask_for_name = False
names = []
random = randint(0, 3)
list = ["✅", "💻", "🔒", "🔐"]
current_url = ""

load_dotenv(".env")
load_dotenv("../.env")

async def job():
    guild = client.get_guild(1086939783374315530)
    load_dotenv(".env")
    CONVEX_URL = os.getenv("CONVEX_URL")
    convex = ConvexClient(CONVEX_URL)
    convex.mutation("setData:createEntry", {"count": guild.member_count})
    data = ConvexClient(CONVEX_URL).query("getData:getInfo")

    member_counts = {}
    result_count = []
    labels = []
    month = ""

    for item in data:
        timestamp = int(item.get("_creationTime", 0))
        date = datetime.fromtimestamp(timestamp / 1000)
        day = int(date.strftime("%d"))
        month = date.strftime("%B ")

        member_counts[day] = item.get("MemberCount", 0)

    start_date = min(member_counts.keys())
    end_date = max(member_counts.keys())

    complete_counts = []
    for day in range(start_date, end_date + 1):
        if complete_counts:
            complete_counts.append(member_counts.get(day, complete_counts[-1]))
        else:
            complete_counts.append(member_counts.get(day, 0))

        labels.append(month + str(day))

    for day in labels:
        if len(labels) > 4:
            result_count.append(day.split(" ")[1])

        else:
            result_count.append(day)


    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 8
    qc.config = {
        "type": "line",
        "data": {
            "labels": result_count,
            "datasets": [{
                "label": "Member Count",
                "data": complete_counts,
                "fill": "false"
            }]
        }
    }
    current_url = qc.get_url()

    channel = client.get_channel(1354542371655782604)
    await channel.send(current_url)

def sync_job():
     asyncio.create_task(job())

@client.event
async def on_ready():
    print("Gamius (1069597015899643944) ist jetzt startklar.")
    sync = await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=ActivityType.listening, name="Creative Programmers"))
    schedule.every(30).day.do(sync_job)
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)


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

        await test()

@client.event
async def on_member_join(member):
    channel_log = client.get_channel(1345087784364282009)
    channel_general = client.get_channel(1086948239414153286)
    role = member.guild.get_role(1094284980089278564)
    guild = member.guild
    time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    member_count = guild.get_channel(1345097985213857823)
    await member.add_roles(role)
    embedVar = discord.Embed(title=f"Member: {member} joined!", description="")
    embedVar.add_field(name="Joined at: ", value=time, inline=False)
    embedVar.add_field(name="Current member count: ", value=guild.member_count, inline=False)
    await channel_log.send(embed=embedVar)
    await channel_general.send(f"Hello {member}! We are {guild.member_count} members now! You can introduce yourself in the 👋 introductions channel!")
    await member_count.edit(name="Member Count: " + str(guild.member_count))

@client.event
async def on_member_remove(member):
    channel_log = client.get_channel(1345087784364282009)
    guild = member.guild
    time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    member_count = guild.get_channel(1345097985213857823)
    embedVar = discord.Embed(title=f"Member: {member} left!", description="")
    embedVar.add_field(name="Left at: ", value=time, inline=False)
    embedVar.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"), inline=False )
    embedVar.add_field(name="Current member count: ", value=guild.member_count, inline=False)
    await channel_log.send(embed=embedVar)
    await member_count.edit(name="Member Count: " + str(guild.member_count))




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
            channel = client.get_channel(payload.channel_id)  # Get the channel
            message = await channel.fetch_message(payload.message_id)
            await message.remove_reaction(payload.emoji, member)

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

                            names.remove(member.id)

                        elif close == False and user.id not in team:
                            await message.remove_reaction("🔒", user)
                            await user.send("**Please wait until this ticket has been claimed or a moderator closes this ticket. \nYou can't close the ticket because we don't want one person to open too many tickets!**")

                        elif close == False and user.id in team:
                            close = True
                            await channel.delete()

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

@client.tree.command(name="echo", description="The Bot say that you write")
async def echo(interaction: discord.Interaction, message: str, channel: discord.TextChannel= None):
    if channel == None:
        channel = interaction.channel
    else:
        channel = channel
    await interaction.response.send_message(content="Message sended succesful!", ephemeral=True)
    await channel.send(message)

client.run(os.getenv("DISCORD_TOKEN"))

