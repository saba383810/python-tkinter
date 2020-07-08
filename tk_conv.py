import tkinter as tk
root = tk.Tk()



label1 = tk.Label( root, text="10進数→16進数")
label1.pack()
def onClick():
    label2 = tk.Label( root, text="10進数 : ")
    label2.pack()
    label3 = tk.Label( root, text="16進数 : ")
    label3.pack()
    label = tk.Label( root, text="------------")
    label.pack()

    label2.config(text = "10進数 : "+ e.get())
    label3.config(text = "16進数 : "+ str.upper(format(int(e.get()),'x')))



e = tk.Entry( root )
# テキストボックス配置
e.pack()

button = tk.Button(root, text='変換', command=onClick)
button.pack()

root.mainloop()