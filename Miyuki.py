#By: BlackZacky
#Discord: BlackZacky#5911

# -*- coding: utf-8 -*-
import discord
import asyncio
import random
import requests
import aiohttp
import websockets
import os
import time
import json
import config
import re
import datetime
import async_timeout
import sys
import psutil

def verificar_login(id):
    logado = False
    verificar_login = open("login.txt", "r")
    for login in verificar_login.readlines():
        login = login.replace("\n", "")
        if login == id:
            logado = True
            break
        else:
            logado = False
    verificar_login.close()
    if logado == True:
        return True
    else:
        return False

def verificar_idlog(id1):
    logado1 = False
    verificar_login1 = ("427640912529588224")
    if verificar_login1 == id1:
        logado1 = True
    else:
        logado1 = False
    if logado1 == True:
        return True
    else:
        return False

prefix = (config.prefix)
adminslist = (config.ListADM)
imgopen = (config.imgopensoruce)
eventt = (config.event)
eventi = (config.eventi)

start_time = time.time()
client = discord.Client()

@client.event
async def on_ready():
    os.system("cls||clear")
    print('LIGOU')
    await client.change_presence(game=discord.Game(name=config.statusmsg, url=config.urllive, type=config.statusbot))
    while True:
       await client.change_presence(game=discord.Game(name='Não sabe meus comandos ? digite '+prefix+'comandos ou '+prefix+'help', type=0))
       await asyncio.sleep(40)
       await client.change_presence(game=discord.Game(name='JrBlackBot 2.0', type=0))
       await asyncio.sleep(30)
       await client.change_presence(game=discord.Game(name='New 2.0', type=0))
       await asyncio.sleep(20)
       #string = "Estou online em "+str(len(client.servers))+", com "+str(len(set(client.get_all_channels())))+" canais."
       #await client.change_presence(game=discord.Game(name=string, type=0))
       #await asyncio.sleep(40)
       await client.change_presence(game=discord.Game(name="Não sabe meus comandos ? "+prefix+"comandos ou "+prefix+"help", type=0))
       await asyncio.sleep(30)
       await client.change_presence(game=discord.Game(name="Para ver meus comandos "+prefix+"comandos", type=0))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name=prefix+"help", type=0))
       await asyncio.sleep(10)
       await client.change_presence(game=discord.Game(name="Olá tudo bem ?", type=0))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name=prefix+"comandos", type=0))
       await asyncio.sleep(40)
       await client.change_presence(game=discord.Game(name="JrBlack 2.0", type=0))

@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'calc'):
        # MAIS
        if message.content.split(' ')[2] == '+':
            if message.content.split(" ")[1]:
                a = int(message.content.split(' ')[1])
                b = int(message.content.split(' ')[3])
                await client.send_message(message.channel, a+b)
        # MENOS
        elif message.content.split(' ')[2] == '-':
            if message.content.split(" ")[1]:
                a = int(message.content.split(' ')[1])
                b = int(message.content.split(' ')[3])
                await client.send_message(message.channel, a-b)
        # Multiplicação
        elif message.content.split(' ')[2] == '*':
            if message.content.split(" ")[1]:
                a = int(message.content.split(' ')[1])
                b = int(message.content.split(' ')[3])
                await client.send_message(message.channel, a*b)

    if message.content.split(' ')[0] == 'jr':
        msg = message.content[3:]
        await client.send_typing(message.channel)
        response = requests.get("http://jrblackbot-com.umbler.net/bot.php?msg="+msg)
        await client.send_message(message.channel, response.text)

    if message.content == prefix+'cadastrar':
        channellogs = client.get_channel('453025344379682826')

        check = ('<:check:455896992690995211>')
        block = ('<:unvalid:455896993110163466>')

        if verificar_login(message.author.id) == True:
            #EMBED 1
            em1 = discord.Embed(title=block+'Aviso:', description='Você já está cadastrado em nosso sistema.', colour=0xff3838, timestamp=message.timestamp)
            em1.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await client.add_reaction(message, ':unvalid:455896993110163466')
            em1.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(message.author, embed=em1)

            print("%s tentou se cadastrar porém já esta cadastrado." % message.author.name)

            #EMBED 2
            em2 = discord.Embed(title=block+'Aviso:', description='**{}** Tentou se cadastrar porém já esta cadastrado!'.format(message.author.name), colour=0xff3838, timestamp=message.timestamp)
            em2.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            em2.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=em2)
        else:
            #EMBED 3
            cadastrar = open("login.txt", "a+")
            cadastrar.write(message.author.id + "\n")
            cadastrar.close()
            await client.add_reaction(message, ':check:455896992690995211')
            em3 = discord.Embed(title=check+'Sucesso:', description='Parabéns **' + message.author.name + '** você foi cadastrado.', colour=0x2ecc71, timestamp=message.timestamp)
            em3.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            em3.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(message.author, embed=em3)

            print("%s foi cadastrado com sucesso." % message.author.name)

            #EMBED 4
            em4 = discord.Embed(title=check+'Sucesso:', description='**{}** foi cadastrado.'.format(message.author.mention), colour=0x2ecc71, timestamp=message.timestamp)
            em4.set_author(name=message.author.name,icon_url=message.author.avatar_url)
            em4.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=em4)

    try:
        if verificar_idlog(message.author.id) == False:
            channellogs = client.get_channel('453025344379682826')
            server = (message.server.name)
            member = (message.author.name)
            log = message.content[0:]
            embedlogs = discord.Embed(title='Mensagem de Texto', colour=0xffb200, timestamp=message.timestamp)
            embedlogs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            embedlogs.add_field(name='Mensagem:',value='```{}```'.format(log), inline=False)
            embedlogs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embedlogs.set_footer(text="JrBlack")
            await client.send_message(channellogs, embed=embedlogs)
    except:
        if verificar_idlog(message.author.id) == False:
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            embedlogs = discord.Embed(title='Mensagem de Texto', colour=0xff7f00, timestamp=message.timestamp)
            embedlogs.add_field(name='Servidor:', value='**DM/Privado**', inline=False)
            embedlogs.add_field(name='Mensagem:',value='```{}```'.format(log), inline=False)
            embedlogs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embedlogs.set_footer(text="JrBlack")
            await client.send_message(channellogs, embed=embedlogs)

    if message.channel == client.get_channel('440641499621752843'):
            await client.add_reaction(message, "👍")
            await client.add_reaction(message, "👎")

    if message.content.startswith(prefix + 'roleta'):
            Roleta = ["DEU SORTE, AINDA ESTA VIVO :(","MORREU:D"]
            choice = random.choice(Roleta)
            embedrol = discord.Embed(title='Roleta', description=choice, color=0x1abc9c)
            embedrol.set_thumbnail(url=config.imgrol)
            await client.send_message(message.channel, embed=embedrol)

    if message.content.startswith(prefix + 'moeda'):
        Coin = ["É CARA!", "É COROA!"]
        choice = random.choice(Coin)
        embedcon = discord.Embed(title='Moeda', description=choice, colour=0x1abc9c)
        embedcon.set_thumbnail(url=config.imgmoeda)
        await client.send_message(message.channel, embed=embedcon)

    if message.content.startswith(prefix + 'dado'):
        choice  = random.randint(1,6)
        embeddad = discord.Embed(title = 'Dado', description = ' Joguei o dado, o resultado é :   {}'.format(choice), colour = 0x1abc9c)
        embeddad.set_thumbnail(url=config.imgdado)
        await client.send_message(message.channel, embed=embeddad)

    if message.content.startswith(prefix + 'eco'):
        eco = message.content[5:].strip()
        try:
            embed3 = discord.Embed(title="Eco", description=" \n ", color=0xff072c)
            embed3.add_field(name="{} Falou...".format(message.author.name), value=eco, inline=False)
            embed3.set_thumbnail(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed3)
            await client.delete_message(message)
        except Exception as e:

            embed3 = discord.Embed(title="ERROR", description=" \n ", color=0xff0000)
            embed3.add_field(name="Falha ao executar.".format(message.author.name),
                            value="Se acontecer esse erro 3#0001\nA frase causadora do foi" + eco, inline=False)
            await client.send_message(message.channel, embed=embed3)
            await client.delete_message(message)

    if message.content.startswith(prefix + 'ping'):
        pingtime = time.time()
        e = discord.Embed(title = 'Ok espere', color = 0x1abc9c)
        pingus = await client.send_message(message.channel, embed=e)
        ping = time.time() - pingtime
        ping1 = discord.Embed(title = 'Pong!', description = ':ping_pong: Ping time - `%.01f seconds`' % ping, colour = 0x1abc9c)
        await client.edit_message(pingus, embed=ping1)

    if message.content.startswith(prefix + 'py'):
        codepy = message.content[4:]
        respostapy = (message.author.mention+' Enviou um code de Python```python\n'+codepy+'```')
        await client.send_message(message.channel, respostapy)
        await client.delete_message(message)

    if message.content.startswith(prefix + 'js'):
        codejs = message.content[4:]
        respostajs = (message.author.mention+' Enviou um code de JS```js\n'+codejs+'```')
        await client.send_message(message.channel, respostajs)
        await client.delete_message(message)

######################### CADASTRADOS #########################
    if message.content.startswith(prefix  + 'comandos') or message.content.startswith(prefix + 'help'):
        helpi = ('<:help:457441667184721943>')
        manuali = ('<:manual:457442220975325186>')
        musici = ('<:musicnotes:457443025929633804>')

        helpuser = discord.Embed(title="Lista de comandos do {}".format(client.user.name),
                        description=manuali+"Página 1",
                        color=0x30abc0,
                        timestamp=message.timestamp)
        helpuser.add_field(name=helpi+'Comandos:',
                           value='**{}report** <Msg> Reportar algum erro ou bug.\n'.format(prefix)+
                                 '**{}roleta** Game roleta russa.\n'.format(prefix)+
                                 '**{}dado** Game Dado.\n'.format(prefix)+
                                 '**{}moeda** Game Cara ou coroa.\n'.format(prefix)+
                                 '**{}eco** <Msg> Bota sua mensagem em um embed.\n'.format(prefix)+
                                 '**{}diz** <Msg> O bot ira enviar a mensagem passada.\n'.format(prefix)+
                                 '**{}votar** <Msg> Você ira iniciar uma votação.\n'.format(prefix)+
                                 '**{}btc** Valor do BitCoin.\n'.format(prefix)+
                                 '**{}usd** Valor do Dolar.\n'.format(prefix)+
                                 '**{}noticias** Noticias atuais.\n'.format(prefix)+
                                 '**{}cep** <Num> localizar de onde é o **cep** passado.\n'.format(prefix)+
                                 '**{}clima** <Lugar> Clima na cidade passada.\n'.format(prefix)+
                                 '**{}ip** <Num> Localizar de onde é o ip passado.\n'.format(prefix)+
                                 '**{}calc** <Num> <+/-/*> <Num> ira fazer um calculo com o numero passado.\n'.format(prefix)+
                                 '**{}cadastrar** Ira lhe cadastrar em nosso sistema.\n'.format(prefix), inline=False)
        global bothelp
        bothelp = await client.send_message(message.channel, embed=helpuser)
        rea = await client.add_reaction(bothelp, "➡")
        reax = message.server.get_member(client.user.id)

        @client.event
        async def on_reaction_add(reaction, user):
            msg = reaction.message
            chat = reaction.message.author
            global testmsgid2
            testmsgid2 = bothelp.id
            global testmsguser2
            testmsguser2 = message.author
            global chatgroup
            chatgroup = message.channel
            if reaction.emoji == "➡" and msg.id == testmsgid2 and user == testmsguser2:
                embedinfo = discord.Embed(name='Lista de comandos do {}'.format(client.user.name),
                                          color=0x30abc0,
                                          description=manuali+'Página 2',
                                          timestamp=message.timestamp)
                embedinfo.add_field(name=helpi+'Comandos:',
                                          value='**{}avatar** <@Usuario> Pega o avatar do usuario.\n'.format(prefix)+
                                                '**{}userinfo** <@Usuario> Informações do usuario solicitado.\n'.format(prefix)+
                                                '**{}botinfo** Informações o bot.\n'.format(prefix)+
                                                '**{}serverinfo** Informações do server.\n'.format(prefix)+
                                                '**{}gcpf** Gera um cpf.\n'.format(prefix)+
                                                '**{}gcnpj** Gera um cnpj.\n'.format(prefix)+
                                                '**{}encurtador** <URL> encurta a url.\n'.format(prefix)+
                                                '**{}proxy** <Num> ira lhe enviar proxys.\n'.format(prefix)+
                                                '**{}traduzir** <Lang><Texto/Palavra> Traduz a palavra passada.\n'.format(prefix)+
                                                '**{}ping** Informa o ping do bot.\n'.format(prefix)+
                                                '**{}py** <Code> Deixa o **code** em um estado mais legível.\n'.format(prefix)+
                                                '**{}js** <Code>Deixa o **code** em um estado mais legível.\n'.format(prefix))
                embedinfo.add_field(name=musici+'Música(BETA):',
                                    value='**{}tocar** <URL_YB> Começar a tocar a música.\n'.format(prefix)+
                                          '**{}pausar** Pausar a música.\n'.format(prefix)+
                                          '**{}resumo** Dar play na música depois de pausada.\n'.format(prefix)+
                                          '**{}entrar** Entrar no canal.\n'.format(prefix)+
                                          '**{}sair** Sair do canal.\n'.format(prefix))
                global infodel
                infodel = await client.edit_message(bothelp, embed=embedinfo)
                reax = message.server.get_member(client.user.id)
                await client.remove_reaction(msg, "➡", reax)
                await client.add_reaction(infodel, '⬅')

            if reaction.emoji == "⬅" and msg.id == testmsgid2 and user == testmsguser2:
                opa = await client.edit_message(bothelp, embed=helpuser)
                reax = message.server.get_member(client.user.id)
                await client.remove_reaction(msg, "⬅", reax)
                await client.add_reaction(infodel, '➡')

    if message.content.startswith(prefix + 'traduzir'):
        msg = message.content.split(' ')[1]
        msg2 = message.content[13:]
        msg3 = str(msg2).replace(" ","+")
        
        trans = ('<:traduzindo:457427699934429196>')
        ori = ('<:pen:457430406413680651>')

        r = requests.get("http://mymemory.translated.net/api/get?q="+msg3+"&langpair=|"+msg)
        if  r.status_code == 200:
            js = r.json()
            traduzido = js['responseData']['translatedText']

        embed = discord.Embed(colour=0x03a6d6, timestamp=message.timestamp)
        embed.add_field(name=ori+"Texto original:",value='```{}```'.format(msg2), inline=False)
        embed.add_field(name=trans+"Texto traduzido:",value='```{}```'.format(traduzido), inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/7ja89PP.png")
        embed.set_footer(text='{} {}'.format(client.user.name,client.user.created_at.strftime("%Y")),
                         icon_url='https://i.imgur.com/XAGx3Ct.png')

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(prefix + 'proxy'):
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title='Comando {}'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            quantidade = message.content[7:]
            conta = 0
            await client.delete_message(message)
            while(conta <= int(quantidade)):
                conta += 1
                requegetusd = requests.get('https://gimmeproxy.com/api/getProxy?protocol=socks5')
                proxy = json.loads(requegetusd.text)
                proxyend = (str(proxy['ipPort']))
                await client.send_message(message.author, '{}'.format(proxyend))

    if message.content.startswith(prefix + 'gcpf'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            response = requests.get("http://jrblackbot-com.umbler.net/gerarcpf.php")
            embed = discord.Embed(description="{}".format(response.text), timestamp=message.timestamp)
            embed.set_author(name="{} Gerador de Cpf".format(message.author.name), icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)
            emsuss = discord.Embed(title='Gerador:', description='**{}** Gerou um CPF'.format(message.author.mention), colour=0x2ecc71)
            emsuss.set_author(name=message.author.name,icon_url=message.author.avatar_url)
            emsuss.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=emsuss)

    if message.content.startswith(prefix + 'gcnpj'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            response = requests.get("http://jrblackbot-com.umbler.net/gerarcnpj.php")
            embed = discord.Embed(description="{}".format(response.text))
            embed.set_author(name="{} Gerador de Cnpj".format(message.author.name), icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)
            emsuss = discord.Embed(title='Gerador:', description='**{}** Gerou um CNPJ'.format(message.author.mention), colour=0x2ecc71, timestamp=message.timestamp)
            emsuss.set_author(name=message.author.name,icon_url=message.author.avatar_url)
            emsuss.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=emsuss)

    if message.content.startswith(prefix + 'ip'):
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title='Não cadastado', colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='{} executou um comando restrito a os cadastrados!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text="Comando {}ip".format(prefix))
            await client.send_message(channellogs, embed=logs)
        else:
            ipmsg = message.content[4:]
            requestip = requests.get('http://ip-api.com/json/'+ipmsg)
            ip = json.loads(requestip.text)
            city = (str(ip['city']))
            country = (str(ip['country']))
            region = (str(ip['regionName']))
            timezone = (str(ip['timezone']))
            zipcode = (str(ip['zip']))
            embedip = discord.Embed(color=0xff6100)
            embedip.set_author(name='{}'.format(message.author.name), icon_url=message.author.avatar_url)
            embedip.add_field(name='LocaleIP:', value='**Ip:** {}\n\n**País:** {}\n\n**Estado:** {}\n\n**Cidade:** {}\n\n**ZipCode/CEP:** {}'.format(ipmsg,country,region,city,zipcode))
            embedip.set_footer(text='© 2018 BlackZacky')
            botmsg = await client.send_message(message.channel, embed=embedip)
            await client.add_reaction(botmsg, "🗑")
            await client.add_reaction(botmsg, "📥")
            testmsgid = botmsg.id
            testmsguser = message.author
            @client.event
            async def on_reaction_add(reaction, user):
                msg = reaction.message
                chat = reaction.message.channel
                if reaction.emoji == "🗑" and msg.id == testmsgid and user == testmsguser:
                    await client.delete_message(message)
                    await client.delete_message(botmsg)
                if reaction.emoji == "📥" and msg.id == testmsgid and user == testmsguser:
                    global respdeleip
                    respdeleip = await client.send_message(message.author, embed=embedip)
            @client.event
            async def on_reaction_remove(reaction, user):
                msg = reaction.message
                if reaction.emoji == "📥" and msg.id == testmsgid and user == testmsguser: #and user == msg_user:
                    await client.delete_message(respdeleip)

    if message.content.startswith(prefix + 'encurtador'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')

        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='O usuario {} tentou encurtar o link ``{}``'.format(member, log), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='Comando {}encurtador'.format(prefix), icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            urlmsg = message.content[12:]
            requesturl = requests.get('https://vurl.com/api.php?url='+urlmsg)
            urlcut = (requesturl.text)
            embedurl = discord.Embed(color=0x00000)
            embedurl.add_field(name='Sua url não encurtada:', value='```{}```\n'.format(urlmsg), inline=False)
            embedurl.add_field(name='Sua url encurtada:', value='```{}```\n'.format(urlcut), inline=False)
            embedurl.set_footer(text='© 2018 BlackZacky')
            botmsg = await client.send_message(message.channel, embed=embedurl)
            await client.add_reaction(botmsg, "🗑")
            await client.add_reaction(botmsg, "📥")
            testmsgid = botmsg.id
            testmsguser = message.author
            @client.event
            async def on_reaction_add(reaction, user):
                msg = reaction.message
                chat = reaction.message.channel
                if reaction.emoji == "🗑" and msg.id == testmsgid and user == testmsguser:
                    await client.delete_message(botmsg)
                    await client.delete_message(message)
                if reaction.emoji == "📥" and msg.id == testmsgid and user == testmsguser:
                    global respdele
                    respdele = await client.send_message(message.author, embed=embedurl)
            @client.event
            async def on_reaction_remove(reaction, user):
                msg = reaction.message
                if reaction.emoji == "📥" and msg.id == testmsgid and user == testmsguser: #and user == msg_user:
                    await client.delete_message(respdele)

    if message.content.startswith(prefix + 'userinfo'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            user = message.mentions[0]
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='{} tentou pegar as informações do usuario {}'.format(member, user), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                user = message.mentions[0]
                usergame = (str(user.game))

                dogtag = ('<:dogtag:455815179184242689>')
                tag = ('<:tags:455815968992657409>')
                calendar = ('<:calendar2:455644265788473344>')
                ID = ('<:ID1:455632735411896326>')
                name = ('<:name:455617266289999873>')
                discordi = ('<:Discord_Icon:451942597871534090>')
                servers = ('<:server:455626929085743105>')
                color = ('<:colors:455818856359919627>')
                #Programas aleatorios
                spotify = ('<:spotify:455824197130780682>')
                netiflix = ('<:netflix:455824196606361617>')
                #Editor de Texto
                vscode = ('<:VisualCode:451942599604043777>')
                pycharm = ('<:PyCharm:455894370483306498>')
                atom = ('<:atom:455824196979916800>')
                sublime = ('<:sublimetext:455824196992499721>')
                #Jogos
                pubg = ('<:pubg:455824196963139594>')
                csgo = ('<:csgo:455824226327330816>')
                insurgency = ('<:insurgecy:455824224926564353>')
                gta = ('<:rockstar:455824196946231298>')
                fortnite = ('<:fortnite:455828353987903500>')

                embedusu = discord.Embed(color=user.color, timestamp=message.timestamp)
                embedusu.set_thumbnail(url=user.avatar_url)
                embedusu.set_author(name='Suas informações', icon_url='https://cdn.discordapp.com/attachments/417075411789414400/455819437514162196/icons8-dog-tag-48.png')
                embedusu.add_field(name=name+"Seu Nome:", value=user.name, inline=True)
                embedusu.add_field(name=ID+"Seu Id:", value=user.id, inline=True)

                if usergame == 'Visual Studio Code':
                    embedusu.add_field(name="Status:", value='{}``VsCode``'.format(vscode), inline=True)
                elif usergame == 'Spotify':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(spotify, user.game), inline=True)
                elif usergame == 'Netflix':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(netflix,user.game), inline=True)
                elif usergame == 'Fortnite':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(fortnite, user.game), inline=True)
                elif usergame == 'Sublime Text':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(sublime, user.game), inline=True)
                elif usergame == 'Atom':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(atom, user.game), inline=True)
                elif usergame == 'Insurgency':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(insurgency, user.game), inline=True)
                elif usergame == 'Counter-Strike Global Offensive':
                    embedusu.add_field(name='Status:', value='{}``CSGO``'.format(csgo), inline=True)
                elif usergame == 'PLAYERUNKNOWN´S BATTLEGROUNDS':
                    embedusu.add_field(name='Status:', value='{}``PUBG``'.format(pubg), inline=True)
                elif usergame == 'JetBrains IDE':
                    embedusu.add_field(name='Status:', value='{}``{}``'.format(pycharm, user.game), inline=True)
                else:
                    embedusu.add_field(name='Status:', value='``{}``'.format(user.game), inline=True)

                embedusu.add_field(name=calendar+"Entrou no serve em:", value='``{}`` ``{}``'.format(user.joined_at.strftime("%d %b %Y"),user.joined_at.strftime("%H:%M")), inline=True)
                embedusu.add_field(name=discordi+"Desde:", value='``{}`` ``{}``'.format(user.created_at.strftime("%d %b %Y"),user.created_at.strftime("%H:%M")), inline=True)
                embedusu.add_field(name="🌀Maior Cargo:", value='``{}``'.format(user.top_role), inline=True)
                embedusu.add_field(name=color+"Cor:", value='``{}``'.format(user.color), inline=True)
                embedusu.add_field(name=tag+"Tag:", value='``{}``'.format(user.discriminator), inline=True)
                embedusu.set_footer(text='2018 BlackZacky', icon_url=client.user.avatar_url)
                await client.send_message(message.channel, embed=embedusu)
            except IndexError:
                await client.send_message(message.channel, ":confused: Não consegui achar este usuario")
            except:
                await client.send_message(message.channel, ":disappointed_relieved: Desculpe, houve um erro")
            finally:
                pass

    if message.content.startswith(prefix + 'serverinfo'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você só pode pegar as informações deste server se estiver **cadastrado**. Para se cadastrar digite **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'ServerInfo'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
            logs.add_field(name='Ocorrido:',value='{} tentou pegar as infor do server **{}**'.format(member, message.server.name), inline=True)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            server = message.server
            a = len([jr.status for jr in server.members
                            if jr.status == discord.Status.online]) # Online
            b = len([jr.status for jr in server.members
                            if jr.status == discord.Status.idle]) # Ausente
            c = len([jr.status for jr in server.members
                            if jr.status == discord.Status.dnd]) # Ocupado
            d = len([jr.id for jr in server.members if jr.bot]) # Bots
            e = len([jr.id for jr in server.channels if jr.type==discord.ChannelType.text]) # Texto
            f = len([jr.id for jr in server.channels if jr.type==discord.ChannelType.voice]) # Voz
            g = len([jr.id for jr in server.role_hierarchy])
            h = len([jr.id for jr in server.members if jr.status == jr.status == discord.Status.offline])

            membros = len(server.members)
            roles = len(server.roles)
            canais = e + f

            admin = ('<:admin:455592802315927552>')
            bot = ('<:bottag:451942596261183509>')
            on = ('<:Online:451944005895454720>')
            off = ('<:Offline:451942598802931723>')
            dnd = ('<:Ocupado:451942598727434243>')
            afk = ('<:Ausente:451942596210589697>')
            emojis = ('<:Cachorro:402533135629287444>')
            ID = ('<:ID1:455632735411896326>')
            location = ('<:location:455623555678339094>')
            calendar = ('<:calendar2:455644265788473344>')
            mundo = ('<:mundo:455623556013883402>')
            voz = ('<:voice:455646876671410187>')
            texto = ('<:pencill:455646876478341142>')

            online = (f"{a}")
            ausente = (f"{b}")
            ocupado = (f"{c}")
            offline = (f"{h}")
            data = (message.server.created_at.strftime("%d %b %Y"))
            hora = (message.server.created_at.strftime('%H:%M'))

            info = discord.Embed(title="{}".format(message.server.name), color=0x551A8B, timestamp=message.timestamp)
            info.add_field(name=mundo+"Server name:", value="``{}``".format(message.server.name), inline=True)
            info.add_field(name=ID+"Server ID:", value="``{}``".format(message.server.id), inline=True)
            info.add_field(name=admin+"Dono:", value="``{}``".format(message.server.owner.name), inline=True)
            info.add_field(name="🌀Cargos:", value="``{}``".format(roles), inline=True)
            info.add_field(name="👥Membros["+str(membros)+"]:", value='{}``{}`` {}``{}`` {}``{}`` \n{}``{}`` {}``{}``'.format(on,online,dnd,ocupado,afk,ausente,off,offline,bot,d), inline=True)
            info.add_field(name="💬Canais["+str(canais)+"]:", value='{}``{}`` {}``{}``'.format(texto,e,voz,f))
            info.add_field(name=calendar+"Criado em:", value="``{}`` ``{}``".format(data,hora), inline=True)
            info.add_field(name=emojis+"Emojis:", value="``{}``".format(f"{len(message.server.emojis)}/100"), inline=True)
            info.set_thumbnail(url=server.icon_url)

            regionRU = (str(message.server.region).title())
            regionJP = (str(message.server.region).title())
            regionEU = (str(message.server.region).title())
            regionBR = (str(message.server.region).title())
            regionUSA = (str(message.server.region).title())

            #Brasil
            if regionBR == 'Brazil':
                info.add_field(name=location+"Região do server:", value='🇧🇷 Brasil')
            #USA
            elif regionUSA == 'Us-Central':
                info.add_field(name=location+"Região do Server:", value='🇺🇸 ``{}``'.format(str(message.server.region).title()))
            elif regionUSA == 'Us-West':
                info.add_field(name=location+"Região do Server:", value='🇺🇸 ``{}``'.format(str(message.server.region).title()))
            elif regionUSA == 'Us-East':
                info.add_field(name=location+"Região do Server:", value='🇺🇸 ``{}``'.format(str(message.server.region).title()))
            elif regionUSA == 'Us-South':
                info.add_field(name=location+"Região do Server:", value='🇺🇸 ``{}``'.format(str(message.server.region).title()))
            #EUROPA
            elif regionEU == 'Eu-Central':
                info.add_field(name=location+"Região do server:", value='🇪🇺 ``{}``'.format(str(message.server.region).title()))
            elif regionEU == 'Eu-Western':
                info.add_field(name=location+"Região do server:", value='🇪🇺 ``{}``'.format(str(message.server.region).title()))
            #Japão
            elif regionJP == 'Japan':
                info.add_field(name=location+"Região do server:", value='🇯🇵 ``{}``'.format(str(message.server.region).title()))
            #Russia
            elif regionRU == 'Russia':
                info.add_field(name=location+"Região do server:", value='🇷🇺 ``{}``'.format(str(message.server.region).title()))
            else:
                info.add_field(name=location+"Região do Server:", value='``{}``'.format(str(message.server.region).title()))

            info.set_footer(text='© 2018 BlackZacky', icon_url='https://cdn.discordapp.com/attachments/417075411789414400/455632372382171138/icons8-open-source-50.png')
            await client.send_message(message.channel, embed=info)

    if message.content.startswith(prefix + 'botinfo'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} você só poderar ver minhas informações quando estiver cadastrado. Digite **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Informações do bot'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
            logs.add_field(name='Ocorrido:',value='{} tentou pegar minhas informações!'.format(member), inline=True)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            current_time = time.time()
            difference = int(round(current_time - start_time))
            text = str(datetime.timedelta(seconds=difference))

            process = psutil.Process(os.getpid())
            python = (process.memory_info().rss)
            ram = (f"{python / 0x400_000:.2f}MB")

            ping = os.popen('ping 157.240.12.35 -n 1')
            result = ping.readlines()
            msLine = result[-1].strip()
            texto = msLine[28:].replace("M¡nimo = ","").replace(" ximo = "," ").replace(" Max ","").replace(" M‚dia = "," ").replace(","," ").replace(" ","").replace("ms","")+"ms"

            python = ('<:Python3:455627590967754752>')
            java = ('<:nodejs:455628405283618820>')
            php = ('<:PHP:417097682968903702>')
            settings = ('<:settings:455613534651547658>')
            git = ('<:git:455614491225489409>')
            on = ('<:Online:451944005895454720>')
            ID = ('<:ID2:455632735558565899>')
            servers = ('<:server:455626929085743105>')
            discordi = ('<:Discord_Icon:451942597871534090>')
            name = ('<:name:455617266289999873>')
            developer = ('<:developer:455623555955163136>')
            code = ('<:code:455627591127400449>')
            timee = ('<:time:455631554551742465>')
            new = ('<:new:455636415380979723>')
            calendar = ('<:calendar:455642715498217494>')
            rami = ('<:ram:455846293412118528>')
            pingi = (':ping_pong:')
            avatar = ('<:shadow:455860851396837396>')
            espaço = ('                                               ')
            espaço2 = ('                              ')
            espaçoram= ('                                  ')

            embedbotin = discord.Embed(color=0x551A8B, timestamp=message.timestamp)
            embedbotin.set_author(name="JrBlack Bot",icon_url=client.user.avatar_url)
            embedbotin.add_field(name=name+'Meu nome:', value='``{}``'.format(client.user.name),inline=True)
            embedbotin.add_field(name=ID+'Meu ID:', value='``{}``'.format(client.user.id),inline=True)
            embedbotin.add_field(name=avatar+'Meu avatar:',value='[**Link**]({})'.format(client.user.avatar_url))
            embedbotin.add_field(name=new+'Minha versão:', value='``2.0``',inline=True)
            embedbotin.add_field(name=calendar+'Fui criado em:', value='``{}`` ``{}``'.format(client.user.created_at.strftime("%d %b %Y"), client.user.created_at.strftime('%H:%M')),inline=True)
            embedbotin.add_field(name=servers+'Servidores:',value='``{}'.format(str(len(client.servers)))+' Server(s)``',inline=True)
            embedbotin.add_field(name=code+'Fui programado em:', value='{}{}{}'.format(python,java,php),inline=True)
            embedbotin.add_field(name=discordi+'Versão discord:', value="``{}``".format(discord.__version__),inline=True)
            embedbotin.add_field(name=developer+'Desenvolvedor:',value='<@272188868877352960>')
            embedbotin.add_field(name=rami+'Ram:',value='``{}``'.format(ram),inline=True)
            embedbotin.add_field(name=pingi+'Ping:',value='``{}``'.format(texto),inline=True)
            embedbotin.add_field(name=timee+'Tempo ligado:', value='``{}``'.format(text),inline=True)
            embedbotin.add_field(name='🔗Links:', value='{}|GitHub:{}{}|Suporte:\n [**link**](https://github.com/BlackZacky/JrBlack){}[**link**](https://discord.gg/Kd7YA)'.format(git,espaço2,settings,espaço))
            #embedbotin.add_field(name='🤔Outros:',value='Caso queira mandar alguma sugestão de comando ou reportar algum erro. Use o comando ``{0}sug`` para sugestões e ``{0}report`` para reportar algo'.format(prefix))

            #embedbotin.set_thumbnail(url=client.user.avatar_url)
            embedbotin.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)

            await client.send_message(message.channel, embed=embedbotin)

    if message.content.startswith(prefix + 'avatar'):
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title='Comando {}'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text="{} Vamos ao Hexa".format(client.user.name))
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                user = message.mentions[0]
                avatarembed = discord.Embed(
                    title="",
                    color=0xFF8000,
                    description="[Clique aqui]("+ user.avatar_url +") para acessar o link do avatar!")
                avatarembed.set_author(name=user.name)
                avatarembed.set_image(url=user.avatar_url)
                await client.send_message(message.channel, embed=avatarembed)
            except:
                user = message.author
                avatarembed = discord.Embed(
                    title="",
                    color=0xFF8000,
                    description="[Clique aqui]("+ user.avatar_url +") para acessar o link do avatar!")
                avatarembed.set_author(name=user.name)
                avatarembed.set_image(url=user.avatar_url)
                await client.send_message(message.channel, embed=avatarembed)

    if message.content.startswith(prefix + 'diz'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} para usar este comando precisa se cadastrar. Digite **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Diz'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            copiar = message.content[5:].strip()
            await client.delete_message(message)
            await client.send_message(message.channel, copiar)

    if message.content.startswith(prefix + 'votar'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            vote = message.content[7:].strip()
            embed = discord.Embed(title='VOTAÇÃO', color=message.author.color)
            embed.add_field(name='{} iniciou uma votação!'.format(message.author.name), value=vote)
            embed.set_thumbnail(url=message.author.avatar_url)
            votee = await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
            await client.add_reaction(votee, '👍')
            await client.add_reaction(votee,'👎')

    if message.content.startswith(prefix + 'clima'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                mensagem = message.content[7:]
                get = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+mensagem+'&appid=73b2c1d66800fad8cbedfdd4cc82031d')
                tempo = json.loads(get.text)
                nome = (str(tempo['name']))
                #main1 = (str(tempo['weather'][0]['main']))
                dmain1 = (str(tempo['weather'][0]['description']))
                clima1 = (str(tempo['weather'][0]['main']))
                umidade1 = (str(tempo['main']['humidity']))
                #temperatura1 = (str(tempo['weather'][0]['']))
                cordenadas = (str(tempo['coord']['lon']))
                cordenadas2 = (str(tempo['coord']['lat']))
                velocidade1 = (str(tempo['wind']['speed']))
                pais1 = (str(tempo['sys']['country']))
                temp2 = (float(tempo['main']['temp']) - 273.15)

                name = ('<:name:455617266289999873>')
                speed = ('<:speed:457728131122462720>')
                coorde = ('<:mundo:455623556013883402>')
                moisture = ('<:moisture:457729735057866752>')
                name = ('<:name:455617266289999873>')
                temp = ('<:temperature:457740598871326721>')
                
                embedclm = discord.Embed(color=0x00c3ff, timestamp=message.timestamp)
                embedclm.set_author(name='OpenWeatherMap {}'.format(mensagem),
                                    icon_url='https://i.imgur.com/2cpM12m.png')
                embedclm.add_field(name=name+'Nome:', value="{}".format(nome))
                #embedclm.add_field(name='Descrição:', value="{}".format(main1))
                
                if clima1 == 'Rain':
                    embedclm.add_field(name='🌧Clima:', value="{}".format(clima1))
                elif clima1 == 'Clouds':
                    embedclm.add_field(name='☁Clima:', value="{}".format(clima1))
                elif clima1 == 'Fog':
                    embedclm.add_field(name='🌫Clima:', value="{}".format(clima1))
                elif clima1 == 'Clear':
                    embedc1m.add_field(name='☀Clima', value="{}".format(clima1))
                else:
                    embedclm.add_field(name='Clima:', value="{}".format(clima1))
                
                embedclm.add_field(name=coorde+'Cordenadas:', value='{}/{}'.format(cordenadas, cordenadas2))
                embedclm.add_field(name=speed+'Velocidade:', value='{}'.format(velocidade1))

                if pais1 == 'BR':
                    embedclm.add_field(name='🇧🇷Pais:', value='BR')
                elif pais1 == 'US':
                    embedclm.add_field(name='🇺🇸Pais:', value='USA')
                elif pais1 == 'RU':
                    embedclm.add_field(name='🇷🇺Pais:', value='RU')
                elif pais1 == 'AR':
                    embedclm.add_field(name='🇦🇷Pais:', value='AR')
                else:
                    embedclm.add_field(name='Pais:', value='{}'.format(pais1))
                
                embedclm.add_field(name=moisture+'Umidade:', value='{}'.format(umidade1))
                embedclm.add_field(name=temp+'Temperatura:', value='{}ºC'.format(temp2))
                embedclm.set_footer(text=eventt, icon_url=eventi)
                await client.send_message(message.channel, embed=embedclm)
            except:
                await client.send_message(message.channel, "Não achei esta cidade :(")

    if message.content.startswith(prefix + 'btc'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                requeget = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=BTC&alt=json')
                btc = json.loads(requeget.text)
                nomebtc = (str(btc['valores']['BTC']['nome']))
                precobtc = (str(btc['valores']['BTC']['valor']))
                fontebtc = (str(btc['valores']['BTC']['fonte']))
                
                namei = ('<:name:455617266289999873>')
                btci = ('<:btc:457746117594054656>')
                linki = ('<:externallink:457746209503838208>')

                embedbtc = discord.Embed(color=0xffe100, timestamp=message.timestamp)
                embedbtc.set_author(name='{}'.format(message.author.name),
                                        icon_url='https://i.imgur.com/KzRJUaX.png')
                embedbtc.add_field(name=namei+'Nome:', value="{}".format(nomebtc))
                embedbtc.add_field(name=btci+'Valor:', value="{}".format(precobtc))
                embedbtc.add_field(name=linki+'fonte:', value="{}".format(fontebtc))
                embedbtc.set_footer(text=eventt, icon_url=eventi)
                embedbtc.set_thumbnail(url=config.imgbtc)

                await client.send_message(message.channel, embed=embedbtc)
            except:
                await client.send_message(message.channel, 'ERROR! :(')

    if message.content.startswith(prefix + 'usd'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                requegetusd = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=USD&alt=json')
                usd = json.loads(requegetusd.text)
                nomeusd = (str(usd['valores']['USD']['nome']))
                precousd = (str(usd['valores']['USD']['valor']))
                fonteusd = (str(usd['valores']['USD']['fonte']))

                namei = ('<:name:455617266289999873>')
                usdi = ('<:usd:457746117396922369>')
                linki = ('<:externallink:457746209503838208>')

                embedusd = discord.Embed(color=0x307000, timestamp=message.timestamp)
                embedusd.set_author(name='{}'.format(message.author.name),
                                        icon_url='https://i.imgur.com/OUuFS20.png')
                embedusd.add_field(name=namei+'Nome:', value="{}".format(nomeusd))
                embedusd.add_field(name=usdi+'Valor:', value="{}".format(precousd))
                embedusd.add_field(name=linki+'fonte:', value="{}".format(fonteusd))
                embedusd.set_footer(text=eventt, icon_url=eventi)
                embedusd.set_thumbnail(url=config.imgusd)

                await client.send_message(message.channel, embed=embedusd)
            except:
                await client.send_message(message.channel, 'ERROR! :(')

    if message.content.startswith(prefix + 'noticias'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Mensagem:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            reqnews = requests.get('https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=eb75df2b12dc41aa9b8d02545227f03c')
            lernews = json.loads(reqnews.text)
            authornews = (str(lernews['articles'][0]['author']))
            titulonews = (str(lernews['articles'][0]['title']))
            descriptionnews = (str(lernews['articles'][0]['description']))
            urlnews = (str(lernews['articles'][0]['url']))
            datanews = (str(lernews['articles'][0]['publishedAt']))
            imgnews = (str(lernews['articles'][0]['urlToImage']))

            newsi = ('<:news:457630823030456334>')
            titlei = ('<:title:457752948642938904>')
            linki = ('<:externallink:457746209503838208>')
            desci = ('<:desc:457753742092140593>')
            writeri = ('<:writer:457755465133064192>')

            embednews = discord.Embed(color=0x65ff00, timestamp=message.timestamp)
            embednews.set_author(name='Noticias Atuais', icon_url='https://i.imgur.com/4MQGOnA.png')
            if not authornews == 'None':
                embednews.add_field(name=writeri+'Autor:', value="{}".format(authornews))
            else:
                embednews.add_field(name=writeri+'Autor:', value='Google News')

            embednews.add_field(name=titlei+'Titulo:', value="{}".format(titulonews))
            embednews.add_field(name=desci+'Descrição:', value="{}".format(descriptionnews))
            embednews.add_field(name=linki+'Url da noticia:', value="{}".format(urlnews))
            embednews.set_footer(text='Data da noticia: '+datanews, icon_url='https://i.imgur.com/YIKnKoW.png')
            embednews.set_thumbnail(url=imgnews)

            await client.send_message(message.channel, embed=embednews)

    if message.content.startswith(prefix + 'cep'):
        channellogs = client.get_channel('453025344379682826')
        block = ('<:unvalid:455896993110163466>')
        if verificar_login(message.author.id) == False:
            await client.send_message(message.channel, "{} Você não esta cadastrado no nosso sistema! de um **{}cadastrar**".format(message.author.mention,prefix))
            channellogs = client.get_channel('453025344379682826')
            member = (message.author.name)
            log = message.content[0:]
            command = message.content.split(' ')[0]
            logs = discord.Embed(title=block+'Não cadastrado.'.format(command), colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=False)
            logs.add_field(name='Ocorrido:',value='{} tentou executar o comando **{}**, mas não esta cadastrado!'.format(member, command), inline=False)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
        else:
            try:
                cepmsg = message.content[5:]
                requestcep = requests.get('http://api.postmon.com.br/v1/cep/'+cepmsg)
                cep = json.loads(requestcep.text)
                bairro = (str(cep['bairro']))
                cidade = (str(cep['cidade']))
                estado = (str(cep['estado']))
                cep2 = (float(cep['cep']))
                ibge = (float(cep['cidade_info']['codigo_ibge']))
                rua = (str(cep['logradouro']))
                embedcep = discord.Embed(color=0xff6100)
                embedcep.set_author(name='{} Consulta :)'.format(message.author.name),
                                            icon_url=message.author.avatar_url)
                embedcep.add_field(name='Bairro:', value="{}".format(bairro))
                embedcep.add_field(name='Cidade:', value="{}".format(cidade))
                embedcep.add_field(name='Estado:', value="{}".format(estado))
                embedcep.add_field(name='Cep:', value="{}".format(cep2))
                embedcep.add_field(name='City Codigo Ibge:', value="{}".format(ibge))
                embedcep.add_field(name='Rua:', value='{}'.format(rua))
                embedcep.set_footer(text=eventt, icon_url=eventi)
                embedcep.set_thumbnail(url=config.imgcep)
                await client.send_message(message.channel, embed=embedcep)
            except:
                await client.send_message(message.channel, 'ERROR! Cep não encontrado! :(')

    if message.content.startswith(prefix + 'reportar'):
        rep = message.content[9:]
        reportchat = client.get_channel('457451253665103872')
        
        notify = ('<:urgent:457453130075078678>')
        server = ('<:server:455626929085743105>')
        loading = ('<a:loading:457644930425290753>')

        embed = discord.Embed(color=0x770700, timestamp=message.timestamp)
        embed.add_field(name=server+'Servidor:', value='``{}``'.format(message.server.name), inline=False)
        embed.add_field(name='💠Author:', value='{}'.format(message.author.mention), inline=False)
        embed.add_field(name=notify+'Report:', value='{}'.format(rep), inline=False)
        await client.send_message(reportchat, embed=embed)
        await client.delete_message(message)
        #load = await client.send_message(message.channel, 'Enviando!\n{}'.format(loading))
        load = await client.send_file(message.channel, 'loading.gif', content='Enviando!')
        await asyncio.sleep(1.5)
        await client.delete_message(load)
        aaa = await client.send_message(message.channel, 'Obrigado por reportar o erro!')
        await asyncio.sleep(3)
        await client.delete_message(aaa)

########################### MUSICA ############################

    if message.content.startswith(prefix + 'entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Não consegui encontrar nem um canal de voz.")
        except Exception as error:
            await client.send_message(message.channel, "Deu um erro: ```{error}```".format(error=error))

    if message.content.startswith(prefix + 'sair'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Não estou conectado a nem um canal de voz no momento.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Erro: ```{haus}```".format(haus=Hugo))

    if message.content.startswith(prefix + 'tocar'):
        try:
            yt_url = message.content[7:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Erro : [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as error:
                    await client.send_message(message.channel, "Erro: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Erro: [{error}]".format(error=e))

    if message.content.startswith(prefix + 'pausar'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Erro: [{error}]".format(error=error))

    if message.content.startswith(prefix + 'resumo'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Erro: [{error}]".format(error=error))

############################ ADMINS ############################
    if message.content.startswith(prefix +'admin'):
        if not message.author.id in adminslist:
            await client.send_message(message.channel, '{} Você não é admin!'.format(message.author.mention))
            print('{} Executou o comando {}admin.'.format(message.author.mention, prefix))
        else:
            man = ('<:bussinesman:457441667193110529>')
            embed = discord.Embed(colour=0xfc4902, timestamp=message.timestamp)
            embed.add_field(name=man+'Comandos Admins:', value='**{}reiniciar** Reiniciar o {}.\n'.format(prefix, client.user.name)+
                                                '**{}nick** <@Usuario> <NovoNick> Muda o nick do usuario selecionado.\n'.format(prefix)+
                                                '**{}mutar** <@Usuario> Muta o usuario selecionado.\n'.format(prefix)+
                                                '**{}desmutar** <@Usuario> Desmuta o usuario selecionado.\n'.format(prefix)+
                                                '**{}ban** <@Usuario> Banimento imediato no usuario informado.\n'.format(prefix)+
                                                '**{}kick** <@Usuario> Expulsão imediata no usuario informado.\n'.format(prefix)+
                                                '**{}status1:** <Msg> Altera o status do {} (Jogando).\n'.format(prefix, client.user.name)+
                                                '**{}status2:** <Msg> Altera o status do {} (Transmitindo).\n'.format(prefix, client.user.name)+
                                                '**{}limpar** <Num> Apaga o tanto de mensagem informado Max 100.\n'.format(prefix)+
                                                '**{}eval**\n'.format(prefix)+
                                                '**{}falar** tts basico kk.\n'.format(prefix))
            embed.set_footer(text='Seja bem vindo admin {}'.format(message.author.name),icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith(prefix +'reiniciar'):
        if message.author.id in adminslist:
            await client.send_message(message.channel, 'Ok estou reiniciando!')
            print ('Reiniciando o bot!')
            os.system("python JrBlackBot.py reload")
        else:
            await client.send_message(message.channel, '{} Sai seu merda.'.format(message.author.mention))

    if message.content.startswith(prefix +'nick'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Desculpe {} você não é admin então não posso mudar o nome deste usuario :rolling_eyes:".format(message.author.mention))
        member = message.mentions[0]
        novo = message.content.split(' ')[2]
        await client.change_nickname(member, novo)

    if message.content.startswith(prefix +'mutar'):
        user = message.mentions[0]
        member = (message.author.name)
        author= (message.author.mention)

        if not message.author.id in adminslist:
            channellogs = client.get_channel('453025344379682826')
            user = message.mentions[1]
            logs = discord.Embed(title='❌Permissões Mute', colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
            logs.add_field(name='Autor:',value='{}'.format(message.author.mention), inline=True)
            logs.add_field(name='Usuario punido:', value='{}'.format(user), inline=True)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')

        block = ('<:unvalid:455896993110163466>')
        channellogs = client.get_channel('453025344379682826')
        logs = discord.Embed(title=block+'Usuario {} foi mutado com sucesso!'.format(user), colour=0xaf0000, timestamp=message.timestamp)
        logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
        logs.add_field(name='Autor:',value='{}'.format(message.author.mention), inline=True)
        logs.add_field(name='Usuario punido:', value='{}'.format(user.mention), inline=True)
        logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
        await client.send_message(channellogs, embed=logs)

        cargo = discord.utils.get(message.author.server.roles, name='mutado')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi mutado pelo Administrador: {}'.format(user.mention,author))

    if message.content.startswith(prefix +'desmultar'):
        user = message.mentions[0]
        check = ('<:check:455896992690995211>')
        author = message.author.mention
        channellogs = client.get_channel('453025344379682826')

        if not message.author.id in adminslist:
            block = ('<:unvalid:455896993110163466>')
            logs = discord.Embed(title='❌Permissões Desmultar', colour=0xff0000, timestamp=message.timestamp)
            logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
            logs.add_field(name='Autor:',value='{}'.format(message.author.mention), inline=True)
            logs.add_field(name='Usuario:', value='{}'.format(user.mention), inline=True)
            logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            await client.send_message(channellogs, embed=logs)
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')

        logs = discord.Embed(title=check+'Usuario {} desmultado com sucesso!'.format(user), colour=0x269900, timestamp=message.timestamp)
        logs.add_field(name='Servidor:', value='**{}**'.format(message.server.name), inline=True)
        logs.add_field(name='Autor:',value='{}'.format(message.author.mention), inline=True)
        logs.add_field(name='Usuario:', value='{}'.format(user.mention), inline=True)
        logs.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        logs.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
        await client.send_message(channellogs, embed=logs)

        cargo = discord.utils.get(message.author.server.roles, name='mutado')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi Desmultado pelo Administrador: {}'.format(user.mention, author))

    if message.content.startswith(prefix +'ban'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Desculpe {} você não é admin então não posso banir :/".format(message.author.mention))
        try:
            author = message.author.mention
            user = message.mentions[1]
            embedban = discord.Embed(name='Ban', timestamp=message.timestamp)
            embedban.add_field()
            embedban.set_footer(name='BlackZacky 2018', icon_url=message.author.avatar_url)
            await client.ban(user)
            await client.send_message(message.channel,"Usuario: {} banido do server pelo Administrador: {}".format(user.mention,author))
        except  discord.errors.Forbidden:
            return await client.send_message(message.channel, '⚠️ Não consegui banir o membro: {}'.format(user.mention))

    if message.content.startswith(prefix +'kick'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Desculpe {} você não é admin então não posso kickar este usuario ;(".format(message.author.mention))
        try:
            author = message.author.mention
            user = message.mentions[1]
            await client.kick(user)
            await client.send_message(message.channel,"Usuario: {} kickado do server pelo Administrador: {}".format(user.mention,author))
        except  discord.errors.Forbidden:
            return await client.send_message(message.channel, '️⚠️ Não consegui kickar o membro: {}'.format(user.mention))

    if message.content.startswith(prefix +'status2:'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Só os admins pode mudar meu status :)")
        trans = message.content[10:]
        stream = ('<:stream:438399396963418131>')
        await client.change_presence(game=discord.Game(name=trans, url='https://www.twitch.tv/relaxbeats', type=1))
        await client.send_message(message.channel, "Mudando o status para ➜ {}{}".format(stream, trans))

    if message.content.startswith(prefix +'status1:'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Só os admins pode mudar meu status :)")
        game = message.content[10:]
        on = ('<:Online:451944005895454720>')
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Mudando o status para ➜ {}{}".format(on, game))

    if message.content.startswith(prefix +'limpar'):
        number = message.content.split(' ')[1]
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Desculpe {} você não é admin então não posso apagar as mesagens ;(".format(message.author.mention))
        elif int(number) > 100:
            return await client.send_message(message.channel, "O limite é 100. :(")
        msgs = []
        number = int(number)
        async for x in client.logs_from(message.channel, limit=number):
            msgs.append(x)
        await client.delete_messages(msgs)
        embed = discord.Embed(title='🗑️ Lixeira', description='Eu acabei de apagar **{}** mensagens.'.format(number), color=0x727272)
        dele = await client.send_message(message.channel, embed=embed)
        await asyncio.sleep(8)
        await client.delete_message(dele)

    if message.content.startswith(prefix +'eval'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, ":/ flw!")
        member = (message.author.name)
        try:
            comando = message.content[6:]
            embed = discord.Embed(title='EVAL', timestamp=message.timestamp)
            embed.add_field(name='📥Entrada', value='``{}``'.format(comando))
            embed.add_field(name='📤Saida', value='``{}``'.format(eval(comando)))
            embed.set_footer(text='© 2018 BlackZacky', icon_url=imgopen)
            evaldel1 = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(evaldel1,'🗑')
            @client.event
            async def on_reaction_add(reaction, user):
                if reaction.emoji == "🗑" and reaction.message.id == evaldel1.id and user == message.author:
                    await client.delete_message(evaldel1)
                    await client.delete_message(message)
        except:
            embederro = discord.Embed(Title='EVAL', timestamp=message.timestamp)
            embederro.add_field(name='📥Entrada', value='``ERRO!``')
            embederro.add_field(name='📤Saida', value='``ERRO!!``')
            embederro.set_footer(text='ERRO!!!', icon_url=imgopen)
            evaldel2 = await client.send_message(message.channel, embed=embederro)
            await client.add_reaction(evaldel2,'🗑')
            @client.event
            async def on_reaction_add(reaction, user):
                if reaction.emoji == "🗑" and reaction.message.id == evaldel2.id and user == message.author:
                    await client.delete_message(evaldel2)
                    await client.delete_message(message)

    if message.content.startswith(prefix +'falar'):
        if not message.author.id in adminslist:
            return await client.send_message(message.channel, "Você não pode executar este comando :/")
        falar = message.content[7:].strip()
        await client.delete_message(message)
        falado = await client.send_message(message.channel, falar, tts=True)
        await client.delete_message(falado)

client.run(config.token)
