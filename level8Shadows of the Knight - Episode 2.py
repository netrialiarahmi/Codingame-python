import sys, math
 
lebar, tinggi = [int(i) for i in input().split()]
input() # jumlah putaran sebelum permainan berakhir tidak digunakan
x_sebelumnya, y_sebelumnya = [int(i) for i in input().split()]
 
# x_sebelumnya dan y_sebelumnya akan digunakan untuk menyimpan posisi sebelumnya
# dan x serta y adalah posisi saat ini
x, y = x_sebelumnya, y_sebelumnya
 
# xs*ys adalah area tempat bom mungkin berada
# pertama-tama kita akan membatasi area tersebut menjadi satu kolom dengan metode dichotomy pada sumbu x
# kemudian menjadi satu jendela dengan metode dichotomy pada sumbu y
kolom_x, jendela_y = range(lebar), range(tinggi)
 
 
def menyempitkan_area(x_sebelumnya, y_sebelumnya, x, y, kolom_x, jendela_y, info):
    print("Menyempitkan area: x_sebelumnya={}, y_sebelumnya={}, x={}, y={}, info={}".format(x_sebelumnya, y_sebelumnya, x, y, info), file=sys.stderr)
    # dichotomy pada sumbu x
    if len(kolom_x) != 1:
        if info == "UNKNOWN":
            pass
        elif info == "SAME":
            kolom_x = [i for i in kolom_x if abs(x_sebelumnya - i) == abs(x - i)]
        elif info == "WARMER":
            kolom_x = [i for i in kolom_x if abs(x_sebelumnya - i) > abs(x - i)]
        else:
            kolom_x = [i for i in kolom_x if abs(x_sebelumnya - i) < abs(x - i)]
    # dichotomy pada sumbu y
    else:
        if info == "UNKNOWN":
            pass
        elif info == "SAME":
            jendela_y = [i for i in jendela_y if abs(y_sebelumnya - i) == abs(y - i)]
        elif info == "WARMER":
            jendela_y = [i for i in jendela_y if abs(y_sebelumnya - i) > abs(y - i)]
        else:
            jendela_y = [i for i in jendela_y if abs(y_sebelumnya - i) < abs(y - i)]
    print(kolom_x, file=sys.stderr)
    print(jendela_y, file=sys.stderr)
    return kolom_x, jendela_y
 
 
while 1:
    info = input()
    # menggunakan informasi untuk menyempitkan area tempat bom mungkin berada
    kolom_x, jendela_y = menyempitkan_area(x_sebelumnya, y_sebelumnya, x, y, kolom_x, jendela_y, info)
    # memilih posisi baru agar memungkinkan untuk membagi area menjadi dua pada giliran selanjutnya
    x_sebelumnya, y_sebelumnya = x, y
    # dichotomy pada sumbu x
    if len(kolom_x) != 1:
        # pembagian dua antara x_sebelumnya dan x harus membagi area menjadi dua sehingga:
        # (x + x_sebelumnya)/2 = (kolom_x[0] + kolom_x[-1])/2
        # trik kecil
        if (x_sebelumnya == 0 and len(kolom_x) != lebar):
            x = (3 * kolom_x[0] + kolom_x[-1]) // 2 - x_sebelumnya
        elif (x_sebelumnya == lebar - 1 and len(kolom_x) != lebar):
            x = (kolom_x[0] + 3 * kolom_x[-1]) // 2 - x_sebelumnya
        else:
            x = kolom_x[0] + kolom_x[-1] - x_sebelumnya
        
        # untuk menghindari titik tetap
        if x == x_sebelumnya:
            x += 1
        x = min(max(x, 0), lebar - 1)
 
    else:
    # transisi ke dichotomy kedua
        if x != kolom_x[0]:
            x = x_sebelumnya = kolom_x[0]
            print(x, y)
            info = input()
        # penyelesaian
        if len(jendela_y) == 1:
            y = jendela_y[0]
        # dichotomy pada sumbu y
        else:
            if (y_sebelumnya == 0 and len(jendela_y) != tinggi):
                y = (3 * jendela_y[0] + jendela_y[-1]) // 2 - y_sebelumnya
            elif (y_sebelumnya == tinggi - 1 and len(jendela_y) != tinggi):
                y = (jendela_y[0] + 3 * jendela_y[-1]) // 2 - y_sebelumnya
            else:
                y = jendela_y[0] + jendela_y[-1] - y_sebelumnya
            y = min(max(y, 0), tinggi - 1)
    
    print(x, y)
