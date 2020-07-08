import tkinter as tk
root = tk.Tk()

val = tk.IntVar()
binsStr = tk.StringVar()
hexStr = tk.StringVar()
val.set(0)

def setValue(scl):
    label.config( text = 'Value = %d' % int(scl))

def setBin():
    binsStr.set("")

# スライドバーの値を表示するラベルを生成
label = tk.Label( root, text = 'Value = %d' % val.get())
label.pack()
# スライドバーの生成
s = tk.Scale( root, label = 'Scale', orient = 'h', from_ = 2, to = 16, showvalue = False, variable = val, command = func )
s.pack()

root.mainloop()