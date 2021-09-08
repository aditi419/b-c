from tkinter import *
root = Tk()
root.title('P147')
root.geometry('500x500')
root.configure(background='lightblue')

word = Entry(root) 
word.place(relx = 0.5,rely = 0.3,anchor = CENTER)

asciiName = Label(root)
asciiName.place(relx = 0.5,rely = 0.5,anchor = CENTER)

encryptedName = Label(root)
encryptedName.place(relx = 0.5,rely = 0.6,anchor = CENTER)

def getCode():
    wt = str(word.get())
    for letter in wt:
        asciiName['text'] += str(ord(letter)) + ' '
        asciiH = int(ord(letter)) 
        encrypted = asciiH - 1
        encryptedName['text'] += str(chr(encrypted))

btn = Button(root,text='Display the Ascii Code and Encrypted value',command=getCode,bg='blue',fg='black')
btn.place(relx = 0.5,rely = 0.4,anchor = CENTER)

mainloop()
