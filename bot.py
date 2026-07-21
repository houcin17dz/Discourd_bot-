import os
import discord
from discord.ext import commands

# إعداد الصلاحيات (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# تعريف البوت مع الرمز الخاص بالأوامر
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user.name} (ID: {bot.user.id})")
    print("البوت يعمل بكامل طاقته وجاهز لسيرفر BAC 2027!")

# 1. أمر التوقيت الدراسي
@bot.command()
async def tawkit(ctx):
    await ctx.send(f"أهلاً بك يا {ctx.author.mention}!\n📅 **التوقيت الدراسي الرسمي لسرڤر BAC 2027:**\n- **الصباح:** المراجعة وحل التمارين.\n- **المساء:** حفظ المواد الأدبية.\nC'est parti ya batal!")

# 2. أمر نتائج البكالوريا والوثائق الرسمية
@bot.command()
async def resultat(ctx):
    try:
        await ctx.author.send("📊 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية.")
        await ctx.author.send("https://i.ibb.co/7453566/resultat.jpg") # رابط الوثيقة اللي حطيتها
        await ctx.send(f"تم إرسال تفاصيل النتائج والوثيقة إلى رسائلك الخاصة يا {ctx.author.mention} 📥")
    except discord.Forbidden:
        await ctx.send(f"عذراً يا {ctx.author.mention}، رسائلك الخاصة مغلقة (DM closed)، يرجى فتحها لتلقي الوثيقة.")

# 3. أمر مواضيع السوجيات (رياضيات والمواد الأخرى)
@bot.command()
async def sujet(ctx, *, matiere="الرياضيات"):
    await ctx.send(f"📚 **آخر المواضيع والسوجيات الخاصة بمادة ({matiere}) لـ BAC 2027:**\nتجدون أحدث السوجيات والتمارين المصححة في قناة الإعلانات والملفات المخصصة لكل مادة. بالتوفيق للجميع!")

# تشغيل البوت باستخدام الرمز السري من منصة Render
bot.run(os.getenv("DISCORD_TOKEN"))

