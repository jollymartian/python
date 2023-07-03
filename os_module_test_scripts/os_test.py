import os

#Pulls back an errolevel into the x variable. 0 for success, 1 for failure
x = os.system("for /f \"tokens=1 delims=-\" %a in ('hostname') do @echo %a")
print(x)
input("Press enter to quit...")