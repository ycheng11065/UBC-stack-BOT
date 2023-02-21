import discord
import os

import navibot as nb
from navibot import NaviBot
from page_tree import PageTree


TOKEN_FILE_PATH = "C:/Users/mashi/Desktop/bot_token.txt"
LOADING_FOOTER_TEXT = "LOADING NOW"


# Adds reactions appropriately, while not attempting to add the ones displayed already
# adds option buttons first, in order as given in bot.option buttons;
# and then adds number buttons
async def add_bot_reactions(bot, old_reactions=None):
    for button in (list(bot.option_buttons.values()) + bot.number_buttons):
        if (old_reactions == None) or (button not in old_reactions):
            await bot.curr_msg.add_reaction(button)

# Removes reactions appropriately, given the next reactions to be displayed;
# removes every reaction currently put, except those which are also displayed next
async def remove_bot_reactions(bot, old_reactions, new_reactions=None):
    for reaction in old_reactions:
        if (new_reactions == None) or (reaction not in new_reactions):
            await bot.curr_msg.remove_reaction(reaction, bot.user)

# Adds a footer indicating we're loading things.
async def display_loading_in_embed(curr_msg, curr_embed):
    curr_embed.remove_footer()
    curr_embed.set_footer(text=LOADING_FOOTER_TEXT)
    return await curr_msg.edit(embed=curr_embed)


# Fetching token to run the discord bot
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


@bot.command()
async def menu(ctx):
    # 0) setting up: starting note is set to the root of tree
    #  & update the current node's embed, and set the set of buttons (= the number of its children)
    bot.setUp(ctx.author)
    curr_embed = bot.create_curr_node_embed()

    bot.curr_msg = await ctx.send(embed=curr_embed)

    await add_bot_reactions(bot)


@bot.event
async def on_reaction_add(reaction, user):
    # if reaction by the bot itself / self.curr_msg is None / user not user who started bot, ignore
    if ((user == bot.user) or (bot.curr_msg == None) or (user != bot.user_using_now) or 
        # if reaction not in the button options, ignore
        ((reaction.emoji not in bot.number_buttons) and 
         (reaction.emoji not in bot.option_buttons.values())) ):
        return
    
    # otherwise
    # 1) get the user's reaction and fetch the according next node
    await display_loading_in_embed(bot.curr_msg, bot.create_curr_node_embed())

    user_reaction_num = None

    # process the additional buttons FIRST
    if (reaction.emoji == bot.option_buttons[nb.BACK_BUTTON_NAME]):
        if len(bot.stack) != 0:
            next_node = bot.stack.pop()
        else:
            next_node = bot.curr_node

    elif (reaction.emoji == bot.option_buttons[nb.MENU_BUTTON_NAME]):
        next_node = PageTree.get_root()
        bot.stack.append(bot.curr_node)

    elif (reaction.emoji == bot.option_buttons[nb.CLOSE_BUTTON_NAME]):
        await bot.curr_msg.delete()
        exit(0)

    else:
        for i in range(len(bot.number_buttons)):
            if reaction.emoji == bot.number_buttons[i]:
                user_reaction_num = i
                break
        next_node = bot.curr_node.list_children[user_reaction_num]
        bot.stack.append(bot.curr_node)

    # 2) update the current node to the next node, update embed, and set the number of buttons (= the number of its children)
    bot.curr_node = next_node
    curr_embed = bot.create_curr_node_embed()

    old_number_buttons = bot.number_buttons
    bot.number_buttons = nb.ALL_BUTTONS[0:len(bot.curr_node.list_children)]        
    
    # 3) remove all buttons that are not needed
    # remove reaction by user first
    await bot.curr_msg.remove_reaction(reaction, bot.user_using_now)
    # then remove all reactions that will not be in the next node
    await remove_bot_reactions(bot, old_number_buttons, bot.number_buttons)

    # 4) display the new embed and add buttons
    bot.curr_msg = await display_loading_in_embed(bot.curr_msg, curr_embed)
    # add appropriate reactions
    await add_bot_reactions(bot, old_number_buttons + list(bot.option_buttons.values()))
    # Remove the display of LOADING
    bot.curr_msg = await bot.curr_msg.edit(embed=bot.create_curr_node_embed())



# REALLY HERE FOR DEBUG
@bot.command()
async def kill(ctx):
    if bot.curr_msg:
        await bot.curr_msg.delete()
    exit(0)


# Running the actual bot
try:
    bot.run(my_secret)
except:
    os.system("kill 1")
