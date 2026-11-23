# PROMPTLAR - Yapay Zeka Kullanım Süreci

Bu ödevi hazırlarken ChatGPT'den Python kodlama konusunda yardım aldım. Özellikle kullanıcıdan doğum bilgilerini alma, yaş ve burç hesaplama, kodun düzenlenmesi ve ödev gereksinimlerini kontrol etme aşamalarında yapay zekadan yararlandım.

## 1. Uygulamanın temel kodunun oluşturulması

**Prompt:**

Bu ödev için Python kullanarak basit bir yaş hesaplama programı yapmak istiyorum. Ama biraz daha farklı olsun diye kullanıcıdan doğum tarihi, doğum saati ve doğduğu şehri de alıp Güneş burcunu ve yükselen burcunu hesaplayan bir uygulama yapmak istiyorum. Terminal üzerinden çalışsın ve kod çok karmaşık olmasın çünkü kendim de anlayıp hocama anlatabilmeliyim.

**AI'nın katkısı:** Kullanıcıdan doğum bilgilerini alan, yaş ve burç hesaplamaları yapan bir program için temel kod yapısını oluşturdu.

**Kararım:** İlk başta basit bir yaş hesaplama fikriyle başlamıştım ama projeyi biraz daha ilgi çekici hale getirmek istedim. Bu yüzden astroloji hesaplamalarını da eklemeye karar verdim.

## 2. Kullanıcıdan alınacak bilgilerin belirlenmesi

**Prompt:**

Kullanıcıdan adını, doğum tarihini, doğum saatini ve doğduğu şehri sorsak istiyorum. Bu bilgilerle yaşını, Güneş burcunu ve yükselen burcunu hesaplayabilir miyiz? Şehir bilgisi de yükselen burcu hesaplamak için kullanılsın.

**AI'nın katkısı:** Kullanıcıdan alınacak bilgileri düzenledi ve doğum yerine göre enlem ve boylam bilgilerini kullanarak yükselen burcu hesaplamak için bir yöntem önerdi.

**Kararım:** Bu öneriyi kabul ettim. Uygulamanın sadece doğum tarihine göre burç söylemesinden ziyade doğum saati ve şehri de kullanmasını istedim.

## 3. Şehir ve yükselen burcu hesaplamasının eklenmesi

**Prompt:**

Türkiye'deki şehirleri kullanabileceğimiz bir liste oluşturabilir misin? Kullanıcı doğduğu şehri yazdığında program o şehrin yaklaşık koordinatlarını alsın ve yükselen burcunu hesaplasın. Bunun için ekstra karmaşık kütüphaneler kullanmamaya çalış.

**AI'nın katkısı:** Şehirlerin yaklaşık koordinatlarını içeren bir dictionary oluşturdu ve astronomik hesaplamalar kullanarak yükselen burcunu belirleyen bir fonksiyon hazırladı.

**Kararım:** Şehirleri tek tek kullanıcıya koordinat olarak girdirmek yerine şehir adıyla seçebilmesini daha kolay buldum. Bu yüzden şehir listesini kullanmaya karar verdim.

## 4. Kodun ödev gereksinimlerine uygunluğunun kontrol edilmesi

**Prompt:**

Bu kod ödevimin gereksinimlerini karşılıyor mu? Değişkenler, if/else, while döngüsü, fonksiyonlar, kullanıcıdan input alma ve try/except gibi konular kullanılmış mı kontrol eder misin? Eksik bir şey varsa söyleyebilir misin?

**AI'nın katkısı:** Kodun temel Python konularını içerip içermediğini kontrol etti ve eksik olabilecek noktalar hakkında öneriler sundu.

**Kararım:** Sadece çalışan bir program yapmak istemediğim için kodun derste öğrendiğimiz konuları da içermesine dikkat ettim. Bu kontrolün ödev açısından önemli olduğunu düşündüm.

## 5. Hatalı kullanıcı girişlerinin kontrol edilmesi

**Prompt:**

Kullanıcı yanlış bir doğum tarihi veya saat girerse program kapanmasın istiyorum. Gelecekteki bir doğum tarihi girilirse uyarı versin ve tekrar sorsun. Aynı şekilde listede olmayan bir şehir girildiğinde de hata vermek yerine tekrar şehir istesin. Bunları basit bir şekilde ekleyebilir misin?

**AI'nın katkısı:** Tarih, saat ve şehir girişlerini kontrol etmek için try/except ve while döngülerinin kullanılmasını önerdi.

**Kararım:** Bu önerileri kabul ettim çünkü kullanıcı yanlış bilgi girdiğinde programın kapanmasını istemiyordum. Programın tekrar giriş istemesini daha kullanışlı buldum.

## Yapay Zekâ Kullanım Beyanı

| Alan | Yanıt |
|---|---|
| **Kullanılan YZ aracı/araçları** | ChatGPT (OpenAI) |
| **Kullanma amacı** | Python programının oluşturulması, kodun açıklanması, doğum tarihi ve saat bilgilerinin işlenmesi ve yükselen burç hesaplama mantığının geliştirilmesi hakkında destek almak. |
| **Kontrol ve sorumluluk** | Yapay zekâ tarafından üretilen içeriği gözden geçirdiğimi, gerekli düzeltmeleri yaptığımı ve teslim ettiğim çalışmanın doğruluğundan ve akademik dürüstlüğünden sorumlu olduğumu beyan ederim. |
| **Öğrencinin adı-soyadı** | Lalin İpek Ersoy |
| **Tarih ve İmza** | 23.11.2026 — İmza: <img width="153" height="117" alt="image" src="https://github.com/user-attachments/assets/c30b144d-56b2-4719-b1b7-11ef576144d2" />
 |

### APA 7 Kaynakça
OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com/

