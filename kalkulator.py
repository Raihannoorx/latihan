#membuat kalkulator sederhana

def perkalian (a,b):
    return a*b

def pertambahan (a,b):
    return a+b

def pergurangan (a,b):
    return a-b

def pembagian (a,b) :
    
    if b !=0 :
        return a/b 
    else:
        print("pembagian tidak bisa jika nilai 0")
     

print("---KALKULATOR SEDERHANA---")
print("//////////////////////////")

while True :
    print("1. perkalian")
    print("2. petambahan")
    print("3. pengurangan")
    print("4. pembagian")
    print("5. keluar")
        
    pilihan = input("pilih operasi : 1/2/3/4/5 : ")
    if pilihan == '5' :
            print("anda keluar")
            break
        
    angka1 = float(input("angka pertama: "))
    angka2 = float(input("angka kedua: ")) 
               
    if pilihan == '1' :
        hasil = perkalian(angka1,angka2)
        print("hasilnya adalah" + str(hasil))
            
    elif pilihan == '2' :
        hasil = pertambahan(angka1,angka2)
        print("hasilnya adalah" + str(hasil))
        
    elif pilihan == '3' :
        hasil = pergurangan(angka1,angka2)
        print("hasilnya adalah " + str(hasil))
            
    elif pilihan == '4' :
        hasil = pembagian(angka1,angka2)
        print("hasillnya adalah " + str(hasil))
        
    else:
        print("anda belum memasukan nilai")           