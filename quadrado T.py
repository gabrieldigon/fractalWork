# Gabriel Dias Goncalves, fractal: Quadrado T.
# Disciplina AED2 - trabalho 1
import tkinter as tk
import random
colors = ["violet","aquamarine","salmon","dark sea green","tomato"]
def desenhar_quadrado(canvas, centro, comprimento_lado):
    metade_lado = comprimento_lado / 2
    x0, y0 = centro[0] - metade_lado, centro[1] - metade_lado
    print("Loading")
    # Essa linha acima esta presente pra facilitar ao testar fractais com niveis maiores
    x1, y1 = centro[0] + metade_lado, centro[1] + metade_lado
    canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill= random.choice(colors))

def desenhar_fractal(canvas, centro, comprimento_lado, profundidade):
    if profundidade == 0:
        desenhar_quadrado(canvas, centro, comprimento_lado)
    else:
        metade_lado = comprimento_lado / 2
        novo_comprimento_lado = metade_lado / 2
        deslocamentos = [(-metade_lado, -metade_lado), (metade_lado, -metade_lado), (-metade_lado, metade_lado), (metade_lado, metade_lado)]
        for deslocamento in deslocamentos:
            novo_centro = (centro[0] + deslocamento[0], centro[1] + deslocamento[1])
            desenhar_fractal(canvas, novo_centro, novo_comprimento_lado, profundidade - 1)
        desenhar_quadrado(canvas, centro, comprimento_lado)

def principal():
    raiz = tk.Tk()
    raiz.title("Fractal do Quadrado")
    
    tamanho_canvas = 1000
    canvas = tk.Canvas(raiz, width=tamanho_canvas, height=tamanho_canvas, bg='white')
    canvas.pack()
    
    comprimento_lado_inicial = 500
    centro_inicial = (tamanho_canvas / 2, tamanho_canvas / 2)
    niveis = 6  
    
    desenhar_fractal(canvas, centro_inicial, comprimento_lado_inicial, niveis)
    
    raiz.mainloop()

if __name__ == "__main__":
    principal()
