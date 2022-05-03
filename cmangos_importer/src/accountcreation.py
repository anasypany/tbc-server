#!/usr/bin/python3

import socket
import time
import string
import secrets
import os
import requests
import discord



def generate_password(length):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def create_account(host, port, account_name, char_name):
    console_user = str(os.getenv('MANGOS_CONSOLE_USER'))
    console_pass = str(os.getenv('MANGOS_CONSOLE_PASSWORD'))
    if console_user == 'None':
        print("Please set the MANGOS_CONSOLE_USER environment variable to use the account creation functionality part of this script")
        exit()
    if console_pass == 'None':
        print("Please set the MANGOS_CONSOLE_PASSWORD environment variable to use the account creation functionality part of this script")
        exit()
    password = str(generate_password(12))
    discord_webhook_url = "https://discord.com/api/webhooks/970581812168507422/Eytl91bLoYe26qUlMJkR_IuyYjsHN2dWmQz8As0T2i4G_BnkC7K5mtQnca85IAbxkoa-"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    while True:
        data = s.recv(4096)
        # print(repr(data))
        if "Username:" in str(data):
            #print(repr(data))
            s.send((console_user + '\n').encode())
            time.sleep(.1)
        if "Password:" in str(data):
            #print(repr(data))
            s.send((console_pass + '\n').encode())
            time.sleep(.1)
        if "mangos>" in str(data):
            #print(repr(data))
            time.sleep(.1)
            command = 'account create ' + account_name + ' ' + password + ' ' + password + '\n'
            #print(command)
            s.send(command.encode())
            time.sleep(.1)
            data = s.recv(4096)
            #print(repr(data))
            if "Account created:" in str(data):
                command = 'account set addon ' + account_name + ' 1\n'
                #print(command)
                s.send(command.encode())
                time.sleep(.1)
                data = s.recv(4096)
                #print(repr(data))
                if "has been granted 1 expansion rights" in str(data):
                    command = 'account set gmlevel ' + account_name + ' 3\n'
                    #print(command)
                    s.send(command.encode())
                    time.sleep(.1)
                    data = s.recv(4096)
                    #print(repr(data))
                    if "You change security level of account" in str(data):
                        command = '.pdump load chars-sql/' + char_name + '.sql ' + account_name + '\n'
                        #print(command)
                        s.send(command.encode())
                        time.sleep(.1)
                        data = s.recv(4096)
                        #print(repr(data))
                        with open("accounts.txt", "a") as f:
                            f.write(char_name + ' ' + password + '\n')
                        with open("./macros/" + char_name + "-macros-cache.txt", "rb") as f:
                            macro_file = discord.File(f)
                        discord_webhook = discord.Webhook.from_url(discord_webhook_url, adapter=discord.RequestsWebhookAdapter())
                        discord_message = "Account Name: " + account_name + "\nPassword: " + password + "\nCharacter Imported: " + char_name
                        discord_webhook.send(discord_message, file=macro_file)
                        break
            elif "Account with this name already exist!" in str(data):
                print("account already exists, loading character")
                command = '.pdump load chars-sql/' + char_name + '.sql ' + account_name + '\n'
                #print(command)
                s.send(command.encode())
                time.sleep(.1)
                data = s.recv(4096)
                #print(repr(data))
                with open("./macros/" + char_name + "-macros-cache.txt", "rb") as f:
                    macro_file = discord.File(f)
                discord_webhook = discord.Webhook.from_url(discord_webhook_url, adapter=discord.RequestsWebhookAdapter())
                discord_message = "Account Name: " + account_name + "\nCharacter Imported: " + char_name
                discord_webhook.send(discord_message, file=macro_file)
            break
        if not data:
            break
        #print(repr(data))
    s.close()


#create_account('192.168.1.240', 3443, "jarptwo", "Jarppi")

# https://discord.com/api/webhooks/970588505145245726/l50cK-i2lAVrdY4F2Hi5daEfZoyQnwWb4qwGDiQKasXRhL1MactSGSq1uxIqSFa2vF8w
# https://discord.com/api/webhooks/970581812168507422/Eytl91bLoYe26qUlMJkR_IuyYjsHN2dWmQz8As0T2i4G_BnkC7K5mtQnca85IAbxkoa-

# https://discord.com/api/webhooks/970588505145245726/l50cK-i2lAVrdY4F2Hi5daEfZoyQnwWb4qwGDiQKasXRhL1MactSGSq1uxIqSFa2vF8w
