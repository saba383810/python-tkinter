import tkinter as tk
root = tk.Tk()

expression = tk.StringVar()

def check():
    def func():
        expression.set("")
        if val1.get()==False:
            expression.set(expression.get()+"偽")
        else:
             expression.set(expression.get()+"真")
        if val2.get()==False:
            expression.set(expression.get()+"偽")
        else:
             expression.set(expression.get()+"真")
             
    return func
# チェック状態を格納する領域を確保
val1 = tk.BooleanVar()
# 未チェック状態に設定（チェック状態にしたい場合はTrue）
val1.set(False)

val2 = tk.BooleanVar()
val2.set(False)

chk1 = tk.Checkbutton( root, text='チェックボックス１', variable=val1)
chk1.pack()

chk2 = tk.Checkbutton( root, text='チェックボックス2', variable=val2)
chk2.pack()

tk.Button(root,text="チェック",command=check()).pack()
e = tk.Label(root, textvariable=expression)
e.pack()

root.mainloop()