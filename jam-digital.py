import tkinter as tk
from time import strftime

class jendela_utama:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = ('JAM DIGITAL')
        self.root.resizable = (0,0)

        self.labe_jam = tk.Label(self.root, text='')
        self.labe_jam.configure(font="ds_digital 80")
        self.labe_jam.pack()

        self.tombol_keluar = tk.Button(self.root, text='keluar', command=lambda: self.root.destroy())
        self.tombol_keluar.pack()

        jendela_utama.Jam(self)
        self.root.mainloop()

    def Jam(self):
        self.waktu = strftime('%H:%M:%S:%P')
        self.labe_jam.configure(text=self.waktu)
        self.root.after(1000, lambda: jendela_utama.Jam(self))
        return self.waktu

if __name__== '__main__' :
    Jam = jendela_utama()
    print("EXIT")