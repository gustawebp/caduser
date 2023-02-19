import PySimpleGUI as sg
import mysql.connector
import random
#BANCO DE DADOS - CONEXAO
conexao = mysql.connector.connect(
    
    
    host='localhost',
    user='root',
    password='',
    database='caduser'
)

cursor = conexao.cursor()

#LAYOUT DO PYSIMPLE

lista_temas = [
    'Black',
    'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey', 'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
sorteadoTema = random.choice(lista_temas) #SORTEIA UM TEMA 

sg.theme(sorteadoTema)


layout = [
    [sg.Text('O USUÁRIO QUE FOR CADASTRADO, SERÁ ENVIADO PARA O BANCO DE DADOS')],
    
    [sg.Text('Digite o nome :')],
    [sg.Input(key='nome', size=(20,1))],
    
    [sg.Text('Digite a idade:')],
    [sg.Input(key='idade', size=(20,1))],
    
    [sg.Text('Digite o telefone:')],
    [sg.Input(key='telefone', size=(20,1))],
    
    
    
    
    [sg.Button('Ok'), sg.Button('Cancelar')]
]



window = sg.Window('Exemplo', layout)


while True:
    event, values = window.read()
    nome_digitado = str(values['nome'])
    idade_digitado = str(values['idade'])
    telefone_digitado = str(values['telefone'])

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if event == 'Ok':
        # CREATE
        comando = "INSERT INTO users (username, idade, telefone) VALUES ('{0}', '{1}', '{2}' )".format(nome_digitado, idade_digitado, telefone_digitado)
        cursor.execute(comando)
        conexao.commit()  # edita o b de dados
        resultado = cursor.fetchall()  # ler o b de dados
        window.close()




