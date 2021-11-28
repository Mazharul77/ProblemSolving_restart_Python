p = float(input())
t = float(input())
t = t/100
a = float(input())
q = float(input())

c = 0
while p <= q:
    p = p+(p*t)+a
    c = c+1

print(c)

