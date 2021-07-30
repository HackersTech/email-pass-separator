import os

print("\033[5;33m link of youtube channel in repo")
print  "\033[4;33m instagram id -- hackers__tech"

os.system('bash k.sh')


print("file should in working directory ")


l=input("Enter file name to seperate password from file ")
if l!='':
        
    k=open(l,'r')

    h=' '
    while h:
        h=k.readline()
        g=h.split(":")
        print(g[1])

else:
    print('\033[5;31m error occured invalid input')
    print("\033[5;35m starting again")
    os.system("python3 password.py")
