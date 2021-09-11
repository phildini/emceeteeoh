# type: ignore

Clock.bpm = 105
var.keys = var([-2, 0, 2, 4], 2)

d1 >> dab(var.keys, chop=8, dur=2, fmod=1, amp=5/6)

h1 >> play("<x-x[--]><  *   *   *   *[**]>")

k1 >> star(
    P[var.keys, 1] + (0,4),
    amp=1/2,
    oct=4
)


p1 >> pluck([0, 1, 2, 3], dur=1/2) + [0, 3, 4,0]

p1.stop()

p2 >> star([0,2,3,4])

h1 >> play("<x-x[--]><  *   *   *   *[**]>")

p1 >> pluck([0, 2, 4], dur=[1, 1/2, 1/2], amp=1)

p1 >> pluck([0, 1, 2, 3], dur=2) 

d1 >> play("@A@A(@A)([A@])", dur=1/2, sample=var.keys)

p1 >> pluck(P[0, 3, 0, 4].stutter(6)) + (0, 2, 4)

p1 >> pluck(var([0, 3, 4, 0], 4), dur=[1, 1/4, 1/4, 1/2]) + (0, 2, 4)
