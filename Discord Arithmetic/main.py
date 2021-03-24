import discord
from discord.ext import commands, tasks

import ClientConfig
client = ClientConfig.client

import os
from dotenv import load_dotenv
import B

import random
from random import choice
import time
from time import sleep

@client.event
async def on_ready():
  print('Logged in as:')
  print("Username:", client.user.name)
  print("Client ID:", client.user.id)
  print('-----------------------------')
  await client.change_presence(status=discord.Status.idle)

@commands.command()
async def analyzeint(self, ctx, x : int, y : int):
  if x > 100000:
    embed = discord.Embed(title = "The number can't be that big!")
    await ctx.send(embed = embed)
  elif y > 100000:
    embed = discord.Embed(title = "The number can't be that big!")
    await ctx.send(embed = embed)
  elif x > y:
    embed = discord.Embed(title = "For the range function to work, ``x`` must be less than ``y``.")
    await ctx.send(embed = embed )
  else:
    a = x + y   #the sum of and x and y
    b = x - y   #the difference of x and y
    c = x * y   #product from x and y
    d = y / x   #quotient of x and y
    e = y // x  #floor division quotient of x and y
    f = x ** y  #x to the power of y
    g = y % x   #modulo of x and y
    h = random.randint(x , y)
    embed = discord.Embed(title = "The number's have been analzyed!", color = random.randint(0, 16777215))
    embed.add_field(name = "When your numbers were added:", value = f"{x} + {y} = **{a}**",inline = False)
    embed.add_field(name = "When your numbers were subtracted:", value = f"{x} - {y} = **{b}**",inline = False)
    embed.add_field(name = "When your numbers were multiplied:", value = f"{x} * {y} = **{c}**",inline = False)
    embed.add_field(name = "When your numbers were divided:",value = f"{y} / {x} = **{d}**",inline = False)
    embed.add_field(name = "When your numbers were floor divisioned:",value = f"{y} // {x} = **{e}**",inline = False)
    embed.add_field(name = "When your numbers were randomly ranged and picked:",value = f"{x} to {y}, randomly picked was **{h}**",inline = False)
    embed.add_field(name = "When you two numbers were moduled by modulo, the remainder was:", value = f"**{g}**")
    await ctx.send(embed=embed)
    #simple and very general number analysis
    
@client.command()
async def solvquad(ctx, xx: int, yy: int, zz: int):
  if xx = None:
    await ctx.send("\nWhat would you like 'a' to be equal to?")
  elif yy = None:
    await ctx.send("\nWhat would you like 'b' to be equal to?")
  elif zz = None:
    await ctx.send("\nWhat would you like 'c' to be equal to?")
  else:
    await ctx.send("Alright, let us insert the given values into Quadratic Equations!\nA Qaudratic Equation goes as such:\t x = -(b) ± √(b)² + 4(a)(c)/ 2(a)\n")
    #this was quite a doozy copying and pasting the individual parts of this equation, such as the positive/negative sign, squared symbol, and square root symbol
    aa = -yy          #this would be negative b
    bb = yy * yy      #this would be b to the power of two
    cc = 4 * xx * zz  #this would be 4(a)(c)
    dd = 2 * xx       #this would be 2(a)
    ee = bb + cc      #simplifying the equation more so
    ff = math.sqrt(ee)
    await ctx.send("\nProcessing the values inserted...\n")
    time.sleep(3)
    await ctx.send(f"Alright, we have plugged in the given variables and simplified the equation. This is what we have:\tx = {aa} ± √ {ee} / {dd} \n")
    await ctx.send(f"The sqaure root of {ee} is:\t {ff})
    #I'll need to finish from these later
                   
B.b()
client.run(os.getenv('TOKENA'))
