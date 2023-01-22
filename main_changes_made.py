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

class NaviBot(commands.Bot):
  additional_buttons = None
  curr_node = None
  numer_buttons = []
  stack = []
  curr_msg = None
    
  #helper functions
  @staticmethod
  def create_embed(node, author):
    embed_to_return = discord.Embed(title=node.title)
    for field in node.list_selection:
      embed_to_return.add_field(name=field["field_name"],
                                value=field["field_value"],
                                inline=field["field_inline"])
    embed_to_return.set_footer(text=f'Hi {author}')
    
    return embed_to_return

  #helper functions 2
  @staticmethod
  def add_button(dict_buttons, button_name, button_emoji):
    dict_buttons[button_name] = button_emoji

  # Returns very first page
  @staticmethod
  def getFirstPage():
    files_manager.return_root_of_tree()

  # Sets up the bot such that it has additional buttons, current node and 
  # other attributes initialized; should run each time we call menu
  def setUp(self):
    #Add additional buttons
    self.additional_buttons = {}
    NaviBot.add_button(self.additional_buttons, MENU_BUTTON_NAME, MENU_ICON)
    NaviBot.add_button(self.additional_buttons, BACK_BUTTON_NAME, BACK_ICON)

    #Setup the current node
    self.curr_node = NaviBot.getFirstPage()

    #Setup the stack
    self.stack = []

  @bot.command()
  async def menu(self, ctx):
    # 0) setting up: starting note is set to the root of tree
    #  & update the current node's embed, and set the set of buttons (= the number of its children)
    self.setUp()
    curr_embed = NaviBot.create_embed(self.curr_node, ctx.author)
    curr_num_buttons = len(self.curr_node.list_children)
    
    self.number_buttons = ALL_BUTTONS[0:curr_num_buttons]
  
    self.curr_msg = await ctx.send(embed=curr_embed)


  @bot.event
  async def on_ready(self):
    print('We have logged in as {0.user}'.format(bot))
    
    # First menu here?


  @bot.event
  async def on_message(self, message):
    if message.author == bot.user:
      return
  
    print(f'Message from {message.author}: {message.content}')
  
    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
  
    await bot.process_commands(message)


  @bot.event
  async def on_reaction_add(self, reaction, user):
    # 0) if reaction by the bot itself, ignore
    if user.author == bot.author:
      return
    # 0.2) if self.curr_msg is None, ignore
    if self.curr_msg == None:
      return
      
    # 1) display the embed and add buttons
    curr_embed = self.curr_node
    self.curr_msg = await self.curr_msg.edit(embed=curr_embed)
  
    for button in self.additional_buttons.values():
        await curr_msg.add_reaction(button)
      
    for button in self.number_buttons:
        await curr_msg.add_reaction(button)
  
    # 2) get the user's reaction and fetch the according next node
    try:
        reaction, user = await bot.wait_for(
            "reaction_add",
            check=lambda reaction, user: (user == ctx.author) and ((reaction.emoji in self.number_buttons) or (reaction.emoji in self.additional_buttons.values())),
            timeout=60.0)
  
    except asyncio.TimeoutError:
        embed = NaviBot.create_embed(self.curr_node, ctx.author)
        embed.set_footer(text="Timed Out.")
        await curr_msg.clear_reactions()
    
    else:
  
        user_reaction_num = None
  
        # process the additional buttons FIRST
        if (reaction.emoji == self.additional_buttons[BACK_BUTTON_NAME]):
          if len(self.stack) != 0:
            next_node = self.stack.pop()
          else:
            next_node = self.curr_node
        
        elif (reaction.emoji == self.additional_buttons[MENU_BUTTON_NAME]):
          next_node = getFirstPage()
          self.stack.append(self.curr_node)
  
        else: 
          for i in range(len(self.number_buttons)):
              if reaction.emoji == self.number_buttons[i]:
                user_reaction_num = i
                break 
          next_node = self.curr_node.list_children[user_reaction_num]
          self.stack.append(self.curr_node)
      
    # 3) update the current node to the next node, update embed, and set the number of buttons (= the number of its children)
        self.curr_node = next_node
        curr_embed = NaviBot.create_embed(self.curr_node, ctx.author)
        curr_num_buttons = len(self.curr_node.list_children)
        new_number_buttons = ALL_BUTTONS[0:curr_num_buttons]
  
      
    # 4) remove all buttons that are not needed
        for button in (list(self.additional_buttons.values()) + self.number_buttons):
            await self.curr_msg.remove_reaction(button, ctx.author)
        for button in self.number_buttons:
          if button not in new_number_buttons:
            await self.curr_msg.remove_reaction(button, bot.user)
  
          # if (len(number_buttons) != len(curr_node.list_children)):
  
        self.number_buttons = new_number_buttons
      


if __name__ == "__main__":
  
  intents = discord.Intents.default()
  intents.message_content = True

  activity = discord.Activity(type=discord.ActivityType.watching, name="for someone to type !menu")

  bot = commands.Bot(command_prefix='!',
                     activity=activity,
                     intents=intents,
                     help_command=EmbedHelpCommand(), 
                     status=discord.Status.idle)
  
  try:
    bot.run(my_secret)
  except:
    os.system("kill 1")
