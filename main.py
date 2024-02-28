import requests
import json
import pyshorteners
import pyautogui as bot
from os import system, remove, getlogin, path
from time import sleep



getlogin()
username = getlogin()

def newweb():
    try:
        webhook_url = input("Digite a URL da webhook: ")
        with open('webhook.txt', 'w') as file:
            file.write(webhook_url)
        print("Webhook salva com sucesso")
        system("cls")
        main()
        return webhook_url
    except Exception as e:
        print(f"Erro ao salvar a webhook: {str(e)}")
        return None

def get_webhook_from_file():
    try:
        with open('webhook.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

discord_webhook_url = get_webhook_from_file() or newweb()

def deleteweb():
    try:
        if path.exists('webhook.txt'):
            remove('webhook.txt')
            print("Webhhok removida")
            system("cls")
            main()
        else:
            print("O arquivo 'webhook.txt' não existe.")
    except Exception as e:
        print(f"Erro ao excluir': {str(e)}")

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

def shorturl():
    url = input("cole seu url aqui: ")
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)

    embed = {
        "title": "Aqui esta seu URL: ",
        "description": short_url,
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
        print("Url enviada com sucesso, retornando ao menu...")
        sleep(4)
        system("cls")
        main()
    else:
        print(f'Erro ao enviar mensagem para o Discord. Código de status: {response.status_code}')

def main():
    print('''
    Escolha sua opção
    
    [1] - Enviar mensagem via WebHook
    [2] - Spam de webhook
    [3] - Mandar print da tela 
    [4] - Encurtador de URL
    [5] - Ver github
    -----------------------------------
    [8] - cadastrar webhook
    [9] - remover webhook
    [10] - sair
    ''')
    op = int(input(":"))
    if op == 1:
        msgwebhook()
    elif op == 2:
        spam()
    elif op == 3:
        imgtela()
    elif op == 4:
        shorturl()
    elif op == 5:
        print()
    elif op == 8:
        newweb()
    elif op == 9:
        deleteweb
    elif op == 10:
        exit
    else:
        print("Opção incorreta")


main()