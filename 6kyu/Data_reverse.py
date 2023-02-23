def data_reverse(data):
    return [item for x in range(len(data),-1,-8) for item in data[x: x+8]]