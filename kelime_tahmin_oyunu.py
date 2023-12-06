import random

def kelime_tahmin_oyunu():
    kelimeler = ["python", "programlama", "veri", "geliştirici", "bilgisayar", "proje", "yazılım", "kodlama", "algoritma", "öğrenme"]
    hedef_kelime = random.choice(kelimeler)
    dogru_tahmin = False
    tahmin_edilen_harfler = []

    print("Merhaba! Kelime tahmin oyununa hoş geldiniz.")

    while not dogru_tahmin:
        kelime_gosterimi = "".join([harf if harf in tahmin_edilen_harfler else '_' for harf in hedef_kelime])
        print(f"Tahmin edilen kelime: {kelime_gosterimi}")

        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen geçerli bir harf girin.")
            continue

        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin.")
            continue

        tahmin_edilen_harfler.append(tahmin)

        if tahmin in hedef_kelime:
            print("Harika! Doğru tahmin ettiniz.")
        else:
            print("Üzgünüm, yanlış tahmin. Başka bir harf deneyin.")

        dogru_tahmin = all(harf in tahmin_edilen_harfler for harf in hedef_kelime)

    print(f"Tebrikler! Kelimeyi doğru tahmin ettiniz. Kelime: {hedef_kelime}")

if __name__ == "__main__":
    kelime_tahmin_oyunu()
