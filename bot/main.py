import discord
from discord.ext import commands
import random
import os

print(os.listdir('glass'))

print(os.listdir('organic'))

print(os.listdir('paper'))

print(os.listdir('plastic'))

print(os.listdir('mem'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)





@bot.command()
async def glass(ctx):
    img_name = random.choice(os.listdir('glass'))
    with open(f'glass/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def organic(ctx):
    img_name = random.choice(os.listdir('organic'))
    with open(f'organic/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def paper(ctx):
    img_name = random.choice(os.listdir('paper'))
    with open(f'paper/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def plastic(ctx):
    img_name = random.choice(os.listdir('plastic'))
    with open(f'plastic/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('mem'))
    with open(f'mem/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.event
async def on_ready():
    print('готов вкалывать {0.user}'.format(bot))

@bot.command()
async def привет(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')

@bot.command()
async def здание(ctx):
    await ctx.send('\n**Как избежать пожара в здание:**\n```Не оставляйте без присмотра включенные в сеть электробытовые приборы.``` ```Не включайте в одну розетку одновременно несколько мощных энергопотребителей - это может привести к перегрузке в электросети и возгоранию.``` ```Своевременно заменяйте неисправные выключатели, розетки и электропроводку.``` ```Нельзя обертывать электролампы и светильники бумагой, тканью и другими горючими материалами.``` ```Не бросайте в мусоропровод или с балкона непогашенные окурки.``` ```В случае возникновения пожара звоните по телефону 01 (112 для абонентов сотовой связи).``` ')

@bot.command()
async def лес(ctx):
    await ctx.send('\n**Как избежать пожара в лесу:**\n```Не бросать горящие спички и окурки на землю.``` ```Не оставлять стеклянные предметы.``` ```Не оставлять промасленные или пропитанные горючими веществами предметы.``` ```Не парковать автомобили в неположенном месте.``` ```Не разжигать костры в пожароопасный период.``` ```Не сжигать мусор в лесу.```')

@bot.command()
async def хелп(ctx):
    await ctx.send('\n**Мои команды:**\n```>привет - Вывод сообщения с приветом.``` ```>здание - даёт инструкции по тому как избежать пожара в здании.``` ```>лес - даёт инструкции по тому как избежать пожара в лесу.``` ```>glass - показывает цвет бака в который надо выбрасывать стекло.``` ```>organic - показывает цвет бака в который надо выбрасывать органику.``` ```>paper - показывает цвет бака в который надо выбрасывать бумагу.``` ```>plastic - показывает цвет бака в который надо выбрасывать пластик.``` ```>mem - команда которая показывает один рандомный мем про экологию.```')





bot.run("")
