from os import closerange
import tkinter as tk
from tkinter.constants import HIDDEN, S

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercise 3")
        self.geometry("445x325")
    
        self.cvs_figure = tk.Canvas(self, bg="white", bd=1, 
                                    relief=tk.SUNKEN, width=300, height=300)
        
        lfrm_figure = tk.LabelFrame(self, text="Figure")
        self.var = tk.StringVar()
        self.var.set("tam giac")
        rbtn_tamgiac = tk.Radiobutton(lfrm_figure, text="Tam giac", width=8, value="tam giac", anchor=tk.W,
                                        variable=self.var, command=self.handle)
        rbtn_tron = tk.Radiobutton(lfrm_figure, text="Tron", width=8, value="tron", anchor=tk.W,
                                        variable=self.var, command=self.handle)
        rbtn_vuong = tk.Radiobutton(lfrm_figure, text="Vuong", width=8, value="vuong", anchor=tk.W,
                                        variable=self.var, command=self.handle)

        lfrm_color = tk.LabelFrame(self, text="Color")
        self.red = tk.IntVar()
        self.green = tk.IntVar()
        self.blue = tk.IntVar()
        chk_red = tk.Checkbutton(lfrm_color, text="Red", width=8, anchor=tk.W, variable=self.red, command=self.handle)
        chk_green = tk.Checkbutton(lfrm_color, text="Green", width=8, anchor=tk.W, variable=self.green, command=self.handle)
        chk_blue = tk.Checkbutton(lfrm_color, text="Blue", width=8, anchor=tk.W, variable=self.blue, command=self.handle)
        chk_red.select() 

        self.cvs_figure.place(x=10, y=10)

        lfrm_figure.place(x=326, y=4)
        rbtn_tamgiac.grid(row=0, column=0, padx=10, pady=5)
        rbtn_tron.grid(row=1, column=0, padx=10, pady=5)
        rbtn_vuong.grid(row=2, column=0, padx=10, pady=5)

        lfrm_color.place(x = 326, y = 191) 
        chk_red.grid(row=0, column=0, padx=10, pady=5)
        chk_green.grid(row=1, column=0, padx=10, pady=5)
        chk_blue.grid(row=2, column=0, padx=10, pady=5)

        self.cvs_figure.update()
        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        R = 255
        G = 0
        B = 0
        color = "#%02X%02X%02X" % (R, G, B)
        points = [10, H-10, W // 2, 10, W-10, H-10]
        self.cvs_figure.create_polygon(points, fill=color, outline=color)
        
    def handle(self):
        self.cvs_figure.delete("all")
        self.cvs_figure.update()   
        color = "#"
        if self.red.get() == 1:
            color = color + "FF"      
        else:
            color = color + "00" 
        if self.green.get() == 1:
            color = color + "FF" 
        else:
            color = color + "00" 
        if self.blue.get() == 1:
            color = color + "FF" 
        else:
            color = color + "00" 
        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        if self.var.get() == 'tam giac':
            points = [10, H-10, W // 2, 10, W-10, H-10]
            self.cvs_figure.create_polygon(points, outline = color, fill = color)
        elif self.var.get() == 'tron':
            self.cvs_figure.create_oval(10, 10, W-10, H-10, outline = color, fill = color)
        else:
            self.cvs_figure.create_rectangle(10, 10, W-10, H-10, outline = color, fill = color)    
if __name__ == "__main__":
    app = App()
    app.mainloop()