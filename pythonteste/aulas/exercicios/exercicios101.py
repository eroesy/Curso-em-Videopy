from datetime import datetime

def voto(idade):
    age = datetime.now().year - idade

    if age < 16:
        return f'Com {age} anos: VOTO NEGADO!.'
    elif 16 <=age <18 or age > 65:
        return f'Com {age} anos: VOTO OPICIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATORIO!.'


f1 = voto(int(input('Ano de nascimento: ')))
print(f1)