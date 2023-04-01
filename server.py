"""Main file which runs the server side."""
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import getenv

from dotenv import load_dotenv

load_dotenv()

HOST: str = getenv('HOST')
PORT = 8080
CLIENT_LIMIT = 5
connected_clients = []
bytes_recv = 2048


def listen_for_messages(client, username):
    """Use this function to accept message from user.

    Args:
        client (socket): communication end point.
        username (str): client username
    """
    while True:
        message = client.recv(bytes_recv).decode('utf-8')
        if message != '':
            final_msg = '{0} ~ {1}'.format(username, message)
            send_messages_to_all(final_msg)
        else:
            print('Сообщение от {0} пустое'.format(username))


def send_message_to_client(client, message):
    """Use this function to send a message to a client.

    Args:
        client (str): The name of the client
        message (str): The message to send to the client
    """
    client.sendall(message.encode())


def send_messages_to_all(message):
    """Use this function to send a message to all clients.

    Args:
        message (str): The message to send to the client
    """
    for user in connected_clients:
        send_message_to_client(user[1], message)


def client_connect(client):
    """Use this function to connect to a client.

    Args:
        client (str): The name of the client
    """
    while True:
        username = client.recv(bytes_recv).decode('utf-8')
        if username != '':
            connected_clients.append((username, client))
            prompt_message = 'СЕРВЕР~ {0} присоединился к чату'.format(username)
            send_messages_to_all(prompt_message)
            break
        else:
            print('Пустой ник')
    Thread(target=listen_for_messages, args=(client, username)).start()


def main():
    """Use this function to start a server."""
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except Exception:
        print('Не удается привязаться к хосту {0} и порту {1}'.format(HOST, PORT))
    else:
        print('Запуск сервера на {0} {1}'.format(HOST, PORT))
    server.listen(CLIENT_LIMIT)
    while True:
        client, address = server.accept()
        print('Успешно подключен к клиенту {0} {1}'.format(address[0], address[1]))
        Thread(target=client_connect, args=(client, )).start()


if __name__ == '__main__':
    main()
