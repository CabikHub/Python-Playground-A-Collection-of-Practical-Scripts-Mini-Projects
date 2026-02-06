# 🛡️ Python Port Scanner

Bu proje, Python ve `socket` kütüphanesi kullanılarak geliştirilmiş, çok iş parçacıklı (multi-threaded) olmayan basit bir port tarama aracıdır. 

 "Siber Güvenlik ve Ağ Programlama" çalışmaları kapsamında, TCP bağlantı mantığını (Three-Way Handshake) anlamak amacıyla geliştirilmiştir.

## ⚠️ YASAL UYARI (LEGAL DISCLAIMER)

**Lütfen Okuyunuz:**
Bu araç **sadece eğitim ve test amaçlı** geliştirilmiştir. 

1.  Bu yazılımı sadece **kendinize ait ağlarda** veya **yazılı izniniz olan sistemlerde** (örn: `scanme.nmap.org`) kullanmalısınız.
2.  İzinsiz ağ taraması yapmak birçok ülkede yasa dışıdır.
3.  Geliştirici (**Emirhan**), bu aracın yanlış kullanımından doğabilecek herhangi bir hasar veya yasal sorumluluktan **sorumlu tutulamaz.**

*Kullanıcı, bu aracı çalıştırarak tüm yasal sorumluluğu kabul etmiş sayılır.*

---

## 🚀 Özellikler

- **Renkli Arayüz:** `colorama` ile okunabilir, renkli terminal çıktıları.
- **Port Analizi:** Hedef IP üzerindeki portların açık/kapalı durumunu (TCP Connect Scan) kontrol eder.
- **Hata Yönetimi:** Bağlantı zaman aşımı ve hatalı girişlere karşı dayanıklıdır.

## 🛠️ Kurulum

1.  Projeyi indirin:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/Port-Scanner.git](https://github.com/KULLANICI_ADIN/Port-Scanner.git)
    cd Port-Scanner
    ```

2.  Gerekli kütüphaneyi yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
    *(Veya manuel olarak: `pip install colorama`)*

## 💻 Kullanım

Aracı terminalden başlatın:

```bash
python main.py
```

# FOR ENG

# 🛡️ Python Port Scanner

This project is a simple, non-multi-threaded port scanning tool developed using Python and the `socket` library.

It was developed within the scope of "Cyber Security and Network Programming" studies to understand the TCP connection logic (Three-Way Handshake).

## ⚠️ LEGAL DISCLAIMER

**Please Read:**
This tool has been developed for **educational and testing purposes only**.

1.  You must use this software only on **networks you own** or **systems for which you have written permission** (e.g., `scanme.nmap.org`).
2.  Unauthorized network scanning is illegal in many countries.
3.  The developer (**Emirhan**) cannot be held **responsible** for any damage or legal liability arising from the misuse of this tool.

*By running this tool, the user is deemed to have accepted all legal responsibility.*

---

## 🚀 Features

- **Colorful Interface:** Readable, colored terminal outputs using `colorama`.
- **Port Analysis:** Checks the open/closed status of ports on the target IP (TCP Connect Scan).
- **Error Management:** Robust against connection timeouts and invalid inputs.

## 🛠️ Installation

1.  Clone the project:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Port-Scanner.git](https://github.com/YOUR_USERNAME/Port-Scanner.git)
    cd Port-Scanner
    ```

2.  Install the required library:
    ```bash
    pip install -r requirements.txt
    ```
    *(Or manually: `pip install colorama`)*

## 💻 Usage

Start the tool via terminal:

```bash
python main.py
