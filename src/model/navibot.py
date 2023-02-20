import discord
from discord.ext import commands
from page_tree import PageTree


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


class NaviBot(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  
  # Sets up the bot such that it has additional buttons, current node and
  # other attributes initialized; should run each time we call menu
  def setUp(self, user_using_now=None):
    # declaring the variables
    self.option_buttons = {}
    self.number_buttons = []
    self.curr_msg = None
    self.user_using_now = None

    #Add additional buttons
    self.add_option_button(MENU_BUTTON_NAME, MENU_ICON)
    self.add_option_button(BACK_BUTTON_NAME, BACK_ICON)
    self.add_option_button(CLOSE_BUTTON_NAME, CLOSE_ICON)

    #Setup the current node
    self.curr_node = PageTree.get_root()

    #Setup the stack
    self.stack = []

    #Setup the user to a single person
    if user_using_now:
      self.user_using_now = user_using_now

  # Creates an embed using the current node and current author
  def create_curr_node_embed(self):
    embed_to_return = discord.Embed(title=self.curr_node.title)
    for field in self.curr_node.list_selection:
      embed_to_return.add_field(name=field["field_name"],
                                value=field["field_value"],
                                inline=field["field_inline"])
    embed_to_return.set_footer(text=f'Hi {self.user_using_now}')

    return embed_to_return
  
  # Add an option button to the list
  def add_option_button(self, button_name, button_emoji):
    self.option_buttons[button_name] = button_emoji

  # # Process reactions appropriately
  # def process_action(self, action):



  #   if (user == bot.user_using_now) and (
  #       (reaction.emoji in bot.number_buttons) or
  #       (reaction.emoji in bot.option_buttons.values())):

  #       # 1) display the embed and add buttons
  #       curr_embed = bot.create_curr_node_embed()
  #       bot.curr_msg = await bot.curr_msg.edit(embed=curr_embed)

  #       for button in bot.option_buttons.values():
  #           await bot.curr_msg.add_reaction(button)

  #       for button in bot.number_buttons:
  #           await bot.curr_msg.add_reaction(button)

  #       # 2) get the user's reaction and fetch the according next node
  #       user_reaction_num = None

  #       # process the additional buttons FIRST
  #       if (reaction.emoji == bot.option_buttons[nb.BACK_BUTTON_NAME]):
  #           if len(bot.stack) != 0:
  #               next_node = bot.stack.pop()
  #           else:
  #               next_node = bot.curr_node

  #       elif (reaction.emoji == bot.option_buttons[nb.MENU_BUTTON_NAME]):
  #           next_node = PageTree.get_root()
  #           bot.stack.append(bot.curr_node)

  #       elif (reaction.emoji == bot.option_buttons[nb.CLOSE_BUTTON_NAME]):
  #           bot.curr_msg.delete()
  #           exit(0)

  #       else:
  #           for i in range(len(bot.number_buttons)):
  #               if reaction.emoji == bot.number_buttons[i]:
  #                   user_reaction_num = i
  #                   break
  #           next_node = bot.curr_node.list_children[user_reaction_num]
  #           bot.stack.append(bot.curr_node)

  #       # 3) update the current node to the next node, update embed, and set the number of buttons (= the number of its children)
  #       bot.curr_node = next_node
  #       curr_embed = bot.create_curr_node_embed()
  #       curr_num_buttons = len(bot.curr_node.list_children)
  #       new_number_buttons = nb.ALL_BUTTONS[0:curr_num_buttons]