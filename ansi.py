import tkinter as tk
from tkinter import filedialog

def save_to_file():
    filename = filename_entry.get()
    x_value = x_entry.get()
    y_value = y_entry.get()
    
    input_text = input_text_area.get("1.0", "end-1c")  # Pega o texto da área de entrada

    # Função para formatar o texto com as cores
    def format_text(text):
        bcolor=0
        ccolor=0
        ints=0
        strs=""
        formatted_text =  f"\033[40;37m"
        for char in text:
            if ints > 0:
                if char == '\\':
                    formatted_text += f"{char}"
                if char >= '0':
                    if char <= '9':
                        strs+=f"{char}"
                        ints=ints+1
                if char >= 'a':
                    if char <= 'f':
                        strs+=f"{char}"
                        ints=ints+1
                if char >= 'A':
                    if char <= 'F':
                        strs+=f"{char}"
                        ints=ints+1

            if ints == 0:
                if char == '\\':
                    ints=1
                else:
                    formatted_text += f"{char}"
            if ints > 2:
                bcolor=((int(strs,16) & 0xF0) >> 4)+40
                ccolor=((int(strs,16) & 0xF))+30
                formatted_text += f"\033[{bcolor};{ccolor}m"
                ints=0
            
        return formatted_text

    formatted_text = format_text(input_text)  

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

