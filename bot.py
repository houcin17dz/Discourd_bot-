import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# 1. Mini serveur web pour Render
app = Flask('')


@app.route('/')
def home():
  return 'Bot is running and alive!'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

# 2. Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


# --- دالة ذكية لإرسال الرسائل (إلى قناة الإعلانات أو للخاص/الشات الحالي مباشرة) ---
async def send_smart(ctx_or_message, content, file_url=None):
  guild = getattr(ctx_or_message, 'guild', None)
  channel = getattr(ctx_or_message, 'channel', ctx_or_message)

  target_channel = None
  if guild:
    for ch in guild.text_channels:
      if (
          'announcement' in ch.name.lower()
          or 'إعلان' in ch.name
          or 'انونسمنت' in ch.name
      ):
        target_channel = ch
        break

  dest = target_channel if target_channel else channel

  await dest.send(content)
  if file_url:
    await dest.send(file_url)


# --- 3. نظام الردود الذكية ---
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  text = message.content.lower()

  if 'سلام' in text or 'اهلا' in text or 'hi' in text:
    await message.channel.send(
        'وعليكم السلام يا بطل! ⚡ كيف يمكنني مساعدتك اليوم؟'
    )
  elif 'شكون انت' in text or 'من أنت' in text:
    await message.channel.send(
        'أنا **Le Mentor**، مساعدك الشخصي لتنظيم الدراسة ومرافقتك نحو البكالوريا!'
        ' 🎯'
    )
  else:
    if not message.content.startswith('!'):
      await message.channel.send(
          'أهلاً بك! لقد فهمت رسالتك، تابع قناة الإعلانات أو اكتب `!help` لمعرفة'
          ' الأوامر المتاحة 🚀'
      )

  await bot.process_commands(message)


# --- الأوامر باللغة العربية بالكامل ---


@bot.command(name='نتائج')
async def resultat_cmd(ctx):
  await send_smart(
      ctx,
      '📌 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد'
      ' المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية',
      'https://i.ibb.co/7453566/resultat.jpg',
  )


@bot.command(name='سوجيات')
async def sujet_cmd(ctx, *, matiere='الرياضيات'):
  content = (
      f'📚 **أحدث السوجيات والمواضيع لـ BAC 2027**\nالمادة: **{matiere}**\nتجدون'
      ' الملفات والمواضيع في قناة الإعلانات بالتوفيق للجميع!'
  )
  await send_smart(ctx, content)


@bot.command(name='توقيت')
async def tawkit_cmd(ctx):
  content = (
      '⏰ **التوقيت الدراسي الرسمي لبداية الموسم:**\n'
      '- الفترة الصباحية: 08:00 صباحاً - 12:00 ظهراً\n'
      '- الفترة المسائية: 13:30 ظهراً - 17:00 مساءً'
  )
  await send_smart(ctx, content)


@bot.command(name='اختبارات')
async def ikhtibarat_cmd(ctx):
  content = (
      '📅 **جدول الاختبارات والفروض الرسمية:**\nتم إدراج جدول الفروض والاختبارات'
      ' الخاصة بالفصول الثلاثة.'
  )
  await send_smart(ctx, content)


@bot.command(name='وزارة')
async def wizarat_cmd(ctx):
  content = (
      '📢 **أحدث إعلانات وزارة التربية الوطنية:**\nأي منشور أو قرار جديد صادر'
      ' عن الوزارة سيتم وضعه هنا فوراً.'
  )
  await send_smart(ctx, content)


bot.run(os.getenv('DISCORD_TOKEN'))
