import discord
from discord.ext import commands
import os
from help import EmbedHelpCommand
import windows
import files_manager
import asyncio


ARROW_LEFT = "⬅"
ARROW_RIGHT = "➡"
ONE = "1️⃣"
TWO = "2️⃣"
THREE = "3️⃣"
FOUR = "4️⃣"
FIVE = "5️⃣"
SIX = "6️⃣"
SEVEN = "7️⃣"
EIGHT = "8️⃣"
NINE = "9️⃣"
TEN = "🔟"

BACK_ICON = ARROW_LEFT
MENU_ICON = "⏪"

BACK_BUTTON_NAME = "back_button"
MENU_BUTTON_NAME = "menu_button"
NUMBER_BUTTONS_NAME = "number_buttons"

ALL_BUTTONS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN]

my_secret = os.environ['key']  # Our token for discord bot to run

def create_embed(curr_menu, author):
  embed_to_return = discord.Embed(title=curr_menu.title)
  embed_to_return.set_footer(text=f'Hi {author}')
  for field in curr_menu.list_selection:
    embed_to_return.add_field(name=field["field_name"],
                              value=field["field_value"],
                              inline=field["field_inline"])
  return embed_to_return

def add_button(dict_buttons, button_name, button_emoji):
  dict_buttons[button_name] = button_emoji

additional_buttons = {}
add_button(additional_buttons, MENU_BUTTON_NAME, MENU_ICON)
add_button(additional_buttons, BACK_BUTTON_NAME, BACK_ICON)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   help_command=EmbedHelpCommand())


@bot.command()
async def menu(ctx):
  # 0) setting up: starting note is set to the root of tree
  #  & update the current node's embed, and set the set of buttons (= the number of its children)
  stack = []
  curr_node = files_manager.return_root_of_tree()
  curr_embed = create_embed(curr_node, ctx.author)
  curr_num_buttons = len(curr_node.list_children)
  
  number_buttons = ALL_BUTTONS[0:curr_num_buttons]

  curr_msg = await ctx.send(embed=curr_embed)
  

  # loop while execution (might wanna set an ending condition / command)
  while True:

    # 1) display the embed and add buttons
    curr_msg = await curr_msg.edit(embed=curr_embed)

    for button in additional_buttons.values():
        await curr_msg.add_reaction(button)
      
    for button in number_buttons:
        await curr_msg.add_reaction(button)

    # 2) get the user's reaction and fetch the according next node
    try:
        reaction, user = await bot.wait_for(
            "reaction_add",
            check=lambda reaction, user: (user == ctx.author) and ((reaction.emoji in number_buttons) or (reaction.emoji in additional_buttons.values())),
            timeout=60.0)

    except asyncio.TimeoutError:
        embed = create_embed(curr_node, ctx.author)
        embed.set_footer(text="Timed Out.")
        await curr_msg.clear_reactions()
    
    else:

        user_reaction_num = None

        # process the additional buttons FIRST
        if (reaction.emoji == additional_buttons[BACK_BUTTON_NAME]):
          if len(stack) != 0:
            next_node = stack.pop()
          else:
            next_node = curr_node
        
        elif (reaction.emoji == additional_buttons[MENU_BUTTON_NAME]):
          next_node = files_manager.return_root_of_tree()
          print(next_node.title)
          stack.append(curr_node)

        else: 
          for i in range(len(number_buttons)):
              if reaction.emoji == number_buttons[i]:
                user_reaction_num = i
                break 
          next_node = curr_node.list_children[user_reaction_num]
          stack.append(curr_node)
      
    # 3) update the current node to the next node, update embed, and set the number of buttons (= the number of its children)
        curr_node = next_node
        curr_embed = create_embed(curr_node, ctx.author)
        curr_num_buttons = len(curr_node.list_children)
        new_number_buttons = ALL_BUTTONS[0:curr_num_buttons]

      
    # 4) remove all buttons that are not needed
        for button in (list(additional_buttons.values()) + number_buttons):
            await curr_msg.remove_reaction(button, ctx.author)
        for button in number_buttons:
          if button not in new_number_buttons:
            await curr_msg.remove_reaction(button, bot.user)

          # if (len(number_buttons) != len(curr_node.list_children)):

        number_buttons = new_number_buttons
            

        


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  # First menu here


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  print(f'Message from {message.author}: {message.content}')

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  await bot.process_commands(message)


# @bot.event
# async def on_reaction_add(reaction, user):
#   # if user.author == bot.author:
#   #   return
#   # print('Curr page?: ', reaction.message == curr_page)
#   # print('Bot?: ', reaction.author == bot.user)
#   if reaction.emoji == ONE and reaction.message == curr_page:
#     faculty = files_manager.return_root_of_tree()
#     faculty_embed = create_embed(faculty)
#     # await curr_page.remove_reaction(ONE, curr_page.author)
#     # await curr_page.remove_reaction(TWO, curr_page.author)
#     # await curr_page.remove_reaction(THREE, curr_page.author)
#     # await curr_page.edit(embed=faculty_embed)

#     await reaction.message.remove_reaction(ONE, curr_page.author)
#     await reaction.message.remove_reaction(TWO, curr_page.author)
#     await reaction.message.remove_reaction(THREE, curr_page.author)
#     await reaction.message.edit(embed=faculty_embed)

#   elif reaction.emoji == TWO:
#     return

#   elif reaction.emoji == THREE:
#     return


try:
  bot.run(my_secret)
except:
  os.system("kill 1")
