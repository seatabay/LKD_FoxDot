"""BOLUM.4: PATERNLER"""

"""BOlUM 4.1: PATERN TEMELLERI"""

'Oynatici objesi icerisine atanan degerlere bir islem uygulamak isteyebiliriz.'

print([2,3,4]*2)

lis = [1,2,3]

print([i*2 for i in lis])

'Ikinci uygulamadaki kodu canli kodlama sirasinda yazmak oldukca zor. Bu yuku almak icin FoxDotta paternler bulunmaktadir.'

p1 >> keys(P[0,1,2,3]*2)

p1.stop()

p2 >> keys(P[:4]*2)

p2.stop()

p3 >> keys(P[0:4] + P[2:6])

p3.stop()

p4 >> keys(P[0:4]  | P[2:6])

p4.stop()

p5 >> keys(P[0:4] ** P[-1:3]) #ussunu alir

p5.stop()

p6 >> keys(P[1:4] & P[3:6]) #ikili sekilde beraber calar(PGroups)

p7 >> keys([(1,3),(2,4),(3,5)])

p_all.stop()

'Patternler arasinda goruldugu uzere islem yapilabilmektedir. Pattern uzunluklarinin ayni olmasina gerek yoktur.'

#TIP 0: Patern objeleri ile davul samplelarini calabilir ve bazi patern metodlarini da kullanabilirsiniz, ornegin reverse!

"""BOLUM 4.2: PATERN METODLARI"""

'Paternler bir obje oldugu icin onlara bagli metodlar ve nitelikler bulunmaktadir. Oynatici objelerine ekledigimiz every metodu burada yerini direk olarak paternlere uyguladigimiz metodlara birakmaktadir.40a yakin patern metodu bulunmaktadir, siklikla kullanilanlara goz atalim:'

##TIP 1: Isterseniz bu metodlari patern kullanmasaniz bile oynatici objelerinde "every" metodu ile kullanabilirsiniz!

'Paterni uzatip elemanlari rastgele dagitmak mi istiyorsunuz?'

p1 >> keys(P[:4].shuffle(2)) #argumanin degeri paternin kac defa cogullanacagini belirtmektedir.

p1.stop()

p2 >> keys(P[:4].shuffle(3),dur = PDur(3,8))

p2.stop()

'Patern patern(PGroups) icinde... Bir varmis bir yokmus!'

P[1,2,3]

p1>> pluck(P(1,2))

p3 >> pluck(P[1,[2,3]].shufflets(3))

p4 >> pluck(P[[1,0],[2,3]].shufflets(3))

print(p3.pitch)

p_all.stop()


#shuffle ve shufflets arasindaki fark:
print(P[1,[2,3]].shuffle(2))
print(P(1,[2,3]).shufflets(2))

'Paterni tersine nasil ceviririz?'

p1 >> keys(P[:4].reverse(), dur = 1/2)

p2 >> keys(P[:4].mirror(), dur = 1/2)

p_all.stop()

'mirror ile reverse ayni isi yapiyor gibi duruyor. O halde neden ikisi de var?'

print(P[:4,[5,6]].reverse())
print(P[:4,[5,6]].mirror())

'Paternimizin icerisindeki sayilari hizaya nasil getiririz?'

p1 >> blip(P[1,6,5,3,4,2,0].sort(reverse=True))

p1.stop()

p2 >> blip(P[(1,3),(7,5,4,3),(4,3,2)].sort()) #PGroup eleman sayisina gore siralar.

p2.stop()

'3 elma, 3 armut, 3 karpuz'

p1 >> pluck(P[0,1,2].stutter(3))

p1.stop()

print(P[0,1,2].stutter([3,4,5])) #dizi vererek hangi elemani kac defa isteyeceginizi belirtebilirsiniz.

'Arpeggiattooo!'

p1 >> pluck(P[0,1].arp([5,6]))

p1.stop()

print(P[1,2].arp([0,1,2,3])) #paternin ilk elemani + arp dizisi, paternin ikinci elemani + arp dizisi...

Clock.clear()

'Cesnilendirelim mi?'

p1 >> blip(P[1,2,3,4].splice())

p1.stop()

p2 >> blip(P[1,2,3,4].splice([7,6,5,4]))

print(P[1,2,3,4].splice([7,6,5,4]))

Clock.clear()

'En buyuk - digerleri'

p1 >> blip(P[2,5,4,12].invert())

p1.stop()

'Ross Geller, is that you bruh?'
# https://www.youtube.com/watch?v=n67RYI_0sc0

p1 >> pads(P[1,2,3,4].pivot(1)) #reverse+rotate yapar.

p1.stop()

print(P[1,2,3,4].pivot(1))

Clock.clear()

'Toplaya toplaya gidek'

p1 >> blip(P[1,2,3,4].accum())

p1.stop()

print(P[1,2,3,4].accum(8))

'GYM CLASS: CARDIO TIME!'

p1 >> pluck(P[1,2,3,4].stretch(7)) #arguman degeri kadar patern uzunlugunu tamamla ve genislet.

p1.stop()

print(P[:4].stretch(6))

'Tras zamani.'

p1 >> keys(P[:5].trim(3))

p1.stop()

'Sondan tras.'

p1 >> blip(P[1:6].ltrim(1))

p1.stop()

print(P[1,2,3,4,5].ltrim(1))

'Donguler'

p1 >> pluck(P[0].loop(4, lambda x:x+2),dur=2)

p1 >> pluck(P[0,1].loop(2) | P[7,8])

p1 >> pluck(P[0].loop(2) + [1,2,3,4])

p1 >> pluck(P[1,2].loop(2) +(0,5)) #P(1,6),P(2,7),P(1,6),P(2,7)...

## loop boyle bi' ise yaramiyor gibi duruyor. Hmmm... baska neler yapilabilir?

p1 >> pluck(P[1,3,5].loop(1) | P**(2,4,6), dur = var([1/4,1],[4,1]),amp=1)

##every mi eklesek?

p1 >> pluck(P[1,3,5].loop(2).every(4,"offadd",2).every(2,"arp",[1,2,3,4]) | P(1,[2,3],5), dur= var([1/2,1],[4,1]), sus=2, lpf=1000,room=1,mix=.7)

p1.stop()

Clock.clear()

'Multiplexer'

p1 >> space(P[1,2,3,[7,8]].duplicate(2)) #nested listler dagitilmaz, oldugu gibi kalir.

p1.stop()

print(P[1,2,3,[7,8]].duplicate(4))

'Duyarsiz duplicate: iter'

p1 >> blip(P[1,2,[3,4]].iter(4)) #nested listler dagitilir.

p1.stop()

print(P[1,2,[3,4]].iter(4))

'Bi duz bi ters,9.5 sis orgu'

##diyelim ki bir paterne tersini de eklemek istiyorsunuz:
print(P[:5]| P[:5].reverse())

## uzun uzadiya yazmak istemeyebilirsiniz.

print(P[:5].palindrome())
print(P[:5].palindrome(2)) #argumana verilen deger tersine cevrilen paternin kacinci indeksinden itibaren eklenecegini belirtir.

p1 >> pluck(P[:4].palindrome([0,1,2,3,4]))

p1.stop()

'eskisini getir yenisini al'

p1 >> pluck(P[:4].every(4,"alt",[4,5,6,7]))#her 4 vurusta bir P[:4] yerine [4,5,6,7] cal.

p1.stop()

'normalize et'

p1 >> pluck(P[:8].norm())

p1.stop()

print(P[0,1,2,3,4,5,6,7,8].norm())

'ciftleri sahneden alalim lutfen'

p1 >> blip(P[1,2,2,2,4,5,5,5].undup())

p1.stop()

print(P[1,2,2,2,3,4,4,4,4].undup())

'jawline'

p2 >> blip(P[0,1,2,3,4]].replace(3,9))

p2.stop()

'jawline,bisektomi,badem goz.. full paket'

p3 >> blip(P[0,1,2,3,4].submap({1:8,2:9,4:[9,10]}))

p3.stop()

'Asil paterne kat cikalim'

p4 >> pluck(P[1,2,3,4].layer("norm")) 

p4 >> pluck(P[0,0].layer("offadd",[1,9]),dur=2) #P[0,1],P[0,9],P[0,1],P[0,9]..seklinde zipleyerek calar.

p5 >> pluck(P[0,1].layer(lambda x:x+2),dur=2)

print(P[1,2,3,4].layer("norm"))

'every ile concat'

p1 >> blip(P[:4].every(4,"concat",[4,5]))

p2 >> blip(P[:4] | [4,5])

#TIP: '|' kullanarak da concat yapabilirsiniz. ancak every metodu icerisinde | operatoru kullanamayiz.

'winrar,lisansli'

p1 >> pluck(P[0,1,2,3].zip([4,5]),dur=2)

'topla-ziple-geciktir'

p1 >> blip(P[0,1,2].offadd(2,2),dur=4)

'offaddin carpimlisi'

p2 >> pluck(P[:4].offmul(2,2),dur=2)

print(P[:4].offmul(2,2))

'geciktirmeli layer'

p3 >> blip(P[:4].offlayer("reverse",2),dur=2)

'oh wow such a drummer thing, amen brothers!'
# https://www.youtube.com/watch?v=tNvGd1WIB1Y

d1 >> play("x-o-",dur=1/2).every(4,"amen")

d1.stop()

"""BOLUM 3.3: PATERN FONKSIYONLARI"""

"""Metodlar ile karsilastirinca daha az patern fonksiyonu bulunmakta! Bu fonksiyonlar belirli degerlere sahip paternler uretmek icin kullanilabilir.Totalde 11 tane patern fonksiyonu vardir. Daha siklikla kullanilanlar orneklerdeki gibi.
"""

d1 >> play(PStep(4,"-","x"))

d1.stop()

d1 >> play(PStep([2,4],"-","x"))

d1.stop()

p1 >> gong(PRange(10,0,2).palindrome()) #PRange(start,stop=None,step=None)

p1.stop()

p1 >> gong(PTri(10,0,2), pan = PSine(32))

p1.stop()

print(PRange(10,0,2))

print(PTri(10,0,2))

'MINI ODEV: PRange fonksiyonu ile PTri fonksiyonuna ayni araligi verin. Daha sonra PRange fonksiyonuna palindrome metodunu uygulayin. Ne gozlemliyorsunuz?'

print(PEuclid(5,8))
print(PEuclid(5,8)+[2,3])#sirayla ekler!

p2 >> blip(PEuclid(5,8)+[2,3])

print(PEuclid2(5,8,"v","s")) #8 eleman, 5i default!

print(PStep(5,"v","s"))

d1 >> play(PEuclid2(5,8,"x2","1s"))

d1.stop()

#PEuclid2 fonksiyonunu PStep+PEuclid gibi dusunebiliriz. Davul ornekleri calarken isinize yarayabilir!

"""Bu fonksiyonlar arasinda siklikla kullanilan bir baska fonksiyon bulunmaktadir: PDur."""

print(PDur(3,8)) #PDur(n,k,start,dur=.25)

print(PDur(PRange(4,0),4))

#PDur Euclidean ritim diye gecmektedir. Ornegin, (3,8)'de 8 vurusa 3 pulse dagitir.

print(PSine(16)) #genligi -1 ile 1 arasinda olan bir sinus dalgasi.

print(PSq(2,2,5))


"""BOLUM 3.4: PATERN URETECLERI"""

'Paternlere istedigimiz degerleri verebiliriz. Ancak muzik yaparken raslantisalligi kullanmak isteyecegimiz zamanlar olabilir. Bu gibi durumlarda patern uretecleri isimize yaramaktadir. '

'rastgele bisiler calalim'

p1 >> pluck(PRand(2,10)[:5])

p1.stop()

print(PRand(2,10)[:10])

'bi giydigimi bi daha giymeyeyim'

print(PxRand(1,5)[:10])

p1 >> blip(PxRand(1,10)[:10]) #ayni elemanlar arka arkaya gelmez!

p1.stop()

p2 >> blip(PxRand([1,2,3])[:10]) #PxRand icerisine dizi vererek belirlediginiz degerleri rastgele calabilirsiniz.

p2.stop()

'Beyaz gurultu(korku sevenler icin)'

print(PWhite(-1,1)[:5])

p1 >> klank(PWhite(-4,4)[:15],tremolo=PSine(16), shape=sinvar([.1,.5],32),dur=4,oct=[4,3,2,1])
p2 >> space(p1.pitch,dur=4, oct=5)

p_all.stop()

'ileri-geri rand!'

print(PWalk(9,2,0)[:20])

p1 >> keys(PWalk(12,3)[:20])

p1.stop()

'ufak ufak degissin'

print(PDelta([.1,-.4],2)[:10])

p1 >> pluck(PDelta([.1,-.1])[:20]+P**(0,1,3,4),dur=PDur(2,8),lpf = sinvar([500,2000],8)).every(8,"reverse")

p1.stop()


"""BOLUM 3.5: PGROUPS: P*+()"""

'Player ya da patern objesi icerisinde () kullandiginizda notalar beraber caliyordu. Bunu saglayan ozellik PGroupstur.'

p1 >> pluck(P[0,1,P([2,3],[4,5])])

print(P[0,1,[2,3]])
print(P[0,1,P([2,3],[4,5])])

p1.stop()

'Genisletilmis PGROUPS mu?'

'tek duration cok nota'

p1 >> blip(P*(1,2,3),dur=1)

p2 >> blip(P*[1,2,3]) 

p2 >> blip(P*(0,1,2), amp=.5) #sirayla ama ayni duration(sure) icerisinde calar.
d1 >> play("X ")

Group(p2,d1).stop()

p1 >> pluck(P+(1,2,3),dur=4,sus=var([0,2],4)) #durationdan bagimsiz, sustaini kullanir.

p1.stop()

p1 >> keys(P+(0,2,4), dur = 1, sus=2).every(2,"arp",[1,2,3,4,5,6])

p1.stop()

'random P*()'

a1 >> pluck(P[0,1,P*(3,5,7,9)])

p1 >> pluck(P[0,1,P**(3,5,7,9)])
d1 >> play("(g [hh])[--]")

Group(p1,d1).stop()

p_all.stop()

'delayli P*()'

p3 >> pluck(P/(2,4,6,8),dur=2)

p3.stop()

'delayi belirleyebildigimiz P/()'

p4 >> pluck(P^(0,2,5,7),dur=4)

p4 >> pluck(P^(var([-1,0,1],8),5,10,.5),dur=1, bpm=80)

p4.stop()




'ZORLU BIR BOLUMUN SONUNA GELDIK. TEBRIK EDIYORUM.'
