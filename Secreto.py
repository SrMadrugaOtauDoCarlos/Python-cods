# -*- coding: utf-8 -*-
from datetime import datetime

#Texto e icone eventos
event = ('Rumo ao Hexa 2018')
eventi = ('https://i.imgur.com/K5JXUOF.png')

#Icons Status Membros
Ausente = ('<:Ausente:451934408874917889>')
Ocupado = ('<:Ocupado:451934409202073600>')
Offline = ('<:Offline:451934409285959680>')
Online = ('<:Online:450373115218886666>')
TagBot = ('<:bottag:451942596261183509>')

#Prefixo
prefix = (">")

#STATUS  
Jogando = (0) 
Transmitindo = (1) 
Ouvindo = (2)
Assistindo = (3)
Ouvindo = (4)

statusmsg = (prefix+'comandos')
statusbot = (Transmitindo)
urllive = ('https://www.twitch.tv/relaxbeats')

#Hora/Data
now = datetime.now()

y = (now.year)
m = (now.month)
d = (now.day)
h = (now.hour)
mn = (now.minute)
s = (now.second)


#Variaveis das imagens
imgip = ('http://importartudo.org/wp-content/uploads/2017/07/ip-americano-importar-tudo.png')
imgcpf = ('https://loja.spcbrasil.org.br/media/catalog/product/cache/1/image/363x/040ec09b1e35df139433887a97daa66f/i/c/icones_350-x-350_px_final_07.png')
imgcep = ('https://tfile.com.br/consultarcep.com.br/upload/img/logo.png')
imgbtc = ('http://pngimg.com/uploads/bitcoin/bitcoin_PNG47.png')
imgusd = ('https://i.imgur.com/rFyY5r8.png')
imgrol = ('http://www.tribunapr.com.br/wp-content/uploads/sites/1/2017/06/revolver_tambor-825x550.jpg?a86372')
imgmoeda = ('https://i.ytimg.com/vi/4-yIMxhg2GQ/hqdefault.jpg')
imgdado = ('https://png.icons8.com/metro/1600/dice.png')
imgopensoruce = ('https://cdn.discordapp.com/attachments/417075411789414400/455632372382171138/icons8-open-source-50.png')

#IDs das pessoas que tem acesso aos comandos de admin.
ListADM = ['272188868877352960', #BLACKZACKY
	   '427640912529588224',] #JR BLACK

ListChat = ['proibidao','nsfw','porn','porns']

#Token do bot
token = ("TOKEN DO SEU BOT")
