import time
import urllib
import sys
import os
import datetime

os.system ('termux-wake-lock')
os.system('clear')


won_data='''\033[1;34;40m
░██╗░░░░░░░██╗░█████╗░███╗░░██╗
░██║░░██╗░░██║██╔══██╗████╗░██║
░╚██╗████╗██╔╝██║░░██║██╔██╗██║
░░████╔═████║░██║░░██║██║╚████║
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝

██████╗░░█████╗░████████╗░█████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║░░██║███████║░░░██║░░░███████║
██║░░██║██╔══██║░░░██║░░░██╔══██║
██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
'''



no_data='''\033[1;30;40m
███╗░░██╗░█████╗░████████╗
████╗░██║██╔══██╗╚══██╔══╝
██╔██╗██║██║░░██║░░░██║░░░
██║╚████║██║░░██║░░░██║░░░
██║░╚███║╚█████╔╝░░░██║░░░
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░

██████╗░░█████╗░████████╗░█████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║░░██║███████║░░░██║░░░███████║
██║░░██║██╔══██║░░░██║░░░██╔══██║
██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
'''
cone='''⼕ㄖ𝓝🝗⼕七讠ㄖ𝓝 ㇄ㄖ丂セ
'''



line = """\033[1;36;40m\n___________________________________________________________\n"""

def upda():
  u= input('''\n1.continue Algorithm\n\n2.update Algorithm\n\nPlase select option : ''')
  if u == '1':
    print("runing...")
  elif u == '2':
    os.system('update.py')
    exit()
  else :
    upda()
upda()  
def login():
  os.system('clear')
  aa= str(input('''\033[1;36;40m𝔼𝕟𝕥𝕖𝕣 𝕡𝕒𝕤𝕤𝕨𝕠𝕣𝕕 :- '''))
  if aa == 'jahoo9808' or aa == 'jahoo1998' or aa == 'jahoo98' or aa == 'jayashan' or aa == 'jayashan ' :
    print("success")
  else:
    os.system('clear')
    b = str(input("\n\033[1;31;40mWrong password\n\n\033[1;33;40mAre you want Reenter password(y/n) : - "))
    if b == 'y' or b == 'Y' :
      login()
    elif b == 'n' or b == 'N' :
      os.system('clear')
      exit()
    else:
      login()
  
login()

os.system('clear')
ready="\n\n>>>>\033[1;33;40m 𝑐ℎ𝑒𝑐𝑘𝑖𝑛𝑔 𝑑𝑒𝑣𝑖𝑐𝑒 𝑖𝑝\n\033[1;31;40m>>>>\033[1;33;40m 𝑐𝑜𝑛𝑛𝑒𝑐𝑡 𝑑𝑒𝑣𝑖𝑐𝑒 𝑖𝑝\n\033[1;31;40m>>>> \033[1;33;40mℎ𝑎𝑛𝑑𝑠ℎ𝑎𝑘𝑒 𝑑𝑒𝑣𝑖𝑐𝑒 𝑖𝑝\n\033[1;31;40m\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"

now = datetime.datetime.now()
print("Today is ",end="")
print(now.strftime("%y-%m-%d"))
print("expired date 2021-1-1\n" )
if now.strftime("%m") == '11' or now.strftime("%m") == '01' :
  print('''Account is deactivate\nplease Contact owner\n\n 
╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓
╋╋┃┃╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋┃┣━━┳┓╋┏┳━━┳━━┫┗━┳━━┳━┓
┏┓┃┃┏┓┃┃╋┃┃┏┓┃━━┫┏┓┃┏┓┃┏┓┓
┃┗┛┃┏┓┃┗━┛┃┏┓┣━━┃┃┃┃┏┓┃┃┃┃
┗━━┻┛┗┻━┓┏┻┛┗┻━━┻┛┗┻┛┗┻┛┗┛
╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋┗━━┛''')
  for j in range (10):
    time.sleep(0.3)
    upda()
  exit()
else:
  print("\033[1;31;40mIp Active\n connect user account")
  for char in ready:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  

try:
    from tqdm import tqdm
  
except ImportError:
    os.system('pip3 install tqdm')
    print('%s Requests installed.')
    os.system('clear')
    from tqdm import tqdm

try:
    f = open("Authorization.txt", "r")
    file1 = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("Authorization.txt", "w")
    f.write(wr)
    f.close
    f = open("Authorization.txt", "r")
    file1 = f.read()
    f.close
    
try:
    f = open("file_url.txt", "r")
    file2 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("file_url.txt", "w")
    f.write(wr)
    f.close
    f = open("file_url.txt", "r")
    file2 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('waiting.......')
    os.system('pip3 install requests')
    print('%s Requests installed.')
    os.system('clear')
    import requests

    
def en():
  print("All messages are received your sim auto close your programe.")
  exit()



auth=file1    
def obj():
    os.system("clear")
    head = {"Host": "megarun.dialog.lk",
              "Authorization": file1, "X-Unity-Version": "2018.3.0f2"}
    url = file2
    
    s = int(input('''\033[1;36;40m
▒█▀▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
▒█▀▀▀ █░░█ ░░█░░ █▀▀ █▄▄▀ 
▒█▄▄▄ ▀░░▀ ░░▀░░ ▀▀▀ ▀░▀▀ 

░█▀▀█ █▀▄▀█ █▀▀█ █░░█ █▀▀▄ ▀▀█▀▀ 
▒█▄▄█ █░▀░█ █░░█ █░░█ █░░█ ░░█░░ 
▒█░▒█ ▀░░░▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ░░▀░░   -  '''))
    
    os.system('clear')
    
    m=0
    rr=0
    print('''         \033[0;30;47m  𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦e 𝐑𝐮𝐧𝐧𝐢𝐧𝐠  \033[1;32;40m     ''')
    for rr in tqdm(range(rr,s),ascii=" >",desc="process...."):
        print("\n\n\n\n")
        if (rr == 0):
            print('''\033[1;30;40m
█░█░█ ▄▀█ █ ▀█▀ █ █▄░█ █▀▀ ░ ░ ░
▀▄▀▄▀ █▀█ █ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄''')
            print("\n\n\n\033[1;33;40m")
            for j in tqdm(range(90),ascii=" >#"):
                time.sleep(1)

        else :
            rj = requests.get(url, headers=head)
            request = str(rj)
            if request == '<Response [204]>':
                print(no_data)
            elif request == '<Response [200]>':
                m+=1
                print(won_data)
            else:
                print(line)
                print(cone)
                print(line)

            rr+=1
            
            print('''\033[1;33;44m   𝒏𝒖𝒎𝒃𝒆𝒓 𝒐𝒇 𝒓𝒆𝒒𝒖𝒆𝒔𝒕𝒔   \033[1;32;40m:''',str(rr-1),"\n")
            print('''\033[1;33;44m   Nuⲙᑲ∈ᖇ 𝖮⨍ ⲙ∈⟆⟆Ꭿge    \033[1;32;40m:''',int(m),"\n")
            print('''\n\n\n\033[1;30;47m      𝑅𝑢𝑛𝑛𝑖𝑛𝑔...      \033[1;32;40m\n\n\n\n''')
            
            if m==20 :
              en()
              
            for j in tqdm(range(90)):
              time.sleep(1)
            
            
              
        os.system('clear')
    rerun()

obj()

def rerun():
    rerun = input('\033[1;0;40m\nDo Restart Algorithm :  (y/n) - ')
    if rerun == "y" or rerun == "Y":
        obj()
    elif rerun == "n" or rerun == "N":
        quit()
    else:
        print('\033[1;30;40mrerun')
        rerun()
