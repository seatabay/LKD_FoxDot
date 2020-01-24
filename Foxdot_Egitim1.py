## FoxDot'a Giris Egitimi ##

'Merhaba! FoxDot egitimine hosgeldiniz. Bu calisma dosyalari, FoxDota giris icin hazirlanmistir.'

'FoxDot, genel olarak bir Python kutuphanesidir, SuperColliderin etkili ses sentezleme mekanizmasi ile haberleserek canli muzik kodlama deneyimi sunmaktadir.Bu calisma dosyasinin yetersiz kaldigi ya da daha fazla bilgiye erismek istediginiz noktada, her yazilim dilinde oldugu gibi dokumantasyona erisebilirsiniz! FoxDotun resmi websitesi:
https://foxdot.org 
Bu dokumantasyon boyunca detayli bir sekilde basitten zora dogru FoxDot kutuphanesinin tum yonlerini ele alacagiz. Eger takildiginiz, cevabini deneyerek bulamadiginiz veya kafa karisikligi yasadiginiz noktalar olursa diger FoxDot kullanicilari ile iletisime gecebileceginiz bir adet forum bulunmaktadir:
https://forum.toplap.org/c/communities/foxdot 

Hadi baslayalim!'

"""1. BOLUM: TEMEL BILGILER"""

"Gozumuzun onune bir adet gitar, piyano ya da benzeri bir enstruman getirelim. Fiziksel dunyada ses yaratmaya yaran bu aletler, dogaldir. Simdi en sevdiginiz enstrumantel parcalardan birini kafanizin icinde calin! Hangi enstruman caliyor? Piyano, gitar, keman, davul... Bu enstrumanlari ayirt etmemizi saglayan sesin bir ozelligi vardir: tini(timbre). Synthesizer, dogada bulunmayan sesleri yaratmamizi saglayan bir donanim/yazilimdir. Yarattigi sese ise #synth demekteyiz. O zaman FoxDot'ta synthleri nasil yaratacagimiza bir bakalim:"

print(sorted(SynthDefs))

"Listelenmis synthler, FoxDot'ta kullanabileceginiz synthlerdir. Peki bu synthi nasil kullaniriz?"

p1 >> gong()

"Duydugunuz ses, C notasidir. Durdurmak icin ise bunu FoxDot'a soylememiz gerekiyor:"

p1 >> gong().stop()

'Evet, sectigimiz enstruman gongdan sonra .stop() yazarak synthi durdurabiliriz. p1 ve >> komutlari, FoxDota emir vermemiz icin gerekli komutlard?r. p1(x1,z1,c2.. de yazabilirsiniz) PLAYER olarak adlandirilan bir objedir. PLAYER objesini yazdiktan sonra, aktive etmek icin >> oklarini kullanmamiz gerekmektedir. Bu oklar tipki + gibi bir operasyon belirtmektedir.'

'Eger player objesinden sonra .stop() yazmak istemezseniz: p1.stop() yazarak da FoxDota susmani gerektigini belirtebilirsiniz.'

p1.stop()

'Buraya kadar enstruman secmeyi, player objesi ve aktive etmeyi ogrendik. Surekli C notasi duymaktan bunalmis olabilirsiniz, peki enstrumanimizin istedigimiz notalari calmasini nasil saglayabiliriz?'

p1 >> gong(1)

p1.stop()

##TIP0: p1,l2,d3.. seklinde degil de kendinizin isimlendirdigi bir oynatici objesi ismi kullanmak isteyebilirsiniz:

## bass1 = Player("bar")
## bass >> ...


'Simdi duydugunuz nota, D(Re) notasidir.FoxDot, enstrumandan sonra nota belirtmediginiz surece C notasi ile baslamaktadir(Scale ve root konularina geldigimizde bunun nasil degistigini gorecegiz.)
0 = C, 1 = D, 2 = E, 3 = F, 4 = G, 5 = A, 6 = B olarak atanmistir.
Peki Eb ya da G# calmak icin ne yapmali?

Eb --> 1.5
G# --> 4.5

FoxDot, ses sentezlerken frekanslar ile calismaktadir. Ornegin, Piyanonun tam ortas?nda bulunan La tu?u, 440 Hzdir(Telefon ederken de duydugunuz biiip sesi, 440 Hzlik LA notasina esittir!). Eger yarim perde inceltmek ya da kalinlastirmak isterseniz 1/2=0.5 ekleyip cikararak elde edebilirsiniz. Dilerseniz 1.2,1.3,1.4.. yazarak atanmis frekanslari dinleyebilirsiniz.

Simdi asagidaki player objesini calistirmayi deneyelim!

p1 >> gong(1,2)

'Hmmm... FoxDot hata veriyor. Neden acaba? gong objesi malesef 1den fazla arguman alamiyor. Peki biz ayni anda ya da sirasiyla farkli notalari nasil calacagiz?'

p1 >> blip([0,1,2,3])

p1.stop()

'FoxDotta enstrumani ayni anda(akor) ya da farkli sekilde calabilmek icin, enstrumanin icerisinde farkli parantezler kullanmak gerekiyor. '

'[] --> soldan saga dogru sirasiyla belirttiginiz notalari calar.'
'() --> belirttiginiz notalari, ayni anda calar.'

p1 >> blip((0,3,5))
 
p1.stop()

p2 >> blip([0,3,5])

p2.stop()


""" Notalari tekli ya da akor olarak calabiliyoruz... Ancak her bir notanin suresini(duration) nasil belirleyebiliriz?"""

p1 >> blip([0,3,5], dur = 1/2)

p1 >> blip([0,3,5], dur = [1/2,1/2,1])

p1.stop()

'ilk player objesinde dur = 1/2, tum notalara uygunlanmaktadir. Eger her bir notanin suresini belirlemek isterseniz, yine koseli parantez kullanarak bunu yapabilirsiniz. Her nota, dur argumani icerisinde yazan deger ile eslestirilmektedir.'

p1 >> blip([0,1,2], dur = [1/2,1/2,1])

p1.stop()

#TIP1: Calmak istemediginiz bir nota olursa rest(dur=..) kullanabilirsiniz.
#Ust Duzey TIP: Calmak istemediginiz notalari yazmanin baska bir yolu daha vardir: amp=[p1.degree==1,p1.degree==2] gibi.Bunu ayni zamanda calmak istediginiz tek bir nota icin de kullanabilirsiniz!

p1 >> gong([1,2,3], amp=[p1.degree ==3,p1.degree == 2],dur=.5)

p1.stop()

'Nota sayisindan daha az sure(duration) degeri verdigimizde, dur listesi tekrar basa doner ve bir sonraki notaya o sureyi uygular.'

'Davul ornekleri calabilmek ya da belirli ses ornekleri calabilmek icin bu ise uygun bir enstruman bulunmaktadir: play.'

print(Samples)

d1 >> play("x-o-")

d1.stop()

"""Bir davul seti hayal edelim. Kick, trampet, zil ve bircok ekipman bir arada bulunmaktadir. FoxDot'ta bu ekipmanlar klavyedeki bir karaktere atanmistir. Ornegin:'

'x --> kick'
'- --> hi-hat'
'o --> snare(trampet)'
'* --> clap'

"Bu orneklerin hepsini gorebilmek icin yukaridaki print fonksiyonunu calistirabilirsiniz."

#TIP2: play objesinin icerisinde yer alan cift tirnak isareti space(bosluk) duyarlidir - samplelarin suresi(dur) ise default olarak 1/2dir.

d1 >> play("x-o-")

d1.stop()

d2 >> play("[----]", sample = 2, dur = 1, bpm = 60)

d2.stop()

'Ses ornekleri, FoxDot icerisinde bir dosyada saklanmaktadir. Bakmak isterseniz Help&Settings --> Open Sample Foldersa tiklayabilirsiniz. Davul orneklerini degistirebilmek icin play objesinin icerisine sample=1,2,3... yazabilirsiniz.Peki dur anahtar argumaninda oldugu gibi sample anahtar argumanina birden fazla deger verirsek ne olur?'

d1 >> play("----", sample = [0,1,2,3], bpm = 60)

d1 >> play("----", sample = 2, dur = [1/2,1/2,1/4,1/4])

d1.stop()

"""Davul paternlerine biraz cesitlilik katmak icin tipki notalarda oldugu gibi parantezleri kullanabiliriz: """

d1 >> play("x-o[--]", bpm = 60)

d1 >> play("x-o(-o)", bpm = 60)

d1 >> play("x-o{-o*}", bpm = 60)

d1.stop()


#TIP2: bpm(beat per minute)'i azaltarak davul paterninde nelerin degistigini daha rahat duyabilirsiniz (eger ritim duyarsizi olaniniz var ise, guzel bir cozum!)


'Her bir parantez, farkli bir gorevi yerine getirmektedir.

'[ ] ---> Tek surede(dur), icerisinde yer alan butun ornekleri calar.'
'( ) ---> Her seferinde, sirasiyla, icerisinde yer alan ornegi parantez disindaki paterne ekler.'
'{ } ---> Her patern bitisinde, rastgele icerisinde yer alan ornegi ekler.'

'Bu parantezleri kullanarak degisik davul paternleri elde edebilirsiniz!'

d1 >> play("x-o(*[--])", bpm = 60)

d1.stop()

d2 >> play("x-o(-[-(-o)])", bpm =60)

d2.stop()

'd1,d2,d3... seklinde farkli playlerlara atayarak davul paternleri olusturmak istemeyebilirsiniz. Bunun icin kullanabileceginiz bir operator bulunmaktadir: <   >'

d1 >> play("<[-x]><x-o->", sample = 3, bpm = 120)

d2 >> play("[---]",sample=[1,2,3], bpm=40)

#TIP 3: [] parantez kullandiginizda uygulayacaginiz dur,sample vb. nitelikler tek bir elemana uygulanir gibi uygulanir.

d2 >> play("<xsss><-([ii])>", sample = 4)

d2.stop()

##TIP 4: sample dizisi uygulanirken kafaniz karisiyorsa,|x2| seklinde oynatici objesi icerisine yazabilir ve direk olarak sample numarasini belirtebilirsiniz.
##Ust Duzey TIP 4: sample=(d1.degree=="x") ile tek tek xleri || dedigimiz delimiter ile ayarlamaniza gerek kalmaz.

d1 >> play("XxXx", sample = (d1.degree=="x"))

d1.stop()

##### ALISTIRMA: herhangi bir synth ve sevdiginiz bir davul paterni yazarak mini capta bir parcacik yapin!

"""2. BOLUM: PLAYER NITELIKLERI"""

'Buraya kadar FoxDotun en temel ozelliklerini gorduk. Nasil enstruman sececegimizi, davul paternlerini nasil olusturabilecegimizi biliyoruz, ancak biraz daha cesnilendirmek istersek ne yapmaliyiz?'

print(sorted(Player.get_attributes()))

'Listede karsimiza cikan bir cok ozellik var! Temel olarak sesimizi manipule etmek istiyorsak oktavini, siddetini, suresini degistirebiliriz. Ancak efekt ekleyerek daha kendine has bir synth elde etmek icin, listede yer alan anahtar argumanlar da kullanilabilir.'

'Attributes(Nitelikler): degree,oct,dur,scale,amp,amplify,bpm,sample,delay.'

p1 >> gong([0,0,0], dur =1 , oct = [3,4,5])

p1.stop()

p2 >> gong(0)

p2.degree = [0,1,2,3]

p2.dur = 1/2

p2.stop()

#TIP4: degree, notanin derecesini belirtir. root ise yarim ton olarak artar. degree=1, D notasiyken root=1 C#a denk gelir.
#TIP5: degree, player objesi icerisinde kullanilamaz.

p1 >> pluck([0],root=[0,2,4,5])
p2 >> pluck(0)
p2.degree = [0,1,2,3]

'Buraya kadar dur, bpm, sample ozelliklerini gorduk. Yukaridaki kodda gong enstrumanini alip, derecesini ve notalarin surelerini degistirdik. Ancak organize bir ses toplulugu olan muzik, sesin siddeti(loudness) degistirilmeden olabilir mi?'

'Hayir. Bu sebepten player objesi icerisinde sesin siddetini ayarlayabilmek icin iki farkl? ozelligimiz bulunmakta: amp ve amplify.'

p1 >> blip([1,2,3,4], amp = .5)

p1.stop()

#TIP6: amp metodunu kullanirken dikkatli olmak gerek! Genellikle 0 ile 1 arasinda secilen bu degeri 1'in ustunde verdiginizde kulakliklarinizi ve kulaklarinizi hasara ugratabilirsiniz!

'amp metodu yeterli gibi duruyor, peki o zaman amplify metodu neden var? ileriki bolumde gorecegimiz TimeVar objesi, verilen degerler ile zaman icerisinde muzigin ozelliklerini kontrol etmemizi saglamaktadir. Es zamanli muzik yaparken, ayni anda tum ozellikleri degistiremeyiz; bu yuzden onceden komut vererek istedigimiz zaman istedigimiz ozelligin degismesini saglayabiliriz! amplify metodu ise TimeVar kullanarak player objesinin siddetini zamanla degistirmemizi saglamaktadir. Nasil mi?'

p1 >> sinepad([0,4,5,2], amp =[0.5,1])
d1 >> play("x ")

p1.amplify = var([1,2],4)

p1.stop()

'Bir de delay niteligine bakalim. Delay, elektronik muzikte sikca kullanilan efektlerden biridir. Aslinda notanin caldiktan sonra belirlenen gecikme ile tekrar calinmasi olan delay, FoxDotta denk gelen notanin verilen deger kadar daha gec calinmasini saglamaktadir. root ise player objesi icerisinde gami degistirmeye yarayan bir metoddur.'

Clock.bpm  = 70

p1 >> sinepad([0,1,2], delay = [0,0,0.5])
d1 >> play("x ")

Group(p1,d1).stop()

'Player objesi icerisinde gami degistirmek istemezseniz, bunu kod icerisinde ya da player icerisinde de yapabileceginiz baska bir yontem daha bulunmaktadir: scale.'

print(Scale.names())

p1 >> blip([0,1,2,3,4,5,6])
#major gam

p2 >> blip([0,1,2,3,4,5,6], scale = Scale.minor)
#minor gam

#TIP7: Eger tum player objelerine uygulamak isterseniz Scale.default = "minor" seklinde de yazabilirsiniz.

#AlISTIRMA: 1. bolumde yaptiginiz mini parcaya oct, amplify veya scale gibi player nitelikleri kullanarak manipule edin!


"UFAK BIR PARCACIK"

Scale.default = "minor"

Clock.bpm = 120

#Basir bir vurmali ile baslayalim
d1 >> play("x x x [xx] ")

#Basimizi ekleyelim

b1 >> sawbass([0,-1,[3.5,2]], dur = [2,2,4],start=1)

#vurmalilara cesni

d2 >> play(" - -")

#birazcik da synth ekleyelim

p1 >> swell(b1.pitch + ([0,2],5))

p1 >> swell(b1.pitch + ([0,2],5), oct=[5,5,6,6])

p1 >> swell(b1.pitch + ([0,2],[5,7]), dur = [1/2,1/2,1/4,1])

d2 >> play(" -|n3|-")

b1.amplify = p1.amplify = 1

Group(d_all).solo(0)

d4 >> play("[---]")

Clock.clear()

""" 3. BOLUM: PLAYER EFEKTLERI """

"""Sesi manipule etmenin en guzel yollarindan biri, efekt eklemektir. Akustik elemanlardan olusan bir grubu canli dinlediginizde, efektler mekanin akustik ozellikleri ve muzisyenlerin performans sirasindaki kullandiklari teknik, ekipman vb. ozellikler tarafindan belirlemektedir. Bunu dijital ortamda yapabilmek efektler ile mumkundur."""

print(Player.get_attributes())


""" Listede bulunan efektler, FoxDot icerisinde kullanabileceginiz efektlerdir. Kisaca bu efektleri aciklayabiliriz:


#Sustain: Notalarin herbirinin kac vurus uzatilacagini belirler, piyanodaki sustain pedaliyla ayni islevi gormektedir.

#Stereo Panning: Sesin cikis yaptigi birden fazla kanal olabilir. FoxDot, su an icin en fazla iki kanaldan cikis vermektedir: sesin iki kanal arasinda gidip gelebilmesi icin bu efekti kullanabilirsiniz.

#Frequency Modifier: Cikis kanallarindan birinde, digerine gore frekans degistirmek icin kullanilir. Ornegin, sadece la notasi caliyorsunuz. Iki kanalda da 440 Hzlik bir frekans duyacaksinizdir. Ancak birinde degisiklik yapmak isterseniz, diyelim ki fmod = 10 Hz, kanalin birinde duyacaginiz frekans 450 Hz olacaktir. Bu efekt, atonal bir ses saglamaktadir.

#Vibrato: Ses perdesini devamli olarak module etmeye yarar.

#Slide: Notanin frekansini zaman icerisinde kaydirmaktadir. Eger bu efekti gecikmeli uygulamak isterseniz slidelay degiskenine parametre atayarak yapabilirsiniz. Slide efektinin hangi frekanstan basladigini belirlemek isterseniz slidefrom ile de bunu gerceklestirebilirsiniz.

#Pitch bend: Notanin frekansini zaman ile degistiren bu efekt, slidedan farkli olarak baslanan frekansa nota suresi sonunda geri doner.

"Buraya kadar belirli efektleri aciklanmis bulunduk, daha fazlasini ogrenmek icin dokumantasyona bakabilir ve bu bolum sonunda istenilen alistirma ile deneyebilirsiniz."""

'Efektleri birlestirince ne yapabilecegimize bir goz atalim.'

b1 >> jbass()

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)])

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)], fmod = [-3,3])

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)], fmod = [-3,3], sus = 2, blur = var([1,2],16))

b1.stop()

#lpf: alcak geciren filtre. degerin altindaki frekanslari gecirir.

p1 >> pads([0,2,4,5])

p1.lpf = [100,200]

#hpf: yuksek geciren filtre. degerin ustundeki frekanslari gecirir.

p1 >> pads([0,2,4,5])

p1.hpf = [1000,1200]

#vibrato: sesin frekansini module edersiniz.

b2 >> blip([1,2,3,4],oct=4, dur = 4)

b2 >> blip(vib=1,vibdepth=[0,.1,.2,.3,.8])

b2.stop()

#slide: argumanin degeri n olsun, frekans (n+1) ile carpilir: ornegin 0 verirseniz frekans sifira gider. ((n+1)*f)

b3 >> pluck(1,dur=4,slide=[-1,1])

b3.stop()

b4 >> pluck(dur=4,slide = [-1,1],slidedelay=1/4) #Baslangici 1 beat geciktirir.
d1 >> play("x ")

b4.stop()

#slidefrom: slidein baslangic noktasini secersiniz; (1+n)*freq degerinden nota degerinize kayar.

b5 >> blip(2,dur=4, slidefrom=[-1,0,1,2,3])

b5.stop()

#pitch bend: slide ile aynidir ancak basladigi frekansa geri doner.

b6 >> pluck(dur=4, bend=[1,2,3],oct=5)

b6.stop()

#chop: ses sinyali arguman degeri kadar bolunur ve mute a alinir.

p1 >> play("2",dur=5)

p1 >> play("2",dur=5, chop=16)

p1 >> play("2", dur=5,chop=16,sus=32)

p1.stop()

#coarse: chop ile aynidir ancak bolunen parcalari sessize almak yerine bolumleri gecikme ile ekler.

p2 >> play("2", dur=8, coarse=16)

p2 >> play("2", dur = 8, coarse=16, sus=32) # sus, bosluklari doldurur.

p2.stop()

#echo: delayden farki, gecikmeler acik bir alandaki balon gibi giderek gozden(kulaktan) kaybolur.

p3 >> keys(dur=8,echo=[.125,.25,.5,1,2,4]) #.125,.25,.5,1.. seklinde vurus(beat) araligiyla delay verilir.

p3.stop()

p3 >> keys(dur=8, echo=.5, echotime=4) #echotime echo sayisini arttirir.

#pan:cikis olarak iki kanal kullanan FoxDotta sesi sag/sol cikislara dagitmak icin kullanilir.

p4 >> pads(dur=4,pan=-1)
p5 >> keys(dur=4,pan=1)

p4.stop()

#spin: pan efektiyle ayni prensipte calisir, ancak sag-sol cikislara dagitim surekli halde olur.

p5 >> pads([0,1],dur=4, spin=4) #sag-sol cikislara 4er defa yayar

p5 >> pads([0,1],dur=4, sus=[1,2], spin=4) #sus degeri spin efekti icin beat gorevi gorur

p5.stop()

#cut: sus efektinin tam karsitidir.

p6 >> pads(dur=2, cut=var([.1,.5,1,2],2))

p6 >> play("<x-o-><-x>",sample=3, cut=var([.1,1],2))

p_all.stop()

#formant: 1 ile 7 arasinda deger alir ve sese rezonans ekler.

p6 >> pads(formant=P[:7],oct=5)

p6.stop()

#tremolo: sesin siddetini bir sinus dalgasiyla sekillendirir. bir vurusta verilen deger kadar module eder.

p7 >> pads(dur=4,tremolo=[0,1,2,3,4])

p7.stop()

#pshift: verilen deger kadar yarim perde yukari ya da asagi ceker.

p8 >> pads(0,pshift = [0,2,4,5])

p9 >> pads([0,1,2,3])

p_all.stop()

#glide: slide gibi frekansi arttirir ama icerisine verdiginiz degerler yarim perdeye denk gelir. slide daha devamlidir.

p0 >> pads(8, dur=4, glide=[4,-4],oct=4)

p0.stop()

##ALISTIRMA: En cok size uygun goldugunuz bir synth ile efektleri deneyin. Farkli efektlerin tek basina ve birlikte nasil bir manipulasyon gucune sahip oldugunu gorun. Boylece size en uygun sesi yakalabilirsiniz. Ornegin, klank synthi ile sustain ve blur efektleri birlikte sesin siddetini amp ya da amplify olmadan arttirabiliyor. Bunun gibi degisik gozlemler yapabilirsiniz!

## 1. Synthini bul. 2. Efekt listesinden lpf, chop, fmod gibi efektleri dene. 3. Deneyerek bu efektlerin nasil degisim yarattigini gozlemle.


"""BOLUM 4: PLAYER KEYS"""

#reset
p1 >> pads([4,5,3,0],dur=2, tremolo=2)

p1.reset()

#solo-only

p1 >> bass([0,4,5,3],dur = 4,amp=.7)

p2 >> swell(p1.pitch[0], cut=.5, spin = 16)

p3 >> gong(p1.pitch, cut = p2.cut)

p1.solo(0)

p1.only()

p_all.stop()

#every

p1 >> keys([0,2,4,6,5]).every(1,"stutter",3)

p2 >> keys([0,2,4,5,6]).every(1,"stutter",3).every(5,"reverse")

#never

p2.never("reverse")

#TIP8: everyi durdurmak icin icindekini silerseniz ise yaramayabilir. panzehiri neverdir.

#after

p1 >> pads([1,2,3,4]).after(5,"stop")

#sometimes

p1 >> gong([0,0,0,3,2]).sometimes("arp",[1,2,3])

#jump

d1 >> play("x-x[---]").every(4.4,"jump",cycle=8)

'ONEMLI: sakin everynin ilk argumanina 0 vermeyin!'

#spread

d1 >> play("Xv")
 
d1 >> play("Xv", pan=[-1,1], pshift=.125) #spread player objesine bu pan ve pshift ozelliklerini ekler.

d1.spread()

d2 >> play("<Xv>< |l3|>")

d2.spread() #iki farkli davul paterninden birini saga birini sola alir.

'MINI ODEV: spreadi ayni play objesi icerisinde farkli davul paternleri varken deneyin ve dinleyin!'

p1 >> pluck([0,4,5,3],dur = 4)

p2 >> blip(p1.pitch[0])

p_all.stop()

p1 >> pluck([0,1], dur = 4,amp=1)

p3 >> blip(p1.pitch)

p2 >> blip(p1.pitch[0].accompany(rel=[3])) #alt ve ust oktavlar arasi rastgele gecis yapar, rel argumanina verilen deger ise ekstra nota ekler.

print(p2.freq)

#TIP 8: p1.pitch seklinde yazmak istemezseniz .follow() kullanabilirsiniz.

p1 >> blip([0,3,5])

p2 >> jbass(p1.pitch, amp=.6)

p3 >> jbass().follow(p1)

p4 >> gong(p1.pitch +(0,2,5))

p5 >> gong().follow(p1) + (0,2,5)

p_all.stop()

Clock.clear()

'Birinci calisma dokumaninin sonuna geldik!'
