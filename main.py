import requests
import json
from os import system
from time import sleep

discord_webhook_url = input("Cole sua webhhok aqui: ")


def msgwebhook():
    message = { 'content':input("Digite sua mensagem: ")}
    json_message = json.dumps(message)

    response = requests.post(discord_webhook_url, data=json_message, headers={'Content-Type': 'application/json'})

    if response.status_code == 204:
        print('Mensagem enviada com sucesso para o Discord! deseja enviar mais? alguma mensagem')
        op = input(":")
        if op == "sim":
            system("cls")
            msgwebhook()
        else:
            system("cls")
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


def main():
    print('''
    Escolha sua opção
    
    [1] - Enviar mensagem via WebHook
    [2] - Spam de webhook
    [6]
    ''')
    op = int(input(":"))
    if op == 1:
        msgwebhook()
    elif op == 2:
        spam()
    else:
        print("Opção incorreta")


main()