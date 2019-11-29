def ast():
    return chr(9679)

def blc():
    return chr(9675)



def linea0(str):
    return str+blc()+' '+blc()+' '

def linea1(str):
    return str+blc()+' '+ ast()+' '

def linea2(str):
    return str+ast()+' '+blc()+' '

def linea3(str):
    return str+ast()+' '+ast()+' '

def esp(str):
    return str+' '*3

def biblioteca(lista):
    i=0    
    linea=0
    str=""
    while(i!=len(lista)):
        #comprobaciones
        if lista[i].isnumeric():    #113
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)
        
        if lista[i].isupper():      #101
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea1(str)

        #Letras
        if (lista[i].lower()=='a')|(lista[i]=='1'):         #200
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='b')|(lista[i]=='2'):       #220
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='c')|(lista[i]=='3'):       #300
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='d')|(lista[i]=='4'):       #310
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='e')|(lista[i]=='5'):       #210
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='f')|(lista[i]=='6'):       #320
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='g')|(lista[i]=='7'):       #330
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='h')|(lista[i]=='8'):       #230
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='i')|(lista[i]=='9'):       #120
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='j')|(lista[i]=='0'):       #130
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif lista[i].lower()=='k':     #202
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='l':     #222
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='m':     #302
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='n':     #312
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='o':     #212
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='p':     #322
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='q':     #332
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='r':     #232
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='s':     #122
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='t':     #132
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='u':     #203
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='v':     #223
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='x':     #303
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='y':     #313
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='z':     #213
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='á':     #233
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='é':     #123
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='í':     #102
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='ó':     #103
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='ú':     #133
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='ñ':     #331
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i].lower()=='w':     #131
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea1(str)

        #caracteres
        elif lista[i]=='&':     #313
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='.':     #001
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==',':     #020
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i]=='¿')|(lista[i]=='?'):       #021
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea1(str)

        elif (lista[i]=='¡')|(lista[i]=='!'):       #032
            if linea==0:
                str=linea0(str)
            elif linea==3:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i]==';':     #022
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)
        
        elif lista[i]=='"':     #023
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='(':     #221
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==')':     #112
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i]=='-':     #003
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='*':     #012
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)
        
        elif lista[i]=='ü':     #231
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==' ': 
            if linea==0:
                str=esp(str)
            elif linea==1:
                str=esp(str)
            elif linea==2:
                str=esp(str)

        i=i+1
        
        
        if i==len(lista):
            i=0
            print(str)      #Python de Windows
            str=""
            linea=linea+1
            
            if linea==3:
                break


lista=input("Dame el texto a traducir: ")
biblioteca(lista)