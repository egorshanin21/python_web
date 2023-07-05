liters = 'WXPQ;\RYZEFGHIJK-LMAЫЬЭBCDNOS/TUVКЛДЕМНЖЗАБВГИЄЁЙЇО' \
             'УФХЩПРСТ:|ЪЮЦЧШЯ7689023541?!.,'

count = len(liters)


def code(message, krok):
    code_message = ''
    for i in message:
        position = liters.find(i)
        new_position = position + krok
        if new_position > count - 1:
            while new_position > count - 1:
                new_position = new_position - count - 1
        if i in liters:
            code_message += liters[new_position]
        else:
            code_message += i
    return code_message





