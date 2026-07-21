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

# 1. أمر التوقيت والشامل (يديه لقناة الإعلانات تاع التواقيت، الاختبارات، والعطل)
@bot.command()
async def tawkit(ctx):
    # تقدر تبدل الرابط هذا برابط قناة الإعلانات الحقيقي في سرڤرك
    announcement_link = "https://discord.com/channels/YOUR_SERVER_ID/YOUR_CHANNEL_ID"
    
    await ctx.send(
        f"أهلاً بك يا {ctx.author.mention} 📅\n"
        "للإطلاع على **التوقيت الدراسي، توقيت الاختبارات، والعطل المدرسية الرسمية**، تفضل بزيارة قناة الإعلانات:\n"
        f"👉 {announcement_link}\n\n"
        "بالتوفيق لجميع الطلبة في مشوار BAC 2027! 🔥"
    )

# 2. أمر نتائج البكالوريا والوثائق الرسمية
@bot.command()
async def resultat(ctx):
    await ctx.send(f"📊 **قوائم الناجحين الرسمية - شهادة البكالوريا دورة 2026**\nالثانوية: عبد المؤمن بن علي - الإدريسية\nالشعبة: تقني رياضي هندسة مدنية يا {ctx.author.mention}")
    await ctx.send("https://i.ibb.co/7453566/resultat.jpg")

# 3. أمر مواضيع السوجيات
@bot.command()
async def sujet(ctx, *, matiere="الرياضيات"):
    await ctx.send(f"📚 **آخر المواضيع والسوجيات لمادة ({matiere}) لـ BAC 2027:**\nتجدون أحدث السوجيات في قناة الإعلانات بالتوفيق!")

bot.run(os.getenv("DISCORD_TOKEN"))
    

