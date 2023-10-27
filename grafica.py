import tkinter as tk
from PIL import Image, ImageTk
import time
from functools import partial
from tkinter import messagebox

def pintar(canvas, x, y, image_path):
    img = Image.open(image_path)
    img = img.resize((cell_size, cell_size), Image.LANCZOS)  # Redimensiona la imagen al tamaño de la celda
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(y * cell_size, x * cell_size, anchor=tk.NW, image=photo)
    canvas.photo = photo
    time.sleep(0.1)  # Añadir un pequeño retraso para visualización
    canvas.update()

def draw_cell(canvas, x, y, color):
    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill=color)

def start_visualization(grid, start, finish,nodos_recorridos, costo):
    root = tk.Tk()
    root.title("Recorrido de nodos")

    canvas = tk.Canvas(root, width=len(grid[0]) * cell_size, height=len(grid) * cell_size+100)
    canvas.pack()
    
    grid[finish[0]][finish[1]] = 4 
    grid[start[0]][start[1]] = 5 
    image_paths = {
        3: './imgs/gato.png',
        -2: './imgs/amo.png',
        4: './imgs/muriel.png',
        5: './imgs/coraje.png'
    }
    image_references = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                draw_cell(canvas, row, col, "black")
            elif grid[row][col] == 1:
                draw_cell(canvas, row, col, "white")
            # elif grid[row][col] == 3:
            #     draw_cell(canvas, row, col, "green")
            elif grid[row][col] in image_paths:
                img = Image.open(image_paths[grid[row][col]])
                img = img.resize((cell_size, cell_size), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                image_references[(row, col)] = photo  # Guarda la referencia de la imagen
                canvas.create_image(col * cell_size, row * cell_size, anchor=tk.NW, image=photo)
    
    canvas.create_text(300, 410, text='Inicio: '+ str(start), fill="black", font=("Arial", 10, "bold"))
    canvas.create_text(300, 430, text='Meta: '+ str(finish), fill="black", font=("Arial", 10, "bold"))
    canvas.create_text(300, 450, text='Costo: '+ str(costo), fill="black", font=("Arial", 10, "bold"))
    canvas.create_text(320, 470, text='Recorrido: '+ str(nodos_recorridos), fill="black", font=("Arial", 8, "bold"))
    
    # Crear un botón de inicio
    start_button = tk.Button(root, text="Iniciar", command=partial(recorrido,grid, nodos_recorridos, canvas, start))
    start_button.pack()
    
    root.mainloop()



def recorrido(grid, nodos_recorridos, canvas, start):
    # print(nodos_recorridos)
    for nodo in nodos_recorridos:
        if grid[start[0]][start[1]] == 5:
            draw_cell(canvas, start[0],start[1], "white")
        
        if nodo[0] == 's':
            messagebox.showinfo("ERROR", "EL PROBLEMA NO TIENE SOLUCIÓN PORQUE NO SE PUEDE LLEGAR A LA META DEBIDO A LOS OBSTACULOS")
        if grid[nodo[0]][nodo[1]] == 3:
            pintar(canvas, nodo[0], nodo[1], './imgs/coraje_asustado.png')
        if grid[nodo[0]][nodo[1]] == -2:
            pintar(canvas, nodo[0], nodo[1], './imgs/coraje_asustado.png')
        if grid[nodo[0]][nodo[1]] == 4:
            pintar(canvas, nodo[0], nodo[1], './imgs/coraje_feliz.png')
        pintar(canvas, nodo[0], nodo[1], './imgs/coraje.png')
            
cell_size = 80  # Tamaño de cada celda en píxeles



