import tkinter as tk
root = tk.Tk()
label = tk.Label( root, text='ボタン1が押されているよ！')
label.pack()

def func1():
    label.config(text="ボタン1が押されているよ！")
def func2():
    label.config(text="ボタン2が押されているよ！")
# ラジオボタンの値を格納する場所を生成
sel = tk.IntVar()
# selに1を代入
sel.set(1)
# ラジオボタン1の生成
rb1 = tk.Radiobutton( root, text = "ボタン1", variable = sel, value = 1, command = func1)
# ラジオボタン1を配置
rb1.pack()
# ラジオボタン2の生成
rb2 = tk.Radiobutton( root, text = "ボタン2", variable = sel, value = 2, command = func2 )
# ラジオボタン2を配置
rb2.pack()
root.mainloop()