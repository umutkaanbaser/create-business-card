import cv2
import numpy as np

def kartvizit_olustur(foto,kisi_foto,bilgiler,oran=1,ekle=True,konum=(50,50),arkaplan=[0,0,0],seffaf=0.3,yazi_rengi=(255,255,255)):
    """
kartvizit_olustur fonksiyonu bir fotorafa kişinin kartvizitini ekler yada kartvizit oluşturup döndürür.
The create business card function adds a contact's business card to a photo or creates and returns a business card.

Argumanlar ve ayarlar | Optional keyword arguments:
---------------------------------------------------
Foto: tr-> Kartvizitin üzerine yazılacağı planlanan fotoraftır,karedir.
Foto: en-> It is a photograph that the square will be written on the business card.

kisi_foto: tr-> Kartvizit sahibinin fotorafı
kisi_foto: en-> photo of business card holder

bilgiler: tr-> Kartvizit sahibinin isim soyisim, telefon, adres gibi bilgileridir. en fazla 5 bilgi verilebilir.
bilgiler: en-> Information such as name, surname, telephone, address of the business card holder. A maximum of 5 information can be given.

oran: tr-> Kartvizit boyutu varsayılan olarak 200x300 'dür, oranda varsayılan olarak 1'dir. oranı yükselterek kartvizit boyutunu değiştirebilirsiniz.
oran: en-> The business card size defaults to 200x300, the ratio defaults to 1. You can change the business card size by increasing the ratio.

ekle: tr-> foto'ya otomatik olarak karvizit belirtilen konuma eklenir ve foto'yu döner.
ekle: en-> The business card is automatically added to the photo at the specified location and return the photo.

konum: tr-> foto'da kartvizitin ekleniceği sol üst koşenin konumudur. Varsayılan olarak 50,50 'dir.
konum: en-> It is the position of the upper left corner where the business card will be added in the photo. By default it is 50.50.

arkaplan: tr-> Kartvizitin arka plan rengi
arkaplan: en-> background color of business card

seffaf: tr-> arkaplan'nın seffafık oranı
seffaf: en-> transparency rate of the background.

yazi_rengi: tr-> yazıların rengidir.
yazi_rengi: en-> color of text
    """
    if(yazi_rengi == (0,0,0)):
        yazi_rengi=(1,1,1)
    H,W = foto.shape[:2]
    kisi_resim =kisi_foto.copy() 
    resim = foto.copy()
    k_x,k_y=konum
    h,w=200*oran,300*oran
    h,w = int(h),int(w)
    kisi_h,kisi_w=int(100*oran),int(100*oran)
    kisi_xmin = 0+int(w/12)
    kisi_xmax = kisi_w+int(w/12)

    kisi_ymin = 0+int(h/4)
    kisi_ymax = kisi_h+int(h/4)
    
    karvizit = np.zeros((h,w,3),dtype=np.uint8)
    arka_plan = karvizit+arkaplan
    kisi_resim = cv2.resize(kisi_resim,(kisi_h,kisi_w))
    karvizit[kisi_ymin:kisi_ymax,kisi_xmin:kisi_xmax]=kisi_resim
    
    cv2.line(karvizit,(0,0),(0,w-2),(0,255,0),1)
    cv2.line(karvizit,(0,0),(w-2,0),(0,255,0),1)
    cv2.line(karvizit,(0,h-2),(w-2,h-2),(0,255,0),1)
    cv2.line(karvizit,(w-2,0),(w-2,w-2),(0,255,0),1)


    bilgi_sayisi=len(bilgiler)
    if(bilgi_sayisi==1):
        nx_basla = int(w/2)
        ny_basla = int(h/2)
        yazi_boy = 0.5*oran
        bilgi = bilgiler[0]
        boy = len(bilgi)
        if(boy>13):
            bilgi=bilgi[:12]
            bilgi+="."
        else:
            ekle = 13-boy
            ekle = int(ekle/2)
            bilgi= " "*ekle+bilgi+" "*ekle
        cv2.putText(karvizit,bilgi,(nx_basla,ny_basla),cv2.FONT_HERSHEY_COMPLEX,yazi_boy,yazi_rengi)
    elif(bilgi_sayisi<=5):
        ham_basla = 170-(170-170*(bilgi_sayisi/5))*0.5
        ny_basla= h-int(ham_basla*oran)
        ny_bit = int(h-ny_basla)
        ara_oran=int((ny_bit-ny_basla)/(bilgi_sayisi-1))
        nx_basla = int(w/2)
        yazi_boy = 0.5*oran
        for i,bilgi in enumerate(bilgiler):
            boy = len(bilgi)
            if(boy>13):
                bilgi=bilgi[:12]
                bilgi+="."
            else:
                ekle = 13-boy
                ekle = int(ekle/2)
                bilgi= " "*ekle+bilgi+" "*ekle
            cv2.putText(karvizit,bilgi,(nx_basla,ny_basla+i*ara_oran),cv2.FONT_HERSHEY_COMPLEX,yazi_boy,yazi_rengi)
    elif(bilgi_sayisi>5):
        raise Exception("En fazla 5 adet bilgi verebilirsin!")
    else:
        raise Exception("lütfen dolu bir liste veriniz")

    
    kesim = resim[k_y:h+k_y,k_x:w+k_x].copy()
    kesim = kesim*seffaf+arka_plan*(1-seffaf)
    kesim = kesim.astype(np.uint8)
    karvizit[karvizit==0] = kesim[karvizit==0]

    if(ekle):
        resim[k_y:h+k_y,k_x:w+k_x]=karvizit
        return resim
    else:
        return karvizit

create_business_card = kartvizit_olustur


