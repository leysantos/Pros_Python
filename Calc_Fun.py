# Programa para calcular fundações rasas e profundas.
# Desenvolvedor: Francirley Santos
# Acadêmico de Engenharia Civil 8º período
# Centro Universitário Luterano de Manaus
# Manaus 29 de março de 2018

from datetime import date

print("+" * 70)
print("CÁLCULO DE FUNDAÇÕES RASAS E PROFUNDAS \n"
      "Desenvolvedor: Francirley Santos \n"
      "Acadêmico de Engenharia Civil 8º Período \n"
      "Centro Universitário Luterano de Manaus \n"
      "Data: {}".format(date.today()))
print("+" * 70)
print()


# Função para localizar o tamanho de ancoragem lb corforme
# o fck, tipo de ancoragem e área de aderencia.
def compAncoragem(Fck, Aderencia, ancoragem):
    global lb
    c10 = [0.99, 0.69, 0.49]
    c15 = [0.73, 0.56, 0.37]
    c20 = [0.62, 0.44, 0.31]
    c25 = [0.54, 0.38, 0.26]
    c30 = [0.48, 0.33, 0.23]
    c35 = [0.43, 0.30, 0.21]
    c40 = [0.39, 0.28, 0.19]
    c45 = [0.36, 0.25, 0.18]
    c50 = [0.34, 0.24, 0.17]
    if Fck == 10 and Aderencia == 1:
        if ancoragem == 1:
            lb = c10[0]
        else:
            lb = c10[1]
    elif Fck == 10 and Aderencia == 2:
        if ancoragem == 1:
            lb = c10[1]
        else:
            lb = c10[2]
    elif Fck == 15 and Aderencia == 1:
        if ancoragem == 1:
            lb = c15[0]
        else:
            lb = c15[1]
    elif Fck == 15 and Aderencia == 2:
        if ancoragem == 1:
            lb = c15[1]
        else:
            lb = c15[2]
    elif Fck == 20 and Aderencia == 1:
        if ancoragem == 1:
            lb = c20[0]
        else:
            lb = c20[1]
    elif Fck == 20 and Aderencia == 2:
        if ancoragem == 1:
            lb = c20[1]
        else:
            lb = c20[2]
    elif Fck == 25 and Aderencia == 1:
        if ancoragem == 1:
            lb = c25[0]
        else:
            lb = c25[1]
    elif Fck == 25 and Aderencia == 2:
        if ancoragem == 1:
            lb = c25[1]
        else:
            lb = c25[2]
    elif Fck == 30 and Aderencia == 1:
        if ancoragem == 1:
            lb = c30[0]
        else:
            lb = c30[1]
    elif Fck == 30 and Aderencia == 2:
        if ancoragem == 1:
            lb = c30[1]
        else:
            lb = c30[2]
    elif Fck == 35 and Aderencia == 1:
        if ancoragem == 1:
            lb = c35[0]
        else:
            lb = c35[1]
    elif Fck == 35 and Aderencia == 2:
        if ancoragem == 1:
            lb = c35[1]
        else:
            lb = c35[2]
    elif Fck == 40 and Aderencia == 1:
        if ancoragem == 1:
            lb = c40[0]
        else:
            lb = c40[1]
    elif Fck == 40 and Aderencia == 2:
        if ancoragem == 1:
            lb = c40[1]
        else:
            lb = c40[2]
    elif Fck == 45 and Aderencia == 1:
        if ancoragem == 1:
            lb = c45[0]
        else:
            lb = c45[1]
    elif Fck == 45 and Aderencia == 2:
        if ancoragem == 1:
            lb = c45[1]
        else:
            lb = c45[2]
    elif Fck == 50 and Aderencia == 1:
        if ancoragem == 1:
            lb = c50[0]
        else:
            lb = c50[1]
    elif Fck == 50 and Aderencia == 2:
        if ancoragem == 1:
            lb = c50[1]
        else:
            lb = c50[2]

    return lb


# Função para localizar o diâmetro da barra, conforme o consumo de aço.
def locDiaBarra(areaAco):
    global diaBarra
    diametro = [6.3, 8, 10, 12.5]
    if areaAco < 2.9:
        diaBarra = diametro[0]
    elif 2.89 < areaAco < 4:
        diaBarra = diametro[1]
    elif 3.99 < areaAco < 6.6:
        diaBarra = diametro[2]
    elif areaAco > 6.59:
        diaBarra = diametro[3]

    return diaBarra


print()
print("#" * 70)
print("Ecolha o tipo de fundação: \n"
      "Opção[1] - Fundação do tipo direta. \n"
      "Opção[2] - Fundação do tipo indireta.")
print("#" * 70)
print()
tipoFundacao = int(input("Informe a opção desejada"
                         "para o tipo de fundação: "))
tSolo = float(input("Informe a tensão admissível do solo "
                    "em (tf/m²): "))
fck = float(input("Infome o fck do concreto em (Mpa): "))
print()
print("#" * 70)
print("Escolha o tipo de área de aderência: \n"
      "Opção[1] - Área de má aderência. \n"
      "Opção[2] - Área de boa aderência.")
print("#" * 70)
print()
aderencia = int(input("Informe a opção desejada para "
                      "o tipo aderência: "))
print()
print("+" * 70)
