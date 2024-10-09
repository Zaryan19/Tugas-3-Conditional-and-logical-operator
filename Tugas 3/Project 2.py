nilai = int(input("Masukkan nilai ujian anda(0-100) : "))

if 100 >= nilai >= 90:
    print("Feedback : Sangat Baik")
elif 89 >= nilai >= 80 :
    print("Feedback : Baik")
elif 79 >= nilai >= 70:
    print("Feedback : Cukup")
elif 69 >= nilai >= 60:
    print("Feedback : Kurang")
else :
    print("Feedback : Sangat Kurang")