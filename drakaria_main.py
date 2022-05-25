# -*- coding: utf-8 -*-
import time
import asari_adven, nim_adven, wetla_adven, grenda_adven
from os import system, name
def clear():
	if name=='posix':
		_=system('clear')
	else:
		_=system('cls')

#def redir(inputStr):
#	words.insert(INSERT, inputStr)
#sys.stdout.write=redir


#The above was print("Group Members:"+ nimet 0, 1, 2)
nimet=['Nuppu', 'Soma', 'Mirka']
kyl=['Y', 'y', 'yes', 'Yes']
ei=['N', 'n', 'No', 'no']


readi=input("\033[1;35;40m Welcome to Drakaria! \nAre you ready to go?")
if readi in kyl:
	print("Great! Wait a moment for your group to gather their equipment.")
	time.sleep(3)
	print("Let's go!")
else:
	print("I'll give you some time.")
	time.sleep(5)
	print("Time to go!")
	time.sleep(3)
	clear()
  #Land-selection below
maa=input("Available lands:\033[1;35;40m 1.Nimeria, \033[1;31;40m 2. Grenda, \033[1;32;40m 3. Wetlands, \033[1;34;40m 4. Asari. \n\033[1;36;40mChoose a land (1-4): ")
#Nimeria
if maa=="1":
  print("You chose \033[1;35;40m Nimeria.")
  time.sleep(4)
  clear()
  nim_adven.Nim_desc()
  nim_adven.adventure()
#Grenda
elif maa=="2":
  print("You chose \033[1;31;40m Grenda.")
  time.sleep(4)
  clear()
  grenda_adven.Gren_desc()
#Wetlands
elif maa == "3":
  print("You chose \033[1;32;40m Wetlands")
  time.sleep(4)
  clear()
  wetla_adven.Wetla_desc()
  wetla_adven.adventure()
#Asari
elif maa == "4":
  print("You chose \033[1;34;40m Asari.")
  time.sleep(4)
  clear()
  asari_adven.Asa_desc()
  asari_adven.adventure()

