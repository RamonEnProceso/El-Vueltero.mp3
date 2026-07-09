from SCLang import *

Clock.clear()

Clock.bpm = 152
Root.default.set("F")

#Kick
p1 >> play("<X   X   X   XX  X   X   X   XXXX>", dur=1/2, rate=1)
#Hithat
p2 >> play("<-   -   -   -   --- -   -   --  -   -   -   - - -   -   -------->", dur= 1/8)
#Snare
p3 >> play("<  o   o   o   o   o   o   o   oo>", dur=1/2, rate=1)

#Bajo
b1 >> bass(
    [5,7,5,7,5,7,[4,7],[4,7]],
    dur = 1,
    amp=0.4)

#Melodía inicial
m1 >> pluck(
    [0, 4, 7, 5, 4, 2, 0, -2],
    dur=[1, 0.5, 0.5, 1, 0.5, 0.5, 1, 1],
    amp=0.5,
    sus=1.75,
)

s1.stop()

b1.stop()

m1.stop()

