import PySimpleGUI as sg 

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')],
]

janela = sg.Window('Login', layout=layout)

while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario_certo = 'MrThimas'
        senha_certa = '12345'
        usuario = values['usuario']
        senha = values['senha']

        if usuario == usuario_certo and senha == senha_certa:
            janela['mensagem'].update('Login feito com sucesso')
        else:
            janela['mensagem'].update('Senha errada')