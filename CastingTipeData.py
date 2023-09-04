# CASTING
# Merubah dari satu type data ke tipe data lain
# Tipe data = FldataStr, float, str, bool

# INTEGER
print ("==================INTEGER=================")
dataInt = 78
print("data : ", dataInt, " - Bertipe ", type(dataInt))

# Format [ variabel = tipedata(variabel asal)]
dataFloat = float(dataInt) #Casting Float
dataStr = str(dataInt) #Casting String
dataBool = bool (dataInt) #Akan false jika nilai variabel 0
print("data : ", dataFloat, " - Bertipe ", type(dataFloat))
print("data : ", dataStr, " - Bertipe ", type(dataStr))
print("data : ", dataBool, " - Bertipe ", type(dataBool))

# FLOAT
print ("==================FLOAT====================")
dataFloat = 78.5
print("data : ", dataFloat, " - Bertipe ", type(dataFloat))

dataInt = int(dataFloat) #Casting int
dataStr = str(dataFloat) #Casting String
dataBool = bool (dataFloat) #Akan false jika nilai float variabel 0

print("data : ", dataInt, " - Bertipe ", type(dataInt))
print("data : ", dataStr, " - Bertipe ", type(dataStr))
print("data : ", dataBool, " - Bertipe ", type(dataBool))

# BOOLEAN
print ("==================BOOLEAN====================")
dataBool = True
print("data : ", dataBool, " - Bertipe ", type(dataBool))

dataInt = int(dataBool) #Casting int
dataStr = str(dataBool) #Casting String
dataFloat = float(dataBool) #Akan false jika nilai float variabel 0
print("data : ", dataInt, " - Bertipe ", type(dataInt))
print("data : ", dataStr, " - Bertipe ", type(dataStr))
print("data : ", dataFloat, " - Bertipe ", type(dataFloat))

# BOOLEAN
print ("==================STRING===================")
dataStr = "Adam"
print("data : ", dataStr, " - Bertipe ", type(dataStr))

# dataInt = int(dataStr) #Casting int
dataStr = str(dataStr) #Casting String
# dataFloat = float(dataStr) #Akan false jika nilai float variabel 0
# print("data : ", dataInt, " - Bertipe ", type(dataInt))
print("data : ", dataStr, " - Bertipe ", type(dataStr))
# print("data : ", dataFloat, " - Bertipe ", type(dataFloat))