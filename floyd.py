import math

print()
print("Ege Erbilen 160255080")
print()
print("Sonuc:")

boyut = 9

sonsuz = math.inf

matris = [   [0,4,sonsuz,5,sonsuz,sonsuz,2,sonsuz,sonsuz],
             [4,0,sonsuz,sonsuz,sonsuz,3,1,5,sonsuz],
             [sonsuz,sonsuz,0,2,1,3,sonsuz,sonsuz,3],
             [5,sonsuz,2,0,sonsuz,2,1,sonsuz,sonsuz],
             [sonsuz,sonsuz,1,sonsuz,0,sonsuz,sonsuz,1,2],
             [sonsuz,3,3,2,sonsuz,0,sonsuz,2,sonsuz],
             [2,1,sonsuz,1,sonsuz,sonsuz,0,sonsuz,sonsuz],
             [sonsuz,5,sonsuz,sonsuz,1,2,sonsuz,0,1],
             [sonsuz,sonsuz,3,sonsuz,2,sonsuz,sonsuz,1,0],
         ]

uzaklık = list(map(lambda i: list(map(lambda j: j, i)), matris))
for k in range(boyut):
    for i in range(boyut):
        for j in range(boyut):
            uzaklık[i][j] = min(uzaklık[i][j], uzaklık[i][k] + uzaklık[k][j])

satir = ["A","B","C","D","E","F","G","H","S"]
metin = ""
say = 0
print("   A  B  C  D  E  F  G  H  S")

for i in range(boyut):
    for j in range(boyut): 
        if (say == 0):
            metin = satir[i] +"  "  + str(uzaklık[i][j])
            say = say + 1
        elif (say == 8):
            say = 0
            metin =  str(uzaklık[i][j])
        else:
            metin =  str(uzaklık[i][j])
            say = say + 1
            
            
        if(uzaklık[i][j] == sonsuz):
            print("sonsuz", end=" ")
            
        else:
            print(metin, end="  ")
            
    print(" ")


