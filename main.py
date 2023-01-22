import discord
from discord.ext import commands
import os
from help import EmbedHelpCommand
# import windows
import files_manager
import asyncio

curr_page = None

ARROW_LEFT = "⬅"
ARROW_RIGHT = "➡"
ONE = "1️⃣"
TWO = "2️⃣"
THREE = "3️⃣"

BUTTONS = [ONE, TWO, THREE]

my_secret = os.environ['key']  # Our token for discord bot to run


def create_embed(curr_menu):
  embed_to_return = discord.Embed(title=curr_menu.title)
  for field in curr_menu.list_selection:
    embed_to_return.add_field(name=field["field_name"],
                              value=field["field_value"],
                              inline=field["field_inline"])
  return embed_to_return

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   help_command=EmbedHelpCommand())

page1 = discord.Embed(
  title='Menu',
  description="This country is not supported, you can ask me to add it" +
  "[here](https://degree-navigator.as.it.ubc.ca/dn4v/Login/dagdisclaimer.asp).",
  color=discord.Colour.blue(),
  url='https://brand.ubc.ca/files/2018/09/Logos_1_2CrestDownload_768px.jpg')

page1.add_field(name='Course Navigation',
                value='type 1 to start navigating your degree',
                inline=False)

page1.add_field(name='!greetings', value='type 2', inline=False)

page1.add_field(name='!farewell', value='type 3', inline=False)


faculty = files_manager.return_root_of_tree()
faculty_embed = create_embed(faculty)
page2 = faculty_embed
# page2 = discord.Embed(title="Bot help 2",
#                       description="page 2",
#                       colour=discord.Colour.blue())
page3 = discord.Embed(title="Bot help 3",
                      description="page 3",
                      colour=discord.Colour.yellow())

bot.help_pages = [page1, page2, page3]


@bot.command()
async def menu(ctx):
  current = 0
  msg = await ctx.send(embed=bot.help_pages[current])

  for button in BUTTONS:
    await msg.add_reaction(button)

  while True:
    try:
      reaction, user = await bot.wait_for(
        "reaction_add",
        check=lambda reaction, user: user == ctx.author and reaction.emoji in
        BUTTONS,
        timeout=60.0)

    except asyncio.TimeoutError:
      embed = bot.help_pages[current]
      embed.set_footer(text="Timed Out.")
      await msg.clear_reactions()

    else:
      previous_page = current

      # if reaction.emoji == ARROW_LEFT:
      #   if current > 0:
      #     current -= 1

      if reaction.emoji == ONE:
        current = 0

      # elif reaction.emoji == ARROW_RIGHT:
      #   if current < len(bot.help_pages) - 1:
      #     current += 1

      elif reaction.emoji == TWO:
        current = 1

      elif reaction.emoji == THREE:
        current = 2

      for button in BUTTONS:
        await msg.remove_reaction(button, ctx.author)

      if current != previous_page:
        await msg.edit(embed=bot.help_pages[current])


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


@bot.event
async def on_reaction_add(reaction, user):
  # if user.author == bot.author:
  #   return
  # print('Curr page?: ', reaction.message == curr_page)
  # print('Bot?: ', reaction.author == bot.user)
  if reaction.emoji == ONE and reaction.message == curr_page:
    faculty = files_manager.return_root_of_tree()
    faculty_embed = create_embed(faculty)
    # await curr_page.remove_reaction(ONE, curr_page.author)
    # await curr_page.remove_reaction(TWO, curr_page.author)
    # await curr_page.remove_reaction(THREE, curr_page.author)
    # await curr_page.edit(embed=faculty_embed)

    await reaction.message.remove_reaction(ONE, curr_page.author)
    await reaction.message.remove_reaction(TWO, curr_page.author)
    await reaction.message.remove_reaction(THREE, curr_page.author)
    await reaction.message.edit(embed=faculty_embed)

  elif reaction.emoji == TWO:
    return

  elif reaction.emoji == THREE:
    return


numbers = [1, 2, 3]


# @bot.command()
# async def menu(ctx):
#   global curr_page
#   #initial
#   custom = discord.Embed(
#     title='Menu',
#     description="This country is not supported, you can ask me to add it" +
#     "[here](https://degree-navigator.as.it.ubc.ca/dn4v/Login/dagdisclaimer.asp).",
#     color=discord.Colour.blue(),
#     url='https://brand.ubc.ca/files/2018/09/Logos_1_2CrestDownload_768px.jpg')

#   custom.add_field(name='Course Navigation',
#                    value='type 1 to start navigating your degree',
#                    inline=False)

#   custom.add_field(name='!greetings', value='type 2', inline=False)

#   custom.add_field(name='!farewell', value='type 3', inline=False)
#   msg = await ctx.channel.send(embed=custom)
#   curr_page = msg

#   for react in BUTTONS:
#     await msg.add_reaction(react)

  # while True:
  #   try:
  #     reaction, user = await bot.wait_for(
  #       "reaction_add",
  #       check=lambda reaction, user: user == ctx.author and reaction.emoji in
  #       BUTTONS,
  #       timeout=60.0)

  #   except asyncio.TimeoutError:
  #     embed = custom
  #     embed.set_footer(text="Timed Out.")
  #     await msg.clear_reactions()




#Current commands
# @bot.command()
# async def faculty(ctx):
#   await windows.faculty(ctx)

# @bot.command()
# async def types_of_specialization(ctx):
#   await windows.types_of_specialization(ctx)

# @bot.command()
# async def major_select_one(ctx):
#   await windows.major_select_one(ctx)

# @bot.command()
# async def major_summary(ctx):
#   await windows.major_summary(ctx)

# @bot.command()
# async def major_general_regs(ctx):
#   await windows.major_general_regs(ctx)

# @bot.command()
# async def communication_req(ctx):
#   await windows.communication_req(ctx)

# @bot.command()
# async def science_and_art(ctx):
#   await windows.science_and_art(ctx)

# @bot.command()
# async def science_breadth_major(ctx):
#   await windows.science_breadth_major(ctx)

# @bot.command()
# async def promotional_req(ctx):
#   await windows.promotional_req(ctx)



try:
  bot.run(my_secret)
except:
  os.system("kill 1")
