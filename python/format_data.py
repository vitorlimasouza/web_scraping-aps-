def format_data(dataframe):
    list_data = []
    for data in dataframe:
        temporary_data = {}
        temporary_data['local'] = data['local']
        temporary_data['casos'] = format_number(data['casos'])
        temporary_data['novos casos'] = format_number(data['novos casos'])
        temporary_data['casos por milhão'] = format_number(data['casos por milhão'])
        temporary_data['mortes'] = format_number(data['mortes'])
        list_data.append(temporary_data)
    return list_data


def format_number(num):
    return ''.join(num.split('.'))
