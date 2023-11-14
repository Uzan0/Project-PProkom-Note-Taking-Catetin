#Membuat project tentang notepad dari sdgs yang ke 4
import os
note=[]
def new():
    judul_note=input('masukkan judul note: ')
    global catatan
    catatan=input('isi note: ')
    global note_baru
    note_baru=f"{judul_note}:{catatan}"
    note.append(note_baru)

def delete_note():
    index=int(input('masukkan indeks note: '))
    del note[index]

def modify():
    index=int(input('masukkan indeks note: '))
    judul_baru=input('masukkan judul baru? (y/n) ')
    if judul_baru == 'y':
        Judul_new = input('masukkan judul baru: ')
        note_baru=f"{Judul_new}:{catatan}" 
    elif judul_baru == 'n':
        print('okei')
    else :
        print('oke')
    ubah_catatan= input('ubah catatan? (y/n) ')
    if ubah_catatan == 'y':
        teks_baru = input('masukkan teks baru: ')
        note_baru=f"{Judul_new}:{teks_baru}"
        note[index]=note_baru
    elif ubah_catatan == 'n':
        print('baiklah ')
    else:
        print('okei')

def sort_note():
    note.sort()

def show_data ():
    print("[1] A-Z\n[2] Z-A")
    choose = input("masukkan ")
    if choose == "1":
        note.sort()
        for i in range (len(note)):
            print(f"{i+1}. {note[i]}")
    else :
        note.sort(reverse=True)
        for i in range (len(note)):
            print(f"{i+1}. {note[i]}")
        

def menu_note():
    print("=" * 36)
    print('|',"MENU".center(32,'_'),'|')
    print('|',' ' *32 ,'|')
    print('|',"Selamat Datang Di Catetin".center(32,' '),'|')
    print('|',' ' *32 , '|')
    print("=" *36)
    print("[1] Create new note " '(N)') 
    print("[2] Modify Existing Note " '(M)')
    print("[3] Sort Notes " '(S)')
    print("[4] Delete Note " '(D)')
    print("[5] show data " '(L)')
    print("[6] Exit " '(E)')
        
    pilih=input('enter your choice: ')
    if pilih.upper() == 'N':
        os.system('cls')
        new()
    elif pilih.upper() == 'M':
        modify()
    elif pilih.upper() == 'S':
        sort_note()
    elif pilih.upper() == 'D':
        os.system('cls')
        delete_note()
    elif pilih.upper() == "L":
        show_data()
    elif pilih.upper() == 'E':
        exit()
    else:
        print('tidak ada opsi yang sesuai')

lagi='y'
while lagi=='y':
    menu_note()
    # print(note)
    lagi=input('lagi? (y/n): ')

print('selesai')
