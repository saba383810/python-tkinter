import tkinter as tk
import hashlib

root = tk.Tk()
root.title("ハッシュ君")
root.geometry("530x80")

def safty_password( id, password ): 
    hash = hashlib.sha256() 
    hash.update( id + password ) 
    return hash.hexdigest()

def onClick():
    id = e.get()
    password = b'password'
    label1.config( text = safty_password(id.encode(),password))

e = tk.Entry( root )
e.pack()

button = tk.Button(root, text='ハッシュ化', command=onClick)
button.pack()

label1 = tk.Label( root, text="")
label1.pack()

root.mainloop()