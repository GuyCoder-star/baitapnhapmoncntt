import tkinter as tk
import math
from tkinter import messagebox as msg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercise 2")
        
        #create widget
        self.lb_nhapa = tk.Label(self, text="Nhap a")
        self.lb_nhapb = tk.Label(self, text="Nhap b")
        self.lb_nhapc = tk.Label(self, text="Nhap c")
        self.lb_nghiem = tk.Label(self, text="Nghiem")
        self.lb_ketqua= tk.Label(self, width =30)
        self.entry_nhapa = tk.Entry(self, width = 30, justify=tk.RIGHT)
        self.entry_nhapb = tk.Entry(self, width = 30, justify=tk.RIGHT)
        self.entry_nhapc = tk.Entry(self, width = 30, justify=tk.RIGHT)
        self.btn_giai = tk.Button(self, text="Giai", width=10, command=self.click_giai)
        self.btn_xoa = tk.Button(self, text="Xoa", width=10, command= self.click_xoa)
        self.btn_thoat = tk.Button(self, text="Thoat", width=10, command=self.click_thoat)
        #take positon
        self.lb_nhapa.grid(row=0, column=0, padx=10, pady=10)
        self.lb_nhapb.grid(row=1, column=0, padx=10, pady=10)
        self.lb_nhapc.grid(row=2, column=0, padx=10, pady=10)
        self.lb_nghiem.grid(row=3, column=0, padx=10, pady=10)
        self.entry_nhapa.grid(row=0,column=1, padx=10, pady=10)
        self.entry_nhapb.grid(row=1,column=1, padx=10, pady=10)
        self.entry_nhapc.grid(row=2,column=1, padx=10, pady=10)
        self.lb_ketqua.grid(row=3,column=1, padx=10, pady=10) 
        self.btn_giai.grid(row=0, column=2, padx=10, pady=10)
        self.btn_xoa.grid(row=1, column=2, padx=10, pady=10)
        self.btn_thoat.grid(row=2, column=2, padx=10, pady=10)
    def click_giai(self):
        #giai phuong trinh bac 2
        a = float(self.entry_nhapa.get())
        b = float(self.entry_nhapb.get())
        c = float(self.entry_nhapc.get())
        if a == 0:
            if b == 0:
                if c == 0:
                    result = " Phuong trinh co vo so nghiem"
                else:
                    result = "Phuong trinh vo nghiem"
            else:
                result = - c / b
        else:
            delta = (b*b - (4*a*c))
            if delta == 0:
                x = -b/(2*a)
                result = "x = %0.2f" %(x)
            elif delta > 0:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                result = "x1 = %0.2f        x2 = %0.2f" %(x1, x2)
            else:
                result = "Phuong trinh vo nghiem"
        return self.lb_ketqua.config(text=result)
    def click_xoa(self):
        Entry = (self.entry_nhapa, self.entry_nhapb, self.entry_nhapc)
        for i in Entry:
            i.delete(0,  tk.END)
    def click_thoat(self):
        notify = msg.askquestion("Notify", "Ban co muon thoat khong?")
        if notify == "yes":
            self.destroy()

if __name__ == "__main__":
    root = App()
    root.mainloop()