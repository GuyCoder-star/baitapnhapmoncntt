import tkinter as tk
import numpy as np
from tkinter import messagebox as msg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercise 4")
        self.geometry('385x286')
        self.resizable(0, 0)

        self.matrix = None
        self.content = None

        btn_open = tk.Button(self, text="OPEN", command=self.click_btn_open, width=8)
        btn_add = tk.Button(self, text="ADD", command=self.click_btn_add, width=8)
        btn_save = tk.Button(self, text="SAVE", command=self.click_btn_save, width=8)
        self.lbl = tk.Label(self, bg="white", width=40, height=10, relief=tk.SUNKEN, font=('Consolas', 12))

        btn_open.place(x=10, y=10)
        btn_add.place(x=10, y=250)
        btn_save.place(x=295, y=250)
        self.lbl.place(x=10, y=45)
    def click_btn_open(self):
        #xu li doc file
        f = open("matran.txt", 'r')
        content = f.read()
        f.close()
        content = content.splitlines()
        #nhap ma tran
        size = content[0].split()
        m = int(size[0])
        n = int(size[1])
        arr = np.zeros((m,n), dtype=np.float)
        for i in range(m):
            line = content[i + 1]
            line = line.split()
            for j in range(n):
                arr[i, j] = float(line[j])
        self.matrix = arr

        content = "%d %d\n" %(m, n)
        for i in range(m):
            for j in range(n):
                content = content + "%8.2f" %arr[i, j]
            content = content + "\n"
        self.content = content
        self.lbl.configure(text=self.content)

    def click_btn_add(self):
        content = self.content + '-'*40 + "\n"
        m, n = self.matrix.shape
        result = np.sum(self.matrix, axis=0)
        for i in range(n):
            content = content + "%8.2f" %(result[i])
            self.content = content
        self.lbl.configure(text=self.content)
    def click_btn_save(self):
        f = open("ketqua.txt", 'w')
        f.write(self.content)
        f.close()
        msg.showinfo("thong bao","ban da luu xong")
        
if __name__ == '__main__':
    app = App()
    app.mainloop()