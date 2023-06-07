cidade = input('nome da cidade por favor: ').strip()

#botando em . upper, toda a forma em que se escrever 'santo' sera elevada para maiscula se tornando um resultado uniforme
#cidade[:5] --> santo contem 5 letras, porem o python começa a contar do 0, logo são 4 caracteres, contudo o [:4] corta o ultimo caracter, ficaria assim :SANT
santo = print(cidade[:5].upper() == '\33[1;31;40mSANTO')
