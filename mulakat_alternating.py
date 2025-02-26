# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# Yani çift indekli karakterleri büyük; diğerlerini küçük yazdıracak fonk. yazın diyor.

range(len("miuul"))     #range: girdiğin değere kadar sayı üretir
range(0, 5)
for i in range(len("miuul")):
    print(i)




def alternating(strone):
    new_strone = " "                          #yaptığımız değişiklikleri buraya kaydedeceğimiz yer
    for strone_index in range(len(strone)):   #Girilen string'in indekslerinde gez
        if strone_index % 2 == 0:             #İndeks çift ise büyük harfe çevir ve kaydet
            new_strone += strone[strone_index].upper()
        else:                                 #İndeks tek ise küçük harfe çevir ve kaydet
            new_strone += strone[strone_index].lower()
    print(new_strone)

alternating("miuul")
