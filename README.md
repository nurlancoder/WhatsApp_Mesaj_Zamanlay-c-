# WhatsApp Otomatik Mesaj Gönderici

Bu proje, kullanıcının belirlediği tarih ve saatte WhatsApp Web üzerinden otomatik olarak mesaj göndermesini sağlar. Kullanıcı, telefon numarası, mesaj, tarih ve saat girerek mesajını zamanlayabilir ve gönderebilir.

**Not:** WhatsApp Web açık olmalıdır ve mesajlar 20-40 saniye beklenerek gönderilecektir.


## Temel Özellikler

- Telefon numarası, mesaj, tarih ve saat girerek WhatsApp mesajını zamanlayın.
- Zamanlanan mesajlar otomatik olarak gönderilecektir.
- Kullanıcı dostu Tkinter GUI arayüzü.


## Gereksinimler
Bu projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:

- `tkinter` — GUI oluşturmak için kullanılır (Python ile birlikte gelir).
- `pywhatkit` — WhatsApp mesajları göndermek için kullanılır.
- `schedule` — Zamanlanmış görevleri yönetmek için kullanılır.
- `time` — Zaman yönetimi için kullanılır.
- `datetime` — Tarih ve saat ile çalışmak için kullanılır.


## Gereksinimlerin Kurulumu
Aşağıdaki komut ile gerekli kütüphaneleri kurabilirsiniz:

bash
pip install pywhatkit schedule
Kullanım
whatsapp_auto.py dosyasını çalıştırın.


Grafik kullanıcı arayüzü açılacaktır. Burada:
Telefon numarasını,
Mesajınızı,
Tarihi (YYYY-AA-GG formatında),
Saati (SS:DD formatında)
girdikten sonra "Mesajı Zamanla" butonuna tıklayın.

Mesajınız belirttiğiniz tarihte ve saatte WhatsApp Web üzerinden gönderilecektir.



### Yüklenmesi Gereken Kütüphaneler

- `pywhatkit`
- `schedule`

Yukarıdaki gereksinimleri ve kullanım talimatlarını README dosyasına ekleyerek projenizi GitHub'a yükleyebilirsiniz.
