import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user.name}")
    print("البوت يعمل بكامل طاقته وجاهز لسيرفر BAC 2027!")

@bot.command()
async def tawkit(ctx):
    await ctx.send(f"أهلاً بك يا {ctx.author.mention}!\n📅 **التوقيت الدراسي الرسمي:**\n- **الصباح:** المراجعة وحل التمارين.\n- **المساء:** حفظ المواد الأدبية.\nC'est parti ya batal!")

@bot.command()
async def resultat(ctx):
    await ctx.send(f"📊 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية يا {ctx.author.mention}")
    await ctx.send("https://i.ibb.co/7453566/resultat.jpg")

@bot.command()
async def sujet(ctx, *, matiere="الرياضيات"):
    await ctx.send(f"📚 **آخر المواضيع والسوجيات لمادة ({matiere}) لـ BAC 2027:**\nتجدون أحدث السوجيات في قناة الإعلانات بالتوفيق!")

bot.run(os.getenv("DISCORD_TOKEN"))
    

