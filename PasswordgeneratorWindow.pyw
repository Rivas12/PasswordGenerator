import PySimpleGUI  as sg
import random
import os

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Password = []


#Layout
layout = [
    [sg.Text('Digite o tamanho da senha:'), sg.Slider(range=(8,50), default_value=12, orientation='h', key='SizePass')],
    [sg.Text('Quer letras maiúsculas:'), sg.Checkbox('', key='maiuscula')],
    [sg.Text('Quer números: '), sg.Checkbox('', key='numeros')],
    [sg.Text('Quer simbolos (@#$%)'), sg.Checkbox('', key='simbolos')],
    [sg.Button('Gerar senha', key='gerar'), sg.Button('Cancelar', key='cancelar')],
]
#Janela
janela = sg.Window("Gerador de senhas", use_default_focus=False).layout(layout)
#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'cancelar':
        janela.close()
        break
    if eventos == 'gerar':
        for _ in range(int(valores['SizePass'])):
            Password.append(''.join(random.sample(Letters, 1)))
        if valores['maiuscula'] == True: 
            ContadorMaiusculas = 0
            for i in range(int(valores['SizePass'])):
                if random.choice([1, 2, 3]) == 1:
                    ContadorMaiusculas += 1
                    Password[i] = Password[i].upper()
            if ContadorMaiusculas == 0:
                ValorAleatorioM = range(int(valores['SizePass']))
                Password[random.choice(ValorAleatorioM)] = Password[ValorAleatorioM].upper()
        
        if valores['numeros'] == True:
            ContadorNumeros = 0
            for i in range(int(valores['SizePass'])):
                if random.choice([1, 2, 3, 4]) == 1:
                    ContadorNumeros += 1
                    Password[i] = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1))
            if ContadorNumeros == 0:
                ValorAleatorioS = range(int(valores['numeros']))
                Password[random.choice(ValorAleatorioS)] = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1))
        
        if valores['simbolos'] == True:
            ContadorSimbolos = 0
            for i in range(int(valores['SizePass'])):
                if random.choice([1, 2, 3, 4]) == 1:
                    if not ContadorSimbolos > valores['SizePass'] * 0.2:
                        ContadorSimbolos += 1
                        Password[i] = ''.join(random.sample(['@','#', '$', '%'], 1))
            if ContadorSimbolos == 0:
                ValorAleatorioS = range(int(valores['SizePass']))
                Password[random.choice(ValorAleatorioS)] = ''.join(random.sample(['@','#', '$', '%'], 1))
                    
        layoutGerar = [
            [sg.Text(f"Sua senha é: {''.join(Password)}")],
            [sg.Button('Copiar', key='copiar'), sg.Button('Fechar', key='fechar')]
        ]
        janelaGerar = sg.Window("Resultado", use_default_focus=False).layout(layoutGerar)
        while True:
            eventosGerar, valoresGerar = janelaGerar.read()
            if eventosGerar == sg.WIN_CLOSED:
                janelaGerar.close()
                break
            if eventosGerar == 'copiar':
                os.system('echo ' + ''.join(Password) + '| clip')
                janelaGerar.close()
            if eventosGerar == 'fechar':
                janelaGerar.close()
                
    Password.clear()
        
        
