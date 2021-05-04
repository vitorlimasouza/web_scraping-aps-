def format_data(data):
    list_data = []
    for i in data:
        temporary_data = {}
        temporary_data['local'] = i['local']
        temporary_data['casos'] = format_number(i['casos'])
        temporary_data['casos por milhão'] = format_number(i['casos por milhão'])
        temporary_data['mortes'] = format_number(i['mortes'])
        list_data.append(temporary_data)
    return list_data


def format_number(num):
    return ''.join(num.split('.'))
