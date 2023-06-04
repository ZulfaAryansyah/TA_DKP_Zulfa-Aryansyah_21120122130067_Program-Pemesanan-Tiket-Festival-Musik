from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import re

def validate_nama():
    nama = entry_nama.get()
    if not re.match("^[a-zA-Z ]+$", nama):
        messagebox.showerror("Error", "Nama hanya boleh mengandung huruf")
        entry_nama.delete(0, END)

def validate_jumlah():
    jumlah = entry_jumlah.get()
    if not jumlah.isdigit():
        messagebox.showerror("Error", "Jumlah tiket harus berupa angka")
        entry_jumlah.delete(0, END)

def pesan_tiket():
    nama = entry_nama.get()
    jumlah = entry_jumlah.get()
    jenis = var_jenis.get()
    band = combobox_band.get()
    
    if not nama or not jumlah or not jenis or band == 'Select':
        messagebox.showerror("Error", "Harap isi semua kolom")
        return
    
    konfirmasi = "Terima kasih, {}! Tiket {} untuk band {} telah dipesan sebanyak {} buah.".format(nama, jenis, band, jumlah)
    
    stack.push(konfirmasi)
    
    result = messagebox.askquestion("Konfirmasi Pemesanan", konfirmasi + "\n\nApakah Anda ingin memesan lagi?")
    
    if result == 'yes':
        entry_nama.delete(0, END)
        entry_jumlah.delete(0, END)
        combobox_band.set('Select')
        var_jenis.set('')  
    else:
        while not stack.is_empty():
            messagebox.showinfo("Riwayat Pemesanan", stack.pop())
        
        window.quit()

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

window = Tk()
window.title("CompFest Ticket Reservation")
window.configure(bg="white")  

image = Image.open("compfest.png")
image = image.resize((350, 450), Image.ANTIALIAS)  
photo = ImageTk.PhotoImage(image)
label_gambar = Label(window, image=photo)
label_gambar.pack(pady=10)  

label_nama = Label(window, text="Nama Pemesan:", bg="white")
label_nama.pack()
entry_nama = Entry(window)
entry_nama.pack()
entry_nama.bind("<FocusOut>", lambda event: validate_nama())

label_jumlah = Label(window, text="Jumlah Tiket:", bg="white")
label_jumlah.pack()
entry_jumlah = Entry(window)
entry_jumlah.pack()
entry_jumlah.bind("<FocusOut>", lambda event: validate_jumlah())

label_band = Label(window, text="Pilih Band:", font=("Times New Roman", 12), bg="White")
label_band.pack()
str_band = StringVar(value='')
combobox_band = ttk.Combobox(window, width=17, font=("Times New Roman", 12), textvariable=str_band, state="readonly")
combobox_band['values'] = ('Bring Me The Horizon', 'My Chemical Romance', 'The 1975')
combobox_band.pack(pady=5)

label_jenis = Label(window, text="Jenis Tiket:", bg="white")
label_jenis.pack()

var_jenis = StringVar()
radio1 = Radiobutton(window, text="Bronze", variable=var_jenis, value="Bronze", bg="white")
radio1.pack()
radio2 = Radiobutton(window, text="Silver", variable=var_jenis, value="Silver", bg="white")
radio2.pack()
radio3 = Radiobutton(window, text="Gold", variable=var_jenis, value="Gold", bg="white")
radio3.pack()

btn_pesan = Button(window, text="Pesan Tiket", command=pesan_tiket)
btn_pesan.pack()

stack = Stack()

window.mainloop()