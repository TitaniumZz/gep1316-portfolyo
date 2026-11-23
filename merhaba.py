
# GEP1316 - Kodlama Okuryazarlığı / Ödev 2
# Kişisel Astroloji Hesaplama Programı

from datetime import date, datetime, timedelta, timezone
import math

# Şehirlerin yaklaşık enlem ve boylam bilgileri
SEHIRLER = {
    "adana": (37.0000, 35.3213),
    "ankara": (39.9334, 32.8597),
    "antalya": (36.8969, 30.7133),
    "aydın": (37.8560, 27.8416),
    "balıkesir": (39.6484, 27.8826),
    "bursa": (40.1885, 29.0610),
    "denizli": (37.7765, 29.0864),
    "diyarbakır": (37.9144, 40.2306),
    "edirne": (41.6771, 26.5557),
    "erzurum": (39.9055, 41.2658),
    "eskişehir": (39.7667, 30.5256),
    "gaziantep": (37.0662, 37.3833),
    "hatay": (36.2021, 36.1600),
    "istanbul": (41.0082, 28.9784),
    "izmir": (38.4237, 27.1428),
    "kahramanmaraş": (37.5753, 36.9228),
    "kayseri": (38.7205, 35.4826),
    "kocaeli": (40.7654, 29.9408),
    "konya": (37.8746, 32.4932),
    "malatya": (38.3552, 38.3095),
    "manisa": (38.6191, 27.4289),
    "mersin": (36.8121, 34.6415),
    "muğla": (37.2153, 28.3636),
    "ordu": (40.9839, 37.8764),
    "rize": (41.0201, 40.5234),
    "sakarya": (40.6940, 30.4358),
    "samsun": (41.2867, 36.3300),
    "şanlıurfa": (37.1674, 38.7955),
    "tekirdağ": (40.9780, 27.5110),
    "trabzon": (41.0027, 39.7168),
    "van": (38.5012, 43.3730),
    "zonguldak": (41.4564, 31.7987),
}

BURCLAR = [
    "Oğlak", "Kova", "Balık", "Koç", "Boğa", "İkizler",
    "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay"
]


# Kullanıcının yaşını hesaplar
def yas_hesapla(dogum_tarihi):
    bugun = date.today()
    yas = bugun.year - dogum_tarihi.year

    if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
        yas -= 1

    return yas


# Doğum tarihine göre Güneş burcunu belirler
def gunes_burcu(dogum_tarihi):
    gun_ay = (dogum_tarihi.month, dogum_tarihi.day)

    tarihler = [
        ((1, 20), "Kova"),
        ((2, 19), "Balık"),
        ((3, 21), "Koç"),
        ((4, 20), "Boğa"),
        ((5, 21), "İkizler"),
        ((6, 21), "Yengeç"),
        ((7, 23), "Aslan"),
        ((8, 23), "Başak"),
        ((9, 23), "Terazi"),
        ((10, 23), "Akrep"),
        ((11, 22), "Yay"),
        ((12, 22), "Oğlak")
    ]

    sonuc = "Oğlak"

    for baslangic, burc in tarihler:
        if gun_ay >= baslangic:
            sonuc = burc

    return sonuc


# Tarih ve saati Julian gün sayısına dönüştürür
def julian_gunu(tarih_saat_utc):
    yil = tarih_saat_utc.year
    ay = tarih_saat_utc.month

    gun = (
        tarih_saat_utc.day
        + (tarih_saat_utc.hour
           + tarih_saat_utc.minute / 60
           + tarih_saat_utc.second / 3600) / 24
    )

    if ay <= 2:
        yil -= 1
        ay += 12

    a = math.floor(yil / 100)
    b = 2 - a + math.floor(a / 4)

    return (
        math.floor(365.25 * (yil + 4716))
        + math.floor(30.6001 * (ay + 1))
        + gun + b - 1524.5
    )


# Doğum saati ve konumuna göre yaklaşık yükselen burcu hesaplar
def yukselen_burcu(dogum_tarihi, dogum_saati, enlem, boylam):
    yerel_saat = datetime.combine(dogum_tarihi, dogum_saati)

    # Türkiye için UTC+3 saat dilimi kullanılır
    yerel_saat = yerel_saat.replace(
        tzinfo=timezone(timedelta(hours=3))
    )

    utc_saat = yerel_saat.astimezone(timezone.utc)

    jd = julian_gunu(utc_saat)
    t = (jd - 2451545.0) / 36525.0

    gst = (
        280.46061837
        + 360.98564736629 * (jd - 2451545.0)
        + 0.000387933 * t * t
        - (t * t * t) / 38710000
    ) % 360

    lst = math.radians((gst + boylam) % 360)
    latitude = math.radians(enlem)
    epsilon = math.radians(23.4393)

    y = -math.cos(lst)

    x = (
        math.sin(lst) * math.cos(epsilon)
        + math.tan(latitude) * math.sin(epsilon)
    )

    longitude = math.degrees(math.atan2(y, x)) % 360

    return BURCLAR[int(longitude // 30)]


# Kullanıcıdan doğum tarihini alır
def tarih_al():
    while True:
        try:
            giris = input("Doğum tarihin (GG.AA.YYYY): ")
            dogum_tarihi = datetime.strptime(
                giris, "%d.%m.%Y"
            ).date()

            if dogum_tarihi > date.today():
                print("Doğum tarihi gelecekte olamaz. Tekrar dene.")
                continue

            return dogum_tarihi

        except ValueError:
            print("Tarih biçimi hatalı. Örnek: 15.08.2003")


# Kullanıcıdan doğum saatini alır
def saat_al():
    while True:
        try:
            giris = input("Doğum saatin (SS:DD, örnek 14:30): ")
            return datetime.strptime(giris, "%H:%M").time()

        except ValueError:
            print("Saat biçimi hatalı. Örnek: 14:30")


# Kullanıcıdan doğum şehrini alır
def sehir_al():
    while True:
        sehir = input("Doğduğun şehir: ").strip().lower()

        if sehir in SEHIRLER:
            return sehir

        print(
            "Bu şehir listede yok. "
            "Örnek: İstanbul, Ankara, İzmir, Bursa."
        )


# Ana program
def program():
    print("=" * 46)
    print("       KİŞİSEL ASTROLOJİ HESAPLAMA")
    print("=" * 46)

    isim = input("Merhaba! Adın ne? ").strip()

    if not isim:
        isim = "Arkadaşım"

    dogum_tarihi = tarih_al()
    dogum_saati = saat_al()
    sehir = sehir_al()

    enlem, boylam = SEHIRLER[sehir]

    yas = yas_hesapla(dogum_tarihi)
    gunes = gunes_burcu(dogum_tarihi)

    yukselen = yukselen_burcu(
        dogum_tarihi,
        dogum_saati,
        enlem,
        boylam
    )

    print("\n" + "=" * 46)
    print(f"Merhaba {isim}! Doğum bilgilerine göre sonuçların:")
    print(f"Yaşın: {yas}")
    print(f"Güneş burcun: {gunes}")
    print(f"Yükselen burcun: {yukselen}")
    print(f"Doğum yerin: {sehir.title()}")
    print("=" * 46)

    print("Not: Burç ve yükselen hesaplamaları yaklaşık sonuç verir.")


if __name__ == "__main__":
    program()
