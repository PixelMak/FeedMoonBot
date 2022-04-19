from discord.ext import commands, tasks
import discord
from discord.message import DeletedReferencedMessage
import authorization
from datetime import datetime, timedelta
import random
import re

bot = commands.Bot(command_prefix='')

global guild
global channel

MainGuildID = 793208749133135873
MainChannelID = 965930019438358529
BullyUser = 269125504185925633
food_list = [   ':green_apple:',
                ':apple:',
                ':pear:',
                ':tangerine:',
                ':lemon:',
                ':banana:',
                ':watermelon:',
                ':grapes:',
                ':blueberries:',
                ':strawberry:',
                ':melon:',
                ':cherries:',
                ':peach:',
                ':mango:',
                ':pineapple:',
                ':coconut:',
                ':kiwi:',
                ':tomato:',
                ':eggplant:',
                ':avocado:',
                ':olive:',
                ':broccoli:',
                ':leafy_green:',
                ':bell_pepper:',
                ':cucumber:',
                ':hot_pepper:',
                ':corn:',
                ':carrot:',
                ':garlic:',
                ':onion:',
                ':potato:',
                ':sweet_potato:',
                ':croissant:',
                ':bagel:',
                ':bread:',
                ':french_bread:',
                ':flatbread:',
                ':pretzel:',
                ':cheese:',
                ':egg:',
                ':cooking:',
                ':butter:',
                ':pancakes:',
                ':waffle:',
                ':bacon:',
                ':cut_of_meat:',
                ':poultry_leg:',
                ':meat_on_bone:',
                ':hotdog:',
                ':hamburger:',
                ':fries:',
                ':pizza:',
                ':sandwich:',
                ':stuffed_flatbread:',
                ':falafel:',
                ':taco:',
                ':burrito:',
                ':tamale:',
                ':salad:',
                ':shallow_pan_of_food:',
                ':fondue:',
                ':canned_food:',
                ':spaghetti:',
                ':ramen:',
                ':stew:',
                ':curry:',
                ':sushi:',
                ':bento:',
                ':dumpling:',
                ':oyster:',
                ':fried_shrimp:',
                ':rice_ball:',
                ':rice:',
                ':rice_cracker:',
                ':fish_cake:',
                ':fortune_cookie:',
                ':moon_cake:',
                ':oden:',
                ':dango:',
                ':shaved_ice:',
                ':ice_cream:',
                ':icecream:',
                ':pie:',
                ':cupcake:',
                ':cake:',
                ':birthday:',
                ':custard:',
                ':lollipop:',
                ':candy:',
                ':chocolate_bar:',
                ':popcorn:',
                ':doughnut:',
                ':cookie:',
                ':chestnut:',
                ':peanuts:',
                ':honey_pot:',
                ':milk:',
                ':baby_bottle:',
                ':coffee:',
                ':tea:',
                ':teapot:',
                ':mate:',
                ':bubble_tea:',
                ':beverage_box:',
                ':cup_with_straw:',
                ':sake:',
                ':beer:',
                ':beers:',
                ':champagne_glass:',
                ':wine_glass:',
                ':tumbler_glass:',
                ':cocktail:',
                ':tropical_drink:',
                ':takeout_box:']
feeded = False

alarm_time = ['07:00','12:00','16:00']#24hrs

@bot.event
async def on_ready():
    global guild
    global channel
    print(f'{bot.user.name} has connected to Discord!')
    guild = bot.get_guild(MainGuildID)
    channel = guild.get_channel(MainChannelID)

@bot.event
async def on_message(message):
    global channel
    if (message.content == 'more' and message.channel == channel):
        await channel.send('{}'.format(message.author.mention))
        await channel.send(random.choice(food_list))

    if (message.content == 'feed' and message.channel == channel):
        await channel.send(f'<@{BullyUser}>')
        await channel.send(random.choice(food_list))
    
    if (message.content > 'feed' and message.channel == channel):
        for id in re.findall(r'\d+',message.content):
            await channel.send(f'<@{id}>')
            await channel.send(random.choice(food_list))

@bot.listen()
async def on_ready():
    task_loop.start()

@tasks.loop(seconds=2)
async def task_loop():
    global feeded
    global channel
    f = '%H:%M'
    now = datetime.strftime(datetime.now(), f)
    for feed_time in alarm_time:
        diff = (datetime.strptime(feed_time, f) - datetime.strptime(now, f)).total_seconds()
        if diff == 0.0:
            break

    if diff == 0.0:
        if not feeded:
            await channel.send(f'Food time <@{BullyUser}>')
            await channel.send(random.choice(food_list))
        feeded = True
    else:
        feeded = False

bot.run(authorization.getkey())