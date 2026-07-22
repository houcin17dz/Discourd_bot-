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


# --- 3. نظام الردود الذكية المتطور (يتكلم كي البنادم) ---
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  text = message.content.lower()  # تحويل النص إلى حروف صغيرة لتحليلها بسهولة

  # التحقق مما إذا كان المستخدم يكلم البوت أو يسأله أسئلة معينة
  if "نتائج الباك" in text or "اللوحة" in text or "موليور" in text:
    await message.channel.send(
        "📚 قوائم الناجحين الرسمية لشهادة البكالوريا متوفرة في قناة"
        " الإعلانات الخاصة بسيرفر BAC 2027 بالتوفيق للجميع!"
    )
  elif "سلام" in text or "اهلا" in text or "hi" in text or "hello" in text:
    await message.channel.send(
        "وعليكم السلام يا بطل! ⚡ كيف يمكنني مساعدتك اليوم في دراستك أو"
        " سيرفر الباك؟"
    )
  elif "شكون انت" in text or "من أنت" in text:
    await message.channel.send(
        "أنا **Le Mentor**، مساعدك الشخصي الذكي لتنظيم الدراسة ومرافقتك نحو"
        " نجاح البكالوريا! 🎯"
    )
  elif "مساعدة" in text or "help" in text:
    await message.channel.send(
        "🛠️ الأوامر المتوفرة حالياً:\n- `!resultat`: لعرض نتائج الباك.\n- `!sujet"
        " [المادة]`: للحصول على أحدث السوجيات.\n- أو يمكنك محادثتي مباشرة هنا"
        " وسأرد عليك!"
    )
  else:
    # رد ذكي افتراضي بدل تكرار الكلام الحرفي
    await message.channel.send(
        f"أهلاً بك! لقد فهمت سؤالك، تابع قناة الإعلانات أو اكتب `!help` لمعرفة"
        " كيف أستطيع مساعدتك أكثر 🚀"
    )

  # ضروري لتشغيل الأوامر مثل !resultat و !sujet
  await bot.process_commands(message)


# --- الأوامر المخصصة ---


@bot.command()
async def resultat(ctx):
  await ctx.send(
      "قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\n الثانوية: عبد"
      " المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية"
  )
  await ctx.send("https://i.ibb.co/7453566/resultat.jpg")


@bot.command()
async def sujet(ctx, *, matiere="الرياضيات"):
  await ctx.send(
      f"إجدون أحدث السوجيات في قناة الإعلانات بالتوفيق**\nBAC 2027: لـ"
      f" **{matiere}** آخر المواضيع والسوجيات"
  )


bot.run(os.getenv("DISCORD_TOKEN"))

