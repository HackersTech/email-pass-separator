import os

print(" link of our youtube channel in repo")
print ("\033[3;37m file should be in working directory/ or give folder path")
os.system("cd ..")
os.system("cd email-pass-separator")
l=input("Enter file name to seperate password from file ")
if l!='':
        
    k=open(l,'r')
    try:
                h=' '
                while h:
                        h=k.readline()
                        g=h.split(":")  #here you can put own separator
                        print(g[1])       #here you can change password to email by putting 0 inside box
    except:
                k.close()

else:
    print('\033[5;31m error occured invalid input')
    print("\033[5;35m starting again")
    os.system("python password.py")
