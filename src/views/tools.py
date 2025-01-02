from PIL import Image,ImageDraw
import customtkinter as ctk

# Função para recortar a imagem em formato circular
def criar_imagem_circular(caminho_imagem, tamanho=(120, 120)):
    # Abrir a imagem
    imagem = Image.open(caminho_imagem)

    # Calcular o menor lado para criar um quadrado central
    lado_menor = min(imagem.size)
    esquerda = (imagem.width - lado_menor) // 2
    topo = (imagem.height - lado_menor) // 2
    direita = esquerda + lado_menor
    inferior = topo + lado_menor

    # Cortar a imagem para um quadrado central
    imagem = imagem.crop((esquerda, topo, direita, inferior))

    # Redimensionar para o tamanho desejado
    imagem = imagem.resize(tamanho, Image.LANCZOS)

    # Criar a máscara circular
    mascara = Image.new("L", tamanho, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, tamanho[0], tamanho[1]), fill=255)

    # Aplicar a máscara na imagem
    imagem_circular = Image.new("RGBA", tamanho, (0, 0, 0, 0))
    imagem_circular.paste(imagem, (0, 0), mask=mascara)

    # Converter para CTkImage
    return ctk.CTkImage(light_image=imagem_circular, size=tamanho)