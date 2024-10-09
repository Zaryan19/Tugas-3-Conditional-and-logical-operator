usia = int(input("Masukkan usia anda: "))  
darah = int(input("Masukkan tekanan darah anda: "))  

if usia >= 60 and darah > 140:
    print("Status kesehatan: Tinggi")
elif usia >= 60 and darah <= 140:
    print("Status kesehatan: Normal")
elif usia < 60 and darah > 130:
    print("Status kesehatan: Tinggi")
else:
    print("Status kesehatan: Normal")