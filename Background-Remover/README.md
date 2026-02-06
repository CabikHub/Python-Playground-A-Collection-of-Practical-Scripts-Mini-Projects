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
```
---
⚠️ Önemli Not
Program ilk kez çalıştırıldığında, yapay zeka modeli (u2net.onnx, yaklaşık 170MB) internetten otomatik olarak indirilir. Bu işlem internet hızınıza bağlı olarak birkaç dakika sürebilir. Sonraki çalıştırmalarda bekleme süresi olmayacaktır.

---
## ⚠️ Sorumluluk Reddi (Disclaimer)

Bu araç **yalnızca eğitim amaçlı** olarak oluşturulmuştur.
 **Kullanım Şartları** ve **telif haklarına** uyma sorumluluğu tamamen kullanıcıya aittir.
---

# 🖼️ AI Background Remover

This project is a tool that removes backgrounds from images in seconds with high accuracy using Python and AI-based libraries.

It uses the **U2Net** model to automatically detect objects and make the background transparent without the need for manual selection.

## 🚀 Features

- **Automatic Detection:** No need to manually select the object.
- **High Quality:** Preserves complex details like hair or fur.
- **Fast Processing:** Delivers quick results with ONNX Runtime support.
- **Simple Usage:** Just specify the input and output paths.

## 🛠️ Technologies & Libraries

I used the following Python libraries to build this project:

- **[rembg](https://github.com/danielgatis/rembg):** The core of the background removal process. It utilizes the U2Net deep learning model.
- **[Pillow (PIL)](https://python-pillow.org/):** Used for image processing, opening, and saving files.
- **Python 3.x:** The main programming language of the project.

## 📦 Installation

To run this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/BackgroundRemover.git](https://github.com/YOUR_USERNAME/BackgroundRemover.git)
   cd BackgroundRemover

2. **Install the required libraries:**
   ```bash
   pip install rembg pillow

💻 Usage
Run the following command in the terminal while in the project directory:
```bash
   python main.py
```

When the code runs, it takes the source image (Squirrel.jpg), processes it, and saves the background-removed version as (output.png).

⚠️ Important Note
When the program is run for the first time, the AI model (u2net.onnx, approx. 170MB) will be downloaded automatically. This may take a few minutes depending on your internet speed. Subsequent runs will be instant.





