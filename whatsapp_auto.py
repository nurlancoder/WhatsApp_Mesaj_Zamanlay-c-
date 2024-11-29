import tkinter as tk
from tkinter import messagebox
import pywhatkit
import schedule
import time
from datetime import datetime, timedelta
import threading

def mesaj_gonder():
    try:
        telefon = telefon_entry.get().strip()
        mesaj = mesaj_entry.get("1.0", tk.END).strip()
        tarih = tarih_entry.get().strip()
        saat = saat_entry.get().strip()

        if not telefon or not mesaj or not tarih or not saat:
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")
            return

        if not telefon.startswith("+"):
            telefon = "+994" + telefon

        gonderme_zamani = f"{tarih} {saat}"
        mesaj_zamanla(telefon, mesaj, gonderme_zamani)
        messagebox.showinfo("Başarılı", "Mesaj gönderme işlemi zamanlandı.")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

def send_whatsapp_message(kisi, mesaj, gonderme_zamani):
    now = datetime.now()
    gonderme_zamani = datetime.strptime(gonderme_zamani, "%Y-%m-%d %H:%M")

    if gonderme_zamani < now + timedelta(minutes=1):
        gonderme_zamani = now + timedelta(minutes=1)
    
    hours = gonderme_zamani.hour
    minutes = gonderme_zamani.minute

    pywhatkit.sendwhatmsg(kisi, mesaj, hours, minutes, wait_time=20, tab_close=True)
    print(f"Mesaj gönderildi: {kisi}, {mesaj}")

def mesaj_zamanla(kisi, mesaj, gonderme_zamani):
    zaman = datetime.strptime(gonderme_zamani, "%Y-%m-%d %H:%M")
    schedule.every().day.at(zaman.strftime("%H:%M")).do(send_whatsapp_message, kisi, mesaj, gonderme_zamani)
    print(f"Mesaj zamanlandı: {kisi}, {mesaj}, {gonderme_zamani}")

# GUI oluşturma
root = tk.Tk()
root.title("WhatsApp Mesaj Gönderici")

tk.Label(root, text="Telefon Numarası:").grid(row=0, column=0, padx=10, pady=5)
telefon_entry = tk.Entry(root, width=30)
telefon_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Mesaj:").grid(row=1, column=0, padx=10, pady=5)
mesaj_entry = tk.Text(root, width=30, height=5)
mesaj_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Tarih (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
tarih_entry = tk.Entry(root, width=30)
tarih_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Saat (HH:MM):").grid(row=3, column=0, padx=10, pady=5)
saat_entry = tk.Entry(root, width=30)
saat_entry.grid(row=3, column=1, padx=10, pady=5)

gonder_button = tk.Button(root, text="Mesajı Zamanla", command=mesaj_gonder)
gonder_button.grid(row=4, column=0, columnspan=2, pady=10)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.daemon = True
schedule_thread.start()

root.mainloop()  
