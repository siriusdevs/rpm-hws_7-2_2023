"""Main file which runs the client side."""
import tkinter as tkin
from os import getenv
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

from dotenv import load_dotenv
from tkinter import scrolledtext, messagebox

load_dotenv()

HOST: str = getenv('HOST')
try:
    PORT = int(getenv('PORT'))
except ValueError:
    PORT = 8001

client = socket(AF_INET, SOCK_STREAM)

GREY = '#696969'
MED_GREY = '#A9A9A9'
BLUE = '#64A292'
WHITE = 'white'
FONT = ('Arial', 17)
BUTTON_FONT = ('Arial', 15)
SMALL_FONT = ('Arial', 13)
bytes_recv = 2048


def send_message():
    """Use this function to send the message."""
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
    else:
        messagebox.showerror('Сообщение не может быть пустым!')


def connect():
    """Use this function to connect to the server."""
    try:
        client.connect((HOST, PORT))
    except Exception:
        messagebox.showerror(
            'Не удалось подключиться к серверу',
            'Не удалось подключиться к серверу {0}:{1}'.format(HOST, PORT),
        )
    else:
        add_message('[СЕРВЕР] Успешное подключение к серверу')
        print('Успешное подключение к серверу')

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror('Неправильное имя', 'Имя не может быть пустым')

    Thread(target=messages_from_server, args=(client, )).start()

    username_textbox.config(state=tkin.DISABLED)
    username_button.config(state=tkin.DISABLED)


def add_message(message):
    """Use this function to add the text in the message.

    Args:
        message (str): The message to people
    """
    message_box.config(state=tkin.NORMAL)
    message_box.insert(tkin.END, '{0}\n'.format(message))
    message_box.config(state=tkin.DISABLED)


def messages_from_server(clien):
    """Use this function to receive messages from others.

    Args:
        clien (socket): communication end point.
    """
    while True:
        message = clien.recv(bytes_recv).decode('utf-8')
        if message != '':
            username = message.split('~')[0]
            text_content = message.split('~')[1]
            add_message('[{0}] {1}'.format(username, text_content))

        else:
            messagebox.showerror(
                'Ошибка', 'Сообщение, полученное от клиента, пустое',
            )


root = tkin.Tk()
root.geometry('670x670')
root.title('Chat')
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=10)

# window options
frame_width = 600
top_frame_height = 100
midl_frame_height = 300
bottom_frame_height = 500
username_textbox_width = 23
username_label_padx = 10
username_button_padx = 15
message_textbox_width = 38
message_textbox_padx = 10
message_button_padx = 10
messg_box_width = 67
messg_box_height = 28.5

top_frame = tkin.Frame(root, width=frame_width, height=top_frame_height, bg=GREY)
top_frame.grid(row=0, column=0, sticky=tkin.NSEW)

middle_frame = tkin.Frame(root, width=frame_width, height=midl_frame_height, bg=MED_GREY)
middle_frame.grid(row=1, column=0, sticky=tkin.NSEW)

bottom_frame = tkin.Frame(root, width=frame_width, height=bottom_frame_height, bg=GREY)
bottom_frame.grid(row=2, column=0, sticky=tkin.NSEW)

username_label = tkin.Label(top_frame, text='Введите имя:', font=FONT, bg=GREY, fg=WHITE)
username_label.pack(side=tkin.LEFT, padx=username_label_padx)

username_textbox = tkin.Entry(top_frame, font=FONT, bg=MED_GREY, fg=WHITE, width=username_textbox_width)
username_textbox.pack(side=tkin.LEFT)

username_button = tkin.Button(top_frame, text='Присоединиться', font=BUTTON_FONT, bg=BLUE, fg=WHITE, command=connect)
username_button.pack(side=tkin.LEFT, padx=username_button_padx)

message_textbox = tkin.Entry(bottom_frame, font=FONT, bg=MED_GREY, fg=WHITE, width=message_textbox_width)
message_textbox.pack(side=tkin.LEFT, padx=message_textbox_padx)

message_button = tkin.Button(bottom_frame, text='Отправить', font=BUTTON_FONT, bg=BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tkin.LEFT, padx=message_button_padx)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MED_GREY, fg=WHITE, width=messg_box_width, height=messg_box_height)
message_box.config(state=tkin.DISABLED)
message_box.pack()


def main():
    """Use this function to open chat window."""
    root.mainloop()


if __name__ == '__main__':
    main()
