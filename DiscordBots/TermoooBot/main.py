import discord
import asyncio
import random
import unidecode
import os
from palavras import palavras
from discord.ext import commands
from dotenv import load_dotenv

activity = discord.Game(name="&help")
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "&", case_insensitive = True, activity=activity, status=discord.Status.idle, intents=intents)

client.remove_command("help")

def configure():
    load_dotenv()

configure()

# Comando de ajuda
@client.command()
async def help(ctx):
  await ctx.send('&termo. A regra do jogo é simples. Uma palavra de cinco letras aleatoria é escolhida, o player então digita uma palavra, o bot analisa cada um dos caracteres das palavras e retorna o resultado')
  await ctx.send(':green_square: = quando a letra esta na palavra e na posição correta')
  await ctx.send(':yellow_square: = quando a letra esta na palavra e na posição incorreta')
  await ctx.send(':red_square: = quando a letra não esta na palavra')

#Comando Termooo
@client.command()
async def termo(ctx):
  # Variaveis
  turn = 0
  num = 0
  resp = ''

  # Mensagem Setup
  await ctx.send('Espere um momento...')
  await asyncio.sleep(1)
  word = unidecode.unidecode(random.choice(palavras))
  print(word)
  await ctx.send('Decidi uma palavra.')
  await ctx.send('Você tem 6 tentativas para acertar a palavra de 5 letras.')
  
  # Função que pega mensagem do usuario
  def check(m):
    return m.channel == ctx.channel
  
  # Transformação da palavra em list de caracteres
  wordT = list(word)

  # Termo
  while turn < 6:
    num = 0
    resp = []
    answer = ""
    passed = False
    #Pega e transforma em list a mensagem do player (para cada turno)
    msg = await client.wait_for("message", check=check)
    realmsg = unidecode.unidecode(msg.content)
    wordP = list(realmsg)
    
    
    # Turno
    if len(wordP) == 5:
      #Criar lista que pega a posição dos caracteres verdes e amarelos
      listGreen = []
      listYellow = []
      
      for i in range(len(wordT)):
        passed = False
        wordTwo = list(wordT)
        del wordTwo[i]
        if wordP[i].lower() == wordT[i].lower():
          resp.append(':green_square: ')
          listGreen.append(i)
          passed = True
        for n in range(len(wordTwo)):
          if wordP[i].lower() == wordTwo[n].lower() and passed == False:
            resp.append(':yellow_square: ')
            listYellow.append(i)
            passed = True
        if passed == False:
          resp.append(':red_square: ')

      # Verificação dos verdes e amarelos
      if len(listYellow) != 0:
        print(wordP)
        for g in listGreen:
          print("G")
          print(g)
          for y in listYellow:
            print("Y")
            print(y)
            if wordP[g] == wordP[y]:
              resp[y] = ':red_square: '
      #Novo problema: Quando uma palavra tem duas letras iguais e o player acerta o uma das letras mas erra a posição da outra letra igual o bot coloca a então letra amarela como uma letra vermelha.
      
      print(listGreen)
      print(listYellow)
      num = num + 1
      turn = turn + 1
    elif realmsg == '&termo':
      answer = 'Complete o jogo atual.'
      turn = 100
    else:
      answer = 'A palavra precisa ter 5 letras.'

    # Transforma resposta em string
    answer = ''.join(resp)
    
    # Verificação de vitoria
    if answer == ':green_square: :green_square: :green_square: :green_square: :green_square: ': 
      await ctx.send('Parabens! você acertou em ' + str(turn) + ' tentativas')
      turn = 7
    
    
    await ctx.send(answer)


client.run(os.getenv('clientID'))