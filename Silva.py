
"""
program that says if you have Silva / SILVA in your last name
by: BIG

"""

N = str(input("digite seu nome completo:"))

palavras = N.split()

if 'Silva' or 'SILVA' in palavras:
    print('sim')

else:
    print('Não')
