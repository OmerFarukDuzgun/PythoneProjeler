
sozluk = {"Bilim insanı": "Aziz Sancar", "Şair": "Mehmet Akif Ersoy", "Astronom": "Ali Kuşçu"}

# a) Sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız.
meslekler = sozluk.copy()
print("Meslekler sözlüğü:", meslekler)

# b) Sözlüğün değerlerini ekrana yazdırınız.
degerler = sozluk.values()
print("Sözlük değerleri:", degerler)

# c) Sözlüğü içi boş bir sözlük hâline getiriniz.
sozluk.clear()
print("Sözlük içi boş hale getirildi:", sozluk)

# d) Sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz.
sozluk["Matematikçi"] = "Cahit Arf"
print("Sözlüğe yeni değer eklendi:", sozluk)

# e) Sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olarak değiştiriniz.
sozluk["Bilim insanı"] = "Canan Dağdeviren"
print("Değer güncellendi:", sozluk)

# f) Sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırınız.
if "Şair" in sozluk:
    print("Şair:", sozluk["Şair"])
else:
    print("Şair anahtarı sözlükte bulunamadı.")