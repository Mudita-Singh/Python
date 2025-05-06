#finding distance between 4 points by Euclidean distance
import math

def Euclidean_distance(A,B,C,D):
    dis1=math.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
    dis2=math.sqrt((C[0]-B[0])**2+(C[1]-B[1])**2)
    dis3=math.sqrt((D[0]-C[0])**2+(D[1]-C[1])**2)
    dis4=math.sqrt((A[0]-D[0])**2+(A[1]-D[1])**2)
    print(f"Distance between A nad B is:{dis1}")
    print(f"Distance between B nad C is:{dis2}")
    print(f"Distance between C nad D is:{dis3}")
    print(f"Distance between A nad D is:{dis4}")
A=(1,2)
B=(3,4)
C=(5,6)
D=(7,8)

Euclidean_distance(A,B,C,D)

