# Bluetooth Chat App

Bu proje, KivyMD kullanarak oluşturulmuş bir Bluetooth Chat uygulamasıdır. Uygulama, kullanıcıların cihazlar arası mesajlaşma yapmasına olanak tanır. Cihaz listesi ekranından, belirli bir cihaza tıklayarak sohbet ekranına geçiş yapılabilir ve mesajlar gönderilebilir.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlar gereklidir:

- Python 3.x
- Kivy
- KivyMD

### Kurulum

Projenin çalışması için gerekli adımlar:

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/kullanici/bluetooth-chat-app.git
    ```
2. Proje dizinine gidin:
    ```bash
    cd bluetooth-chat-app
    ```
3. Gereksinimleri yükleyin:
    ```bash
    pip install kivy kivymd
    ```

### Kullanım

Uygulamayı başlatmak için şu komutu çalıştırın:

```bash
python main.py
```

Uygulama başladığında, cihazlar listesinden bir cihaz seçerek sohbet ekranına geçiş yapabilirsiniz. Mesajınızı yazdıktan sonra, `send` düğmesine tıklayarak mesajınızı gönderebilirsiniz.

### Proje Yapısı

- `main.py`: Uygulamanın ana Python dosyası. Ekran yöneticisi ve ekranlar burada tanımlanır.
- `main.kv`: Kivy dilinde yazılmış UI tasarım dosyası.

### Özellikler

- Cihaz listesi ekranı
- Dinamik olarak oluşturulan sohbet ekranları
- Mesaj gönderme ve alma (simule edilmiş)
- Mesajların soldan veya sağdan hizalanması

https://github.com/Deryaglmz/BluetoothChat/assets/129391768/af48c096-4112-4ee0-8eb8-7f5a531f951e
