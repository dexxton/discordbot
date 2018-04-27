# Crubot by dest
import requests
import discord
import asyncio

from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("011001100010001")
    print ("loading//.." + bot.user.name + ", Awaiting your command")
    
@bot.event
async def on_member_join(member):
    await bot.send_message(bot.get_channel('INSERTWELCOMECHANNELID'), " Welcome {0.mention}, I am the CRU Bot..Enjoy your time here. Please do your best to, message in the relevant chat server, and Respect one another. For a list of commands type !cmdlist" .format(member))
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:  " + bot.user.name + ", Awaiting your command $$$")

@bot.command(pass_context=True)
async def cmdlist(ctx):
    embed = discord.Embed(title="The following are valid commands", color=0x42f4cb)
    embed.add_field(name="!cmdlist", value="Get cmdlist message", inline=False)
    embed.add_field(name="!ping", value="Get a bot responce", inline=False)
    embed.add_field(name="!cru", value="Get the price of Curium", inline=False)
    embed.add_field(name="!btc", value="Get the price of bitcoin", inline=False)
    embed.add_field(name="!ltc", value="Get the price of Litecoin", inline=False)
    embed.add_field(name="!difficulty", value="Get the current CRU difficulty ", inline=False)
    embed.add_field(name="!blockcount", value="Get the current CRU blockcount ", inline=False)
    embed.add_field(name="!hashrate", value="Get the current CRU Network Hashrate (h/s) ", inline=False)
    embed.add_field(name="!supply", value="Get the current CRU supply ", inline=False)
    embed.add_field(name="which coin gunna do goddest", value="type CRU", inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cru(ctx):
    btcapi = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    btcprice = requests.get(btcapi)
    value = btcprice.json()['bpi']['USD']['rate']
    await bot.say("Current Curium price is: $" + CRUprice)    
    
@bot.command(pass_context=True)
async def btc(ctx):
    btcapi = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    btcprice = requests.get(btcapi)
    value = btcprice.json()['bpi']['USD']['rate']
    await bot.say("Current Bitcoin price is: $" + value)

@bot.command(pass_context=True)
async def ltc(ctx):
    url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
    response = requests.get(url)
    value = response.json()[0]['price_usd']
    await bot.say("Current Litecoin price is: $" + value)

@bot.command(pass_context=True)
async def difficulty(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getdifficulty'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU difficulty:" + value)

@bot.command(pass_context=True)
async def blockcount(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getblockcount'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU blockcount:" + value)

@bot.command(pass_context=True)
async def hashrate(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getnetworkhashps'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU Network Hashrate (h/s):" + value)

@bot.command(pass_context=True)
async def supply(ctx):
    ckapi = 'https://explorer.curiumofficial.com/ext/getmoneysupply'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU supply:" + value)

@bot.listen()
async def on_message(message):
    if message.content.startswith('cru'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> cha ching :moneybag: :dollar:" % (userID))


bot.run("TYPEYOURTOKENHERE")
