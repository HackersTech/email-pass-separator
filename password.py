import os

print(" link of our youtube channel in repo")
print ("\033[5;37m file should be in working directory/ or give folder path")
os.system("cd ..")
os.system("cd email-password-separator")
l=input("Enter file name to seperate password from file ")
if l!='':
        
    k=open(l,'r')
    try:
                h=' '
                while h:
                        h=k.readline()
                        g=h.split(":")
                        print(g[1])
    except:
                k.close()

else:
    print('\033[5;31m error occured invalid input')
    print("\033[5;35m starting again")
    os.system("python password.py")
