import math
nama = []
asal = []
umur = []
TPS = []
jatah = [0]
i=0
low=0
up=0
kuota=0

print("### PROGRAM PENDAFTARAN DPTb ###")
tps=int(input("Masukkan jumlah TPS yang ada : "))
print("Masukkan jumlah DPT per TPS")
for a in range (0,tps):
    tpsnew=int(input("Jumlah DPT ke {} :".format(a+1)))
    TPS.append(tpsnew)
    jatah.append(math.floor(0.02*tpsnew))
    kuota+=jatah[a+1]
print("Jatah surat DPTb : ",kuota)

def menu():
    global pilih
    print("\n Menu\n")
    print("1. Tambah Pemilih\n2. Data Pemilih\n3. Pembagian TPS\n4. Jatah DPTb\n5. Keluar")
    pilih=int(input("Masukkan menu yang dipilih : "))
    if pilih==1:
        pilih1()
    elif pilih==2:
        pilih2()
    elif pilih==3:
        pilih3()
    elif pilih==4:
        pilih4()
    elif pilih==5:
        print("Terimakasih")
    else :
        print("Format masukan salah. Anda dikembalikan ke menu")
        menu()

def ask():
    tanya=str(input("\n Ingin mengisi data lagi? (Y/N)"))
    if (tanya=="N" or tanya=="n"):
        print("Terimakasih. Anda dikembalikan ke Menu")
        menu()
    elif (tanya=="Y" or tanya=="y"):
        pilih1()
    else : 
        print("Format masukan salah")
        ask()

def pilih2():
    global i
    print("\nData Daftar Pemilih Tambahan (DPTb)\n")
    for j in range (i):
        print(j+1,".","Nama : ",nama[j],"\nAlamat Asal : ",asal[j],"","\nUmur : ",umur[j])
        menu()

def pilih1():
    global i
    print("Input Data Pendaftar ke {} : ".format(i+1))
    namanew=str(input("Nama        : "))
    nama.append(namanew)
    asalnew=str(input("Alamat Asal : "))
    asal.append(asalnew)
    umurnew=str(input("Umur        : "))
    umur.append(umurnew)
    i+=1
    ask()

def pilih3():
    global i,tps,jatah,up,low,kuota
    print("Anda memiliki",len(nama),"Data Daftar Pemilih Tambahan (DPTb)")
    for j in range (tps):
        print("\nTPS",j+1)
        low+=jatah[j]
        up+=jatah[j+1]
        if i>up:
            for k in range (low,up):
                print((k+1)-low,".","Nama : ",nama[k],"","Alamat Asal: ",asal[k],"","Umur : ",umur[k])
        else :
            for l in range (low,i):
                print((l+1)-low,".","Nama : ",nama[l],"","Alamat Asal: ",asal[l],"","Umur : ",umur[l])
        if i>kuota :
            print("\nDaftar DPTb yang tidak mendapat TPS")
            for m in range (kuota,i):
                print((m+1)-kuota,".","Nama : ",nama[m],"","Alamat Asal: ",asal[m],"","Umur : ",umur[m])
                print("\nSisa Surat Suara : 0")
        else :
            print("\nDaftar DPTb yang tidak mendapat TPS")
            print("\nSisa Surat Suara : ",kuota-i)

def pilih4():
    global kuota
    print("\nJatah DPTb Setiap TPS\n")
    for a in range (0,tps):
        print("TPS ke {}".format(a+1),jatah[a+1],"suara")
    print("\nTotal Suara : ",kuota)
    menu()

menu()    
            
    
    
        
            
            
        
    