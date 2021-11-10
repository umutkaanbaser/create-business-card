# kartvizit oluştur | create business card
Merhaba arkadaşlar. Bu döküman ile opencv ile yaptığınız projelere fotoraflara yada kameradan aldığınız karelere kişinin bilgilerinin ve fotorafının yer aldığı bir kartvizit ekleyebilirsiniz.

Hello guys. In this document, you can add a business card with the person's information and photo to the projects you do with opencv, to the photos or to the frames you take from the camera.

<div style="float:left;">
<img src="https://raw.githubusercontent.com/umutkaanbaser/create-business-card/main/ornek_example_1.jpg" width="350" title="Bill Gates Örnek Kartvizit 1"/>
<img src="https://raw.githubusercontent.com/umutkaanbaser/create-business-card/main/ornek_example_2.jpg" width="350" title="Bill Gates Örnek Kartvizit 2"/>
</div>

# Dahil etme | inclusion
* Fonksiyonu kolaylıkda dahil edip kullanabilirsiniz.Kullanmak istediğiniz dosyaya 'from kartvizit import *' yazarak kolayca dahil edilebilir.
* You can easily include and use the function. It can be easily included by typing 'from business card import *' to the file you want to use.
```
from kartvizit import *
```

# Ayarlar ve Argumanlar | Optional keyword arguments
* Ayarlar ve Argumanlara aynı zamanda help(kartvizit_olustur) yada help(create_business_card) yazarakta bakabilirsiniz. 
* You can also view Settings and Arguments by typing help(create business card) or help(create_business_card).
* 9 Arguman almaktadır.
* It takes 9 arguments.
  <br/><br/>
  **Foto=[required] (np.array)(np.uint8)** <br/>
  Foto: tr-> Kartvizitin üzerine yazılacağı planlanan fotoraftır,karedir.<br/>
  Foto: en-> It is a photograph that the square will be written on the business card.<br/>
  
  **kisi_foto=[required] (np.array)(np.uint8)** <br/>
  kisi_foto: tr-> Kartvizit sahibinin fotorafı<br/>
  kisi_foto: en-> photo of business card holder<br/>

  **bilgiler=[required] (list)** <br/>
  bilgiler: tr-> Kartvizit sahibinin isim soyisim, telefon, adres gibi bilgileridir. en fazla 5 bilgi verilebilir.<br/>
  bilgiler: en-> Information such as name, surname, telephone, address of the business card holder. A maximum of 5 information can be given.<br/>

  **oran=1 (float)** <br/>
  oran: tr-> Kartvizit boyutu varsayılan olarak 200x300 'dür, oranda varsayılan olarak 1'dir. oranı yükselterek kartvizit boyutunu değiştirebilirsiniz.<br/>
  oran: en-> The business card size defaults to 200x300, the ratio defaults to 1. You can change the business card size by increasing the ratio.<br/>

  **ekle=True (boolean)**<br/>
  ekle: tr-> foto'ya otomatik olarak karvizit belirtilen konuma eklenir ve foto'yu döner.Varsayılan olarak True'dur.<br/>
  ekle: en-> The business card is automatically added to the photo at the specified location and return the photo.Default by True<br/>

  **konum=(50,50) (tuple)**<br/>
  konum: tr-> foto'da kartvizitin ekleniceği sol üst koşenin konumudur. Varsayılan olarak 50,50 'dir.<br/>
  konum: en-> It is the position of the upper left corner where the business card will be added in the photo. Default by (50,50).<br/>

  **arkaplan=[0,0,0] (list)**<br/>
  arkaplan: tr-> Kartvizitin arka plan rengi.Varsayılan olarak [0,0,0]<br/>
  arkaplan: en-> background color of business card.Default by [0,0,0]<br/>

  **seffaf=0.7 (float)**<br/>
  seffaf: tr-> arkaplan'nın seffafık oranı.Varsayılan olarak 0.7'dir<br/>
  seffaf: en-> transparency rate of the background.Default by 0.7<br/>

  **yazi_rengi=(255,255,255) (tuple)** </strong><br/>
  yazi_rengi: tr-> yazıların rengidir.Varsayılan olarak (255,255,255)'dir<br/>
  yazi_rengi: en-> color of text.Default by (255,255,255)<br/>
  
# Kullanim | use
  * Kullanıma ornek_example.py dosyasından da bakabilirsiniz.
  * You can also check the usage example_example.py file.
 ```
  # O anki kareyi alarak kartvizit ekleyip geri döner.
  frame = kartvizit_olustur(frame,
                            kisi_foto,
                            bilgiler,
                            oran=.7,
                            arkaplan=[15,45,222],
                            seffaf=0.3,
                            yazi_rengi=(1,1,1))
  ```
