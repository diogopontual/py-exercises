def merge(data, l, m, r):
    sL = m - l + 1
    auxL = [0] * sL
    for i in range(0,sL):
        auxL[i] = data[l+i]
    sR = r - m
    auxR = [0] * sR
    
    for j in range(0,sR):
         auxR[j] = data[m + 1 + j]

    iL = 0
    iR = 0
    for k in range(l,r + 1):
        if iL >= len(auxL):            
            data[k] = auxR[iR]
            iR+=1
        elif iR >= len(auxR) :
            data[k] = auxL[iL]
            iL+=1
        elif auxL[iL] < auxR[iR]:
            data[k] = auxL[iL]
            iL+=1
        else:
            data[k] = auxR[iR]
            iR+=1        

def mergeSort(data, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(data, l, m)
        mergeSort(data, m+1, r)
        merge(data,l,m,r)


def sort(data):
    return mergeSort(data, 0, len(data)-1)


data = [21,18, 31,35,2,15,17,13,22,1,87,35,23,45,54,31,16,7,3]
sort(data)
print('result',data)
