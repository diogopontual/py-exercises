def sort(data,sorted = []):
    if len(data) == 0:
        return sorted
    s = 0
    for i in range(len(data)):
        if data[i] < data[s]:
            s = i
    sorted.append(data.pop(s))
    return sort(data,sorted)

def sort1(data):
    cursor = 0;
    while cursor < len(data):
        min = cursor
        for i in range(cursor,len(data)):
            if data[i] < data[min]:
                min = i
        if min != cursor:
            tmp = data[min]
            data[min] = data[cursor]
            data[cursor] = tmp
        cursor += 1
    return data


print(sort(["gustavo","paula","diogo","davi","augusto","beto","beto"]))