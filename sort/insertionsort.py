def sort(data):
    for i in range(1,len(data)):
        j = i - 1
        tmp = data[i]
        while j >= 0 and data[j] > tmp:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = tmp

    return data

print(sort(["jose","renata","ziraldo","paula","diogo","daniel","augusto"]))