import matplotlib.pyplot as plt
import math
import random


# function that finds average

def avg(L):
    sum = 0
    for i in L:
        sum += i
    return (sum / len(L))

# function to calculate rms value
def rms(R):
    sq_sum = 0
    for value in R:
        sq_sum += value ** 2
    return math.sqrt(sq_sum / len(R))



def random_walk(M, N ,rms , avg):
    random.seed(None)
    r2 = 0
    R2 = []
    X = []
    Y = []
    for j in range(0, M):

        X1 = []
        Y1 = []
        x = 0.0
        y = 0.0
        r2 = 0.0
        X1.append(x)
        Y1.append(y)

        for i in range(0, N):
            theta = 2 * math.pi * random.random()
            random_x = math.cos(theta)
            random_y = math.sin(theta)
            x = x + random_x
            y = y + random_y



            #Above movement is tatally random(no constrained) movement in any positon in 2D space.

            #Below one is constrained random walk in 2D space.Movement is only in east,west,north and south direction.
            #Though that part is inactive (It was just for check whether the R_rms value lesser or greater than upper method)

            """
            step = random.choice(['NORTH', 'SOUTH', 'EAST', 'WEST'])
            if step == 'NORTH':
                y = y + 1
            elif step == 'SOUTH':
                y = y - 1
            elif step == 'EAST':
                x = x + 1
            else:
                x = x - 1
            """





            X1.append(x)
            Y1.append(y)
        X.append(X1)
        Y.append(Y1)
        r2 = math.sqrt(x ** 2 + y ** 2)
        R2.append(r2)


    r_rms = rms(R2)

    sum_x = 0
    sum_y = 0
    for i in range(len(X)):
        sum_x = sum_x + X[i][len(X[i]) - 1]
        sum_y = sum_y + Y[i][len(Y[i]) - 1]

    avg_x = sum_x / len(X)
    avg_y = sum_y / len(Y)
    rad_dis = math.sqrt(avg_x ** 2 + avg_y ** 2)




    return X, Y, r_rms, avg_x, avg_y, rad_dis



figure, axes = plt.subplots(nrows=2, ncols=3)

RMS = []
steps = []

M = 100
N = 250
#add = 200
print("\n\nFor Steps = 250; No. of walks = 100 : ")


X1, Y1, r_rms1, avg_x1, avg_y1, rad_dis1 = random_walk(M, N,rms,avg)


print("R_rms = ", r_rms1 , "rootN = ", math.sqrt(N))
print("Average X = ", avg_x1,"Average Y = ", avg_y1)
print("Radial distance R = ", rad_dis1)

RMS.append(r_rms1)
steps.append(math.sqrt(N))
for i in range(5):
    axes[0, 0].set_xlabel('X')
    axes[0, 0].set_ylabel('Y')
    axes[0, 0].set_title("For steps = 250")
    axes[0, 0].plot(X1[i], Y1[i])

N = N + 250
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")

X2, Y2, r_rms2, avg_x2, avg_y2, rad_dis2 = random_walk(M, N,rms,avg)

print("R_rms = ", r_rms2,"rootN = ", math.sqrt(N))
print("Average X = ", avg_x2,"Average Y = ", avg_y2)
print("Radial distance R = ", rad_dis2)
RMS.append(r_rms2)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 1].set_xlabel('X')
    axes[0, 1].set_ylabel('Y')
    axes[0, 1].set_title("For steps = 500")
    axes[0, 1].plot(X2[i], Y2[i])

N = N + 250
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")

X3, Y3, r_rms3, avg_x3, avg_y3, rad_dis3 = random_walk(M, N,rms,avg)

print("R_rms = ", r_rms3,"rootN = ", math.sqrt(N))
print("Average X = ", avg_x3,"Average Y = ", avg_y3)
print("Radial distance R = ", rad_dis3)

RMS.append(r_rms3)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 2].set_xlabel('X')
    axes[0, 2].set_ylabel('Y')
    axes[0, 2].set_title("For steps = 750")
    axes[0, 2].plot(X3[i], Y3[i])

N = N + 250
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")

X4, Y4, r_rms4, avg_x4, avg_y4, rad_dis4 = random_walk(M, N,rms,avg)

print("R_rms = ", r_rms4,"rootN = ", math.sqrt(N))
print("Average X = ", avg_x4,"Average Y = ", avg_y4)
print("Radial distance R = ", rad_dis4)

RMS.append(r_rms4)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')
    axes[1, 0].set_title("For steps = 1000")
    axes[1, 0].plot(X4[i], Y4[i])

N = N + 250
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")


X5, Y5, r_rms5, avg_x5, avg_y5, rad_dis5 = random_walk(M, N,rms,avg)
print("R_rms = ", r_rms5,"rootN = ", math.sqrt(N))
print("Average X = ", avg_x5,"Average Y = ", avg_y5)
print("Radial distance R = ", rad_dis5)
RMS.append(r_rms5)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 1].set_xlabel('X')
    axes[1, 1].set_ylabel('Y')
    axes[1, 1].set_title("For steps = 1250")
    axes[1, 1].plot(X5[i], Y5[i])



N = N + 250
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")


X6, Y6, r_rms6, avg_x6, avg_y6, rad_dis6 = random_walk(M, N,rms,avg)
print("R_rms = ", r_rms6,"rootN = ", math.sqrt(N))
print("Average X = ", avg_x6,"Average Y = ", avg_y6)
print("Radial distance R = ", rad_dis6)
RMS.append(r_rms6)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 2].set_xlabel('X')
    axes[1, 2].set_ylabel('Y')
    axes[1, 2].set_title("For steps = 1500")
    axes[1, 2].plot(X6[i], Y6[i])

# All random_walk plot in one place.
plt.figure()




plt.ylabel('R_rms')
plt.xlabel('Root of N')
plt.plot(steps, RMS)

plt.grid(True)
plt.show()




"""
/home/tamoghna/anaconda3/envs/Pycharm_py/bin/python /home/tamoghna/PycharmProjects/pythonProject/sample3.py


For Steps = 250; No. of walks = 100 : 
R_rms =  16.8653127040948 rootN =  15.811388300841896
Average X =  -1.099964468190638 Average Y =  -0.18717460648186182
Radial distance R =  1.1157760369328393


For Steps = 500 ; No. of walks = 100 : 
R_rms =  21.050440217628207 rootN =  22.360679774997898
Average X =  2.260774801495899 Average Y =  0.35544690079373426
Radial distance R =  2.2885465261520666


For Steps = 750 ; No. of walks = 100 : 
R_rms =  28.32553570263876 rootN =  27.386127875258307
Average X =  -1.670270328377276 Average Y =  -5.467479169933195
Radial distance R =  5.7169162529733555


For Steps = 1000 ; No. of walks = 100 : 
R_rms =  29.91102920032012 rootN =  31.622776601683793
Average X =  -0.4687483407829345 Average Y =  -2.7968087486624
Radial distance R =  2.8358180801280772


For Steps = 1250 ; No. of walks = 100 : 
R_rms =  35.65745611289155 rootN =  35.35533905932738
Average X =  3.014933357655876 Average Y =  -3.764943579661452
Radial distance R =  4.823341508657678


For Steps = 1500 ; No. of walks = 100 : 
R_rms =  39.24362269394478 rootN =  38.72983346207417
Average X =  1.1651009320542862 Average Y =  -0.9810352902130178
Radial distance R =  1.5231186501770329

"""