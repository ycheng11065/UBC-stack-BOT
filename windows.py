import discord


async def communication_req(ctx):
    embed = discord.Embed(title='communication requirement', color = discord.Color.blue())
    embed.add_field(name='choose 2 of the following', value='[CPSC 110](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=110) \n or [CPSC 103](LINK) + [CPSC 107](LINK)', inline=False)
    await ctx.send(embed=embed)

  
if __name__ == "main":  
  # faculty_pages =  {"page": faculty, "children":[{"page":types_of_specialization, "children": [{"page":major_select_one, "children":[{"page":major_summary, "children":[{"page":general_science_req, "children":[]}]}, {"page":major_general_reqs, "children":[{"page":communication_req, "children":[]}, {"page":science_and_art, "children":[]}, {"page":science_breadth_major, "children":[]}, {"page":lower_level, "children":[]}, {"page":upper_level_major, "children":[]}, {"page":promotional_req, "children":[]}]}, {"page":specialization_list, "children":[{"page":cpscx00lvl, "children":[{"page":cpsc100lvl, "children":[]}, {"page":cpsc200lvl, "children":[]}, {"page":cpsc300lvl, "children":[]}]}]}]}]}]}
  
  
  # faculty page
  faculty = embed = discord.Embed(title='select your faculty', color=discord.Colour.blue())
  faculty.add_field(name='', value=':one:  science', inline=False)
  
  # async def faculty(ctx):
  #   embed = discord.Embed(title='select your faculty', color=discord.Colour.blue())
  
  #   embed.add_field(name='', value=':one:  science', inline=False)
  #   await ctx.send(embed=embed)
  
    # emoji = bot.get_emoji("\U0001F642")
    # await embed.add_reaction(emoji)
  
  # ALL THE PAGES
  
  # types_of_specialization page
  types_of_specialization = discord.Embed(title='select a type of specialization', color=discord.Colour.blue())
  types_of_specialization.add_field(name='', value=':one:  major', inline=False)
  types_of_specialization.add_field(name='', value=':two:  combined major', inline=False)
  types_of_specialization.add_field(name='', value=':three:  honours', inline=False)
  types_of_specialization.add_field(name='', value=':four:  combined honours', inline=False)
  types_of_specialization.add_field(name='', value=':five:  minor', inline=False)
  
  
  # async def types_of_specialization(ctx):
  #   embed = discord.Embed(title='select a type of specialization',
  #                         color=discord.Colour.blue())
  #   embed.add_field(name='', value=':one:  major', inline=False)
  #   embed.add_field(name='', value=':two:  combined major', inline=False)
  #   embed.add_field(name='', value=':three:  honours', inline=False)
  #   embed.add_field(name='', value=':four:  combined honours', inline=False)
  #   embed.add_field(name='', value=':five:  minor', inline=False)
  #   await ctx.send(embed=embed)
  
  # major_select_one page
  major_select_one = embed = discord.Embed(title='select one', color=discord.Colour.blue())
  major_select_one.add_field(name='', value=':one:  summary \n :two:  general requirements \n :three: specializations', inline=False)
  
  # async def major_select_one(ctx):
  #   embed = discord.Embed(title='select one', color=discord.Colour.blue())
  #   embed.add_field(name='', value=':one:  summary \n :two:  general requirements \n :three: specializations', inline=False)
  #   await ctx.send(embed=embed)
  
  #major_summary page
  major_summary = discord.Embed(title='summary', color=discord.Colour.blue())
  major_summary.add_field(name='minimum of the following', value='overall credits \n upper year credits', inline=True)
  major_summary.add_field(name=':', value='120 \n 48', inline=True)
  major_summary.add_field(name='', value='overall science credits \n upper year science credits', inline=True)
  major_summary.add_field(name='', value='72 \n 30', inline=True)
  major_summary.add_field(name='maximum of the following:', value='double counted \n neither arts or science', inline=False)
  major_summary.add_field(name='', value='0 \n 24', inline=True)
  
  # async def major_summary(ctx):
  #   embed = discord.Embed(title='summary', color=discord.Colour.blue())
    
  #   embed.add_field(name='minimum of the following', value='overall credits \n upper year credits', inline=True)
  #   embed.add_field(name=':', value='120 \n 48', inline=True)
    
  #   embed.add_field(name='', value='overall science credits \n upper year science credits', inline=True)
  #   embed.add_field(name='', value='72 \n 30', inline=True)
    
  #   embed.add_field(name='maximum of the following:', value='double counted \n neither arts or science', inline=False)
  #   embed.add_field(name='', value='0 \n 24', inline=True)
  #   await ctx.send(embed=embed)
  
  #major_general_reqs page
  major_general_reqs = discord.Embed(title='general science requirements', color=discord.Colour.blue())
  major_general_reqs.add_field(name='', value=':one:  communication requirement \n :two:  science and art requirement \n :three:  science breadth requirement \n :four:  lower level requirement \n :five:  upper year requirement \n :six:  promotional requirement', inline=False)
  
  #specialization_list page
  specialization_list = embed = discord.Embed(title='list of specializations', color=discord.Color.blue())
  specialization_list.add_field(name='', value='computer science', inline=False)
  
  #cpscx00lvl page
  cpscx00lvl = embed = discord.Embed(title='computer science required courses', color=discord.Color.blue())
  cpscx00lvl.add_field(name='', value='100-level courses \n 200-level courses \n 300 and 400-level courses', inline=False)
  cpscx00lvl.add_field(name='', value='52 credits of electives', inline=False)
  
  #cpsc100lvl page
  cpsc100lvl = embed = discord.Embed(title='100 level courses', color=discord.Color.blue())
  cpsc100lvl.add_field(name='promotional requirements', value='CPSC 110 \n or CPSC 103 + CPSC 107', inline=False)
  cpsc100lvl.add_field(name='graduation requirements', value='communication requirements \n CPSC 121 [Here is the link](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=121) \n MATH 100 \n MATH 101', inline=False)
  
  #cpsc300lvl page
  cpsc300lvl = embed = discord.Embed(title='200 level courses', color=discord.Color.blue())
  cpsc300lvl.add_field(name='promotional requirements', value='none', inline=False)
  cpsc300lvl.add_field(name='graduation requirements', value='CPSC 310 \n CPSC 313 \n CPSC 320 \n CPSC 300-level or higher \n CPSC 400-level or higher', inline=False)
  
  #cpsc300lvl page
  cpsc200lvl = embed = discord.Embed(title='300 level courses', color=discord.Color.blue())
  cpsc200lvl.add_field(name='promotional requirements', value='none', inline=False)
  cpsc200lvl.add_field(name='graduation requirements', value='CPSC 210 \n CPSC 213 \n CPSC 221 \n MATH 200 \n MATH 221 \n STAT 241', inline=False)
  
  # async def major_general_reqs(ctx):
  #   embed = discord.Embed(title='general science requirements',
  #                         color=discord.Colour.blue())
  #   embed.add_field(name='', value=':one:  communication requirement \n :two:  science and art requirement \n :three:  science breadth requirement \n :four:  lower level requirement \n :five:  upper year requirement \n :six:  promotional requirement', inline=False)
  #   await ctx.send(embed=embed)
  
  #communication_req page
  # communication_req =  embed = discord.Embed(title='communication requirement', color = discord.Color.blue())
  # communication_req.add_field(name='choose 2 of the following', value='WRDS 150B \n ENGL 110 \n ENGL 111 \n SCIE 113 \n SCIE 300 `(only for combined major in science)` \n CHEM 300 `(only for chemistry majors`', inline=False)
  
  async def communication_req(ctx):
    embed = discord.Embed(title='communication requirement', color = discord.Color.blue())
    embed.add_field(name='choose 2 of the following', value='[go to google.com](https://www.google.com/)', inline=False)
                    #'[WRDS 150B] (https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=WRDS&course=150B) \n ENGL 110 \n ENGL 111 \n SCIE 113 \n SCIE 300 `(only for combined major in science)` \n CHEM 300 `(only for chemistry majors`'
                    #, inline=False)
    # embed.description = "WRDS 150B [here](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=WRDS&course=150B)."
    await ctx.send(embed=embed)
    
  #science_and_art page
  science_and_art = embed = discord.Embed(title='science and art requirement', color=discord.Color.blue())
  science_and_art.add_field(name='students must complete', value='72 credits from science courses \n 12 credits from arts courses', inline=False)
  
  # async def science_and_art(ctx):
  #   embed = discord.Embed(title='science and art requirement', color=discord.Color.blue())
  #   embed.add_field(name='students must complete', value='72 credits from science courses \n 12 credits from arts courses', inline=False)
  #   await ctx.send(embed=embed)
  
  
  #science_breadth_major page
  science_breadth_major = embed = discord.Embed(title='science breadth requirement', color=discord.Color.blue())
  science_breadth_major.add_field(name='all science courses fall under the following categories', value='mathematics \n biology \n chemistry \n physics \n computer science \n statistics \n earth and planetary science', inline=False)
  science_breadth_major.add_field(name='students in a majors or honours program must complete at least 3 credits from 6 of the 7 categories', value='', inline=False)
  
  # async def science_breadth_major(ctx):
  #   embed = discord.Embed(title='science breadth requirement', color=discord.Color.blue())
  #   embed.add_field(name='all science courses fall under the following categories', value='mathematics \n biology \n chemistry \n physics \n computer science \n statistics \n earth and planetary science', inline=False)
  #   embed.add_field(name='students in a majors or honours program must complete at least 3 credits from 6 of the 7 categories', value='', inline=False)
  #   await ctx.send(embed=embed)
  
  
  #lower_level_major page
  lower_level_major = embed = discord.Embed(title='lower level requirements', color=discord.Color.blue())
  lower_level_major.add_field(name='foundational requirement', value='either grade 12 level or 3 100-level credits in all of biology, chemistry, and physics', inline=False)
  lower_level_major.add_field(name='science lab requirement', value='complete at least one 100-level lab in science', inline=False)
  
  # async def lower_level_major(ctx):
  #   embed = discord.Embed(title='lower level requirements', color=discord.Color.blue())
  #   embed.add_field(name='foundational requirement', value='either grade 12 level or 3 100-level credits in all of biology, chemistry, and physics', inline=False)
  #   embed.add_field(name='science lab requirement', value='complete at least one 100-level lab in science', inline=False)
  #   await ctx.send(embed=embed)
  
  
  # upper_level_major page
  upper_level_major = discord.Embed(title='upper level requirement', color=discord.Color.blue())
  upper_level_major.add_field(name='without a minor', value='30 out of 48 credits from 300 level or higher courses must be in science', inline=False)
  upper_level_major.embed.add_field(name='with a minor', value='42 out of 48 credits from 300 level or higher courses must be in science', inline=False)
  
  # async def upper_level_major(ctx):
  #   embed = discord.Embed(title='upper level requirement', color=discord.Color.blue())
  #   embed.add_field(name='without a minor', value='30 out of 48 credits from 300 level or higher courses must be in science', inline=False)
  #   embed.add_field(name='with a minor', value='42 out of 48 credits from 300 level or higher courses must be in science', inline=False)
  #   await ctx.send(embed=embed)
  
  # promotional_req page
  promotional_req = embed = discord.Embed(title='promotional requirements', color=discord.Color.blue())
  promotional_req.add_field(name='to second year', value='complete at least 24 credits \n at least 15 credits of 100-level science \n all completed within 48 attempted credits', inline=False)
  promotional_req.add_field(name='to third year', value='complete at least 48 credits \n at least 15 credits of 100-level science \n all completed within 48 attempted credits', inline=False)
  promotional_req.add_field(name='to fourth year', value='''complete at least 72 credits \n completed all lower level requirements \n all 100 and 200-level and at least 40% of 
      upper level specialization specific courses, not including electives''', inline=False)
  
  
  
  # async def promotional_req(ctx):
  #   embed = discord.Embed(title='promotional requirements', color=discord.Color.blue())
  #   embed.add_field(name='to second year', value='complete at least 24 credits \n at least 15 credits of 100-level science \n all completed within 48 attempted credits', inline=False)
  #   embed.add_field(name='to third year', value='complete at least 48 credits \n at least 15 credits of 100-level science \n all completed within 48 attempted credits', inline=False)
  #   embed.add_field(name='to fourth year', value='''complete at least 72 credits \n completed all lower level requirements \n all 100 and 200-level and at least 40% of 
  #     upper level specialization specific courses, not including electives''', inline=False)
  #   await ctx.send(embed=embed)
  
    
  
  faculty_pages1 =  {"page": faculty, "children":[{"page":types_of_specialization, "children": [{"page":major_select_one, "children":[{"page":major_summary, "children":[{"page":general_science_req, "children":[]}]}, {"page":major_general_reqs, "children":[ {"page":communication_req, "children":[]}, {"page":science_and_art, "children":[]}, {"page":science_breadth_major, "children":[]}, {"page":lower_level, "children":[]}, {"page":upper_level_major, "children":[]}, {"page":promotional_req, "children":[]}]}, {"page":specialization_list, "children":[{"page":cpscx00lvl, "children":[{"page":cpsc100lvl, "children":[]}, {"page":cpsc200lvl, "children":[]}, {"page":cpsc300lvl, "children":[]}]}]}]}]}]}