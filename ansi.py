import tkinter as tk
from tkinter import filedialog

def save_to_file():
    filename = filename_entry.get()
    x_value = x_entry.get()
    y_value = y_entry.get()
    input_text = input_text_area.get("1.0", "end-1c")  # Pega o texto da área de entrada

    # Função para formatar o texto com as cores
    def format_text(text, color):
        formatted_text = ""
        for char in text:
            formatted_text += f"\x1b[38;5;{color}m{char}\x1b[0m"
        return formatted_text

    formatted_text = format_text(input_text, 0xf0)  # 15 é a cor inicial (0x0f)

    # Salva o texto formatado no arquivo
    with open(filename, 'w') as file:
        file.write(formatted_text)

# Cria a janela principal
root = tk.Tk()
root.title("Janela Azul")
root.configure(bg="blue")

# Caixa de texto para o nome do arquivo
filename_label = tk.Label(root, text="Nome do Arquivo:")
filename_label.configure(bg="blue")
filename_label.pack()
filename_entry = tk.Entry(root)
filename_entry.pack()

# Caixa de texto para o valor x
x_label = tk.Label(root, text="Valor de x:")
x_label.configure(bg="blue")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

# Caixa de texto para o valor y
y_label = tk.Label(root, text="Valor de y:")
y_label.configure(bg="blue")
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()

# Área de texto para entrada de texto
input_text_label = tk.Label(root, text="Texto de Entrada:")
input_text_label.configure(bg="blue")
input_text_label.pack()
input_text_area = tk.Text(root, height=10, width=40)
input_text_area.configure(bg="blue")
input_text_area.pack()

# Botão para salvar o texto no arquivo
save_button = tk.Button(root, text="Salvar", command=save_to_file)
save_button.configure(bg="blue")
save_button.pack()

root.mainloop()

