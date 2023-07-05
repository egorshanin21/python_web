liters = 'WXPQ;\RYZEFGHIJK-LMAЫЬЭBCDNOS/TUVКЛДЕМНЖЗАБВГИЄЁЙЇО' \
             'УФХЩПРСТ:|ЪЮЦЧШЯ7689023541?!.,'

liter = liters[::-1]

count = len(liters)


def decode(message, krok):
    code_message = ''
    for i in message:
        position = liter.find(i)
        new_position = position + krok
        if new_position > count - 1:
            while new_position > count - 1:
                new_position = new_position - count - 1
        if i in liter:
            code_message += liter[new_position]
        else:
            code_message += i
    return code_message
