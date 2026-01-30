import cv2
import numpy as np
import os

def extract_histogram(image_path):
    # 1. Carrega a imagem
    image = cv2.imread(image_path)
    if image is None:
        return None

    # 2. Converte de BGR (padrão OpenCV) para HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 3. Calcula o histograma apenas para o canal H (Matiz/Cor)
    # Usamos 180 bins porque no OpenCV o Hue vai de 0 a 179
    hist = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])

    # 4. Normaliza o histograma
    # Isso é vital para que o tamanho da imagem ou distância não mude o resultado
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    return hist.flatten()

def load_dataset(folder_path):
    features = []
    image_names = []

    # Percorre os arquivos na pasta usando a lógica de IDs que você criou
    files = sorted(os.listdir(folder_path))
    
    for filename in files:
        if filename.endswith(".jpg"):
            path = os.path.join(folder_path, filename)
            hist = extract_histogram(path)
            
            if hist is not None:
                features.append(hist)
                image_names.append(filename)
    
    return np.array(features), image_names