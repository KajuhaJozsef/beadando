import numpy as np

v=np.array([0,1,1,1,0])

def eadando2(vec):
    torlendo=[]
    lepes=0
    while len(vec)!=0:
        for i in range(vec.shape[0]):
            if vec[0]==vec[i]:
                torlendo.append(i)
            else:
                break
        vec=np.delete(vec,torlendo)
        lepes+=1
        print(vec)
        torlendo.clear()
    print(lepes,'lépéssel lehet kitörölni a vektort')




eadando2(v)




