import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready and running for BAC 2027!")

@bot.command()
async def hello(ctx):
    await ctx.send("Marhaban bik ya batal fi server BAC 2027! Bot yaamal bi najah.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()
    if "tawkit" in msg or "jadwal" in msg or "timing" in msg:
        await message.channel.send(f"Ahlan bik ya {message.author.mention}! Tawkit dirasi mawjoud fi qanat al-i'lanat, aw iktib amr !schedule liyasilka fi al-khass.")

    await bot.process_commands(message)

@bot.command()
async def schedule(ctx):
    try:
        await ctx.author.send("📅 Ilayka attawkit addirasi rrasmi liserver BAC 2027:\n- Sabahan: Al-muraja'a wa hall attamarīn\n- Masa'an: Hifd al-mawadd al-adabiyya\nC'est parti ya batal!")
        await ctx.send(f"Tamma irsal attawkit ila risailika al-khassa ya {ctx.author.mention} 📩")
    except discord.Forbidden:
        await ctx.send(f"Udhran ya {ctx.author.mention}, rasailuka al-khassa mughlaqa (DM closed).")

@bot.command()
async def tawkit(ctx):
    await ctx.send("Bienvenue ! L'emploi du temps est disponible dans le salon des annonces, ou vous pouvez consulter votre planning pour le BAC 2027.")
bot.run(os.getenv("DISCORD_TOKEN"))

