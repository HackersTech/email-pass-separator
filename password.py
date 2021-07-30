import os

print("\033[5;33m link of our youtube channel in repo")



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
