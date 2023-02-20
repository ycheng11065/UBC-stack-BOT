import discord
from discord.ext import commands
import os
import files_manager
import asyncio

#Need to time out the others once we've used it up already

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
CLOSE_ICON = "❌"

BACK_BUTTON_NAME = "back_button"
MENU_BUTTON_NAME = "menu_button"
CLOSE_BUTTON_NAME = "close_button"
NUMBER_BUTTONS_NAME = "number_buttons"

ALL_BUTTONS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN]

my_secret = "MTA3Njk0MTEzMjE5OTY0MTEwOA.GTm3Ud.WMsils4ApqHxPP-El4fGQQQGzNYnixXE8KScVg"  # Our token for discord bot to run


#helper functions
def create_embed(node, author):
  embed_to_return = discord.Embed(title=node.title)
  for field in node.list_selection:
    embed_to_return.add_field(name=field["field_name"],
                              value=field["field_value"],
                              inline=field["field_inline"])
  embed_to_return.set_footer(text=f'Hi {author}')

  return embed_to_return


#helper functions 2
def add_button(dict_buttons, button_name, button_emoji):
  dict_buttons[button_name] = button_emoji


# Returns very first page
def getFirstPage():
  return files_manager.return_root_of_tree()


class NaviBot(commands.Bot):
  additional_buttons = None
  curr_node = None
  number_buttons = []
  stack = []
  curr_msg = None
  user_using_now = None

  def __init__(self, *args, **kwargs):
    super(NaviBot, self).__init__(*args, **kwargs)
    self.setUp()

  # Sets up the bot such that it has additional buttons, current node and
  # other attributes initialized; should run each time we call menu
  def setUp(self, user_using_now=None):
    #Add additional buttons
    self.additional_buttons = {}
    add_button(self.additional_buttons, MENU_BUTTON_NAME, MENU_ICON)
    add_button(self.additional_buttons, BACK_BUTTON_NAME, BACK_ICON)
    add_button(self.additional_buttons, CLOSE_BUTTON_NAME, CLOSE_ICON)

    #Setup the current node
    self.curr_node = getFirstPage()

    #Setup the stack
    self.stack = []

    #Setup the user to a single person
    if user_using_now:
      self.user_using_now = user_using_now


if __name__ == "__main__":

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
    curr_embed = create_embed(bot.curr_node, ctx.author)
    curr_num_buttons = len(bot.curr_node.list_children)

    bot.number_buttons = ALL_BUTTONS[0:curr_num_buttons]

    bot.curr_msg = await ctx.send(embed=curr_embed)

    for button in bot.additional_buttons.values():
      await bot.curr_msg.add_reaction(button)

    for button in bot.number_buttons:
      await bot.curr_msg.add_reaction(button)

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
      curr_embed = create_embed(bot.curr_node, bot.user_using_now)
      bot.curr_msg = await bot.curr_msg.edit(embed=curr_embed)

      for button in bot.additional_buttons.values():
        await bot.curr_msg.add_reaction(button)

      for button in bot.number_buttons:
        await bot.curr_msg.add_reaction(button)

      # 2) get the user's reaction and fetch the according next node
      user_reaction_num = None

      # process the additional buttons FIRST
      if (reaction.emoji == bot.additional_buttons[BACK_BUTTON_NAME]):
        if len(bot.stack) != 0:
          next_node = bot.stack.pop()
        else:
          next_node = bot.curr_node

      elif (reaction.emoji == bot.additional_buttons[MENU_BUTTON_NAME]):
        next_node = getFirstPage()
        bot.stack.append(bot.curr_node)

      elif (reaction.emoji == bot.additional_buttons[CLOSE_BUTTON_NAME]):
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
      curr_embed = create_embed(bot.curr_node, bot.user_using_now)
      curr_num_buttons = len(bot.curr_node.list_children)
      new_number_buttons = ALL_BUTTONS[0:curr_num_buttons]

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

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

    await bot.process_commands(message)

  try:
    bot.run(my_secret)
  except:
    os.system("kill 1")
