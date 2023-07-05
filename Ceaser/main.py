import tkinter as tk
from code import code
from decode import decode

root = tk.Tk()

window = tk.Canvas(root, width=1280, height=860, relief='raised')
root.title('Ceaser')
window.pack()


title = tk.Label(root, text='Кодування та декодування повідомлень')
title.config(font=('helvetica', 18))
window.create_window(620, 45, window=title)

text_1 = tk.Label(root, text='Крок шифрування:')
text_1.config(font=('helvetica', 14))
window.create_window(620, 70, window=text_1)

step = tk.Entry(root)
step.config(width=10)
window.create_window(620, 100, window=step)

# text_2 = tk.Label(root, text='Повідомлення:')
# text_2.config(font=('helvetica', 14))
# window.create_window(620, 150, window=text_2)
#
# user_message = tk.Text(root, width=50, height=5, font=('Arial', 14))
# window.create_window(620, 220, window=user_message)


text_2 = tk.Label(root, text='Повідомлення:')
text_2.config(font=('helvetica', 10))
window.create_window(512, 120, window=text_2)

user_message = tk.Entry(root)
user_message.config(width=50, font=('Arial', 14))
window.create_window(620, 220, window=user_message)

def button_code():
    int_step = int(step.get())
    user_message_data = user_message.get().upper()
    new_message = code(user_message_data, int_step)
    label3 = tk.Label(root, text=f'Ваше повідомлення з кроком {int_step} '
                                 f'успішно закодовано!',
                      font=('helvetica', 10))
    window.create_window(620, 260, window=label3)
    label4 = tk.Label(root, text='УВАГА! Не повідомляйте крок стороннім особам'
                                 ' крім адресата та беспосереднього командира',
                      font=('helvetica', 10, 'bold'))
    window.create_window(620, 280, window=label4)

    text_widget = tk.Text(root, height=10, width=50)
    text_widget.place(x=325, y=350)
    text_widget.insert(tk.END, "Ваше повідомлення: " + new_message)

def button_decode():
    int_step = int(step.get())
    user_message_data = user_message.get().upper()
    new_message = decode(user_message_data, int_step)

    label3 = tk.Label(root, text=f'Ваше повідомлення з кроком {int_step} '
                                 f'декодовано!\n '
                                 f'Можете його скопіювати та '
                                 f'роздрокувати данні.',
                      font=('helvetica', 10))
    window.create_window(620, 290, window=label3)

    label4 = tk.Label(root, text='УВАГА! Повідомлення яке ви отримали має ВИЩИЙ рівень приватності! Передавати повідомлення стороннім особам\n'
                                 'СУВОРО ЗАБОРОНЕНО! Негайно передайте повідомлення Вашому командиру!',
                      font=('helvetica', 10, 'bold'))
    window.create_window(620, 320, window=label4)

    text_widget = tk.Text(root, height=10, width=50)
    text_widget.place(x=325, y=350)
    text_widget.insert(tk.END, "Ваше повідомлення: " + new_message)

def close_window():
    root.destroy()

label5 = tk.Label(root, text='Після кодування або декодування повідомлення закрий застосунок!\n'
                             ' При необхідності запусти заново.',
                      font=('helvetica', 10, 'bold'))
window.create_window(620, 800, window=label5)

button = tk.Button(root, text="Закрити застосунок", command=close_window,
                   bg='brown', fg='white', font=('helvetica', 9, 'bold'))
window.create_window(620, 830, window=button)


button1 = tk.Button(text='Кодувати повідомлення', command=button_code,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
window.create_window(620, 300, window=button1)

button2 = tk.Button(text='Декодувати повідомлення', command=button_decode,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
window.create_window(620, 350, window=button2)
if __name__ == '__main__':

    root.mainloop()