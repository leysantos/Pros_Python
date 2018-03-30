# Programa para calcular fundações rasas e profundas.
# Desenvolvedor: Francirley Santos
# Acadêmico de Engenharia Civil 8º período
# Centro Universitário Luterano de Manaus
# Manaus 29 de março de 2018

from datetime import date
import math
import os

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


# Função para localizar o diâmetro da barra, conforme
# o consumo de aço.
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
print("#" * 70)
print("Escolha a opção de ancoragem para armadura do "
      "pilareite: \n"
      "Opção[1] - Sem gancho. \n"
      "Opção[2] - Com gancho.")
print("#" * 70)
print()
ancoragem = int(input("Informe a opção de ancoragem"
                      "para o pilareite: "))
lb = compAncoragem(fck, aderencia, ancoragem)

# Condição que verifica o tipo de fundação indireta.
if tipoFundacao == 1:
    print()
    print("#" * 70)
    print("Escolha o tipo de sapata rasa: \n"
          "Opção[1] - Sapata Isolada. \n"
          "Opção[2] - Sapata Corrida. \n"
          "Opção[3] - Sapata de Divisa. \n"
          "Opção[4] - Sapata Associada.")
    print("#" * 70)
    tipoSapata = int(input("Informe a opção desejada"
                           "para o tipo de sapata: "))

    # Início da condição que verifica o tipo sapata rasa.
    if tipoSapata == 1:
        cargaPilar = float(input("Informe o carregamento "
                                 "que chega no pilar em "
                                 "(tf): "))
        aPilar = float(input("Informe o lado (a) do pilar "
                             "em (m): "))
        bPilar = float(input("Informe o lado (b) do pilar "
                             "em (m): "))
        # Equação para determinar a área da sapata rasa em m².
        areaSapata = (1.05 * cargaPilar) / tSolo
        # Equação do 2º para determinar os lados da sapata
        # em (m).
        aSapata = (((aPilar - bPilar) / 2) +
                   math.sqrt(((aPilar - bPilar) ** 2) / 4) +
                   areaSapata)
        bSapata = areaSapata / aSapata
        # Cálculo dos balanços da sapata em (m).
        balanco = (aSapata - aPilar) / 2
        # Cálculo da altura do cone da sapata em (m).
        h = (aSapata - aPilar) / 3

        # Condição para determinar o melhor altura útil
        # do cone da sapata em (m).
        if h > lb:
            d = h * 1.25
        else:
            d = lb * 1.25
        # Cobrimento da armadura em (m).
        cob = 0.05
        h = d + cob
        # Altura da base da sapata em (m).
        h0 = d/3
        # Altura para apoiar a sapata em solos resistêntes.
        hTotalRasa = aSapata/2
        hTotalProfunda = aSapata*2
        # Equação para determinar o ângulo da sapata em graus.
        angulo = math.atan((h-h0)/balanco)*(180/math.pi)

        # Dimensionamento das armaduras na sapata.
        # Cálculo da tensão que a sapata gera no solo em
        # (tf/m²)
        tensaoSp = (1.05*cargaPilar)/(aSapata*bSapata)
        # Condição para verificar e calcular Xa e Xb.
        if (h/2) <= balanco <= (h*2):
            msgLimiteCBE70 = "Ok, os limites para calcular " \
                             "Xa e Xb estão dentro dos padrões" \
                             "da CBE-70"
            Xa = balanco + (0.15*aPilar)
            Xb = balanco + (0.15*bPilar)
        else:
            msgLimiteCBE70 = "ERRO, os limites para calcular" \
                             "Xa e Xb não estão dentro dos padrões" \
                             "da CBE-70 \n" \
                             "O tipo de fundação não é recomendado" \
                             "!"

