class Pekerja:
    def __init__(self, name, gaji):
        self.name = name
        self.gaji = gaji
    def naikgaji(self, nilai):
        self.gaji += nilai

class Manager(Pekerja):
    def __init__(self, name, gaji=70000):
        Pekerja.__init__(self, name, gaji)
    def naikgaji(self, nilai, bonus=0.1):
        nilaiupdt = nilai + nilai * bonus
        Pekerja.naikgaji(self, nilaiupdt)
    def display(self):
        return f'''
        Nama = {self.name}
        Jabatan = Manager
        Gaji = {self.gaji}
        '''

class Supervisor(Pekerja):
    def __init__(self, name, gaji=50000):
        Pekerja.__init__(self, name, gaji)
    def naikgaji(self, nilai, bonus=0.05):
        nilaiupdt = nilai + nilai * bonus
        Pekerja.naikgaji(self, nilaiupdt)
    def display(self):
        return f'''
        Nama = {self.name}
        Jabatan = Supervisor
        Gaji = {self.gaji}
        '''

spvs = Supervisor("Dimas", 40000)
print(spvs.display())
spvs.naikgaji(3000)
print(spvs.display())

mngr = Manager("Adiknya Dimas")
print(mngr.display())
mngr.naikgaji(30000, 0.3)
print(mngr.display())
