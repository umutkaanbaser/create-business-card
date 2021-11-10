# kartvizit oluştur | create-business-card
Merhaba arkadaşlar. Bu dökümanda opencv ile yaptığınız projelere fotoraflara yada kameradan aldığınız karelere kişinin bilgilerinin ve fotorafının yer aldığı bir kartvizit ekleyebilirsiniz.

Hello guys. In this document, you can add a business card with the person's information and photo to the projects you do with opencv, to the photos or to the frames you take from the camera.

#Dahil etme | inclusion
*Fonksiyonu kolaylıkda dahil edip kullanabilirsiniz.Kullanmak istediğiniz dosyaya 'from kartvizit import *' yazarak kolayca dahil edilebilir.
*You can easily include and use the function. It can be easily included by typing 'from business card import *' to the file you want to use.
```
from kartvizit import *
```

# Ayarlar ve Argumanlar | Optional keyword arguments
* Ayarlar ve Argumanlara aynı zamanda help(kartvizit_olustur) yada help(create_business_card) yazarakta bakabilirsiniz. 
* 9 Arguman almaktadır.

  Foto=[required] (np.array)(np.uint8)
  Foto: tr-> Kartvizitin üzerine yazılacağı planlanan fotoraftır,karedir.
  Foto: en-> It is a photograph that the square will be written on the business card.

  kisi_foto=[required] (np.array)(np.uint8)
  kisi_foto: tr-> Kartvizit sahibinin fotorafı
  kisi_foto: en-> photo of business card holder

  bilgiler=[required] (list)
  bilgiler: tr-> Kartvizit sahibinin isim soyisim, telefon, adres gibi bilgileridir. en fazla 5 bilgi verilebilir.
  bilgiler: en-> Information such as name, surname, telephone, address of the business card holder. A maximum of 5 information can be given.

  oran=1 (float)
  oran: tr-> Kartvizit boyutu varsayılan olarak 200x300 'dür, oranda varsayılan olarak 1'dir. oranı yükselterek kartvizit boyutunu değiştirebilirsiniz.\n
  oran: en-> The business card size defaults to 200x300, the ratio defaults to 1. You can change the business card size by increasing the ratio.

  ekle=True (boolean)
  ekle: tr-> foto'ya otomatik olarak karvizit belirtilen konuma eklenir ve foto'yu döner.Varsayılan olarak True'dur.
  ekle: en-> The business card is automatically added to the photo at the specified location and return the photo.Default by True

  konum=(50,50) (tuple)
  konum: tr-> foto'da kartvizitin ekleniceği sol üst koşenin konumudur. Varsayılan olarak 50,50 'dir.
  konum: en-> It is the position of the upper left corner where the business card will be added in the photo. Default by (50,50).

  arkaplan=[0,0,0] (list)
  arkaplan: tr-> Kartvizitin arka plan rengi.Varsayılan olarak [0,0,0]
  arkaplan: en-> background color of business card.Default by [0,0,0]

  seffaf=0.7 (float)
  seffaf: tr-> arkaplan'nın seffafık oranı.Varsayılan olarak 0.7'dir
  seffaf: en-> transparency rate of the background.Default by 0.7

  yazi_rengi=(255,255,255) (tuple)
  yazi_rengi: tr-> yazıların rengidir.Varsayılan olarak (255,255,255)'dir
  yazi_rengi: en-> color of text.Default by (255,255,255)
  
  #Kullanim | use
  *Kullanıma ornek_example.py dosyasından da bakabilirsiniz.
 ```
  # O anki kareyi alarak kartvizit ekleyip geri döner.
  frame = kartvizit_olustur(frame,
                            kisi_foto,
                            bilgiler,
                            oran=.7,
                            arkaplan=[15,45,2220],
                            seffaf=0.3,
                             yazi_rengi=(1,1,1))
  ```
