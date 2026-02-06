import socket #Ağ bağlantıları kurmak için (Dahili Kütüphane)
import time # İşlem Süresini ölçmek için (Dahili kütüphane)
from datetime import datetime #Raporlama için tarih/saat bilgisi (Dahili)

from colorama import init, Fore, Style # Terminal çıktılarını renklendirmek için Harici Kütüphane

#Burada Coloromayı başlatıyoruz
init()

def port_scan(hedef, baslangic_portu, bitis_portu):
    """
    Verilen hedef IP üzerindeki belirli port aralığını tarar
    ve açık olanları renkli olarak listeler.

    """
    #1. ADIM: Hedef Adresi Çözümleme
    #Kullanıcı "google.com" girerse bunu "142.250..." gibi sayısal IP'ye çevirmek için kullanıyoruz.
    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        #Eğer adres çözümlemezse (yanlış yazılırsa) kırmızı hata mesajı verecek.
        print(Fore.RED + " Hata: Hostname çözülemedi! Adresi kontrol ediniz."+ Style.RESET_ALL)
        return

    #Bilgilendirme Ekranı (Mavi Renk)

    print(Fore.CYAN+ "-" * 50)
    print(f"Hedef IP: {Fore.YELLOW}{hedef_ip}")
    print(f"{Fore.CYAN} Başlangıç Zamanı: {datetime.now()}")
    print("-" * 50 + Style.RESET_ALL) #RESET_ALL ile rengi normale çeviriyoruz.

    # Kronometreyi başlatalım
    baslangic_zamani = time.time()

    try:
        #2. ADIM: Portları Döngüyle gezmek için
        for port in range(baslangic_portu, bitis_portu + 1):

            #Soket nesnesi Oluşturma:
            #AF_INET = IPv4 adreslemesi kullanacağımızı belirtmek için kullanılır.
            # SOCK_STREAM = TCP protokolü (bağlantı tabanlı) kullanacağımızı belirtir.

            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Zaman aşımı (Timeout):
            #Eğer bir port 0.5 saniyede cevap vermezse "Kapalı olarak varsayıp diğerlerini dene."
            #Bunu yapmazsak program stucklanabilir.
            s.settimeout(0.5)

            #3. ADIM: Kapıyı Çalma (Bağlantı Denemesi)
            # connect_ex: Bağlanmayı dener ve sonuç olarak bir sayı (kod) döner.
            # 0 dönerse -> Bağlantı başarısız (Port KAPALI veya FİLTRELİ)

            sonuc = s.connect_ex((hedef_ip,port))

            if sonuc == 0:
                #Port açık ise YEŞİL renkte ekrana yazdır.
                print(f"{Fore.GREEN}[+] Port {port}: AÇIK {Style.RESET_ALL}")

            #Soketi Kapat (Açık kalan bağlantı sistem kaynağını tüketir)
            s.close()

    except KeyboardInterrupt:
        # Kullanıcı terminalde CTRL+C Yaparsa programı durdur.
        print(Fore.RED + "\n Tarama kullanıcı tarafından iptal edildi! "+ Style.RESET_ALL)

    except socket.error:
        #Sunucu ile ilgili genel bir bağlantı hatası oluşursa.
        print(Fore.RED + "\n Sunucuya bağlanılamadı!"+ Style.RESET_ALL)

    #4. Adım Bitiş RAPORU
    gecen_sure = time.time() - baslangic_zamani
    print(Fore.CYAN+ "-" * 50)
    print(f" Tarama tamamlandı.")

    #Süreyi virgülden sonra 2 basamak olacak şekilde formatlayalım Örnek (5.34 sn)
    print(f" Toplam süre: {Fore.WHITE}{gecen_sure:.2f} saniye{Style.RESET_ALL}")

    # --- MAİN ---

    #Bu dosya doğrudan çalıştırılırsa (import edilmediğinde) bursaı çalışır.
if __name__ == "__main__":
        # Ekrana ASCII yazdıralıme
        print(Fore.BLUE + r"""
        
        
        
          ____            _     _   
         |  _ \ ___  _ __| |_  | |  
         | |_) / _ \| '__| __| | |  
         |  __/ (_) | |  | |_  |_|  
         |_|   \___/|_|   \__| (_)  
            """ + Style.RESET_ALL)

        # Kullanıcıdan Hedef adresini iste
        hedef_adres = input(f"{Fore.YELLOW} Taranacak Adres Örn: google.com veya localhost olsun): {Style.RESET_ALL}")

        #Fonksiyonu çağır (ÖRN: 1 ile 100 arasındaki portları tara)
        #Not: Tüm portları taramak (65.535) uzun süreceği için 100 ile deniyorum.
        port_scan(hedef_adres,1,100)



