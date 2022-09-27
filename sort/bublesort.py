def sort(data):
    it = 0
    last = len(data) - 1
    while True:
        swapped = False
        for i in range(0,last):
            it += 1
            if data[i] > data[i+1]:
                tmp = data[i+1]
                data[i+1] = data[i]
                data[i] = tmp
                swapped = True
        if swapped == False:
            break
    print(it)
    return data

print(sort(["paula","diogo","daniel","augusto"]))