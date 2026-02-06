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
---

# FOR ENG
---

# 🖼️ AI Background Remover

This project is a tool that removes image backgrounds within seconds and with high accuracy using Python and AI-based libraries.

Without any need for manual selection, it automatically detects objects using the **U2Net** model and makes the background transparent.

## 🚀 Features

* **Automatic Detection:** No need to manually select the object.
* **High Quality:** Preserves complex details such as hair strands or fur.
* **Fast Processing:** Produces quick results with ONNX Runtime support.
* **Simple Usage:** You only need to specify input and output paths.

## 🛠️ Technologies and Libraries Used

The following Python libraries were used while developing this project:

* **[rembg](https://github.com/danielgatis/rembg):** The core of the background removal process. Uses the U2Net deep learning model.
* **[Pillow (PIL)](https://python-pillow.org/):** Used for image processing, opening, and saving images.
* **Python 3.x:** The main programming language of the project.

## 📦 Installation

You can follow the steps below to run the project on your computer:

1. **Clone the project:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/BackgroundRemover.git
   cd BackgroundRemover
   ```

2. **Install the required libraries:**

   ```bash
   pip install rembg pillow
   ```

---

## 💻 Usage

While in the project directory, run the following command in the terminal:

```bash
python main.py
```

## ⚠️ Important Note

When the program is run for the first time, the AI model (**u2net.onnx**, approximately 170MB) is automatically downloaded from the internet. This may take a few minutes depending on your internet speed. There will be no waiting time on subsequent runs.

---

