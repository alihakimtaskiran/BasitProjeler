haftalık_ders_saati=40
notlar=[]
notlar.append(input("Beden:"))
notlar.append(float(input("Bilgisayar:")))
notlar.append(float(input("Coğrafya:")))
notlar.append(float(input("Din:")))
notlar.append(float(input("Felsefe:")))
notlar.append(float(input("Biyoloji:")))
notlar.append(float(input("Fizik:")))
notlar.append(float(input("Kimya:")))
notlar.append(float(input("Matematik:")))
notlar.append(float(input("Görsel Sanatlar/Müzik:")))
notlar.append(float(input("İkinci Yabancı Dil:")))
notlar.append(float(input("Seçmeli Fen Bilimler:")))
notlar.append(float(input("Tarih:")))
notlar.append(float(input("Edebiyat:")))
notlar.append(float(input("Yabancı Dil:")))
ortalama=sum(notlar)/haftalık_ders_saati
print("Ortalama",ortalama)
input("")
