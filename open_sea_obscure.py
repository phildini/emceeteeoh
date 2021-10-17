# type: ignore

# https://www.youtube.com/watch?v=zNdeMgIgrAw
# Reveal
b1 >> play("V v ")

h2 >> play(
    " -",
    sample=2,
    dur=1 / 2,
)

c1 >> play(" *", dur=1)

# Initial

Scale.default.set("chromatic")
Clock.bpm = 100
(
    h1
    >> play(
        "--",
        dur=1 / 3,
        sample=4,
        hpf=linvar([0, 5000], 16),
    ).spread()
)

c = (2, 5, 9, 12)
R = PRand(5)
p1 >> gong(
    [0, 2],
    dur=1 / 4,
    oct=5,
)

p2 >> sinepad(c, dur=8) + Pvar([R * 2, R, R * 2])
b1 >> play("<V>< [ *] >", dur=4)


m = Master()
# Mess with these for fun shit
m.reverb = 1
m.mix = 0.4
m.sus = 0.2

m.lpf = linvar([100, 2000], 16)

m.lpf = 0
