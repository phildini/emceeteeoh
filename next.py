# type: ignore

Clock.bpm = 160


# p1 >> bass([0, 1, 2, 3, 4, 5, 6, 7])


d2 >> dbass([0, 4, 0, -4, 0, 4, 0, -4], amp=[0.5])

p1 >> play("1234", dur=2)

p2 >> play(
    "&",
    sample=1,
    dur=2,
    sus=2,
    # slide=1,
    # pan=linvar([-1, 1], 8),
    fmod=2,
)

p3 >> play()
