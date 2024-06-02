from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import calendar

data_list = []

def system():
    root = Tk()
    root.geometry("1525x800")
    root.title("Reservasi Restoran")
    root.attributes('-fullscreen', True)

    orderno = StringVar()
    pemesan = StringVar()
    tglrsv = StringVar()
    jamrsv = StringVar()
    paket = StringVar()
    harga = StringVar()
    pajak = StringVar()
    total = StringVar()
    
    def TotalHargaPesanan():

        total_harga = float(harga.get())

        total_pajak = (total_harga * 0.1)
        total_seluruh = str(total_harga + total_pajak)

        pajak.set(total_pajak)
        total.set(total_seluruh)

    def Hapus():
        orderno.set("")
        pemesan.set("")
        tglrsv.set("")
        jamrsv.set("")
        paket.set("")
        harga.set("")
        pajak.set("")
        total.set("")

    def Keluar():
        root.destroy()


    root.configure(bg="#FFFFFF")

    frameAtas = Frame(root, bg="#FFFFFF", width=1600, height=50)
    frameAtas.pack(side=TOP)

    frameKiri = Frame(root,bg="#FFFFFF", width=1200, height=900)
    frameKiri.pack(side=LEFT)

    frameKanan = Frame(root, width=400, height=700)
    frameKanan.pack(side=RIGHT)
    

    def BukaPaketCustom():
        jendela_paket_custom = Toplevel(root)
        jendela_paket_custom.title("Paket Custom")
        jendela_paket_custom.configure(bg="#ccb79b")

        style = ttk.Style()
        style.configure("Kustom.Label", background="#FFFFFF", font=('Calibri', 16, 'bold'), padding=10)
        style.configure("Kustom.TLabel", background="#FFFFFF", font=('Calibri', 12, 'bold'), padding=10)
        style.configure("Kustom.TEntry", font=('Calibri', 14), padding=5)
        style.configure("Kustom.TButton", background="#CDAA7D", font=('Calibri', 14, 'bold'), padding=10)
        style.configure("Harga.TLabel", font=('Calibri', 12, 'italic'), padding=5, background="#977a59", foreground="white")

        judul_label = ttk.Label(jendela_paket_custom, text="😊😊 Paket Custom 😊😊", style="Kustom.Label")
        judul_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        ikan_label = ttk.Label(jendela_paket_custom, text="Jumlah Ikan:", style="Kustom.TLabel")
        ikan_label.grid(row=2, column=0, padx=10, pady=10)
        ikan_entry = ttk.Spinbox(jendela_paket_custom, from_=0, to=10, style="Kustom.TEntry")
        ikan_entry.grid(row=2, column=1, padx=10, pady=10)
        ikan_harga_label = ttk.Label(jendela_paket_custom, text="Rp 10,000/ikan", style="Harga.TLabel")
        ikan_harga_label.grid(row=2, column=2, pady=10)

        nasi_label = ttk.Label(jendela_paket_custom, text="Jumlah Nasi:", style="Kustom.TLabel")
        nasi_label.grid(row=3, column=0, padx=10, pady=10)
        nasi_entry = ttk.Spinbox(jendela_paket_custom, from_=0, to=10, style="Kustom.TEntry")
        nasi_entry.grid(row=3, column=1, padx=10, pady=10)
        nasi_harga_label = ttk.Label(jendela_paket_custom, text="Rp 5,000/nasi", style="Harga.TLabel")
        nasi_harga_label.grid(row=3, column=2, pady=10)

        esteh_label = ttk.Label(jendela_paket_custom, text="Jumlah Es Teh:", style="Kustom.TLabel")
        esteh_label.grid(row=4, column=0, padx=10, pady=10)
        esteh_entry = ttk.Spinbox(jendela_paket_custom, from_=0, to=10, style="Kustom.TEntry")
        esteh_entry.grid(row=4, column=1, padx=10, pady=10)
        esteh_harga_label = ttk.Label(jendela_paket_custom, text="Rp 3,000/es teh", style="Harga.TLabel")
        esteh_harga_label.grid(row=4, column=2, pady=10)

        hitung_button = ttk.Button(jendela_paket_custom, text="Hitung Total", command=lambda: hitung_total_custom(ikan_entry, nasi_entry, esteh_entry, jendela_paket_custom), style="Kustom.TButton")
        hitung_button.grid(row=5, column=0, columnspan=3, pady=20)


    def hitung_total_custom(ikan_entry, nasi_entry, esteh_entry, window):
   
        ikan_qty = int(ikan_entry.get())
        nasi_qty = int(nasi_entry.get())
        es_teh_qty = int(esteh_entry.get())

        harga_ikan = 10000 
        harga_nasi = 5000  
        harga_es_teh = 3000 

        total_harga = (ikan_qty * harga_ikan) + (nasi_qty * harga_nasi) + (es_teh_qty * harga_es_teh)

        paket.set("Custom")
        harga.set(total_harga)
        TotalHargaPesanan();

        window.destroy()


    def TampilkanData():
        my_tree.delete(*my_tree.get_children())
        for data in data_list:
            my_tree.insert('', 'end', values=data)



    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    background="#DEB887",
                    )
    style.map('Treeview',
              background=[('selected', '#FFD39B')],foreground=[('selected', 'black')])

    my_tree = ttk.Treeview(frameKanan)
    my_tree['columns'] = ("Ordno", "Pemesan","Tgl Rsrvsi", "Jam Rsrvsi", "Paket", "Harga", "Pajak", "Total",)

    horizontal_bar = ttk.Scrollbar(frameKanan, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(frameKanan, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("Ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Pemesan", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("Tgl Rsrvsi", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("Jam Rsrvsi", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("Paket", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Harga", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("Pajak", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("Total", anchor=CENTER, width=100, minwidth=25)

    my_tree.heading("Ordno", text="Order No", anchor=CENTER)
    my_tree.heading("Pemesan", text="Pemesan", anchor=CENTER)
    my_tree.heading("Tgl Rsrvsi", text="Tgl Rsrvsi", anchor=CENTER)
    my_tree.heading("Jam Rsrvsi", text="Jam Rsrvsi", anchor=CENTER)
    my_tree.heading("Paket", text="Paket", anchor=CENTER)
    my_tree.heading("Harga", text="Harga", anchor=CENTER)
    my_tree.heading("Pajak", text="Pajak", anchor=CENTER)
    my_tree.heading("Total", text="Total", anchor=CENTER)


    my_tree.pack()
    TampilkanData()


    def validasi_tanggal(tanggal_str):
        try:
            datetime.datetime.strptime(tanggal_str,  '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validasi_jam(jam_str):
        try:
            datetime.datetime.strptime(jam_str, '%H:%M')
            return True
        except ValueError:
            return False

  
    def TambahData():
        orders = orderno.get()
        pemesans = pemesan.get()
        jamrsvs = jamrsv.get()
        tglrsvs = tglrsv.get()
        pakets = paket.get()
        hargas = harga.get()
        pajaks = pajak.get()
        totals = total.get()

        pesanan_ada = [data[0] for data in data_list]
        waktudanjam_ada = [(data[2], data[3]) for data in data_list]

        if orders == "" or pemesans == "" or jamrsvs == "" or tglrsvs == "" or pakets == "" or hargas == "" or pajaks == ""  or totals == "":
            messagebox.showinfo("Peringatan", "Silahkan mengisi input yang masih kosong!!!")
        elif orders in pesanan_ada:
            messagebox.showinfo("Peringatan", f"Nomer Order {orders} telah digunakan!")
        elif not validasi_tanggal(tglrsvs):
            messagebox.showinfo("Peringatan", "Format tanggal tidak valid. Harap masukkan waktu dalam format DD/MM/YYYY dengan data tanggal yang benar.")
        elif not validasi_jam(jamrsvs):
            messagebox.showinfo("Peringatan", "Format waktu tidak valid. Harap masukkan waktu dalam format HH:MM rangenya 00:00 - 24:00.")
        elif (tglrsvs, jamrsvs) in waktudanjam_ada:
            messagebox.showinfo("Peringatan", f"Reservasi pada {tglrsvs} jam {jamrsvs} sudah ada!")
        else:
            my_tree.delete(*my_tree.get_children())
            data_list.append((orders, pemesans, tglrsvs, jamrsvs, pakets, hargas, pajaks, totals))
            messagebox.showinfo("Pesan", "Reservasi berhasil ditambahkan")
        TampilkanData()
       

    def CetakNota():
      if not my_tree.selection():
        messagebox.showwarning("Peringatan", "Silahkan memilih data terlebih dahulu")
      else:   
        item_terpilih = my_tree.focus()
        konten = my_tree.item(item_terpilih)
        
        order_no = konten["values"][0]
        pemesan_qty = konten["values"][1]
        tglrsv_qty = konten["values"][2]
        jamrsv_qty = konten["values"][3]
        paket_qty = konten["values"][4]
        harga = konten["values"][5]
        pajak = konten["values"][6]
        total = konten["values"][7]
        
        jendela_nota = Toplevel(root)
        jendela_nota.title("Receipt")
        jendela_nota.geometry("400x450")


        Label(jendela_nota, font=('Calibri', 16, 'bold'), bg="#d3d3d3", text="RESERVASI RESTORANT", fg="Black", anchor='center').pack(pady=0)

        Label(jendela_nota, font=('Calibri', 16,'bold'), bg="#d3d3d3", text="IKAN BAKAR PAK SUWARNO", fg="black", anchor='center').pack(pady=(0,10))

        pemisah = Label(jendela_nota, text="-" * 50)
        pemisah.pack()

        Label(jendela_nota, text="Order No: " + str(order_no), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Nama Pemesan: " + str(pemesan_qty), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Tanggal Reservasi: " + str(tglrsv_qty), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Jam Reservasi: " + str(jamrsv_qty), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Paket: " + str(paket_qty), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Harga: Rp." + str(harga), justify='center', font=('Calibri', 12)).pack(anchor='center')
        Label(jendela_nota, text="Pajak 10%: Rp." + str(pajak), justify='center', font=('Calibri', 12)).pack(anchor='center')

        pemisah = Label(jendela_nota, text="-" * 50)
        pemisah.pack()
        Label(jendela_nota, text="Total:          Rp." + str(total), justify='center', bg="#d3d3d3", anchor='center', font=('Calibri', 12)).pack(anchor='center')
        pemisah = Label(jendela_nota, text="-" * 50)
        pemisah.pack()

        Label(jendela_nota, font=('Calibri', 16, 'bold'), text="Kami Akan Selalu Melayani Pelanggan", fg="red").pack(anchor='center')
        Label(jendela_nota, font=('Calibri', 16, 'bold'), text="Dengan Senyuman Terindah", fg="red").pack(anchor='center')
        Label(jendela_nota, font=('Calibri', 16, 'bold'), text="😊😊😊", fg="red").pack(anchor='center')



    judul_utama = Label(frameAtas, font=('Calibri', 25, 'bold'), bg="#FFFFFF", text="RESERVASI RESTORANT", fg="Black", anchor=W)
    judul_utama.grid(row=0, column=0)
    judul_restoran = Label(frameAtas, font=('Calibri', 25, 'bold'), bg="#FFFFFF", text="IKAN BAKAR PAK SUWARNO", fg="black", anchor=W)
    judul_restoran.grid(row=1, column=0)

    gambar = Image.open("D:/BASPRO FINAL PROJECT/suwarno.png")
    ukuran_baru = (1400, 170)
    gambar_resize = gambar.resize(ukuran_baru)
    gambar_photo = ImageTk.PhotoImage(gambar_resize)

    tampilakn_foto = Label(frameAtas, image=gambar_photo)
    tampilakn_foto.grid(row=2, column=0)
    

    ordlbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Order No.", fg="black",bg='white', bd=2, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=orderno).grid(row=1, column=1)

    peslbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Pemesan", fg="black",bg='white', bd=5, anchor=W).grid(row=2,
                                                                                                         column=0)
    pestxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=pemesan).grid(row=2, column=1)

    tglrsvlbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Tanggal Reservasi", fg="black",bg='white', bd=5, anchor=W).grid(row=3,
                                                                                                         column=0)
    tglrsvtxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=tglrsv).grid(row=3, column=1)
    
    jamrsvlbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Jam Reservasi", fg="black",bg='white', bd=5, anchor=W).grid(row=4,
                                                                                                         column=0)
    jamrvstxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=jamrsv).grid(row=4, column=1)

    pktlbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Paket", fg="black",bg='white', bd=2, anchor=W).grid(row=5,
                                                                                                             column=0)
    pkttxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=paket).grid(row=5, column=1)

    hrglbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Harga", fg="black",bg='white', bd=2, anchor=W).grid(row=6,
                                                                                                            column=0)
    hrgtxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                     textvariable=harga).grid(row=6, column=1)

    pajaklbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Pajak", bd=2,bg='white', anchor=W).grid(row=7, column=0)
    pajaktxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                    textvariable=pajak).grid(row=7, column=1)

    totallbl = Label(frameKiri, font=('Calibri', 16, 'bold'), text="Total", bd=2,bg='white', anchor=W).grid(row=8, column=0,pady=(10,0))
    totaltxt = Entry(frameKiri, font=('Calibri', 16, 'bold'), bd=3, insertwidth=4, justify='right',
                   textvariable=total).grid(row=8, column=1,pady=(10,0))
 


    custompaketbtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Custom Paket", bg="#CDAA7D", fg="black", bd=3, relief="ridge", padx=5, pady=5,
                width=12, command=BukaPaketCustom, overrelief="solid", highlightthickness=3, highlightbackground="black",).grid(row=6, column=5)

    hapusbtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Hapus", bg="#CDAA7D", fg="black", relief="ridge", bd=3, padx=5,
                      pady=5, width=12, command=Hapus,  overrelief="solid", highlightthickness=1, highlightbackground="black").grid(row=4, column=5)

    keluarbtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Keluar", relief="ridge", overrelief="solid", bg="#CDAA7D", fg="black", bd=3, padx=5,
                     pady=5, width=12, command=Keluar).grid(row=6, column=3,padx=(50,10))

    tambahbtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Tambah",relief="ridge", overrelief="solid", bg="#CDAA7D", fg="black", bd=3, padx=5, pady=5,
                    width=12, command=TambahData).grid(row=2, column=5)

    cetaknotabtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Cetak Nota",relief="ridge", overrelief="solid", bg="#CDAA7D", fg="black", bd=3,
                       padx=5, pady=5, width=12, command=CetakNota).grid(row=4, column=3,padx=(50,10))

    def Menu():
        def scroll_tanpa_menggunakan_scrollbar(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        halaman_paket = Toplevel(root)
        halaman_paket.geometry("400x400")
        halaman_paket.title("Pilihan Paket")
        halaman_paket.configure(bg="#ccb79b")

        label_judul = ttk.Label(halaman_paket, text="😊😊 Silahkan Memilih Paket 😊😊", font=('Calibri', 16, 'bold'), background="#FFFFFF")
        label_judul.pack(pady=10)

        canvas = Canvas(halaman_paket, background="#ccb79b", highlightbackground="#FFFFFF", highlightthickness=0, height=300)
        canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        scrollbar = Scrollbar(halaman_paket, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas, style="FramePutih.TFrame")
        canvas.create_window((60, 0), window=frame, anchor='nw')

        def saat_frame_dikonfigurasi(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", saat_frame_dikonfigurasi)

        def paket_dipilih(jenis_paket):
            harga_paket = hargaPaket.get(jenis_paket, "Harga tidak tersedia")
            harga.set(harga_paket)
            paket.set(jenis_paket)
            TotalHargaPesanan()
            halaman_paket.destroy()

        infoPaket = {
            "Bakar Meriah": "5 Ikan, 5 Nasi, 5 Es Teh  (Rp.140.000)",
            "Pesona Bakaran Solo": "1 Ikan, 1 Nasi, 1 Es Teh (Rp.28.000)",
            "Duet Bakaran Ikan": "2 Ikan, 2 Nasi, 2 Es Teh (Rp.56.000)",
            "Bakar Tiga Rasa": "3 Ikan, 3 Nasi, 3 Es Teh (Rp.84.000)",
            "Kebersamaan Bakaran Empat": "4 Ikan, 4 Nasi, 4 Es Teh (Rp.132.000)",
        }

        hargaPaket = {
            "Bakar Meriah": "140000",
            "Pesona Bakaran Solo": "28000",
            "Duet Bakaran Ikan": "56000",
            "Bakar Tiga Rasa": "84000",
            "Kebersamaan Bakaran Empat": "132000",
        }

        style = ttk.Style()
        style.configure("FramePutih.TFrame", background="#ccb79b")
        style.configure("TombolPaket.TButton", font=('Calibri', 14), padding=(10, 5, 10, 5), background = "#d3d3d3")
        style.configure("Harga.TLabel", font=('Calibri', 12, 'italic'), padding=5, foreground="white")

        for jenis_paket, info_menu in infoPaket.items():
            tombol_paket = ttk.Button(frame, text=jenis_paket, style="TombolPaket.TButton", command=lambda p=jenis_paket: paket_dipilih(p))
            tombol_paket.pack(pady=5)
            info_menu_label = ttk.Label(frame, text=info_menu, style="Harga.TLabel", background="#977a59")
            info_menu_label.pack(pady=5)  


        canvas.bind_all("<MouseWheel>", scroll_tanpa_menggunakan_scrollbar)
       

    menubtn = Button(frameKiri, font=('Calibri', 16, 'bold'), text="Daftar Paket", relief="ridge", overrelief="solid", bg="#CDAA7D", fg="black", bd=3, padx=5,
                     pady=5, width=12, command=Menu).grid(row=2, column=3,padx=(50,10))

    root.mainloop()


system()