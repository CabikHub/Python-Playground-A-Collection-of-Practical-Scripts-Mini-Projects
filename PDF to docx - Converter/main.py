import os  # İşletim sistemi araçları (Dosya Kontrolü için kullanılır)
import time # Zaman araçları (Süre Tutmak için)
from pdf2docx import Converter #PDF'i Word'e çeviren kütüphane

def pdf_to_word(pdf_path, docx_path):
    """
    Belirtilen PDF dosyasını Word (docx) formatına çevirir.
    Dosya kontrolü ve süre hesaplaması yapar.
    """
    # 1. ADIM: Dosya kontrolü
    # İşleme başlamadan önce dosya gerçekten burada mı diye kontrol ederiz.

    if not os.path.exists(pdf_path):
        print(f"HATA: '{pdf_path}' dosyası bulunamadı! ")
        return

    print (f"İşlem başlıyor: {pdf_path}")

    #2. ADIM: Kronometreyi burada başlatıyoruz.
    #Şu anki zamanı kaydediyoruz (ÖRN:17:38:30)
    baslangic_zamani = time.time()


    try:
        #3. ADIM: Dönüştürme işlemi burada başlıyor.

        cv = Converter(pdf_path) # PDF Dosyasını yükle
        cv.convert(docx_path)    # Word dosyasına çevir ve kaydet
        cv.close()               # Dosyayı burada kapat.

        #4. ADIM: Süreyi hesapla
        #Şu anki zamandan başlangıcı çıkar (Bitiş - Başlangıç = Geçen süre)
        gece_sure = time.time() - baslangic_zamani

        print(f"Başarılı! Dosya oluşturuldu: {docx_path}")
        print(f"İşlem süresi: {gece_sure:.2f} saniye")

    except Exception as hata:
        #Eğer beklenmedik bir sorun olursa program çökmesin, hatayı bize söylesin diye bu bloğu yazıyoruz.
        print(f"Bir hata oluştu: {hata}")

#Bu blok, dosya doğrudan çalıştığında devreye girer.

if __name__ == "__main__":
    giris_dosyasi ="sample.pdf"
    cikis_dosyasi ="sample.docx"

    # Fonksiyonu çağıralım burada
    pdf_to_word(giris_dosyasi,cikis_dosyasi)