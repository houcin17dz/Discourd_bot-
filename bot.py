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


# --- دالة مساعدة للبحث عن قناة announcements تلقائياً ---
async def send_to_announcements(guild, content, file_url=None):
  target_channel = None
  for channel in guild.text_channels:
    if (
        'announcement' in channel.name.lower()
        or 'إعلان' in channel.name
        or 'انونسمنت' in channel.name
    ):
      target_channel = channel
      break

  if target_channel:
    await target_channel.send(content)
    if file_url:
      await target_channel.send(file_url)
    return target_channel
  return None


# --- 3. نظام الردود الذكية والأوامر الشاملة ---
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  text = message.content.lower()

  # الرد على أسئلة النتائج
  if (
      'نتائج الباك' in text
      or 'اللوحة' in text
      or 'نتيجة' in text
      or 'resultat' in text
  ):
    await send_to_announcements(
        message.guild,
        '📌 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد'
        ' المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية',
        'https://i.ibb.co/7453566/resultat.jpg',
    )
  # الترحيب
  elif 'سلام' in text or 'اهلا' in text or 'hi' in text:
    await message.channel.send(
        'وعليكم السلام يا بطل! ⚡ كيف يمكنني مساعدتك اليوم في السيرفر؟'
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


# --- الأوامر الجديدة والقديمة كاملة ---


@bot.command()
async def resultat(ctx):
  await send_to_announcements(
      ctx.guild,
      '📌 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد'
      ' المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية',
      'https://i.ibb.co/7453566/resultat.jpg',
  )
  await ctx.send('✅ تم نشر النتائج في قناة الإعلانات!')


@bot.command()
async def sujet(ctx, *, matiere='الرياضيات'):
  content = (
      f'📚 **أحدث السوجيات والمواضيع لـ BAC 2027**\nالمادة: **{matiere}**\nتجدون'
      ' الملفات والمواضيع في قناة الإعلانات بالتوفيق للجميع!'
  )
  await send_to_announcements(ctx.guild, content)
  await ctx.send(f'✅ تم نشر سوجي {matiere} في قناة الإعلانات!')


@bot.command()
async def توقيت(ctx):
  content = (
      '⏰ **التوقيت الدراسي الرسمي لبداية الموسم:**\n'
      '- الفترة الصباحية: 08:00 صباحاً - 12:00 ظهراً\n'
      '- الفترة المسائية: 13:30 ظهراً - 17:00 مساءً\n'
      '*(راجع قناة الإعلانات لأي تعديلات جديدة)*'
  )
  await send_to_announcements(ctx.guild, content)
  await ctx.send('✅ تم نشر التوقيت الدراسي في قناة الإعلانات!')


@bot.command()
async def اختبارات(ctx):
  content = (
      '📅 **جدول الاختبارات والفروض الرسمية:**\n'
      'تم إدراج جدول الفروض والاختبارات الخاصة بالفصول الثلاثة في قناة'
      ' الإعلانات. بالتوفيق لكل التلاميذ!'
  )
  await send_to_announcements(ctx.guild, content)
  await ctx.send('✅ تم نشر جدول الاختبارات في قناة الإعلانات!')


@bot.command()
async def وزارة(ctx):
  content = (
      '📢 **أحدث إعلانات وزارة التربية الوطنية:**\n'
      'أي منشور أو قرار جديد صادر عن الوزارة سيتم وضعه هنا فوراً في قناة'
      ' الإعلانات المخصصة.'
  )
  await send_to_announcements(ctx.guild, content)
  await ctx.send('✅ تم نشر المستجدات الرسمية في قناة الإعلانات!')


bot.run(os.getenv('DISCORD_TOKEN'))
