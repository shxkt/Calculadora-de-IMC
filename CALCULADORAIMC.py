import PySimpleGUI as sg

custom_font = ('Roboto', 16, 'bold')

sg.theme('LightGreen')
layout = [
    [sg.Text('Escolha a categoria', text_color='white', font=custom_font, pad=(15, 5))],
    [sg.Button('Adultos', font=custom_font, size=(10, 1), border_width=2, pad=(70, 20))],
    [sg.Button('Idosos', font=custom_font, size=(10, 1), border_width=2, pad=(70, 22))],
]

window = sg.Window('CALCULADORA IMC', layout, size=(280, 220), background_color="", font=custom_font)

while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Adultos' or event == 'Idosos':
        window.close()

        layout2 = [
            [
                sg.Text(f'Digite seu peso:'),
                sg.Input(key='peso', font=custom_font, size=(10, 2)),
            ],
            [
                sg.Text(f'Digite sua altura:'),
                sg.Input(key='altura', font=custom_font, size=(10, 2)),
            ],
            [sg.Button('Calcular', font=custom_font, size=(10, 2))],
        ]

        window2 = sg.Window('BY: dshykat', layout2, size=(280, 150), background_color="", font=custom_font)

        while True:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED:
                print('Encerrando!')
                break
            if event2 == 'Calcular':
                peso = float(values2['peso'])
                altura = float(values2['altura'])

                def calcular_imc(peso, altura):
                    calculo_imc = peso / (altura**2)
                    return calculo_imc

                calculo_imc = calcular_imc(peso, altura)

                if event == 'Adultos':
                    if calculo_imc <= 18.5:
                        print('IMC: {:.2f} - Você está abaixo do peso.'.format(calculo_imc))
                    elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
                        print('IMC: {:.2f} - Você está no peso adequado.'.format(calculo_imc))
                    elif calculo_imc >= 25 and calculo_imc <= 29.9:
                        print('IMC: {:.2f} - Você está com excesso de peso.'.format(calculo_imc))
                    elif calculo_imc >= 30 and calculo_imc <= 34.9:
                        print('IMC: {:.2f} - Você está com obesidade grau 1.'.format(calculo_imc))
                    elif calculo_imc >= 35 and calculo_imc <= 39.9:
                        print('IMC: {:.2f} - Você está com obesidade grau 2.'.format(calculo_imc))
                    elif calculo_imc >= 40:
                        print('IMC: {:.2f} - Você está com obesidade grau 3.'.format(calculo_imc))

                if event == 'Idosos':
                    if calculo_imc <= 22:
                        print('IMC: {:.2f} - Você está abaixo do peso.'.format(calculo_imc))
                    elif calculo_imc >= 22 and calculo_imc <= 27:
                        print('IMC: {:.2f} - Você está no peso adequado.'.format(calculo_imc))
                    elif calculo_imc >= 27:
                        print('IMC: {:.2f} - Você está sobrepeso.'.format(calculo_imc))

        window2.close()
