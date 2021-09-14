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
