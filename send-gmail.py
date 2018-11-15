# -*- coding: utf-8 -*-
import smtplib
 
# Credenciais
remetente    = '[remetente]'
senha        = '[senha do email remetente]'
 
# Informações da mensagem
destinatario = '[email]'
assunto      = '[assunto do email]'
texto        = '[mensagem]'


# Preparando a mensageogramas 
msg = '\r\n'.join([
  'From: %s' % remetente,
  'To: %s' % destinatario,
  'Subject: %s' % assunto,
  '',
  '%s' % texto
  ])
 
msg = '\r\n'.join([
  'From: %s' % remetente,
  'To: %s' % destinatario2,
  'Subject: %s' % assunto,
  '',
  '%s' % texto
  ])


# Enviando o email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()


server.login(remetente,senha)
#for i in range(n): enviar n emails de uma unica vez //send a lot of emails n times ,by:BIG: algustosergio2008@gmail.com
      server.sendmail(remetente, destinatario, msg)
server.quit()
