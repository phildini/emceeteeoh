# type: ignore
# https://twitter.com/naka_Zma/status/1437337756255113220
R = PRand(2)[:8]
T = R / 4


def p(player, synth, degrees, octaves, amp):
    player >> synth(degrees, oct=octaves, dur=T, sus=T | R, amp=amp)


def m(synth, degrees, octaves):
    p(p1, synth, degrees, octaves, 1)
    p(p2, synth, (degrees * 2, degrees * 4, degrees * 8, degrees * 16), octaves, 0.25)


m(donk, Pvar([R, R * 2, R]), (3, R))

d1 >> play("vVX", cut=T, dur=T, rate=T, dist=0.05 * R).spread()

# https://twitter.com/naka_Zma/status/1434830610070048771
Clock.bpm = linvar([120, 130], 16)
R = PRand(3)
D = PDur(31, 43)
pt1 = P["V-T-"].amen()
pt2 = P["V   "]
d1 >> play(pt1, dur=D, sus=0.001, dist=0.02).spread().every(16, "stutter", R)
b1 >> play(pt2, dur=D)

h1 >> play("[--]", rate=R * 0.5)

M.sample = R

# https://twitter.com/naka_Zma/status/1444225643579805698
a = sinvar([-0.9, 1, 1], 64)

p = P[0, 0, 0, 1]

b = b_all

b1 >> bass(tremolo=p * 3, dur=2, amp=a).every(8, "spread", p)

b3 >> dbass(tremolo=P[[16, 0, 0], 0, 0, [4, 3, 8, 2]], dur=2, amp=1 - a).every(
    16, "stutter", 8
)

b.oct = (3, 4)

b.dist = p

b.reverb = 1

b.room = 2

b.mix = Pvar([0, 1], [14, 1])

# https://twitter.com/naka_Zma/status/1439182411628175365
Scale.default.set("chromatic")
Clock.bpm = 100
h1 >> play("--", dur=1 / 3, sample=4, hpf=linvar([0, 5000], 16)).spread()

c = (2, 5, 9, 12)
R = PRand(5)
# p1 >> gong([0, 2], dur=1 / 4, oct=5)
p2 >> sinepad(c, dur=8) + Pvar([R * 2, R, R * 2])
b1 >> play("<V><  [ *] >", dur=4)

# https://twitter.com/naka_Zma/status/1438278505666469892
Clock.bpm = 130
pt1 = P[1, 2, 0, 4]
p1 >> play(
    "<V><X><v>", sample=pt1, dur=PDur(P[3, 4, 7, 3], 16), cut=pt1 / 4, rate=0.8
).every(32, "stutter", 32, room=2, reverb=3, mix=0.6)

h1 >> play("--", dur=1 / 4)
(
    s2
    >> sinepad(
        pt1 | P[1, 0, 3, 2].layer("rotate"), sus=0.4, slide=0.05, dur=1 / 4
    ).spread()
)
