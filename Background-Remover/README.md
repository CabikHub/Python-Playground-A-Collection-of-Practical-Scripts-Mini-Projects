# 🖼️ AI Background Remover (Arka Plan Temizleyici)

Bu proje, Python ve yapay zeka tabanlı kütüphaneler kullanarak görsellerin arka planını saniyeler içinde, yüksek doğrulukla temizleyen bir araçtır.

Manuel seçim yapmaya gerek kalmadan, **U2Net** modelini kullanarak nesneleri otomatik olarak algılar ve arka planı şeffaf hale getirir.

## 🚀 Özellikler

- **Otomatik Algılama:** Nesneyi manuel seçmeye gerek yoktur.
- **Yüksek Kalite:** Saç telleri veya kürk gibi karmaşık detayları korur.
- **Hızlı İşlem:** ONNX Runtime desteği ile hızlı sonuç üretir.
- **Basit Kullanım:** Sadece giriş ve çıkış yollarını belirlemeniz yeterlidir.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

Bu projeyi geliştirirken aşağıdaki Python kütüphanelerinden yararlandım:

- **[rembg](https://github.com/danielgatis/rembg):** Arka plan temizleme işleminin kalbi. U2Net derin öğrenme modelini kullanır.
- **[Pillow (PIL)](https://python-pillow.org/):** Görüntü işleme, açma ve kaydetme işlemleri için kullanıldı.
- **Python 3.x:** Projenin temel programlama dili.

## 📦 Kurulum (Installation)

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Projeyi klonlayın:**
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/BackgroundRemover.git](https://github.com/KULLANICI_ADIN/BackgroundRemover.git)
   cd BackgroundRemover
   
2. Gerekli kütüphaneleri yükleyin:

   ``` bash
   pip install rembg pillow
   
---
💻 Kullanım (Usage)
Proje dizinindeyken terminale şu komutu yazarak çalıştırabilirsiniz:
``` bash
python main.py

⚠️ Önemli Not
Program ilk kez çalıştırıldığında, yapay zeka modeli (u2net.onnx, yaklaşık 170MB) internetten otomatik olarak indirilir. Bu işlem internet hızınıza bağlı olarak birkaç dakika sürebilir. Sonraki çalıştırmalarda bekleme süresi olmayacaktır.