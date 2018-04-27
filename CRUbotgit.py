# Crubot by dest
# trollboxbot by dest
import requests
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game

# "!" is the command trigger
bot = commands.Bot(command_prefix='!')

# on start up bot will print this data with its user name
@bot.event
async def on_ready():
    print ("011001100010001")
    print ("loading//.." + bot.user.name + ", Awaiting your command")

 # on member join will send a message to incoming user greeting them.. (still in progress may not work)
 # dont forget to put the channel id# in the code too
@bot.event
async def on_member_join(member):
    await bot.send_message(bot.get_channel('YOUNEEDCHANNELID#HERE'), " Welcome" + bot.user.name + " , at your service, type !cmdlist for a list of commands")

#embed list of commands
@bot.command(pass_context=True)
async def cmdlist(ctx):
    embed = discord.Embed(title="The following are valid commands", color=0x42f4cb)
    embed.add_field(name="!cmdlist", value="Get cmdlist message", inline=False)
    embed.add_field(name="!ping", value="Get a bot responce", inline=False)
    embed.add_field(name="!btc", value="Get the price of bitcoin", inline=False)
    embed.add_field(name="!ltc", value="Get the price of Litecoin", inline=False)
    embed.add_field(name="!difficulty", value="Get the current CRU difficulty ", inline=False)
    embed.add_field(name="!blockcount", value="Get the current CRU blockcount ", inline=False)
    embed.add_field(name="!hashrate", value="Get the current CRU Network Hashrate (h/s) ", inline=False)
    embed.add_field(name="!supply", value="Get the current CRU supply ", inline=False)
    embed.add_field(name="!installguide", value="Get the Masternode install guide ", inline=False)
    embed.add_field(name="which coin gunna do goddest", value="type CRU", inline=False)
    await bot.say(embed=embed)

# ping the bot command to test
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:  " + bot.user.name + ", Awaiting your command $$$")

# get the latest masternode install guide
@bot.command(pass_context=True)
async def installguide(ctx):
    await bot.say("Here is the latest masternode install guide version https://e-rave.nl/curium-master-node-setup-cold-wallet")

# get the current price of btc
@bot.command(pass_context=True)
async def btc(ctx):
    btcapi = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    btcprice = requests.get(btcapi)
    value = btcprice.json()['bpi']['USD']['rate']
    await bot.say("Current Bitcoin price is: $" + value)

# get the current price of ltc
@bot.command(pass_context=True)
async def ltc(ctx):
    url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
    response = requests.get(url)
    value = response.json()[0]['price_usd']
    await bot.say("Current Litecoin price is: $" + value)

# retun the current Currium difficulty
@bot.command(pass_context=True)
async def difficulty(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getdifficulty'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU difficulty:" + value)

# return the current curium block count
@bot.command(pass_context=True)
async def blockcount(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getblockcount'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU blockcount:" + value)

# return the current curium hashrate
@bot.command(pass_context=True)
async def hashrate(ctx):
    ckapi = 'https://explorer.curiumofficial.com/api/getnetworkhashps'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU Network Hashrate (h/s):" + value)

# return the current curium supply amount
@bot.command(pass_context=True)
async def supply(ctx):
    ckapi = 'https://explorer.curiumofficial.com/ext/getmoneysupply'
    response = requests.get(ckapi).json()
    value = str(response)
    await bot.say("Current CRU supply:" + value)

# listen for someone to say cru then message them 
@bot.listen()
async def on_message(message):
    if message.content.startswith('cru'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> cha ching :moneybag: :dollar:" % (userID))
        
# alt way to get latest install guide
@bot.listen()
async def on_message(message):
    if message.content.startswith('install-guide'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Here is the latest Masternode install guide https://e-rave.nl/curium-master-node-setup-cold-wallet" % (userID))

bot.run("TYPEYOURTOKENHERE")
