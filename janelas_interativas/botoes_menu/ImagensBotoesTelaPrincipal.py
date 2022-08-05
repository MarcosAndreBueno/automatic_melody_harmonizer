class ImagensBotaoTelaPrincipal:
    global listIMG
    listIMG = []

    def set(self, img):
        listIMG.append(img)

    def get(self, pos):
        img = listIMG[pos-1]
        return img
