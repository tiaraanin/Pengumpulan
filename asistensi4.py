import matplotlib.pyplot as plt

#Class

class Rapor_SD :
    jumlah = 0
    nilai = 0

    lulus = 0
    gagal = 0

    def __init__(self,nama, kelas, nilaisikap, nilaiakhir):
        self.nama = nama
        self.kelas = kelas
        self.sikap = nilaisikap
        self.nilai += nilaiakhir
        Rapor_SD.jumlah +=1

    def Cek_Kelulusan(self) :
        print(f"Nama : {self.nama} \nKelas : {self.kelas} \nNilai Sikap : {self.sikap} \nNilai Akhir : {self.nilai}")

        if self.sikap == 'A' or self.sikap == 'B':
            if self.nilai >= 76 :
                print('Anda dinyatakan lulus')
                Kelas_1.lulus += 1
                
            else:
                print('Anda dinyatakan tidak lulus')
                Kelas_1.gagal += 1
        else:
            print('Anda dinyatakan tidak lulus')
            Kelas_1.gagal += 1    

#Inheritance

class Kelas_1(Rapor_SD):
    jumlah = 0
    def __init__(self, nama, kelas, nilaisikap, nilaiakhir):
        super().__init__(nama,kelas,nilaisikap,nilaiakhir)
        Kelas_1.jumlah += 1

#Override

class Kelas_6(Rapor_SD):
    jumlah = 0
    lulus = 0
    gagal = 0
    def __init__(self,nama,kelas,sikap,nilai,nilaiUN):
        super().__init__(nama,kelas,sikap,nilai)
        self.UN = nilaiUN
        Kelas_6.jumlah += 1

    def Cek_Kelulusan(self):
        print (f"Nama : {self.nama} \nKelas : {self.kelas} \nNilai Sikap : {self.sikap} \nNilai Akhir : {self.nilai} \nNilai UN : {self.UN}")

        if self.sikap == 'A' or self.sikap == 'B':
            if self.UN >= 2.8 :
                if self.nilai >= 76 :
                    print('Anda dinyatakan lulus')
                    Kelas_6.lulus += 1
                else:
                    print('Anda dinyatakan tidak lulus')
                    Kelas_6.gagal += 1
            else:
                print('Anda dinyatakan tidak lulus')
                Kelas_6.gagal += 1
        else:
            print('Anda dinyatakan tidak lulus')
            Kelas_6.gagal += 1


#Data Siswa

print('='*100)
print('    REKAP KELULUSAN SISWA PAK HARDI SDN 0123 MAKMUR JAYA ABADI SEJAHTERA TAHUN AJARAN 2021/2022')
print('='*100)


print('Hasil Kelulusan Kelas I')

print('\n')
Bima = Kelas_1('Bima','1','D',99)
Bima.Cek_Kelulusan()

print('\n')
Aufaa = Kelas_1('Aufaa','1','A',40)
Aufaa.Cek_Kelulusan()

print('\n')
Gian = Kelas_1('Gian','1','D',99)
Gian.Cek_Kelulusan()

print('\n')
Diana = Kelas_1('Diana','1','C',99)
Diana.Cek_Kelulusan()

print('\n')
Mauren = Kelas_1('Mauren','1','B',90)
Mauren.Cek_Kelulusan()

print('\n')
Ujang = Kelas_1('Ujang','1','A',90)
Ujang.Cek_Kelulusan()

print('\n')
Rudi = Kelas_1('Rudi','1','B',90)
Rudi.Cek_Kelulusan()

print('\n')
Asep = Kelas_1 ('Asep','1','A',96)
Asep.Cek_Kelulusan()

print('\n')
Udin = Kelas_1 ('Udin','1','A',75)
Udin.Cek_Kelulusan()

print('\n')
Jaka = Kelas_1 ('Jaka','1','B',89)
Jaka.Cek_Kelulusan()

print('\n')
Rudi = Kelas_1 ('Rudi','1','A',79)
Rudi.Cek_Kelulusan()

print('\n')
Hartono = Kelas_1 ('Hartono','1','B',84)
Hartono.Cek_Kelulusan()

print('\n')
Bambang = Kelas_1 ('Bambang','1','B',78)
Bambang.Cek_Kelulusan()

print('Hasil Kelulusan Kelas VI')

print('\n')
Michael = Kelas_6 ('Michael','6','A',79,3.6)
Michael.Cek_Kelulusan()

print('\n')
Thomas = Kelas_6 ('Thomas','6','A',97,3.7)
Thomas.Cek_Kelulusan()

print('\n')
John= Kelas_6 ('John','6','A',95,3.8)
John.Cek_Kelulusan()

print('\n')
Hardi = Kelas_6 ('Tom Hardy Sasono','6','A',99,4.0)
Hardi.Cek_Kelulusan()

print('\n')
Jeki = Kelas_6 ('Jeki','6','B',93,3.4)
Jeki.Cek_Kelulusan()

print('\n')
Jeri = Kelas_6 ('Jeri','6','B',93,2.7)
Jeri.Cek_Kelulusan()

print('\n')
Jeni = Kelas_6 ('Jeni','6','B',50,3.4)
Jeni.Cek_Kelulusan()
print('\n')

#Rekapitulasi

print('='*50)
print('\t\tREKAPITULASI')
print('='*50)

print('Assalamualaikum Warrahmatullahi Wabarakatuh. \nSalam sejahtera bagi kita semua. \n\n   Bapak, Ibu, dan Wali Murid yang saya hormati, berikut hasil pendidikan anak-anak bapak dan ibu selama belajar di kelas yang saya wali-kan.\n\n   Saya mohon maaf barangkali ada kurang dalam mengajari anak bapak dan ibu, namun saya sudah berusaha sekuat tenaga saya untuk mengupayakan dan memberikan \npendidikan yang terbaik untuk anak bapak dan ibu. \nSaya mengucapkan selamat bagi anak-anak saya yang sudah berhasil lulus dan naik kelas. Pertahankan, dan tingkatkan prestasi kalian. \nBanggakan orangtua kalian, jadikan ini sebagai momen kalian untuk meraih mimpi yang lebih besar di depan sana. \nUntuk anak-anakku yang gagal dan tinggal kelas, tidak apa apa. Belum terlambat untuk memperbaiki semuanya. \nYang penting, jangan pernah menyerah dan teruslah berusaha semaksimal kalian. \nSemoga tahun depan kalian bisa lulus dan naik kelas. Amin Amin Ya Rabbal Alamin')
print('\n')
print('   Mungkin sekian yang dapat saya sampaikan. Berikut rekap hasil dan grafik kelulusan siswa-siswa saya.\n\nIkan hiu kerja paruh waktu \nWassalamualaikum Warrahmatullahi Wabarakatuh')
print('\n')
print(' '*75,'TTD')
print(' '*73,'Wali Kelas')
print(' '*65,'Ir.Hj.Hardi ST., MT.,Ph.D,IPU')

print('*'*15)
print(' Rincian Data')
print('*'*15,'\n')
print('Sebanyak ',Rapor_SD.jumlah,' siswa telah menerima hasil kelulusannya hari ini.')
print('Di jenjang kelas I, sebanyak ',Kelas_1.lulus,' siswa berhasil naik kelas dan sebanyak ',Kelas_1.gagal,' tinggal kelas')
print('Di jenjang kelas VI, sebanyak ',Kelas_6.lulus,' siswa berhasil lulus dan sebanyak ',Kelas_6.gagal,' tinggal kelas')

jumlah_gagal = Kelas_1.gagal + Kelas_6.gagal

jumlah_lulus = Kelas_1.lulus + Kelas_6.lulus

persentase_lulus = ( jumlah_lulus / Rapor_SD.jumlah ) * 100
print (f'\nPersentase kelulusan siswa Pak Hardi pada tahun ajaran 2021/2022 ini adalah sebesar {persentase_lulus} % \nSebanyak {jumlah_lulus} siswa gabungan kelas 1 dan kelas 6 ajaran Pak Hardi dinyatakan lulus \nSebanyak {jumlah_gagal} siswa dinyatakan gagal dan harus mengulang kembali di jenjang kelas yang sama pada tahun ajaran depan.')


x = ["Total Siswa","Lulus",'Gagal']
y = [Rapor_SD.jumlah,jumlah_lulus,jumlah_gagal ]
plt.title("Data Kelulusan Siswa Pak Hardi")

plt.bar(x,y)
plt.show()

