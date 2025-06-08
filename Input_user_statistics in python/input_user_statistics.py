angkaPilihan_user_1 = int(input("Masukan Angka Pilihan Lo Yang Pertama : "))
angkaPilihan_user_2 = int(input("Masukan Angka PIlihan Lo Yang Kedua : "))
angkaPilihan_user_3 = int(input("Masukan Angka Pilihan Lo Yang Ketiga : "))
angka_hasil = [angkaPilihan_user_1, angkaPilihan_user_2, angkaPilihan_user_3] 

jumlah = sum(angka_hasil)
rata_rata = jumlah / len(angka_hasil)
maksimum = max(angka_hasil)
minimum = min(angka_hasil)

print(f"Jumlah      : {jumlah}")
print(f"Rata - rata : {rata_rata}")
print(f"Maksimum    : {maksimum}")
print(f"Minimum     : {minimum}")
