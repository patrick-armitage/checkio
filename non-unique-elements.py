def checkio(data):
    temp_data = data[:]
    items_to_remove = []
    for n in data:
        temp_data.remove(n)
        if n in temp_data:
            temp_data = data[:]
        else:
            items_to_remove.append(n)

    for item in items_to_remove:
        data.remove(item)
    return data
