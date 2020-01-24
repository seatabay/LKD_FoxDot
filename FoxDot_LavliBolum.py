"""BOLUM 4.1:TimeVar"""

'Muzik zamanla degisir. Ona heyecanini ve duygusunu veren budur; zaman eksenindeki akis. Notalarin suresi, sesin siddetinin artis ve azalisini diziler kullanarak yapabilirsiniz. Ancak surekli oynatici objesinde degisim yaparken bir baska synth veya bir baska oynatici objesini degistirmeniz mumkun degildir. Zamana bagli degiskenler sizin icin bu ameleligi ortadan kaldirmaktadir.'


p1 >> blip(var([1,2,3]))

p1.stop()

p2 >> blip(var([0,7,14],[1,2,3]),dur=1)

p2.stop()

akorlar = var([0,2,4,6])

p1 >> blip(akorlar)

p1 >> blip(akorlar+[0,2,4])

p2 >> blip(akorlar+(0,2,4))

'enterlamak istemiyorum'

var.akorlar = var([0,3,10,7],1)

p1 >> pluck(var.akorlar)
p2 >> space(var.akorlar)

'Python advanced'

def odd_test(num):
    if num % 2 == 1:
        return 5
    else:
        return 3
        
var.degisken = var([1,1,2,.5])

cikis = var.degisken.transform(odd_test)

p1 >> pluck(cikis)

"""BOLUM 4.2: TimeVar Cesitleri"""
'var degiskeni kullandigimizda degerler listesine sureleri biz belirleriz. Ama tek tek degerleri yazmak yerine lineer, eksponansiyel olarak artis ya da dusus istersek yararlabilecegimiz timevar cesitleri bulunmaktadir.'

print(Clock.now(),linvar([0,1],16))

p1 >> pads(linvar([0,4],4))

p2 >> pads(sinvar([0,4],4))

p3 >> pads(expvar([0,4],4),dur=2)

deg = Pvar([[0,0],[4,5,6]],4)

print(deg)

p4 >> pluck(deg)

"""BOLUM 4.3: TimeVar Advanced"""

d1 >> play("x-o-", amp = var([0,1],[8,inf],start=3))


"""BOLUM 5: TempoClock"""

print(Clock.now())

print(Clock.bar_length())

print(Clock.bars())

p1 >> blip(P[:8])

def update(key,bpm=None):
    Root.default=int(key)
    if bpm is not None:
        Clock.bpm = bpm
        return
        
Clock.schedule(update,Clock.now()+10, args=[4], kwargs={"bpm":250})

'En kullanisli tempoclock: nextBar'

@nextBar
def key_change():
    Scale.default = "minor"
    Root.default = var([1,5,7],4)
    Clock.bpm = var([100,300],4)
    
p1 >> blip(P[:8])
