# TIPEDATA

# Integer : angka satuan
dataInt = 10
print("data : ", dataInt, " - Bertipe ", type(dataInt))

# Float : Angka dengan koma
dataFloat = 5.4
print("data : ", dataFloat, " - Bertipe ", type(dataFloat))

# String : Kumpulan karakter
dataString = "adam"
print("data : ", dataString, " - Bertipe ", type(dataString))

# Boolean : data biner true/false
dataBool = False
print("data : ", dataBool, " - Bertipe ", type(dataBool))

# TIPE DATA KHUSUS

# Bilangan kompleks
dataCompleks = complex(4,8)
print("data : ", dataCompleks, " - Bertipe ", type(dataCompleks))

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.8)
print("data : ", data_c_double, " - Bertipe ", type(data_c_double))