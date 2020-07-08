import tkinter as tk
root = tk.Tk()
# スライドバーの値を格納する場所を生成
val = tk.IntVar()
# valに0を代入
val.set(0)

# スライドバーを動かしたときの処理
def setVal(scl):
    label1.config( text = 'Value = %d' % int(scl))
    str1 = getBin(int(scl))
    label2.config(text="{}.{}.{}.{}".format(str1[0:8],str1[8:16],str1[16:24],str1[24:32]))
    label3.config(text="{}.{}.{}.{}".format(int(str1[0:8],2),int(str1[8:16],2),int(str1[16:24],2),int(str1[24:32],2)))

def getBin(num):
    bindata=""
    for i in range(num):
        bindata +="1"
    for i in range(32-num):
        bindata +="0"
    return bindata

# スライドバーの値を表示するラベルを生成
label1 = tk.Label( root, text = 'Value = %d' % val.get())
label1.pack()
label2 = tk.Label( root, text="00000000.00000000.00000000.00000000")
label2.pack()
label3 = tk.Label( root, text="0.0.0.0")
label3.pack()

# スライドバーの生成
s = tk.Scale( root, label = 'Scale', orient = 'h', from_ = 0, to = 32, showvalue = False, variable = val, command =setVal )
s.pack()

root.mainloop()