# type: ignore

Clock.bpm = 123


(
    a1
    >> pluck(
        [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 4, 0, 1],
        delay=[0, 0.5, 0, 1.5],
        amp=[0.5, 1, 0.5, 1.5],
    )
)

p2 >> dirt(
    dur=1 / 4,
    amp=[1, 1 / 2, 1 / 2, 1, 0, 1, 0, 1, 1 / 2, 1 / 2, 1, 0, 1, 1 / 2, 1 / 4, 1],
    amplify=var([1, 0], [6, 2]),
)


p3 >> star(
    dur=1 / 4,
    amp=[1, 1 / 2, 1 / 2, 1, 0, 1, 0, 1, 1 / 2, 1 / 2, 1, 0, 1, 1 / 2, 1 / 4, 1],
)

# d_all.stop()

# p_all.stop()

# Stutter 4 times with alternating panning and higher rate
d1 >> play("x-o-").every(4, "stutter", 4, dur=3, pan=[-1, 1], rate=2)

d2 >> dbass([0, 0, 0, 4, 0, 0, 0, -4], amp=[0.5])

Group(p2, d2).only()

a1.solo()
