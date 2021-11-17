""" lap trinh mot messagebox in dong chu xin chao va nut thoat """
import tkinter as tk
from tkinter import messagebox as msg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercise 1")
        self.lb = tk.Label(self, text="Khoa CNTT - DHSPKT TP HCM \n Chao mung cac ban SV khoa 2021",
                            bg="white", font=("Calibri", 15), relief=tk.SUNKEN)
        self.btn = tk.Button(self, text="Exit", relief=tk.RAISED, command=self.click_exit, width=10, font=("Calibri", 10))

        self.lb.grid(row=0, column=0, padx=10, pady=10)
        self.btn.grid(row=1, column=0, padx=10, pady=10)
        
    def click_exit(self):
        notify = msg.askquestion("Notify", "Do you exit program?")
        if notify == "yes":
            self.destroy()
if __name__ == "__main__":
    root = App()
    root.mainloop()