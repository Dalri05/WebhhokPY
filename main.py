import requests
import json
import pyautogui as bot
from os import system
from os import getlogin
from time import sleep

discord_webhook_url = input("Cole sua webhhok aqui: ")
getlogin()
username = getlogin()


import requests
import json

def msgwebhook():
    message_content = input("Digite sua mensagem: ")

    embed = {
        "title": "Mensagem do Usuário " + username,
        "description": message_content,
        "color": 16711680 
    }

    payload = {
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(discord_webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print('Mensagem enviada com sucesso para o Discord!')
        op = input("Deseja enviar mais mensagens? (sim/não): ")
        if op.lower() == "sim":
            msgwebhook()
        else:
            main()
    else:
        print(f'Erro ao enviar mensagem para o Discord. Código de status: {response.status_code}')




def spam():
    quantmsg = int(input("Digite a quantidade de mensagens que deseja enviar: "))
    message = { 'content':input("Digite sua mensagem: ")}
    
    for _ in range(quantmsg):
        json_message = json.dumps(message)
        print("Enviando mensagens...")
        response = requests.post(discord_webhook_url, data=json_message, headers={'Content-Type': 'application/json'})

        if response.status_code == 204:
            print('Mensagem enviada com sucesso para o Discord! deseja enviar mais? alguma mensagem')

def imgtela():
    screenshot = bot.screenshot()

    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)

    with open(screenshot_path, 'rb') as file:
        response = requests.post(discord_webhook_url, files={'file': file})
        system("cls")
        main()

    if response.status_code == 204:
        print('Print enviada...')
        sleep(3)
        system("cls")
        main()


def main():
    print('''
    Escolha sua opção
    
    [1] - Enviar mensagem via WebHook
    [2] - Spam de webhook
    [3] - Mandar print da tela 
    ''')
    op = int(input(":"))
    if op == 1:
        msgwebhook()
    elif op == 2:
        spam()
    elif op == 3:
        imgtela()
    else:
        print("Opção incorreta")


main()