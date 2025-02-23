# Kor-Asistan v0.1 🚀

Kor-Asistan, sesli veya yazılı komutlarla çalışan, modüler ve genişletilebilir bir CLI asistanıdır. Kullanıcı dostu arayüzü, hata yönetimi ve farklı uygulamaları entegre edebilme yeteneği ile kişisel kullanım için güçlü bir araçtır.

---

## 🎯 **Özellikler**

### ✅ **Genel Özellikler:**
- 🎙️ **Sesli ve Yazılı Komut Desteği** (speech_recognition)
- 🎨 **Renkli ve Anlaşılır Çıktılar** (colorama)
- ⚙️ **Komut Alma Tercihlerini Kaydetme ve Okuma**
- 🏗️ **Tamamen Modüler Yapı** – Yeni uygulamalar kolayca eklenebilir.
- 🔄 **Kullanıcı Dostu Menü ve Hata Yönetimi**

### 🔹 **Mevcut Uygulamalar:**
#### 🔑 **Şifre Oluşturucu (Passgen)**
- **Güçlü ve rastgele şifreler üretir.**
- **Türkçe karakter desteğiyle özelleştirilmiş algoritma.**
- **Özel karakter, büyük harf ve sayı tercihlerine göre şifre oluşturma.**
- **Otomatik panoya kopyalama desteği (pyperclip).**

#### ☁️ **Hava Durumu Uygulaması**
- **API kullanarak gerçek zamanlı hava durumu verilerini çeker.**
- **Kullanıcının girdiği şehir için sıcaklık, hissedilen sıcaklık ve hava durumu bilgilerini gösterir.**
- **Güneşin doğuş ve batış saatlerini hesaplar.**
- **Kapsamlı hata yönetimi içerir.**

#### 📝 **Not Defteri Uygulaması**
- **Not oluşturma, listeleme, okuma ve silme işlemleri yapılabilir.**
- **Dosya tabanlı kayıt sistemi ile notlar kalıcıdır.**
- **Kullanıcı dostu hata yönetimi ve rehberlik mesajları içerir.**

---

## 🚀 **Kurulum**

Öncelikle, bağımlılıkları yükleyin:

```sh
pip install colorama speechrecognition pyperclip requests beautifulsoup4
```

Ardından uygulamayı çalıştırın:

```sh
python main.py
```

---

## 📌 **Nasıl Kullanılır?**

### 🎙️ **Sesli Komut Kullanımı:**
1. Uygulamayı başlatın.
2. Mikrofon ile konuşarak aşağıdaki komutları verebilirsiniz:
   - "şifre oluştur"
   - "hava durumu"
   - "not al"
3. Sistem, sesli komutları algılayarak ilgili işlemi gerçekleştirir.

### ⌨️ **Yazılı Komut Kullanımı:**
1. Program başlarken giriş yöntemi olarak "Yazı" seçeneğini belirleyin.
2. Terminale aşağıdaki komutlardan birini girin:
   ```sh
   >> şifre oluştur
   >> hava durumu
   >> not al
   ```
3. Komutunuzu çalıştırarak ilgili uygulamayı açabilirsiniz.

---

## 🔄 **Geliştirme Aşamasındaki Özellikler**
- 📢 **Haberler Uygulaması** – Günlük haberleri çekecek.
- 📊 **Gelişmiş Hava Durumu Grafikleri** – Görselleştirilmiş sıcaklık değişimleri.
- 🔍 **Notlarda Arama ve Kategorilendirme** – Notları daha düzenli hale getirme.

---

## 🤝 **Katkıda Bulunma**
Projeyi geliştirmek isterseniz pull request gönderebilir veya hata bildirebilirsiniz. Her türlü katkıya açığız! ✨

---

📌 **Lisans:** MIT License  
📌 **Geliştirici:** koray-killi
📌 **Sürüm:** v0.1

