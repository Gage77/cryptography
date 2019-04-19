def dot(a, b):
    dotproduct = 0
    for i, j in zip(a, b):
        dotproduct += i*j
    return dotproduct

def getNewV(v2, v1, m):
    newv = []
    newv.append(v1[0] - m*v2[0])
    newv.append(v1[1] - m*v2[1])
    return newv

def fun(v1, v2, numsteps):
    # Check to swap
    if v2[0] * v2[1] < v1[0] * v1[1]:
        v1, v2 = v2, v1

    top = dot(v1, v2)
    print('top = ' + str(top))
    bottom = dot(v1, v1)
    print('bottom = '+ str(bottom))
    m = top // bottom
    print('m = ' + str(m))
    if m == 0:
        return (v1, v2, numsteps)
    else:
        newv2 = getNewV(v1, v2, m)
        print('NEW V2 ' + str(newv2))
        newnumsteps = numsteps + 1
        return fun(v1, newv2, newnumsteps)

# Part a
v1 = [120670, 110521]
v2 = [323572, 296358]
val = fun(v2, v1, 1)
print('======= part a =======')
print(val)
print('======= part a =======')

# Part b
v3 = [174748650, 45604569]
v4 = [35462559, 9254748]
val = fun(v3, v4, 1)
print('======= part b =======')
print(val)
print('======= part b =======')

# Part c
v5 = [725734520, 613807887]
v6 = [3433061338, 2903596381]
val = fun(v5, v6, 1)
print('======= part c =======')
print(val)
print('======= part c =======')