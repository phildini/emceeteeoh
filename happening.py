# type: ignore

Clock.bpm = 125


p1 >> pluck(
    [0, 1, 2, 3],
    delay=[0, 0.5, 0, 1.5],
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

# Stutter 4 times with alternating panning and higher rate
d1 >> play("x-o-").every(4, "stutter", 4, dur=3, pan=[-1, 1], rate=2)

p1.stop()

# You can also specify the number of events to stutter using the 'n' keyword
d1 >> play("x-o-", dur=1 / 2).every(6, "stutter", dur=3, n=4)

p1.solo()
