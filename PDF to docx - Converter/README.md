# 📄 PDF to Word Converter (PDF'ten Word'e Dönüştürücü)

Bu proje, Python kullanarak PDF dosyalarını düzenlenebilir Word (.docx) belgelerine dönüştüren, hata kontrollü ve performans ölçümlü bir araçtır.

Ofis otomasyon süreçlerini anlamak ve Python ile belge işlemlerini yönetmek amacıyla geliştirdim.

## 🚀 Özellikler

Bu script sadece düz bir dönüştürme yapmaz, aynı zamanda şunları sunar:

-   **🔍 Dosya Kontrolü:** İşlem öncesi `os` kütüphanesi ile dosyanın varlığını kontrol eder, hata almayı engeller.
-   **⏱️ Performans Takibi:** `time` kütüphanesi ile dönüştürme işleminin tam olarak kaç saniye sürdüğünü hesaplar.
-   **🛡️ Hata Yönetimi:** `try-except` blokları sayesinde olası hataları (bozuk dosya vb.) program çökmeden kullanıcıya bildirir.

## 🛠️ Kullanılan Kütüphaneler

Projede aşağıdaki kütüphaneler kullanılmıştır:

-   **[pdf2docx](https://pypi.org/project/pdf2docx/):** PDF ayrıştırma ve Word oluşturma işlemleri için.
-   **os:** (Dahili) Dosya yolu ve varlık kontrolleri için.
-   **time:** (Dahili) İşlem süresini ölçmek için.

## 📦 Kurulum (Installation)

Projeyi kendi bilgisayarınızda çalıştırmak için:

1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/PDF-Converter.git](https://github.com/KULLANICI_ADIN/PDF-Converter.git)
    cd PDF-Converter
    ```

2.  **Gerekli kütüphaneyi yükleyin:**
    ```bash
    pip install pdf2docx
    ```

## 💻 Kullanım (Usage)

Proje klasörüne dönüştürmek istediğiniz PDF dosyasını atın (örneğin: `sample.pdf`) ve kodu çalıştırın:

```bash
python main.py
```
# 📄 PDF to Word Converter

This project is a tool that converts PDF files into editable Word (.docx) documents using Python, featuring error control and performance measurement.

understand to office automation processes and manage document operations with Python.

## 🚀 Features

This script does not just perform a plain conversion; it also offers:

-   **🔍 File Verification:** Checks for the file's existence using the `os` library before processing to prevent errors.
-   **⏱️ Performance Tracking:** Calculates exactly how many seconds the conversion takes using the `time` library.
-   **🛡️ Error Handling:** Notifies the user of potential errors (corrupt files, etc.) without crashing the program, thanks to `try-except` blocks.

## 🛠️ Libraries Used

The following libraries were used in this project:

-   **[pdf2docx](https://pypi.org/project/pdf2docx/):** For PDF parsing and Word generation.
-   **os:** (Built-in) For file path and existence checks.
-   **time:** (Built-in) To measure processing time.

## 📦 Installation

To run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PDF-Converter.git](https://github.com/YOUR_USERNAME/PDF-Converter.git)
    cd PDF-Converter
    ```

2.  **Install the required library:**
    ```bash
    pip install pdf2docx
    ```

## 💻 Usage

Place the PDF file you want to convert into the project folder (e.g., `sample.pdf`) and run the code:

```bash
python main.py
