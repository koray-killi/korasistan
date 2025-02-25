# Korasistan v1.0 📌

**Author: koray-killi**

---

## 📜 İçindekiler

- [1. Giriş](#1-giriş)
  - [1.1 Proje Tanımı](#11-proje-tanımı)
  - [1.2 Özellikler](#12-özellikler)
- [2. Kurulum](#2-kurulum)
  - [2.1 Gereksinimler](#21-gereksinimler)
  - [2.2 Yükleme Adımları](#22-yükleme-adımları)
- [3. Kullanım](#3-kullanım)
  - [3.1 Terminal Komutları](#31-terminal-komutları)
  - [3.2 Sesli Komutlar](#32-sesli-komutlar)
- [4. Uygulama Modülleri](#4-uygulama-modülleri)
  - [4.1 🔑 Şifre Oluşturucu (Passgen)](#41-şifre-oluşturucu-passgen)
  - [4.2 🌦 Hava Durumu (Weather)](#42-hava-durumu-weather)
  - [4.3 📝 Not Defteri (Note)](#43-not-defteri-note)
  - [4.4 📰 Haber Önizleme (News)](#44-haber-önizleme-news)
- [5. Geliştirme ve Katkıda Bulunma](#5-geliştirme-ve-katkıda-bulunma)
- [6. Lisans](#6-lisans)

---

## 1. Giriş

### 1.1 Proje Tanımı

**Korasistan**, terminal tabanlı, sesli ve yazılı komutları destekleyen, modüler bir kişisel asistan uygulamasıdır. Kullanıcılara şifre oluşturma, hava durumu sorgulama, not alma ve haber başlıklarını görüntüleme gibi özellikler sunar.

### 1.2 Özellikler

- 🎙 **Sesli ve Yazılı Komut Desteği**
- 📜 **Modüler Yapı** (Kolayca yeni özellikler eklenebilir)
- 🎨 **Renkli ve Kullanıcı Dostu Arayüz** (`colorama` ile)
- 🔑 **Güçlü Şifre Üretme Sistemi**
- 🌦 **Gerçek Zamanlı Hava Durumu API Kullanımı**
- 📝 **Dosya Tabanlı Not Tutma Sistemi**
- 📰 **Haber Kaynaklarından Otomatik Veri Çekme**

---

## 2. Kurulum

### 2.1 Gereksinimler

Korasistan’ı çalıştırmak için aşağıdaki yazılımlar gereklidir:

- Python 3.x
- `pip` (Python Paket Yöneticisi)

### 2.2 Yükleme Adımları

Öncelikle, gerekli bağımlılıkları yükleyin:

```sh
pip install -r requirements.txt
```

Alternatif olarak:

```sh
pip install colorama speechrecognition pyperclip requests beautifulsoup4
```

Ardından, uygulamayı çalıştırmak için:

```sh
python main.py
```

---

## 3. Kullanım

### 3.1 Terminal Komutları

Korasistan, terminal üzerinden aşağıdaki komutlarla çalıştırılabilir:

```sh
>> şifre oluştur
>> hava durumu
>> not al
>> haberler
>> girdi değiştir
>> çıkış
```

### 3.2 Sesli Komutlar

Kullanıcı giriş yöntemi olarak mikrofonu seçtiğinde aşağıdaki sesli komutları verebilir:

- "şifre oluştur"
- "hava durumu"
- "not al"
- "haberler"

---

## 4. Uygulama Modülleri

### 4.1 🔑 Şifre Oluşturucu (Passgen)

- Kullanıcıdan alınan seçeneklere göre güçlü ve rastgele şifreler üretir.
- Şifreler `pyperclip` ile otomatik olarak panoya kopyalanır.
- Büyük harf, özel karakter ve sayı içeriğini özelleştirme imkanı sağlar.

### 4.2 🌦 Hava Durumu (Weather)

- OpenWeatherMap API ile gerçek zamanlı hava durumu verilerini alır.
- Kullanıcının belirlediği şehir için sıcaklık, hissedilen sıcaklık ve hava durumu bilgilerini listeler.
- Gün doğumu ve gün batımı saatlerini gösterir.

### 4.3 📝 Not Defteri (Note)

- Kullanıcıların not almasına, notlarını listelemesine ve silmesine olanak tanır.
- Notlar `.txt` formatında kaydedilir.
- Basit bir metin tabanlı arayüz sunar.

### 4.4 📰 Haber Önizleme (News)

- Haber kaynaklarından başlıkları çeker (`BeautifulSoup` ile).
- Kullanıcı seçtiği haberleri tarayıcıda açabilir.
- Mynet, Hürriyet, Sözcü gibi kaynakları destekler.

---

## 5. Geliştirme ve Katkıda Bulunma

Projeye katkıda bulunmak için aşağıdaki adımları takip edebilirsiniz:

1. Bu repoyu forkladıktan sonra yerel bilgisayarınıza klonlayın:
   ```sh
   git clone https://github.com/koray-killi/korasistan.git
   ```
2. Yeni bir özellik ekleyin veya mevcut bir hatayı düzeltin.
3. Değişikliklerinizi push edin ve bir pull request oluşturun.

Katkılarınız memnuniyetle karşılanacaktır! 🚀

---

