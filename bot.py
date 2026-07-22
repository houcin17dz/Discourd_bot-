import os
from threading import Thread
import discord
from discord.ext import commands
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

# 2. Configuration du bot, des intents et des permissions de lecture
intents = discord.Intents.default()
intents.message_content = True  # ضرورية لقراءة محتوى الرسائل
intents.guilds = True
intents.dm_messages = True  # لقراءة الرسائل في الخاص أيضاً

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


# --- 3. أمر الرد التلقائي على أي كلمة (عربي أو إنجليزي) ---
@bot.event
async def on_message(message):
  # عدم الرد على البوت نفسه لمنع التكرار (Loop)
  if message.author == bot.user:
    return

  # يمكنك تعديل الرد بالطريقة التي تحبها
  user_text = message.content
  await message.channel.send(f'وصلتني كلمتك: **{user_text}**، راني نسمع فيك!')

  # ضروري جداً لكي تستمر الأوامر الأخرى (مثل resultat و sujet) في العمل
  await bot.process_commands(message)


# --- Vos commandes personnalisées ---


@bot.command()
async def resultat(ctx):
  await ctx.send(
      'قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\n الثانوية: عبد'
      ' المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية'
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

