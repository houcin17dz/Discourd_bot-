import os
from threading import Thread
from discord.ext import commands
import discord
from flask import Flask

# 1. Mini serveur web pour éviter le problème de Time Out sur Render
app = Flask('')


@app.route('/')
def home():
  return 'Bot is running and alive!'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


# Démarrer le serveur en premier
keep_alive()

# 2. Configuration du bot et des commandes
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


# --- Vos commandes personnalisées ---


@bot.command()
async def resultat(ctx):
  await ctx.send(
      "قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\n الثانوية: عبد"
      " المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية"
  )
  await ctx.send('https://i.ibb.co/7453566/resultat.jpg')


@bot.command()
async def sujet(ctx, *, matiere='الرياضيات'):
  await ctx.send(
      f'إجدون أحدث السوجيات في قناة الإعلانات بالتوفيق**\nBAC 2027: لـ'
      f' **{matiere}** آخر المواضيع والسوجيات'
  )


# Lancement du bot avec le token enregistré dans Render
bot.run(os.getenv('DISCORD_TOKEN'))
    

