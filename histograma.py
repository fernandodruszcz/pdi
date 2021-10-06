import cv2
import glob

# pega o nome de todas as imagens .png no diretorio atual
imgList = glob.glob("./*.png")
imgListSize = len(imgList)
methodsName = ["Correlation", "Chi Square", "Intersection", "Bhattacharyya Distance"]
methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_BHATTACHARYYA]
hitRate = [0.0, 0.0, 0.0, 0.0]

print("----------------Para as imagens coloridas----------------")
for method in methods:
    print(f'Testando o método {methodsName[methods.index(method)]}')
    hits = 0
    for i in range(imgListSize):
        # imagem a ser comparada
        img1 = cv2.imread(imgList[i])
        hist = cv2.calcHist([img1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

        # nos metodos chi square e bhattaryya distance quando menor for o valor melhor
        # ja em correlation e intersection ao contrario
        if((methods.index(method) == 1) or (methods.index(method) == 3)):
            closest = float('inf')
        else:
            closest = 0.0
        closestName = ""
        # comparacoes:
        for j in range(imgListSize):
            # if para nao comparar imagens iguais
            if i != j:
                img2 = cv2.imread(imgList[j])
                hist2 = cv2.calcHist([img2], [0 , 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

                comp = cv2.compareHist(hist, hist2, method)

                # nos metodos chi square e bhattaryya distance quando menor for o valor melhor
                # ja em correlation e intersection ao contrario
                if((methods.index(method) == 1) or (methods.index(method) == 3)):
                    if(comp < closest):
                        closest = comp
                        closestName = imgList[j]
                elif(comp > closest):
                    closest = comp
                    closestName = imgList[j]

                #print(f'Comparando imagem {imgList[i]} a {imgList[j]} \t\t comp={comp}')

        # pega o nome do personagem
        character1 = imgList[i][:-5]
        character2 = closestName[:-5]
        # verifica se o resultado esta correto
        if(character1 == character2):
            hits = hits + 1
        #print(f'\nO mais próximo de {character1} é {character2}')
    hitRate[methods.index(method)] = hits/imgListSize
    print(f'Hits = {hits}, hitRate = {hitRate[methods.index(method)]}')


print("----------------Para as imagens em tons de cinza----------------")

for method in methods:
    print(f'Testando o método {methodsName[methods.index(method)]}')
    hits = 0
    for i in range(imgListSize):
        # imagem a ser comparada
        img1 = cv2.imread(imgList[i], 0)
        hist = cv2.calcHist([img1], [0], None, [256], [0, 256])

        # nos metodos chi square e bhattaryya distance quando menor for o valor melhor
        # ja em correlation e intersection ao contrario
        if((methods.index(method) == 1) or (methods.index(method) == 3)):
            closest = float('inf')
        else:
            closest = 0.0
        closestName = ""
        # comparacoes:
        for j in range(imgListSize):
            # if para nao comparar imagens iguais
            if i != j:
                img2 = cv2.imread(imgList[j], 0)
                hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

                comp = cv2.compareHist(hist, hist2, method)

                # nos metodos chi square e bhattaryya distance quando menor for o valor melhor
                # ja em correlation e intersection ao contrario
                if((methods.index(method) == 1) or (methods.index(method) == 3)):
                    if(comp < closest):
                        closest = comp
                        closestName = imgList[j]
                elif(comp > closest):
                    closest = comp
                    closestName = imgList[j]

                #print(f'Comparando imagem {imgList[i]} a {imgList[j]}')

        # pega o nome do personagem
        character1 = imgList[i][:-5]
        character2 = closestName[:-5]
        # verifica se o resultado esta correto
        if(character1 == character2):
            hits = hits + 1
        #print(f'\nO mais próximo de {character1} é {character2}')
    hitRate[methods.index(method)] = hits/imgListSize
    print(f'Hits = {hits}, hitRate = {hitRate[methods.index(method)]}')

