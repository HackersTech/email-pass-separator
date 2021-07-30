import os
os.system('clear')
print("\033[5;33m link of youtube channel in repo")
os.system('bash k.sh')



print("file should in working directory ")
print('for updating press u / else enter the name of file')

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
elif l==u or l==U :
        os.system('bash u.sh')
else:
    print('\033[5;31m error occured invalid input')
    print("\033[5;35m starting again")
    os.system("python password.py")
