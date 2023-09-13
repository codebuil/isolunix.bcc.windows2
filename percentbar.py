import tkinter as tk
import math
import time

def desenhar_meio_circulo(canvas):
    # Calcula as coordenadas para o meio círculo
    centro_x, centro_y = 150, 150
    raio = 100
    canvas.create_arc(centro_x - raio, centro_y - raio, centro_x + raio, centro_y + raio, start=210, extent=-120, fill="yellow", outline="yellow")

def atualizar_barra_porcentagem(canvas, porcentagem):
    # Calcula o ângulo correspondente à porcentagem
    angulo = (porcentagem / 100) * 180  # 180 graus no total (meio círculo)

    # Calcula as coordenadas para a extremidade da barra
    centro_x, centro_y = 150, 280
    raio = 100
    x1 = centro_x - raio * math.cos(math.radians( angulo))
    y1 = centro_y - raio * math.sin(math.radians( angulo))
    root.title(f"Porcentagem: {porcentagem}%")
    # Atualiza a barra de porcentagem
    canvas.coords(barra, centro_x, centro_y, x1, y1)

def testar_barra_porcentagem():
    porcentagem = 0
    while porcentagem <= 100:
        atualizar_barra_porcentagem(canvas, porcentagem)
        porcentagem += 10
        root.update()
        time.sleep(1)

# Criar a janela
root = tk.Tk()
root.title("Meio Círculo e Barra de Porcentagem")
root.configure(bg="yellow")
root.geometry("300x300")

# Canvas para desenhar o meio círculo e a barra de porcentagem
canvas = tk.Canvas(root, width=300, height=300, bg="yellow")
canvas.pack()

# Desenha o meio círculo
desenhar_meio_circulo(canvas)

# Cria a barra de porcentagem vazia
barra = canvas.create_line(150, 280, 150, 50, width=10, fill="black")

# Chama a sub-rotina principal para testar a barra de porcentagem
testar_barra_porcentagem()

root.mainloop()

