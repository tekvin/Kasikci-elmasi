import random

sayi=random.randint(1,1000) #1 ve 1000 arasında rastgele bir sayı üret
isim=str(input("İsminizi giriniz:")) #Kullanıcıdan isim girmesini iste.

#oyunun hikayesini anlat
print("Bugün gazete manşetlerinde Topkapı Sarayı’nda bulunan Kaşıkçı Elması’nın çalındığı ve haberde elması çalan kişinin kaşık şeklindeki elmas yerine yuvarlak bir elmas koyduğu haberi yer almaktadır.")
print(f"Dedektif {isim}, elmasın çalındığı gün Topkapı Sarayı’nı ziyaret eden 1000 kişi içerisinden hırsızı bulacaktır. Dedektif {isim} elinde 1000 ziyaretçinin Kaşıkçı Elması’nın bulunduğu mekana giriş saatine göre sıralanmış isim listesi bulunmaktadır. Dedektif, hırsızdan sonraki  herkesin Kaşıkçı Elması’nın şeklini yuvarlak olarak söyleyeceğine inanmakta ve bu şekilde hırsızı bulmayı planlamaktadır.")
print( f"Dedektif {isim} mümkün olduğunca az kişiyle görüşebilmesi için bir strateji izlemesi gerekmektedir çünkü maksimum 10 deneme şansı vardır.")

# Tahmin sayısını takip etmek için sayaç
tahminsayisi=0

#Oyun döngüsü
while tahminsayisi < 10:
 
 if tahminsayisi==10:
    break
    print("Tahmin sayısını aştınız.Oyun bitti.")
 tahmin=int(input(f"Söyle bakalım dedektif {isim}, Kaşıkçı elmasını kaçıncı ziyaretçi çalmıştır?"))

 if tahmin < 1 or tahmin > 1000:
        print("Lütfen 1 ile 1000 arasında bir sayı giriniz.")
        continue
 
 tahminsayisi+=1
 if tahmin == sayi:
        print(f"Tebrikler dedektif {isim}, doğru tahmin! Elması çalan kişi {sayi}. ziyaretçiydi.")
        break
 
 elif tahmin > sayi :
        print(f"Elmas yuvarlaktı dedektif {isim}, lütfen tekrar deneyin. Tahmin sayısı:{tahminsayisi}")
 
 else :
      print(f"Elmas kaşık şeklindeydi dedektif {isim}, lütfen tekrar deneyin. Tahmin sayısı:{tahminsayisi}")

if tahminsayisi == 10:
    print(f"Tahmin sayısını aştınız. Oyun bitti. Doğru cevap {sayi}. ziyaretçiydi.")