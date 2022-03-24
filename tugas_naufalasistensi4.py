class JenisHewan:
    def __init__(self, jenis, ras):
        self.jenis = jenis
        self.ras = ras
    def keterangan(self) :
        return (f"Jenis Hewan : {self.jenis}, \nRas Hewan : {self.ras}")

class Vaksinasi(JenisHewan) :
    jumlahvaksinasi = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Vaksinasi.jumlahvaksinasi +=1
    def keterangan(self) :
        return (f"Perawatan Vaksinasi untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class Surgery(JenisHewan) :
    jumlahsurgery = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Vaksinasi.jumlahvaksinasi +=1
    def keterangan(self) :
        return (f"Perawatan Vaksinasi untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class MedicalCare(JenisHewan) :
    jumlahmedicalcare = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        MedicalCare.jumlahmedicalcare +=1
    def keterangan(self) :
        return (f"Perawatan Medical Care untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class WellnessCare(JenisHewan) :
    jumlahwellnesscare = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        WellnessCare.jumlahwellnesscare +=1
    def keterangan(self) :
        return (f"Perawatan Wellness Care untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class Penitipan(JenisHewan) :
    jumlahpenitipan = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Penitipan.jumlahpenitipan +=1
    def keterangan(self) :
        return (f"Penitipan selama seminggu untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class Grooming(JenisHewan) :
    jumlahgrooming = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Grooming.jumlahgrooming +=1
    def keterangan(self) :
        return (f"Perawatan Grooming untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class Laboratorium(JenisHewan) :
    jumlahlab = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Laboratorium.jumlahlab +=1
    def keterangan(self) :
        return (f"Perawatan Laboratorium untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

class Emergency(JenisHewan) :
    jumlahemergency = 0
    def __init__(self, jenis, ras, harga) :
        super().__init__(jenis,ras)
        self.harga = harga
        Emergency.jumlahemergency +=1
    def keterangan(self) :
        return (f"Perawatan Emergency untuk {self.jenis} dengan ras {self.ras} seharga Rp {self.harga}")

print("\n","-"*5, "Pelayanan Eight Vet Clinic", "-"*5, "\n")
kucing1 = Grooming ('Kucing', 'Anggora', 200000)
kucing2 = Penitipan ('Kucing', 'Persia', 500000)
anjing1 = Vaksinasi ('Anjing', 'Husky', 150000)
kucing3 = Grooming ('Kucing', 'British Short Hair', 200000)
anjing2 = MedicalCare ('Anjing', 'Golden Retriever', 300000)
anjing3 = Grooming ('Anjing', 'Mallamute', 350000)
kucing4 = Penitipan ('Kucing', 'Bengal', 500000)
kucing5 = WellnessCare ('Kucing', 'Himalayan', 300000)


print("-"*50)
print("\n")
print (kucing1.keterangan())
print (kucing2.keterangan())
print (kucing3.keterangan())
print (kucing4.keterangan())
print (kucing5.keterangan())
print (anjing1.keterangan())
print (anjing2.keterangan())
print (anjing3.keterangan())
print("\n")
print("="*50)
print ("Rekap Jumlah Pelayanan Selama Seminggu")
print("="*50)
print ("Grooming\t:", Grooming.jumlahgrooming)
print ("Vaksinasi\t:", Vaksinasi.jumlahvaksinasi)
print ("Surgery\t\t:", Surgery.jumlahsurgery)
print ("Medical Care\t:", MedicalCare.jumlahmedicalcare)
print ("Wellness Care\t:", WellnessCare.jumlahwellnesscare)
print ("Penitipan\t:", Penitipan.jumlahpenitipan)
print ("Pemeriksaan Lab\t:", Laboratorium.jumlahlab)
print ("Emergency\t:", Emergency.jumlahemergency)

import matplotlib.pyplot as plt
import numpy as np
x= ["Grooming", "Vaksinasi", "Surgery", "Medical Care", "Wellness Care", "Penitipan", "Pemeriksaan Lab", "Emergency"]
y = [Grooming.jumlahgrooming, Vaksinasi.jumlahvaksinasi, 
    Surgery.jumlahsurgery, MedicalCare.jumlahmedicalcare, 
    WellnessCare.jumlahwellnesscare, Penitipan.jumlahpenitipan,
    Laboratorium.jumlahlab, Emergency.jumlahemergency]
plt.title("Data Pelayanan Selama Seminggu")

plt.bar(x,y)
plt.show()