import tkinter as tk  # Mengimpor modul tkinter untuk membuat antarmuka pengguna grafis
from tkinter import filedialog, messagebox  # Mengimpor filedialog untuk memilih file dan messagebox untuk pesan popup
from tkinter import Label, Button, Frame  # Mengimpor widget Label, Button, dan Frame dari tkinter
from PIL import Image, ImageTk  # Mengimpor modul PIL untuk memproses gambar
import cv2  # Mengimpor OpenCV untuk pemrosesan gambar
import numpy as np  # Mengimpor numpy untuk operasi array

class ImageNegativeConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PENGUBAH CITRA NEGATIF by kelompok 6")  # Mengatur judul jendela aplikasi
        self.root.geometry("500x600")  # Mengatur ukuran awal jendela

        self.label = Label(root, text="No image selected")  # Membuat label untuk menampilkan pesan
        self.label.pack(pady=10)  # Menambahkan label ke jendela dengan padding vertikal 10

        self.image_frame = Frame(root)  # Membuat frame untuk menampilkan gambar
        self.image_frame.pack(pady=10)  # Menambahkan frame ke jendela dengan padding vertikal 10

        self.image_label = Label(self.image_frame)  # Membuat label untuk menampilkan gambar di dalam frame
        self.image_label.pack()  # Menambahkan label gambar ke frame

        self.button_frame = Frame(root)  # Membuat frame untuk tombol
        self.button_frame.pack(side=tk.BOTTOM, pady=10)  # Menambahkan frame tombol ke jendela di bagian bawah dengan padding vertikal 10

        self.insert_btn = Button(self.button_frame, text="Insert Image", command=self.insert_image)  # Membuat tombol untuk memasukkan gambar
        self.insert_btn.grid(row=0, column=0, padx=5)  # Menambahkan tombol ke frame tombol dengan padding horizontal 5

        self.negative_btn = Button(self.button_frame, text="Negative Now!", command=self.convert_to_negative, state=tk.DISABLED)  # Membuat tombol untuk mengubah gambar menjadi negatif
        self.negative_btn.grid(row=0, column=1, padx=5)  # Menambahkan tombol ke frame tombol dengan padding horizontal 5

        self.save_btn = Button(self.button_frame, text="Save Image", command=self.save_image, state=tk.DISABLED)  # Membuat tombol untuk menyimpan gambar
        self.save_btn.grid(row=0, column=2, padx=5)  # Menambahkan tombol ke frame tombol dengan padding horizontal 5

        self.image_path = None  # Variabel untuk menyimpan path gambar
        self.image = None  # Variabel untuk menyimpan objek gambar PIL
        self.cv_image = None  # Variabel untuk menyimpan objek gambar OpenCV

    def insert_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])  # Membuka dialog untuk memilih file gambar
        if self.image_path:
            self.cv_image = cv2.imread(self.image_path)  # Membaca gambar menggunakan OpenCV
            self.image = Image.open(self.image_path)  # Membuka gambar menggunakan PIL
            self.display_image(self.image)  # Menampilkan gambar
            self.label.config(text="Image loaded successfully")  # Mengubah teks label menjadi "Image loaded successfully"
            self.negative_btn.config(state=tk.NORMAL)  # Mengaktifkan tombol "Negative Now!"
            self.save_btn.config(state=tk.NORMAL)  # Mengaktifkan tombol "Save Image"

    def display_image(self, img):
        img.thumbnail((400, 400))  # Mengubah ukuran gambar menjadi thumbnail dengan batas maksimal 400x400
        img_tk = ImageTk.PhotoImage(img)  # Mengonversi gambar PIL menjadi format yang bisa ditampilkan oleh tkinter
        self.image_label.config(image=img_tk)  # Menampilkan gambar pada label gambar
        self.image_label.image = img_tk  # Menyimpan referensi gambar agar tidak dikumpulkan oleh garbage collector

    def convert_to_negative(self):
        if self.cv_image is not None:
            negative_image = 255 - self.cv_image  # Mengubah gambar menjadi negatif dengan mengurangkan nilai pixel dari 255
            self.cv_image = negative_image  # Menyimpan gambar negatif ke variabel
            self.image = Image.fromarray(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))  # Mengonversi gambar negatif menjadi format PIL
            self.display_image(self.image)  # Menampilkan gambar negatif
            self.label.config(text="Negative image created")  # Mengubah teks label menjadi "Negative image created"

    def save_image(self):
        if self.image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp"), ("TIFF", "*.tiff")])  # Membuka dialog untuk menyimpan gambar
            if save_path:
                self.image.save(save_path)  # Menyimpan gambar ke path yang dipilih
                messagebox.showinfo("Image Saved", "Image saved successfully!")  # Menampilkan pesan bahwa gambar telah disimpan

if __name__ == "__main__":
    root = tk.Tk()  # Membuat objek root tkinter
    app = ImageNegativeConverterApp(root)  # Membuat instance dari kelas ImageNegativeConverterApp
    root.mainloop()  # Memulai loop utama tkinter
