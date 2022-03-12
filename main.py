import discord
import os
import requests
import json
import random

client = discord.Client()


def get_quote():
  res = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_joke():
  res=requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data=json.loads(res.text)
  joke = json_data['setup'] + " -" + json_data['punchline']
  return(joke)

valo_motivation=["I got your backs... just, you know, from the front.","This place is nice, but not nice enough to die in.", "Don't mess up that pretty face, Phoenix!", "Damn right we're crushing it!", "They're not better than me."]

words1=['I am indu', 'I am candy', 'I am blast', 'I am mathi']
words2=['No, you are candy','No, you are indu','No, you are mathi','No, you are blast']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg=message.content 
    user=message.author.name
    if message.content.startswith('$hi'):
        await message.channel.send('Hi,'+user+ '. I am CandyBot!')
      
    if(msg.startswith('$motivateme')):
      quote=get_quote()
      await message.channel.send(quote)

    if message.content.startswith('$valodialog'):
      await message.channel.send(random.choice(valo_motivation))

    if any(word in msg for word in words1):
      result=random.choice(words2)
      if(result[-1]==msg[-1]):
        await message.channel.send('You are right!')
      else:
        await message.channel.send(result)
      
    if(msg=='$joke'):
      joke=get_joke()
      await message.channel.send(joke)

    if(msg.startswith('I\'m')):
      name=msg[4:]
      await message.channel.send('Hi! '+name)

    if(msg=='$help'):
      await message.channel.send('List of commands\n•$hi\n•$valodialog\n•I\'m (your name)\n•$motivateme\n•$joke\n•this or that')

    if('or' in msg):
      li=[]
      choose=[]
      li=list(msg.split(' '))
      if(len(li)==3):
        choose.append(li[0])
        choose.append(li[2])
        await message.channel.send(user +', Obviously '+ random.choice(choose)+'!')

my_secret = os.environ['token']
client.run(my_secret)