class Daftar:

    flashdisk_32_GB = 80000
    flashdisk_64_GB = 150000
    hardisk_1_TB = 1000000
    UPS_1000W = 500000
    CPU_desktop = 5000000

    namaflashdisk_32_GB = "flashdisk_32_GB"
    namaflashdisk_64_GB = "flashdisk_64_GB"
    namahardisk_1_TB = "hardisk_1_TB"
    namaUPS_1000W = "UPS_1000W"
    namaCPU_desktop = "CPU_desktop"

    def __init__(self, nama , shop, jlm, nama1, shop1, jlm1, nama2 = "", shop2 =0, jlm2=0, nama3 = "", shop3=0, jlm3=0, nama4 = "", shop4=0, jlm4=0):
        self.nama = nama
        self.nama1 = nama1
        self.nama2 = nama2
        self.nama3 = nama3
        self.nama4 = nama4
        self.belanja = shop
        self.jumlah = jlm
        self.belanja1 = shop1
        self.jumlah1 = jlm1
        self.belanja2 = shop2
        self.jumlah2 = jlm2
        self.belanja3 = shop3
        self.jumlah3 = jlm3
        self.belanja4 = shop4
        self.jumlah4 = jlm4

    def cek(self):
        totalpembelian = self.belanja * self.jumlah + self.belanja1 * self.jumlah1 + self.belanja2 * self.jumlah2 + self.belanja3 * self.jumlah3 + self.belanja4 * self.jumlah4
        totalpembelianasli = totalpembelian
        if(totalpembelian < 500000):
            diskon = "Diskon 0 %"
            jumlahdiskon = totalpembelian * 0
            totalpembelian = totalpembelian
            bonus = "-"

        elif(totalpembelian >= 500000 and totalpembelian < 1500000):
            diskon = "Diskon 1 %"
            jumlahdiskon = totalpembelian * 0.01
            totalpembelian = totalpembelian * 0.99
            bonus = "-"

        elif (totalpembelian >= 1500000 and totalpembelian < 5000000):
            diskon = "Diskon 4 %"
            jumlahdiskon = totalpembelian * 0.04
            totalpembelian = totalpembelian * 0.96
            bonus = "-"

        else :
            diskon = "Diskon 10 %"
            jumlahdiskon = totalpembelian * 0.1
            totalpembelian = totalpembelian * 0.9
            if(totalpembelian > 10000000):
                bonus = totalpembelian // 10000000

        return "No \t Nama Barang \t\t Harga \t\t jumlah \t\t jumlah * Harga \n1. \t {} \t {} \t\t {} \t\t\t\t\t {}\n2. \t {} \t {} \t {} \t\t\t\t\t {}\n3. \t {} \t\t {} \t {} \t\t\t\t\t {}\n4. \t {} \t {} \t\t {} \t\t\t\t\t {}\n5. \t {} \t {} \t\t {} \t\t\t\t\t {} \n---------------------------------------------------------------------- + \n \t\t\t\t\t\t\t\t\t Total \t\t\t\t {} \n \t\t\t\t\t {} x \t{}\t\t\t\t {} \n---------------------------------------------------------------------- - \n\t\t\t\t\t\t\t Total dibayar \t\t\t\t{} \n\t\t\t\t\t\t\t\t\t Bonus \t\t\t\t\t{} ".format(self.nama, self.belanja,self.jumlah,self.jumlah*self.belanja,self.nama1, self.belanja1,self.jumlah1,self.jumlah*self.belanja1,self.nama2, self.belanja2,self.jumlah2,self.jumlah2*self.belanja2,self.nama3, self.belanja3,self.jumlah3,self.jumlah3*self.belanja3,self.nama4, self.belanja4,self.jumlah4,self.jumlah4*self.belanja4,totalpembelianasli,diskon,totalpembelianasli, jumlahdiskon,totalpembelian,bonus)

barang1 = Daftar("flashdisk_32_GB",Daftar.flashdisk_32_GB,5,"flashdisk_64_GB",Daftar.flashdisk_64_GB,4,"hardisk_1_TB",Daftar.hardisk_1_TB,2)
# barang2 = Daftar(Daftar.CPU_desktop,1,Daftar.UPS_1000W,1,Daftar.hardisk_1_TB,1)
# barang3 = Daftar(Daftar.CPU_desktop,2,Daftar.flashdisk_32_GB,5,Daftar.hardisk_1_TB,2)
# barang4 = Daftar(Daftar.flashdisk_32_GB,1,Daftar.flashdisk_64_GB,1)
# barang5 = Daftar(Daftar.flashdisk_32_GB,1,Daftar.flashdisk_64_GB,1,Daftar.hardisk_1_TB,1,Daftar.UPS_1000W,1,Daftar.CPU_desktop,1)

print(barang1.cek())