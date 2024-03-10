
#dictionary
alph=["0","1","2","3","4","5","6","7","8","9",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",";",":","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~",
"á","é","í","ó","ú","à","è","ì","ò","ù","ä","ë","ï","ö","ü","â","ê","î","ô","û","ñ","ç","ø","ÿ","æ","å","æ","ø"," "
]
paralalph=[]
#construction
def Construction():
    global alph
    global paralalph
    base=int(input("base"))
    succ=int(input("succ"))
    alt=int(input("alt"))
    morph=int(input("morph"))
    shift=int(input("shift"))
    for x in range(0,len(alph)):
        y=x+(base*alt+morph+succ+succ*shift+shift)
        if y<10:
            y="000"+str(y)
        elif y<100:
            y="00"+str(y)
        elif y<1000:
            y="0"+str(y)
        paralalph.append(str(y))
#encrypt
def Encrypt():
    global alph
    global paralalph
    Input=input("> ")
    encrypt=""
    for x in Input:
        encrypt=encrypt+paralalph[alph.index(x)]
    print(encrypt)
#decrypt
def Decrypt():
    global alph
    global paralalph
    encrypt=input("> ")
    y=4
    Input=""
    for x in range(0,len(encrypt),4):
        Input=Input+alph[paralalph.index(encrypt[x:y])]
        y+=4
    print(Input)
#menu
ex=0
while ex==0:
    print("SELECT ACTION:\n1) Decrypt\n2) Encrypt\n3) Construct\n4) Exit")
    I=input("> ")
    if I=="1":
        Decrypt()
    elif I=="2":
        Encrypt()
    elif I=="3":
        paralalph.clear()
        Construction()
    elif I=="4":
        ex+=1
    else:
        print("Invalid input")