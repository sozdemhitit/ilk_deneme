# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:48:40 2023

@author: P558

Python da SQLITE veritabanı uygulaması

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql 

def tabloOlustur():
   bag= sql.connect("hafta9_ders1.db")
   cursor = bag.cursor()
   cursor.execute("""
               
CREATE TABLE "Ogrenciler" (
	"Id"	INTEGER NOT NULL,
	"Ogrenci_No"	TEXT NOT NULL,
	"Adi"	TEXT,
	"Soyadi"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
                  """
                  )
   

   bag.commit()
   bag.close()    
   print("tablo oluşturuldu")

   
def veriekle():
    bag = sql.connect("hafta9_ders1.db")
    cursor = bag.cursor()
    
    cursor.execute(
        """
        insert into Ogrenciler (Ogrenci_No, Adi, Soyadi) 
        Values (?,?,?)""", (txt_no.get(),txt_adi.get(),txt_soyadi.get())
        )
    bag.commit()
    bag.close()
    tk.messagebox.showinfo(message="Kayıt tamamlandı")

form = tk.Tk()
form.title("veri giriş formu")
form.geometry("700x550")

ana_frame = tk.Frame(form)
ana_frame.pack()


kullanici_bilgileri_frame = tk.LabelFrame(ana_frame, text="Kullanıcı Bilgileri")
kullanici_bilgileri_frame.grid(row=0, column=0, padx=15, pady=2)


lbl_adi = tk.Label(kullanici_bilgileri_frame, text="Adı : ")
lbl_adi.grid(row=0, column=0)

lbl_soyadi = tk.Label(kullanici_bilgileri_frame, text="Soyadı : ")
lbl_soyadi.grid(row=0, column=1)

txt_adi = tk.Entry(kullanici_bilgileri_frame)
txt_adi.grid(row=1, column=0)

txt_soyadi = tk.Entry(kullanici_bilgileri_frame)
txt_soyadi.grid(row=1, column=1)

lbl_bolum = tk.Label(kullanici_bilgileri_frame, text="Bölüm : ")
lbl_bolum.grid(row=0, column=2)

cmb_bolum = ttk.Combobox(kullanici_bilgileri_frame, values=["Bilgisayar Programcılığı", "Elektronik ve Otomasyon"])
cmb_bolum.grid(row=1, column=2)

lbl_yas = tk.Label(kullanici_bilgileri_frame, text="Yaş : ")
lbl_yas.grid(row=2, column=0)

spn_yas = tk.Spinbox(kullanici_bilgileri_frame, from_=15, to=100)
spn_yas.grid(row=3, column=0)


lbl_uyruk = tk.Label(kullanici_bilgileri_frame, text="Uyruk : ")
lbl_uyruk.grid(row=2, column=1)

lbl_no = tk.Label(kullanici_bilgileri_frame, text="Öğrenci No :")
lbl_no.grid(row=2, column=2)

txt_no = tk.Entry(kullanici_bilgileri_frame)
txt_no.grid(row=3, column=2)

cmb_uyruk = ttk.Combobox(kullanici_bilgileri_frame, values=["Türkiye", "Azerbaycan", "Bosna Hersek"])
cmb_uyruk.grid(row=3, column=1)

for eleman in kullanici_bilgileri_frame.winfo_children():
    eleman.grid_configure(padx=5, pady=2)

kayit_bilgileri_frame = tk.LabelFrame(ana_frame, text="Kayıt Bilgleri")
kayit_bilgileri_frame.grid(row=1, column=0)

lbl_kayit = tk.Label(kayit_bilgileri_frame, text="Ders Kaydı Var mı?")
lbl_kayit.grid(row=0, column=0)

ders_kayit = tk.StringVar(value="Ders Kaydı Yok")

chk_kayit= tk.Checkbutton(kayit_bilgileri_frame, text= "Var",
                          variable =ders_kayit,
                          onvalue="Ders Kaydı Var",
                          offvalue = "Ders Kaydı Yok")
chk_kayit.grid (row=1, column=0)


lbl_sinif = tk.Label(kayit_bilgileri_frame, text="Sınıf : ")
lbl_sinif.grid(row=0, column=1)

spn_sinif = tk.Spinbox(kayit_bilgileri_frame, from_=0, to=4)
spn_sinif.grid(row=1, column=1)

lbl_donem = tk.Label(kayit_bilgileri_frame, text="Dönemi : ")
lbl_donem.grid(row=0, column=2)

spn_donem = tk.Spinbox(kayit_bilgileri_frame, from_=1, to=2)
spn_donem.grid(row=1, column=2)


onay_frame = tk.LabelFrame(ana_frame)
onay_frame.grid(row=2, column=0)

onay_kontrol = tk.StringVar(value="onaylanmadi")

chk_onay = tk.Checkbutton(onay_frame, text="Bilgileri Onaylıyorum!", 
                          variable=onay_kontrol, 
                          onvalue="onaylandi", 
                          offvalue="onaylanmadi"
    )
print(onay_kontrol.get())

chk_onay.grid(row=0,column=0)

for elemanlar2 in kayit_bilgileri_frame.winfo_children():
    elemanlar2.grid_configure(padx = 5, pady=5)

btn_kaydet = tk.Button(ana_frame, text="KAYDET" , command=veriekle )
btn_kaydet.grid(row=3, column=0, sticky="news", padx=15, pady=5)

btn_tabloOlustur= tk.Button(ana_frame, text="tablo oluştur", command=tabloOlustur)
btn_tabloOlustur.grid(row=4,column=0)

form.mainloop()

