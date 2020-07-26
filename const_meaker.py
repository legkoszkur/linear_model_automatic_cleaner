from data_input import the_data
from model_specification import x_egzo

def zerolistmaker(n):
    listofzeros = [1] * n
    return listofzeros

const = zerolistmaker(len(the_data))

the_data['const'] = const

x_egzo.append('const')