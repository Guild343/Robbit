import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get
from discord import gateway
from random import *
import os
import keep_alive
import io
from random import choice
import json
import requests


#ПРЕФИКС
prefix = '?'

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('?хелп'))

log = gateway.log

@bot.event 
async def on_command_error(ctx, error):
    try:
        from colorama import Fore
    except:
        import os
        os.system("pip install colorama")
        from colorama import Fore

    print(f'{Fore.RED}[=======================Ошибка!=======================]{Fore.RESET}\nАвтор получивший ошибку: {Fore.YELLOW}{ctx.author}{Fore.RESET}\nСодержание сообщения: {Fore.YELLOW}{ctx.message.content}{Fore.RESET}\nДата происшествия: {Fore.YELLOW}{ctx.message.created_at.day}.{ctx.message.created_at.month}.{ctx.message.created_at.year}{Fore.RESET}\nОшибка: {Fore.YELLOW}{str(error).replace("Command raised an exception:", "", 1)}{Fore.RESET}')

@bot.command(aliases = ["а"])
@commands.has_permissions(manage_channels=True)
async def reloadchat(ctx):
    channel = ctx.message.channel
    await channel.send (embed=discord.Embed(description='**<:1a79bbdd825ff4cffe6081c8206d3b69:838759023406350366> Релоад Чат**\nУчастником.'))

@bot.command()
async def хелп(ctx):
    embed = discord.Embed(
        title="<a:nitro:818888284024340501>***Доступные команды:***",
        description=
                '\nВы можете получить детальную справку по каждой команде, выполнив её со знаком ?. Например: !хелп ?''\n\n**<:Ship2:825600198712885279>Информация**\n`хелп` `сервер` `инфо` `роль`\n**<:Ship5:818889272987484192> весёлое **\n`лиса` `пес` `кот` `шар` `шип`\n**<:818248040954855445:831262181903171661> модерация**\n`бан` `кик` `пинг` `reloadchat` \n**<:pingsuka:840868519196622870>Экономика **\n`баланс` `работа (скоро)` `ютуб` \n**<:darova:840868870079774752>Диалог**\n`привет` `какдела` `нормально` `ничего` `пока`\n**<:pingsuka:840868519196622870>Все команды!**\n`сервер` `инфо` `роль` `аватарка` `ютуб` `лиса` `шар` `шип` `бан` `кик` `пинг` `инфо` `reloadchat` `привет` `какдела` `нормально` `ничего` `пока` \n\nРейдан © 2021 Все права зафырканы',
        colour=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar_url)
    message = await ctx.send(embed=embed)
    bot.remove_command('хелп')

@bot.command()
async def пес(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900,
                          title='<:494223467399348225:825600595230064650> Случайные собаки<:494223467399348225:825600595230064650> ')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed

@bot.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900,
                          title='<:494223467399348225:825600595230064650> Случайные коты<:494223467399348225:825600595230064650> ')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embe

@bot.command()
async def пинг(ctx):
    ping = ctx.bot.latency * 1000
    if ping < 50:
        embed = discord.Embed(
            color=0x6CE5E8,
            title=":ping_pong: Играй в Понг!",
            description="> **<:Ship5:818889272987484192>Задержка бота<:darova:840868870079774752>** :white_circle: {0:.2f}ms".format(
                ctx.bot.latency * 1000))
        await ctx.send(embed=embed)
    else:
        if ping < 150:
            embed = discord.Embed(
                color=0x6CE5E8,
                title=":ping_pong: Понг!",
                description="> **Задержка бота:** :green_circle: {0:.2f}ms".
                format(ctx.bot.latency * 1000))
            await ctx.send(embed=embed)
        else:
            if ping < 300:
                embed = discord.Embed(
                    color=0x6CE5E8,
                    title=":ping_pong: Понг!",
                    description="> **Задержка бота:** :yellow_circle: {0:.2f}ms"
                    .format(ctx.bot.latency * 1000))
                await ctx.send(embed=embed)
            else:
                if ping < 500:
                    embed = discord.Embed(
                        color=0x6CE5E8,
                        title=":ping_pong: Понг!",
                        description=
                        "> **Задержка бота:** :orange_circle: {0:.2f}ms".
                        format(ctx.bot.latency * 1000))
                    await ctx.send(embed=embed)
                else:
                    if ping < 750:
                        embed = discord.Embed(
                            color=0x6CE5E8,
                            title=":ping_pong: Понг!",
                            description=
                            "> **Задержка бота:** :red_circle: {0:.2f}ms".
                            format(ctx.bot.latency * 1000))
                        await ctx.send(embed=embed)
                    else:
                        if ping > 750:
                            embed = discord.Embed(
                                color=0x6CE5E8,
                                title=":ping_pong: Понг!",
                                description=
                                "> **Задержка бота:** :black_circle: {0:.2f}ms"
                                .format(ctx.bot.latency * 1000))
                            await ctx.send(embed=embed)
                        else:
                            pass

@bot.command(aliases = ["аватарка"]) 
async def avatar(ctx, member : discord.Member ):
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name = "<:1a79bbdd825ff4cffe6081c8206d3b69:838759023406350366>Аватар<a:8_:843027197131620372>", value = f"\n\n<a:6_:843027197299916832>**Ваша аватарка**--->")
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('<a:3_:843027198419140648>')  

@bot.command()
@commands.has_permissions(ban_members=True)
async def бан(ctx, member: discord.Member, *, reason=None):
   if member == ctx.message.author:
      embed = discord.Embed(color=discord.Color.Red(),title="Ошибка 404 !",description="ты глупый чтоб мог себя забанить?")
      await ctx.send(embed=embed)      
   else:
      await member.ban(reason=reason)
      author = ctx.message.author
      embed = discord.Embed(color=0x6CE5E8, description=f"""{author.name} забанил участника {member}
      Причина: {reason}""".replace("None", "Отсуствует"), title="Блокировка")
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Вызвал: {ctx.author}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
      await ctx.send(f"{ctx.author.mention} вам не позволено выполнять данную команду")  

@bot.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx, member: discord.Member, *, reason=None):
  if member == ctx.message.author:
      embed = discord.Embed(color=discord.Color.red(),title="Ошибка!",description="Вы не можете кикнуть себя!")
      await ctx.send(embed=embed)
  else:
      await member.ban(reason=reason)
      author = ctx.message.author
      embed = discord.Embed(color=0x6CE5E8, description=f"""{author.name} кикнул участника {member}
      Причина: {reason}""".replace("None", "Отсуствует"), title="Кикнутное")
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Вызвал: {ctx.author}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

@bot.command(aliases = ["emb"])
async def ембед(ctx, *, arg: str = None):
    if arg is None:
      embed = discord.Embed(title = "Ошибка!", color=discord.Color.red(), description= "Отсуствует аргумент!")
      embed.add_field(name = "Доступные аргументы", value = "``текст``", inline = True)
      await ctx.send(embed = embed)
    else:
      author = ctx.message.author
      embed = discord.Embed(color=0x0000ff, description=arg, title = f"""""")
      await ctx.send(embed = embed)


@bot.command() 
async def info(ctx,member:discord.Member=None):
  if member is None:
    member = ctx.author
    embed = discord.Embed(description=f"""**Ник** - {member.name}
**ID** - {member.id}
**Серверный ник** - {member.nick}
**Статус** - {member.status}
**Тэг** - #{member.discriminator}""".replace("None", "Отсутствует").replace("offline", "Не в сети <:offline:840225792813826119>").replace("dnd", "Не беспокоить <:dnd:840225792743309313>").replace("online", "В сети <:online:840225793031405588>").replace("idle", "Не активен"), title=f"Инфо о участнике - {member.name}", color=0x6CE5E8)
    embed.add_field(name="Даты", value=f"""**Дата создания** - {member.created_at.year}.{member.created_at.month}.{member.created_at.day}
**Присоединился к серверу** - {member.joined_at.year}.{member.joined_at.month}.{member.joined_at.day} {member.joined_at.hour}:{member.joined_at.minute}:{member.joined_at.second}""", inline=False)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(description=f"""**Ник** - {member.name}
**ID** - {member.id}
**Серверный ник** - {member.nick}
**Статус** - {member.status}
**Тэг** - #{member.discriminator}""".replace("None", "Отсутствует").replace("offline", "Не в сети <:offline:840225792813826119>").replace("dnd", "Не беспокоить <:dnd:840225792743309313>").replace("online", "В сети  <:online:840225793031405588>").replace("idle", "Не активен"), title=f"Инфо о участнике - {member.name}", color=0x6CE5E8)
    embed.add_field(name="Даты", value=f"""**Дата создания** - {member.created_at.year}.{member.created_at.month}.{member.created_at.day}
**Присоединился к серверу** - {member.joined_at.year}.{member.joined_at.month}.{member.joined_at.day} {member.joined_at.hour}:{member.joined_at.minute}:{member.joined_at.second}""", inline=False)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)

@bot.command(aliases = ["баланс"]) 
async def balance(ctx, member : discord.Member):
    money_user = 250
    bank_user = 600
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name = "💳Баланс", value = f"💰У вас на руках= {money_user}\n🏛У вас в банке {bank_user}")
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('<a:3_:843027198419140648>')

@bot.command(aliases = ["ютуб"]) 
async def streaming(ctx, member : discord.Member):
    subscribers_user = 0
    video_user = 2
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name = "❗Стриминг❗", value = f"\n\n🟥**`Подписчиков = {subscribers_user}`** \n🟨**`Видио на канале = {video_user}`**")
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('<a:3_:843027198419140648>')   

@bot.command(aliases = ["обнова 0.01"]) 
async def обнова(ctx):
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name = "***❗Обновления Бота***\n", value = f"\n\n🟥***Тут публикуются обновления бота!***\n\n1.Были добавлены новые команды!")
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('<a:3_:843027198419140648>')   

@bot.command(aliases = ["жб"]) 
async def жалоб(ctx):
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name = "***❗Жалобы***\n", value = f"\n\n🟥***В разработке!!***\n🟥***Comming soon!")
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('<a:3_:843027198419140648>')  


@bot.command()
async def main(ctx,*, arg = None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author}\n please enter:\n.miner rules\n.miner commands')
    elif arg == "rules":
        await ctx.send(f'{author}\n Rules\nИх пока что нету=)')
    elif arg == "commands":
        await ctx.send(f'{author}\n My commands\n.userinfo - example: .userinfo @Miner\n.serverinfo - example: .serverinfo\n пока больше команд нету, но мы постараемся добавить=)')
    else:
        await ctx.send(f'{author}\n this command not registered!')

import random
@bot.command()
async def привет(ctx):
    await ctx.send(f':grinning: {random.choice(["Привет","Ку","Салам","hello","Хай"])}, {ctx.author.mention}')

import random
@bot.command()
async def какдела(ctx):
    await ctx.send(f':grinning: {random.choice(["Нормально", "Хорошо"])}, а у тебя? {ctx.author.mention}')

import random
@bot.command()
async def c(ctx):
    await ctx.send(f':grinning: {random.choice(["Иди нахуй", "Ебало офни даун"])} {ctx.author.mention}')

import random
@bot.command()
async def нормально(ctx):
    await ctx.send(f':grinning: {random.choice(["Понятненько,Что делаеш?"])} {ctx.author.mention}')

import random
@bot.command()
async def нечего(ctx):
    await ctx.send(f':grinning: {random.choice(["Почему? Пису Сосав?"])} {ctx.author.mention}')

import random
@bot.command()
async def пока(ctx):
    await ctx.send(f':grinning: {random.choice(["Пока..Было хорошо обшаться (0)_(0)"])} {ctx.author.mention}')         

@bot.command(aliases=['roleinfo', 'рольинфо', 'rinf'])
async def роль(ctx, role: discord.Role = None):
    if role is None:
        await ctx.send(
            "**Укажите роль в которой хотите посмотреть информацию!**")
    else:
        rol = discord.Embed(
            description=f' **Информация о роли {role.mention}**',
            color=0x25c059)
        rol.set_thumbnail(url=ctx.guild.icon_url)
        rol.add_field(name="Название:", value=f'{role.name}', inline=False)
        rol.add_field(
            name="Айди роли:",
            value=f'{role.id} ',
        )
        rol.add_field(name="Сервер:", value=f'{role.guild} ', inline=False)
        rol.add_field(name="Положение роли:",
                      value=f'{role.position} ',
                      inline=False)
        rol.add_field(name="Отображение от других участников:",
                      value=f'{role.hoist} ',
                      inline=False)
        rol.add_field(name="Участников с этой ролью:",
                      value=f'{len(role.members)} ',
                      inline=False)
        rol.add_field(name="Код цвета роли:",
                      value=f'{role.color}',
                      inline=False)
        rol.add_field(name="Дата созадния роли:",
                      value=f'{role.created_at.strftime("%d.%m.%Y %H:%M")}',
                      inline=False)
        rol.add_field(name="Могут ли участники упоминать роль:",
                      value=f'{role.mentionable}',
                      inline=False)
        rol.set_footer(text=f'Вызвал: {ctx.author}',
                       icon_url=ctx.author.avatar_url)
        await ctx.send(embed=rol)


@bot.command()
async def сервер(ctx):
    idle = 2  # Статусы
    dnd = 0
    offline = 0
    online = 0
    guild = ctx.guild  # Guild
    members = ctx.guild.member_count
    text_channels = len(ctx.guild.text_channels)
    channels = len(ctx.guild.channels)
    categories = len(ctx.guild.categories)
    voice_channels = len(ctx.guild.voice_channels)
    for member in ctx.guild.members:
        if "idle" in member.status:
            idle += 1
        elif "dnd" in member.status:
            dnd += 1
        elif "online" in member.status:
            online += 1
        elif "offline" in member.status:
            offline += 1
        embed = discord.Embed(title="<:748834437097062421:825600198712885279> Инфо о сервере<:748834437097062421:825600198712885279> ",
                              description=f"""**<:494223467399348225:825600595230064650> Название<:494223467399348225:825600595230064650> ** - {guild.name}
**ID** - {guild.id}
**Участники** - {members}""",
                              color=0xe74c3c)
        embed.add_field(name="Подробнее о участниках",
                        value=f"""**В сети** - {online}
**Не в сети** - {offline}
**Не беспокоить** - {dnd}
**Не активны** - {idle}""",
                        inline=False)
        embed.add_field(name="Подробнее о каналах",
                        value=f"""**Всего** - {channels}
**Текстовые каналы** - {text_channels}
**Голосовые каналы** - {voice_channels}
**Категории** - {categories}
**АФК канал** - {guild.afk_channel}
**Системный канал** - {guild.system_channel}""".replace("None", "Отсутствует"),
                        inline=False)
        embed.add_field(
            name="Подробнее о сервере",
            value=f"""**Создатель** - {guild.owner}
**Дата создания** - {guild.created_at.day}.{guild.created_at.month}.{guild.created_at.year}
**Уровень верефикации** - {guild.verification_level}""".replace(
                "very_high",
                "Очень высокий").replace("high", "Высокий").replace(
                    "medium", "Средний").replace("low", "Низкий").replace(
                        "None", "Отсутствует"),
            inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

from asyncio import sleep
import random
@bot.command(name = "ball", aliases = ["шар"])
async def ball(ctx, *, arg=None):
    if arg:
        msg = await ctx.send(embed = discord.Embed(title="Шар судьбы",description=random.choice(['Дай-ка подумать...', 'Дай-ка подумать над ответом...', 'Минутку, я думаю...', 'Хм...']), color=0x001000))
        emb = discord.Embed(title="Шар судьбы", description=f'Вопрос: {arg}', timestamp=ctx.message.created_at, color=0x009900)
        emb.add_field(name="Ответ", value=random.choice([f"Уверен на {random.randrange(0, 100)}% что {random.choice(['нет', 'да'])}.", "Да.", "Нет.", "Возможно.", "Пожалуй я откажусь от ответа :eyes:", "Понятия не имею.", "Я не понял, повтори.", "Определённо да.", "Определённо нет.", "Конечно же\nнет.", "Конечно же да.", "Конечно."]))
        await sleep(2)
        await msg.edit(embed = emb)
    else:
        emb=discord.Embed(title="Шар судьбы", description="Самая обычная команда которая дает ответ на ваш вопрос синонимами да или нет")
        emb.add_field(name="Принцип работы", value="H:ball_of_fate (<Ваш вопрос>)", color=0x009900)
        await ctx.send(embed=emb)

@bot.command(name="ship",aliases=["шип","шиперить"])
async def ship(ctx,member:discord.Member=None):
    if member!=None:
        if member.id==822368382426152990:
            await ctx.send(embed=discord.Embed(title='Замечание',description='Я всего лишь бот, а не пользователь интернета, так что я не могу сравнить насколько ты меня любишь. ‘•~•`'))
        elif member.id!=ctx.author.id:
            num=random.randrange(0,100)
            comment='Какой крейне печальный результат... 😭'
            symbols=[":Ship0:",":Ship1:",":Ship2:",":Ship3:",":Ship4:",":Ship5:"]
            symbol1,symbol2,symbol3,symbol4,symbol5,symbol6,symbol7,symbol8,symbol9,symbol10=symbols[0],symbols[3],symbols[3],symbols[3],symbols[3],symbols[3],symbols[3],symbols[3],symbols[3],symbols[5]
            if num>=10:
                symbol1=symbols[1]
                comment='Ну, видимо не судьба. 🥲'
            if num>=20:
                symbol2=symbols[2]
                comment='Это конечно больше чем 10%, но всё равно печально. :worried:'
            if num>=30:
                symbol3=symbols[2]
                comment='Результат такой себе, но сойдёт. :confused:'
            if num>=40:
                symbol4=symbols[2]
                comment='Хоть даже не половина, но тоже неплохо. :kissing:'
            if num==50:
                symbol5=symbols[2]
                comment='Вау, ровно половина. :eyes:'
            if num>50:
                symbol5=symbols[2]
                comment='Больше половины, неплохо. :hugging:'
            if num>=60:
                symbol6=symbols[2]
                comment='Ещё больше половины, здорово. :slight_smile:'
            if num>=70:
                symbol7=symbols[2]
                comment='Хорошее число, но можно было побольше. :smirk:'
            if num>=80:
                symbol8=symbols[2]
                comment='Отличное число! :smile:'
            if num>=90:
                symbol9=symbols[2]
                comment='Не 100, но тоже круто! :grin:'
            if num>=100:
                symbol10=symbols[4]
                comment='НАИЛУЧШЕЕ ЧИСЛО! :heart_eyes:'
            emb=discord.Embed(title='Шип',description=f"{ctx.author.mention} совместим(а) с {member.mention} на\n{symbol1}{symbol2}{symbol3}{symbol4}{symbol5}{symbol6}{symbol7}{symbol8}{symbol9}{symbol10} {num}%\n{comment}")
            await ctx.send(embed=emb)
        else:
            await ctx.send(embed=discord.Embed(title='Ошибка!',description='Самолюбие это, конечно, хорошо, но проверять насколько это извращение. •~•'))
    else:
        emb=discord.Embed(title='Команда "ship"',description='С помощью этой команды можно узнать насколько вы совместимы с кем-то.')
        emb.add_field(name='Принцип работы',value='-ship <упоминание>\nСамого себя нельзя.')
        await ctx.send(embed=emb)		

@bot.command()  # У кого bot поменяйте
async def инфо(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        embed = discord.Embed(description=f"""**Ник** - {member.name}
**ID** - {member.id}
** Серверный ник** - {member.nick}
**Статус** - {member.status}
**Тэг** - #{member.discriminator}""".replace("None", "Отсутствует").replace(
            "offline", "Не в сети").replace("dnd", "Не беспокоить").replace(
                "online", "В сети").replace("idle", "Не активен"),
                              title=f"Инфо о участнике - {member.name}",
                              color=0x6CE5E8)
        embed.add_field(
            name="Даты",
            value=
            f"""**Дата создания** - {member.created_at.year}.{member.created_at.month}.{member.created_at.day}
**Присоединился к серверу** - {member.joined_at.year}.{member.joined_at.month}.{member.joined_at.day} {member.joined_at.hour}:{member.joined_at.minute}:{member.joined_at.second}""",
            inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description=f"""**Ник** - {member.name}
**ID** - {member.id}
**Серверный ник** - {member.nick}
**Статус** - {member.status}
**Тэг** - #{member.discriminator}""".replace("None", "Отсутствует").replace(
            "offline", "Не в сети").replace("dnd", "Не беспокоить").replace(
                "online", "В сети").replace("idle", "Не активен"),
                              title=f"Инфо о участнике - {member.name}",
                              color=0x6CE5E8)
        embed.add_field(
            name="Даты",
            value=
            f"""**Дата создания** - {member.created_at.year}.{member.created_at.month}.{member.created_at.day}
**Присоединился к серверу** - {member.joined_at.year}.{member.joined_at.month}.{member.joined_at.day} {member.joined_at.hour}:{member.joined_at.minute}:{member.joined_at.second}""",
            inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

@bot.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900,
                          title='<:494223467399348225:825600595230064650> Случайная Лиса<:494223467399348225:825600595230064650> ')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed



# Запуск севера
keep_alive.keep_alive()

# Логин бота
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)