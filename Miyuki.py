const Discord = require('discord.js');
const moment = require("moment");

exports.run = async (bot, message, args) => {
  let memberInfo = message.mentions.members.first();

  if(!memberInfo){
    moment.locale("pt-BR")
    let role = message.member.highestRole;
    let userinf = new Discord.RichEmbed()
    .setAuthor(message.author.username)
    .setThumbnail(message.author.avatarURL)
    .setDescription("Aqui está a informação do usuario!")
    .setColor(role.hexColor)
    .addField("Nome do usuario:", `${message.author.username}#${message.author.discriminator}`, true)
    .addField("ID:", message.author.id, true)
    .addField('Currently:', `${message.author.presence.status.toUpperCase()}`, true)
    .addField('Jogando:', `${message.author.presence.game === null ? "Não está jogando" : message.author.presence.game.name}`, true)
    .addField('Conta criada:', moment(message.author.createdAt).format('LL'), true)
    .addField('Entrou no servidor:', moment(message.member.joinedAt).format('LL'), true)
    .addField('Cargos:', message.member.roles.filter(r => "<@" + r.id + ">").array().join(' '), true)

    message.channel.send(userinf);

  }else{
    let role = memberInfo.highestRole;
    let userinfoo = new Discord.RichEmbed()
    .setAuthor(memberInfo.displayName)
    .setThumbnail(memberInfo.user.avatarURL)
    .setDescription("Aqui está a informação do usuario!")
    .setColor(role.hexColor)
    .addField("Nome do usuario:", `${memberInfo.user.username}#${memberInfo.user.discriminator}`)
    .addField("ID:", memberInfo.id)
    .addField('Conta criada:', moment(message.author.createdAt).format('LL'), true)
    .addField('Entrou no servidor:', `${memberInfo.joinedAt}`, true)
    .addField('Currently', `${memberInfo.user.presence.status.toUpperCase()}`, true)
    .addField('Jogando:', `${memberInfo.user.presence.game === null ? "Não está jogando" : memberInfo.user.presence.game.name}`, true)
    .addField('Cargos:', memberInfo.roles.filter(r => "<@" + r.id + ">").array().join(' '), true)

    message.channel.send(userinfoo);
  }
}

exports.config = {
    name: 'userinfo',
    aliases: ['userinfo']
}
