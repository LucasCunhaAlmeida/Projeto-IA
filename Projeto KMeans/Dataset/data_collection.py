import cv2
import os

# Configurações iniciais
SAVE_PATH = "images/"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Função para pegar o próximo ID disponível (Auto incremento)
def get_next_id(folder):
    files = os.listdir(folder)
    # Filtra apenas arquivos que começam com 'img_' e terminam com '.jpg'
    ids = [int(f.split('_')[1].split('.')[0]) for f in files if f.startswith('img_') and f.endswith('.jpg')]
    return max(ids) + 1 if ids else 1

cap = cv2.VideoCapture(0)
print("Pressione 'S' para salvar a imagem ou 'Q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Exibe instruções na tela
    cv2.putText(frame, "Pressione 'S' para Capturar", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Captura de Objetos", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    # Salvar imagem
    if key == ord('s'):
        obj_id = get_next_id(SAVE_PATH)
        filename = f"img_{obj_id}.jpg"
        cv2.imwrite(os.path.join(SAVE_PATH, filename), frame)
        print(f"Salvo: {filename}")

    # Sair (tecla Q ou fechar no X)
    elif key == ord('q') or cv2.getWindowProperty("Captura de Objetos", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()