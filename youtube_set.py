# type: ignore

Clock.bpm = 105
var.keys = var([-2, 0, 2, 4], 2)

d1 >> dab(
    var.keys,
    chop=8,
    dur=2,
    fmod=1,
    amp=5 / 6,
    pan=[-1, 1],
)

d1 >> dab(
    var.keys,
    chop=16,
    dur=2,
    amp=5 / 6,
)

h1 >> play("<x-x[--]><  *   *   *   *[**]>")

k1 >> star(
    P[var.keys, 1] + (0, 4),
    amp=1 / 2,
    oct=4,
)

Clock.clear()

# d1 >> play("x-o-")

# d1 >> play("(x-)(-x)o-")

# d1 >> play("x-o[---]", dur=1)

# d1 >> play("(x[--])xo{-[--][-x]}")
