import pyqrcode  # QR kod oluşturma kütüphanesi


def generate_qr_code():
    """
    Kullanıcıdan alınan URL'yi QR koda çevirir ve SVG formatında kaydeder.
    """

    # 1. ADIM: Kullanıcıdan Veri Alma
    # QR kodun nereye gideceğini (linki) kullanıcıya soruyoruz.
    url = input("QR Kodu oluşturulacak URL'yi girin: ")

    # Boş veri girişini engellemek için küçük bir kontrol (Opsiyonel)
    if not url:
        print(" Hata: Lütfen geçerli bir URL girin!")
        return

    print(" QR Kod oluşturuluyor, lütfen bekleyin...")

    try:
        # 2. ADIM: QR Kod Nesnesini Yaratma
        # pyqrcode kütüphanesi ile veriyi şifreliyoruz.
        qr_object = pyqrcode.create(url)

        # 3. ADIM: Dosyayı Kaydetme
        # Oluşan kodu 'qrcode.svg' adıyla vektörel formatta kaydediyoruz.
        # scale=8 -> QR kodun büyüklüğünü ayarlar (Daha büyük = Daha net).
        qr_object.svg('qrcode.svg', scale=8)

        print(f" Başarılı! 'qrcode.svg' dosyası oluşturuldu.")
        print(f"🔗 Bağlantı: {url}")

    except Exception as e:
        print(f"⚠️ Bir hata oluştu: {e}")


# Bu blok, dosya doğrudan çalıştırıldığında devreye girer.
if __name__ == "__main__":
    generate_qr_code()