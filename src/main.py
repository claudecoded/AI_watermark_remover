import cv2
import numpy as np
import os

def remove_watermark(image_path, output_path, low_threshold=150, high_threshold=255):
    """
    Remove marcas d'água de imagens utilizando a técnica de Inpainting do OpenCV.
    
    :param image_path: Caminho da imagem original.
    :param output_path: Caminho onde a imagem processada será salva.
    :param low_threshold: Limiar inferior para detecção de tons claros/brancos da marca.
    :param high_threshold: Limiar superior para a máscara.
    """
    if not os.path.exists(image_path):
        print(f"Erro: O arquivo {image_path} não foi encontrado.")
        return

    # 1. Carrega a imagem original
    img = cv2.imread(image_path)

    # 2. Converte para escala de cinza para facilitar a detecção de formas/textos
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Cria uma máscara binária (detecta pixels claros que geralmente formam marcas d'água)
    # Ajuste os thresholds se a marca d'água for escura ou colorida
    _, mask = cv2.threshold(gray, low_threshold, high_threshold, cv2.THRESH_BINARY)

    # 4. Aplica o algoritmo de Inpainting para preencher a área da máscara
    # cv2.INPAINT_TELEA é ideal para restauração rápida e remoção de ruídos textuais
    result = cv2.inpaint(img, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # 5. Salva o resultado final
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, result)
    print(f"Sucesso! Imagem sem marca d'água salva em: {output_path}")

if __name__ == "__main__":
    # Exemplo de uso local
    # Certifique-se de criar uma pasta 'input' com uma imagem dentro para testar
    INPUT_IMAGE = "input/imagem_com_marca.jpg"
    OUTPUT_IMAGE = "output/imagem_limpa.jpg"
    
    print("Iniciando a remoção da marca d'água...")
    remove_watermark(INPUT_IMAGE, OUTPUT_IMAGE)
