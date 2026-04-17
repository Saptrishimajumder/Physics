import time

x1=0
x2=10

v1=5
v2= -5

m1=1
m2=1

timestep=0.1
while True:
    x1 += v1*timestep
    x2 += v2*timestep
    print("Ball1:", round(x1, 2), "Ball2:", round(x2, 2))
    if abs(x1-x2)< 0.5 and (v1-v2>0):
        print("collision")

        u1=v1
        u2=v2
        v1 = ((m1 - m2)*u1 + 2*m2*u2) / (m1 + m2)
        v2 = ((m2 - m1)*u2 + 2*m1*u1) / (m1 + m2)
        break
    print("Distance:", round(abs(x1 - x2), 2))

    time.sleep(0.1)