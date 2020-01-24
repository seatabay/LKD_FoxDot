Cheat Sheet

FOXDOT'U BASLATMAK

SuperCollider: FoxDot.start    
Terminal: python -m FoxDot
Player objesi atama: p1 >>
Davul ornegi calma: p1 >> play()
Ses dosyasi calma: p1 >> loop()
Ses dosyasini kolayca calma: p1 >> stretch()
Mikrofon girisi: p1 >> audioin()

PLAYER NITELIKLERI

degree: player objesi icerisindeki notalarin nereden baslayacagini belirtir
root: player objesi icerisindeki notalarin nereden baslayacagini belirtir, ANCAK YARIM TON OLARAK ARTTIRIR.Vereceginiz deger harf de olabilir, orn: root = "C#" gibi. 
Orn: degree = 1 ile root= 2 ayni gorevi gorur.
amp: player objesinin ses siddetini ayarlar.
amplify: amp degerini TimeVar kullanarak belirli araliklarla arttirip azaltabilirsiniz.
Orn: p1 >> pluck([0,1,2], amp = [.5,.8,1])
p1.amplify = var([0,1],4) #Her 4 vurusta bir ses siddetini 0 yapar.

PLAYER EFEKTLERI

pan(): kulaklik ya da hoparlorun sag ve sol cikislari arasinda sesi kesikli olarak dagitir.
spin(): kulaklik ya da hoparlorun sag ve sol cikislari arasinda sesi devamli olarak dagitir.
---
chop(): sesi verilen deger kadar boler, belirli araliklarini susturur.
coarse(): sesi verilen deger kadar boler, belirli araliklari gecikme ile calar.
#Sus kullanarak chop ve coarse uygulanmis sesi eski haline dondurebilirsiniz.
--
reverb(room,mix): ses bir odadaymis gibi duvarlara carparak yankilanir ve geri gelir.
echo(echo,echotime): ses acik alandaymis gibi yankilanir ve sonumlenip gider. echo, tekrarlayan sesin araligidir. echotime, sesin kac defa tekrarlanacagidir.
delay: ana ses gecikmeli olarak calinir.
--
slide(slide,slidedelay): sesin frekansi (1+n)*frekans degerine kaydirilir.
glide(glide,glidedelay): sesin frekansi icine verilen degere esit semitone(yarim ton) kadar asagi yada yukari kaydirilir.
slidefrom(slidefrom,slidedelay): slide ile ayni islemi yapar; ancak hangi degerden itibaren kaydirilacagini siz belirlersiniz.
bend(bend,benddelay): slide ile ayni islemi yapar; ancak kaydirildigin degerden baslangica geri doner.
pshift(): sesin frekansini, icine verilen degere esit semitone(yarim ton) kadar asagi ya da yukari kaydirir.
NOT: pshift ve glide semitone araligiyla calisir. slide, slidefrom ve bend sesin frekansini devamli olarak degistirir!

GRUPLAR

--Grup objeleri ayni anda birden fazla player objesinde degisim yapmak icin mukemmeldir.

Group(b1,a1..): Player objelerini bir gruba atar ve amp, lpf, oct gibi nitelikleri kullanabilirsiniz.
p1.stop(): Player objesini durdurur.
p1.solo(1,0): "1" icin sadece p1 player objesini calar, digerlerini susturur. "0" degerini verirseniz muzik eski haline doner.
p1.only(): .solo() ile ayni islemi yapar; ancak geri donusu yoktur.
Master().: Tum player objelerine ayni anda islem yapilmasini saglar.
    
PRINT

--Synthler
print(sorted(SynthDefs))

--Davul samplelari
print(Samples)

--Player metodlari
print(sorted(Player.get_attributes()))

--Gamlar(scales)
print(Scale.names())

PARANTEZLER

--Davul ornekleri icin:
[]: tek vurusta icindeki tum ornekleri calar
(): her dongude sirasiyla icindeki ornegi calar
{}: her dongude rastgele icindeki ornegi calar

--Notalar icin:
(): tum notalari birlikte calar
[]: tum notalari sirasiyla calar

TimeVar

var([a,b,c],4): 4 vurus a, 4 vurus b, 4 vurus c calar.
linvar([a,b],4): 4 vurus icerisinde a degerinden b'ye lineer olarak artar ve azalir.
sinvar([a,b],4): 4 vurus icerisinde a'dan b'ye sinus dalgasi formunda degisir.
expvar([a,b],4): 4 vurus icerisinde a'dan b'ye eksponansiyel olarak artar.
Pvar([a,b],[d,e],4): 4 vurus [a,b] arasi degisir, 4 vu???????????

PATERNLER

--Aritmetik operatorler
P[](*,-,+,/) : Icindekilerle operatore gore islem yapar

--Paternler arasi islemler
P[] (*,+,**) P[]: Paternlerin ayni indeksteki elemanlarini carpar/toplar
P[] | P[] : Paternleri birlestirir
P[] & P[] : Paternlerin ayni indeksteki elemanlarini beraber calar

--Patern Uretecleri
PRand(lo,hi)/PRand([degerler]): verilen degerler arasi ya da icerisinde rastgele degerler doner.
PxRand(lo,hi)/PxRand([degerler]): verilen degeleri arasi ya da icerisinde rastgele degerler doner, calinan bir deger bir tekrar etmez.
PwRand([degerler],[agirliklar]): verilen her bir degerin calinma olasiligini, agirliklar listesine gore belirler. Orn: PwRand([1,2,3],[1,1,2]) --> "3" notasi, "1,2" notalarina gore 2 kat daha fazla calinir.

--Patern Metodlari

shuffle(n):Asil paterni n defa ekler, eklenen paternlerin elemanlari rastgeledir.
shufflets(n): Asil paterni n defa ekler, eklenen paternlerin elemanlari rastgeledir; ANCAK TUM ELEMANLAR PGROUPS OLARAK ALGILANIR VE BIR ARADA CALINIR.
reverse(): Paterni tersine cevirir.
mirror(): Paterni tersine cevirir; ANCAK ICERISINDE BASKA BIR PATERN VARSA O DA TERSINE CEVRILIR.
pivot(n): n. siradaki elemanin indeksi ayni kalacak sekilde once paterni tersine cevirir, daha sonra n. eleman yerine gelecek sekilde soldan saga kaydirir.
trim(n): baslangictan n. elemandan SONRASINI paternden cikarir.
ltrim(n): sondan n. elemandan ONCESINI paternden cikarir.
duplicate(n): Patern icindeki paternler DAGITILMADAN elemanlar n kadar tekrarlanir.
iter(n): Patern icindeki paternler DAGITILARAK elemanlar n kadar tekrarlanir.
replace((a,b)): Patern icindeki a elemanini b ile degistirir.
submap({a:b,c:d,...}): replace metodunun birden fazla degisken alan halidir.
concat([a,b,c..]): every metodunda "|" operatoru kullanilmaz, bunun yerine concat kullanilabilir. Asil paterne verilen diziyi ekler.
offadd(a,b):Paterne a degerini ekler, asil patern ile zipler ve b gecikmesi ile elde edilen paterni calar.
offmul(a,b):Patern elemani ile a degerini carpar, asil patern ile zipler ve b gecikmesi ile elde edilen paterni calar. 
offlayer(): layer ile ayni gorevi gorur, elde edilen sonuc gecikmeli olarak calar.

--PGroups 
P*(): sure(dur) niteliginin degerinde hepsini esit aralikla calar(davuldaki []in muadili)
P+(): sus niteliginin degerinde hepsini esit aralikla calar
P**(): sure(dur) niteliginin degerinde hepsini esit aralikla, rastgele calar(davuldaki {}+[] gibi)
P/(): sure(dur) niteliginin degerinde hepsini esit aralikla calar ve delay(gecikme) ekler
P^(): sure(dur) ve sus niteliklerinden bagimsiz olarak verilen son deger kadar delay(gecikme) ekler
