# type: ignore

# b - gentle beeps
p1 >> play('b' , dur=2, sample=[1,2,3,4])

# B - spacey beeps
p2 >> play('B', dur=2, sample=[0,1,2,3,4])

# u - snares
p3 >> play('u', dur=2, sample=[0,1,2,3,4])

# U - longer spacey snares 
p4 >> play('U', dur=2, sample=[0,1,2,3,4])

# r - hits on metal
p4 >> play('r', dur=2, sample=[0,1,2,3,4,5,6])

# R - longer on metal
p4 >> play('R', dur=2, sample=[0,1,2,3])