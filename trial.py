# Membuat project tentang notepad dari sdgs yang ke 4
import os
import sqlite3
import pandas as con
import datetime
import time

print()
print("=" * 57)
print('|', ' ' * 53, '|')
print('|', "Selamat Datang Di CATETIN".center(53, ' '), '|')
print('|', ' ' * 53, '|')
print("=" * 57)
print()
time.sleep(2)
os.system('cls')


def loading_screen():
    print()
    print("=" * 57)
    print('|', ' ' * 53, '|')
    print('|', "Loading.....".center(53, ' '), '|')
    print('|', ' ' * 53, '|')
    print("=" * 57)
    print()
    
    for _ in range(5):  
        time.sleep(1)  
    print("\nLoading complete!")
    os.system('cls')


loading_screen()


note = []
def new():
    konfirmasi= input('apakah anda yakin lanjut ke new (y/n)')
    if(konfirmasi == 'y'):
        os.system('cls')
        pass
    elif(konfirmasi == 'n'):
        os.system('cls')
        menu_note()
    else:
        os.system('cls')
        print('anda salah memasukkan pilihan')
        new()
    judul_note = input('Nama Judul Catatan: ')
    global catatan
    global waktu
    waktu = datetime.datetime.now()
    catatan = input('Isi Catatan: ')
    note_baru = f"{judul_note}:{catatan}:{waktu.strftime('%d''/''%m''/''%Y')}"
    note.append(note_baru)
    os.system('cls')


def shownotes():
    global con
    con = sqlite3.connect('dbpath')
    global cur
    cur = con.cursor()
    dataframe = con.read_sql_query("SELECT * FROM catetan", con)

    if dataframe.empty:
        print("No notes found. Create a new note to get started!")
    else:
        showdf = con.read_sql_query("SELECT * FROM catetan", con)
        print(showdf)
        con.commit()
        con.close()


def exportnotes():
    global dataframe
    dataframe = con.DataFrame('notebaru', columns=['Name', 'Content','DateTime'])

    cur.execute("CREATE TABLE IF NOT EXISTS catetan (Name TEXT, Content TEXT, DateTime TEXT)")

    for i in dataframe.itertuples():
        cur.execute("INSERT INTO catetan (Name, Content, DateTime) VALUES (?, ?)", (i.Name, i.Content, i.Datetime))

    con.commit()
    con.close()
    print(dataframe)


def simpan():
    simpan = input("apakah ingin anda save? (y/n):")
    if simpan == 'y':
        pass
        os.system('cls')
        menu_note()
    else :
        del note[len(note)-1]
        os.system('cls')
        menu_note()


def modify():
    konfirmasi= input('apakah anda yakin untuk lanjut ke dalam modify (y/n)')
    if(konfirmasi== 'y'):
        pass
    elif(konfirmasi == 'n'):
        os.system('cls')
        menu_note()
    else :
        print("Anda salah memasukkan ")
        modify()
    if len(note) == 0:
        print("Tidak ada catatan")
        confirm = input('Buat catatan baru atau kembali ke menu? (N/M) : ')
        if(confirm.upper() == "N") :
            os.system('cls')
            new()
            simpan()
        else:
            os.system('cls')
            menu_note()
    else:
        print()
        index = int(input('Masukkan nomor catatan: '))
        while index >= len(note):
            index = int(input('Masukkan nomor catatan: '))
        else:
            os.system('cls')
            pass
            
        print()
        print("[>] Ubah Judul " '(J)')
        print("[>] Ubah Isi Catatan " '(C)')
        print("[>] Delete Catatan " '(D)')
        print("[>] Menu " '(M)')
        print()

        pilih = input('Masukkan pilihan: ')
        print()
        if pilih.upper() == 'J':
            konfirmasi = input('apakah anda yakin lanjut ke ubah judul (y/n)')
            if(konfirmasi== 'y'):
                os.system('cls')
                pass
            elif(konfirmasi == 'n'):
                os.system('cls')
                menu_note()
            else:
                os.system('cls')
                print('anda salah memasukkan pilihan ')
                modify()
            Judul_new = input('Masukkan judul baru : ')
            print()
            confirm = input('Apa kamu yakin mengubah judul? (y/n)')
            if(confirm.lower() == 'y'):
                global judul_anyar
                modstring = note[index].split(':')
                judul = modstring[0]
                memuat = modstring[1]
                judul_anyar = f"{Judul_new}:{memuat}:{waktu.strftime('%d''/''%m''/''%Y')}"
                note[index] = judul_anyar
                os.system('cls')
                menu_note()
            elif(confirm.lower() == 'N'):
                print('Baik')
                os.system('cls')
                menu_note()
            else:
                print('Tidak ada opsi valid')
                os.system('cls')

        elif pilih.upper() == 'C':
            konfirmasi = input('apakah anda yakin lanjut ke ubah catatan? (y/n)')
            if(konfirmasi== 'y'):
                os.system('cls')
                pass
            elif(konfirmasi == 'n'):
                os.system('cls')
                menu_note()
            else:
                os.system('cls')
                print('anda salah memasukkan pilihan ')
                modify()
            teks_baru = input('Masukkan teks baru: ')
            print()
            confirm = input('Apa kamu yakin mengubah catatan? (y/n)')
            if(confirm.lower() == 'y') :
                modstring = note[index].split(':')
                judul = modstring[0]
                memuat = modstring[1]
                catatan_baru = f"{judul}:{teks_baru}:{waktu.strftime('%d''/''%m''/''%Y')}"
                note[index] = catatan_baru
                os.system('cls')
                menu_note()
            elif(confirm.lower() == 'n'):
                print('Baik')
                os.system('cls')
                menu_note()
            else:
                print('Tidak ada opsi valid')
                os.system('cls')
                menu_note()
            
        elif pilih.upper() == 'D':
            confirm = input('Apa kamu yakin menghapus catatan? (y/n)')
            if(confirm.lower() == 'y'):
                del note[index]
                os.system('cls')
                menu_note()
            elif(confirm.lower() == 'n'):
                print('baik')
                os.system('cls')
                menu_note()
            else:
                print('Tidak ada opsi valid')
                os.system('cls')
                menu_note()

        elif pilih.upper() == 'M':
            confirm = input('apa kamu yakin menuju ke menu? (y/n)')
            if(confirm.lower() == 'y'):
                os.system('cls')
                menu_note()
            elif(confirm.lower() == 'n'):
                modify()
            else:
                print('Tidak ada opsi valid')
                modify()


def sort_note():
    konfirmasi = input('apakah anda yakin untuk sort note? (y/n)')
    if(konfirmasi== 'y'):
        os.system('cls')
        pass
    elif(konfirmasi == 'n'):
        os.system('cls')
        menu_note()
    note.sort()
    os.system('cls')
    menu_note()


def show_data():
    if len(note) == 0:
        print('|', "empty".center(53, ' '), '|')
    else:
        print(f"|{f'Nomor':<5}|{f'Judul':^12}|{f'Isi Catetin':^15}|{f'Tanggal':^20}|")
        print("=" *57)
        for i in range(len(note)):
            split = note[i].split(':')
            Judul = split[0]
            memuat = split[1]
            waktu = split[2] 
            print(f"|{f'{i}':<5}|{f'{Judul}':<12}|{f'{memuat}':<15}|{f'{waktu}':<20}|")
    print("=" * 57)


def menu_note():
    print("=" * 57)
    print('|', ' ' * 53, '|')
    print('|', "Catetin".center(53, ' '), '|')
    print('|', ' ' * 53, '|')
    print("=" * 57)
    show_data()
    print()
    print("Choose Menu : ")
    print("Create new note " '(N)')
    print("Modify Existing Note " '(M)')
    print("Sort Notes " '(S)')
    print("Exit " '(E)')
    print()


    pilih = input('Masukkan pilihan : ')
    if pilih.upper() == 'N':
        new()
        simpan()
    elif pilih.upper() == 'M':
        modify()
    elif pilih.upper() == 'S':
        sort_note()
    elif pilih.upper() == 'E':
        val= input('apakah anda yakin ingin keluar? (y/n): ')
        if val=='y':
            exit()
        elif val=='n':
            os.system('cls')
            menu_note()
        else:
            print('tidak ada opsi yang sesuai')
            menu_note()
    else:
        print('tidak ada opsi yang sesuai')



if __name__ == "__main__" :
    menu_note()