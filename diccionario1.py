from tkinter import *

def ast():
    return chr(9679)

def blc():
    return chr(9675)


#str=""
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
    flag=0
    linea=0
    str=""
    while(i!=len(lista)):
        #comprobaciones
        if lista[i].isnumeric():
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)
        
        if lista[i].isupper():
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea1(str)

        #Letras
        if (lista[i].lower()=='a')|(lista[i]=='1'):
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='b')|(lista[i]=='2'):
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='c')|(lista[i]=='3'):
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='d')|(lista[i]=='4'):
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='e')|(lista[i]=='5'):
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='f')|(lista[i]=='6'):
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='g')|(lista[i]=='7'):
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='h')|(lista[i]=='8'):
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='i')|(lista[i]=='9'):
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i].lower()=='j')|(lista[i]=='0'):
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea0(str)

        elif lista[i].lower()=='k':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='l':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='m':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='n':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='o':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='p':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='q':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='r':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='s':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='t':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='u':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='v':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='x':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='y':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='z':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='á':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='é':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='í':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i].lower()=='ó':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='ú':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i].lower()=='ñ':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i].lower()=='w':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea3(str)
            elif linea==2:
                str=linea1(str)

        #caracteres
        elif lista[i]=='&':
            if linea==0:
                str=linea3(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='.':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==',':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea0(str)

        elif (lista[i]=='¿')|(lista[i]=='?'):
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea1(str)

        elif (lista[i]=='¡')|(lista[i]=='!'):
            if linea==0:
                str=linea0(str)
            elif linea==3:
                str=linea2(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==';':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea2(str)
        
        elif lista[i]=='"':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='(':
            if linea==0:
                str=linea2(str)
            elif linea==1:
                str=linea2(str)
            elif linea==2:
                str=linea1(str)

        elif lista[i]==')':
            if linea==0:
                str=linea1(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

        elif lista[i]=='-':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea0(str)
            elif linea==2:
                str=linea3(str)

        elif lista[i]=='*':
            if linea==0:
                str=linea0(str)
            elif linea==1:
                str=linea1(str)
            elif linea==2:
                str=linea2(str)

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
            if linea==0:
                bl1.configure(text=str)
                bl1.config(font=20)
            elif linea==1:
                bl2.configure(text=str)
                bl2.config(font=20)
            elif linea==2:
                bl3.configure(text=str)
                bl3.config(font=20)
            print(str)  #pinta en el terminal el texto en braille
            str=""
            
            linea=linea+1
            
            
            if linea==3:
                break


wd=Tk()
wd.title("Traductor")
wd.geometry('800x200')
wd.resizable(0,0)
lbl=Label(wd, text="Dame el texto")
bl0=Label(wd)
bl1=Label(wd)
bl2=Label(wd)
bl3=Label(wd)
lbl.grid(column=0, row=0)
txt=Entry(wd, width=100)
txt.grid(column=1, row=0)
txt.focus()

#txt.focus()
def clicked():
    bl1.grid(column=1, row=2)
    bl2.grid(column=1, row=3)
    bl3.grid(column=1, row=4)
    biblioteca(txt.get())
    bl0.configure(text=txt.get())
    bl0.grid(column=1, row=1)
    bl0.config(font=20)
    txt.delete(0, END)

btn=Button(wd, text="traducir", command=clicked)
btn.grid(column=2, row=0)
btn.focus()
wd.mainloop()
