import os

#Pulls back an errorlevel into the x variable. 0 for success, 1 for failure
x = os.system("for /f \"tokens=1 delims=-\" %a in ('hostname') do @echo %a")
print(x)

#Use if loop to evaluate errorlevel
if x == 0:
    var = "Successful"
else:
    var = "Unsuccessful"

print(var)
input()
