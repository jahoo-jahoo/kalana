import time
import os

print("waiting \nRemove your old version")
os.system('rm -rf jahoo.py')
os.system('cd ..')
os.system('ls')
aa=input("Enter your update link : ")
os.system(aa)
print("wait.....\nupdate...")
os.system('clear')
print("sucess")

bb=input('Are you want running new algorithm ? (y/n)')
if bb == 'y':
    os.system('jahoo.py')
    



