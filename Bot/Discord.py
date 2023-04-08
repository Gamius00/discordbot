import asyncio

import discord
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import date
from discord import ActivityType
from datetime import datetime
from random import *

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".", intents=intents)
name = None
did_ask_for_name = False
names = []
moderatoren = [726409024894926869, 779381502311137301]
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
                    channel = client.get_channel(1020625253275275304)
                    await channel.send(embed=embedVar)
                    await client.process_commands(message)

                    if message.channel.name.startswith("ticket") or message.channel.name.startswith("claim") :
                        channel = client.get_channel(1020627023808434197)
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

@client.command()
async def changenick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed to {member.mention}')

@client.command()
async def report(ctx, member: discord.Member, Nachweis, * ,discription):
    if Nachweis.startswith("https://"):
        await ctx.message.delete()
        zeit = date.today()
        await ctx.author.send(f'You have report {member.mention} on ' + str(zeit) + ' because of: ' + '"' + discription + '". \nOur Team check that!')
        channel = client.get_channel(1020625253275275304) #ID des jeweiligen Channels
        embedVar2 = discord.Embed(title="Report", description=str(client.user.name) + " (" + str(client.user.id) + ")" + " have reported " + member.mention , color=797979)
        embedVar2.add_field(name="Reason", value=discription, inline=False)
        embedVar2.add_field(name="Proof", value=Nachweis, inline=False)
        embedVar2.add_field(name="Day", value=zeit, inline=False)
        embedVar2.add_field(name="Procedure", value="Press ✅ to chancel the report or press ❌ to caution the user! ", inline=False)
        message = await channel.send(embed=embedVar2)
        guild: discord.Guild = client.get_guild(982704251732123699)
        channel = discord.TextChannel = guild.get_channel(1020625253275275304)
        #Emoji Hinzufügen
        await message.add_reaction('✅')
        await message.add_reaction('❌')

        while True:

            reaction, user = await client.wait_for('reaction_add')
            if user != message.author and str(reaction.emoji) == '✅' and reaction.message.id == message.id:
                            embedVar4 = discord.Embed(title="Bearbeitet von " + str(user),
                                                          description="Die Meldung von " + str(client.user.name) + " (" + str(
                                                              client.user.id) + ") " + "wurde abgebrochen am " + str(zeit),
                                                          color=189018)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar4)

            elif user != message.author and str(reaction.emoji) == '❌' and reaction.message.id == message.id:
                            embedVar3 = discord.Embed(title="Bearbeitet von " + str(user),
                                                          description="Die Meldung von " + str(client.user.name) + " (" + str(
                                                              client.user.id) + ") " + "wurde angnommen am " + str(
                                                              zeit) + ". Gemeldet wurde " + str(member) + " wegen " + discription,
                                                          color=990001)
                            await message.clear_reactions()
                            await message.edit(embed=embedVar3)
                            await member.send("Du wurdest auf folgendem Server gemeldet: " + str(guild.name) + " wegen " + discription + ". Wir haben intern entschieden dich zu ...")

    else:
        await ctx.message.delete()
        await ctx.author.send("Bitte gebe einen Link zu der Nachricht an. Sollte es diese Nachricht nicht mehr geben, gib bitte den Kanal an in welchem das Ereignis geschehen ist!")


@client.command()
async def ticket(ctx,*, frage):

    member = ctx.message.author
    Mod = get(member.guild.roles, name="🔧| Moderator")
    guild = ctx.message.guild

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True),
        Mod: discord.PermissionOverwrite(view_channel=True)
    }

    if ctx.author.id not in names:
            names.append(ctx.author.id)
            await ctx.message.delete()
            print("[Gelöscht] " + "(" + str(client.user.id) + ") " + str(ctx.message.content))
            guild = ctx.message.guild
            channel = await guild.create_text_channel('ticket-' + str(ctx.author.name), overwrites=overwrites)
            client.get_channel(channel)
            embed = discord.Embed(title="Ticket von " + str(ctx.author) + " (" + str(ctx.author.id) + ") ", description="Anliegen: " + str(frage))
            embed.add_field(name="Es wird sich so schnell wie möglich ein Teammitglied bei dir melden!" + "", value="", inline=False)
            embed.add_field(name="Beanspruchungsstatus ❌", value="", inline=False)
            embed.add_field(name="🔒 Schließen", value="", inline=False)
            embed.add_field(name="🖱️ Beanspruchen", value="", inline=False)
            embed.set_footer(text="© Gamius", icon_url="https://cdn.discordapp.com/attachments/1072590655202791525/1072590882110455860/Profilbild_Discord.png")
            message = await channel.send(embed=embed)
            await message.add_reaction("🔒")
            await message.add_reaction("🖱️")
            close = False

            while True:

                reaction, user = await client.wait_for("reaction_add")

                if reaction.emoji == "🔒" and user != client.user and reaction.message.id == message.id:
                         if close == True:
                            await channel.delete()
                            print("Das Ticket von: " + str(client.user.id) + " wurde geschlossen.")
                            names.remove(ctx.author.id)

                         elif close == False and user.id not in moderatoren:
                             await message.remove_reaction("🔒", user)
                             await user.send("**Warte bitte bis dieses Ticket geclaimt wurde oder ein Moderator dieses Ticket schließt. \nDu kannst das Ticket nicht schließen, da wir nicht möchten \ndas eine Person zu viele Tickets öffnet! **")

                         elif close == False and user.id in moderatoren:
                                 close = True
                                 await channel.delete()
                                 print("Das Ticket von: " + str(client.user.id) + " wurde geschlossen.")
                                 names.remove(ctx.author.id)

                elif reaction.emoji == "🖱️" and user != client.user and reaction.message.id == message.id:
                    if user.id in moderatoren:
                        await message.clear_reaction("🖱️")
                        embed2 = discord.Embed(title="Ticket von " + str(user) + " (" + str(user.id) + ") ",description="Anliegen: " + str(frage))
                        embed2.add_field(name="**Das Ticket wurde von " + str(user) + " beansprucht.**",value="", inline=False)
                        embed2.add_field(name="Beanspruchungsstatus ✅", value="",inline=False)
                        embed2.add_field(name="🔒 Schließen", value="", inline=False)
                        embed2.set_footer(text="© Gamius" ,icon_url="https://cdn.discordapp.com/attachments/1072590655202791525/1072590882110455860/Profilbild_Discord.png")
                        await message.edit(embed=embed2)
                        await channel.edit(name="claim " + str(user.name))
                        close = True

                    else:
                        await message.remove_reaction("🖱️", user)
                        await user.send("**Du kannst das Ticket nicht claimen, dies können nur Moderatoren.**")


    else:
        await ctx.message.delete()
        await ctx.author.send("**Es ist bereits ein Ticket von dir geöffnet!**")

token = open("api.key", "r")
client.run(token.read())

