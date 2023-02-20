import discord
import os

from src.model import navibot as nb
from model.navibot import NaviBot
from model.page_tree import PageTree


TOKEN_FILE_PATH = "C:/Users/mashi/Desktop/bot_token.txt"

with open(TOKEN_FILE_PATH) as file:
  my_secret = file.read() # Our token for discord bot to run


intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.watching,
                            name="for someone to type !menu")

bot = NaviBot(command_prefix='!',
            activity=activity,
            intents=intents,
            status=discord.Status.idle)

@bot.command()
async def menu(ctx):
    # 0) setting up: starting note is set to the root of tree
    #  & update the current node's embed, and set the set of buttons (= the number of its children)
    bot.setUp(ctx.author)
    curr_embed = bot.create_curr_node_embed()
    curr_num_buttons = len(bot.curr_node.list_children)

    bot.number_buttons = nb.ALL_BUTTONS[0:curr_num_buttons]

    bot.curr_msg = await ctx.send(embed=curr_embed)

    for button in bot.additional_buttons.values():
        await bot.curr_msg.add_reaction(button)

    for button in bot.number_buttons:
        await bot.curr_msg.add_reaction(button)

# REALLY HERE FOR DEBUG
@bot.command()
async def kill(ctx):
    if bot.curr_msg:
        bot.curr_msg.delete()
    exit(0)

@bot.event
async def on_reaction_add(reaction, user):
    # 0) if reaction by the bot itself, ignore
    if user == bot.user:
        return
    # 0.2) if self.curr_msg is None, ignore
    if bot.curr_msg == None:
        return
    
    if (user == bot.user_using_now) and (
        (reaction.emoji in bot.number_buttons) or
        (reaction.emoji in bot.additional_buttons.values())):

        # 1) display the embed and add buttons
        curr_embed = bot.create_curr_node_embed()
        bot.curr_msg = await bot.curr_msg.edit(embed=curr_embed)

        for button in bot.additional_buttons.values():
            await bot.curr_msg.add_reaction(button)

        for button in bot.number_buttons:
            await bot.curr_msg.add_reaction(button)

        # 2) get the user's reaction and fetch the according next node
        user_reaction_num = None

        # process the additional buttons FIRST
        if (reaction.emoji == bot.additional_buttons[nb.BACK_BUTTON_NAME]):
            if len(bot.stack) != 0:
                next_node = bot.stack.pop()
            else:
                next_node = bot.curr_node

        elif (reaction.emoji == bot.additional_buttons[nb.MENU_BUTTON_NAME]):
            next_node = PageTree.get_root()
            bot.stack.append(bot.curr_node)

        elif (reaction.emoji == bot.additional_buttons[nb.CLOSE_BUTTON_NAME]):
            bot.curr_msg.delete()
            exit(0)

        else:
            for i in range(len(bot.number_buttons)):
                if reaction.emoji == bot.number_buttons[i]:
                    user_reaction_num = i
                    break
            next_node = bot.curr_node.list_children[user_reaction_num]
            bot.stack.append(bot.curr_node)

        # 3) update the current node to the next node, update embed, and set the number of buttons (= the number of its children)
        bot.curr_node = next_node
        curr_embed = bot.create_curr_node_embed()
        curr_num_buttons = len(bot.curr_node.list_children)
        new_number_buttons = nb.ALL_BUTTONS[0:curr_num_buttons]

        # 4) remove all buttons that are not needed
        for button in (list(bot.additional_buttons.values()) +
                        bot.number_buttons):
            await bot.curr_msg.remove_reaction(button, bot.user_using_now)
        for button in bot.number_buttons:
            if button not in new_number_buttons:
                await bot.curr_msg.remove_reaction(button, bot.user)

        # if (len(number_buttons) != len(curr_node.list_children)):

        bot.number_buttons = new_number_buttons

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# First menu here?
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'Message from {message.author}: {message.content}')

    await bot.process_commands(message)


# Running the actual bot
try:
    bot.run(my_secret)
except:
    os.system("kill 1")
