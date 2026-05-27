# Turing Makinesi ile Araç Plaka Formatı Tanıyıcı

Bu proje, Özdevinirler Kuramı dersi final ödevi kapsamında geliştirilmiştir. Python programlama dili kullanılarak deterministik bir **Turing Makinesi (TM)** simülatörüyle araç plakalarının format doğrulaması gerçekleştirilmektedir.

# Amaç ve Problem Tanımı
Projenin amacı; if-else kontrol blokları veya Regex yerine, otomatlar teorisinin en gelişmiş modeli olan Turing Makinesi mimarisini kullanarak karakter bazlı analiz ve durum tabanlı doğrulama yapmaktır.

Sistem, Türkiye standartlarına uygun olan **NNLLNNN** (2 Rakam, 2 Büyük Harf, 3 Rakam) formatındaki plakaları doğrular:
* **N (Rakam):** `0–9` arası karakterler
* **L (Harf):** `A–Z` arası büyük harfler
* **Uzunluk:** Tam olarak 7 karakter (Eksik veya fazla karakterler doğrudan reddedilir).

## 🛠️ Turing Makinesi Modeli (7'li Küme)
$M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$

* **Q (Durumlar):** $\{q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_{red}\}$
* **$\Sigma$ (Giriş Alfabesi):** $\{0-9, A-Z\}$
* **$\Gamma$ (Bant Alfabesi):** $\{0-9, A-Z, B\}$ (`B`: Blank / Boşluk sembolü)
* **$q_0$ (Başlangıç Durumu):** $q_0$
* **$q_{accept}$ (Kabul Durumu):** $q_7$
* **$q_{reject}$ (Red Durumu):** $q_{red}$

## 💻 Kurulum ve Çalıştırma

Projede herhangi bir harici kütüphane kullanılmamıştır, standart Python 3 ailesiyle doğrudan çalıştırılabilir.

```bash
# Repoyu bilgisayarınıza klonlayın
git clone [https://github.com/KULLANICI_ADINIZ/Turing-Makinesi-Plaka-Taniyici.git](https://github.com/KULLANICI_ADINIZ/Turing-Makinesi-Plaka-Taniyici.git)

# Proje klasörüne giriş yapın
cd Turing-Makinesi-Plaka-Taniyici

# Simülasyonu başlatın
python main.py


📊 Test Senaryoları
Geçerli Girdiler (KABUL): 55AB123, 34TR456, 06AA789

Geçersiz Girdiler (RED): 5AB123 (Eksik karakter), 555AB12 (Fazla rakam), 55ab123 (Küçük harf ihlali)
