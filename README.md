# SEL0337
Repositório Aplicação de Microprocessadores 2

# Explicação Referente ao Código Camera.py

Foram utilizadas as bibliotecas picamera e time. Da picamera foi utilizada a função PiCamera, responsável por capturar imagens e vídeos. Já da time foi utilizada a
função sleep, responsável por adicionar um delay especifico durante a execução do código.

O funcionamento do código acontece da seguinte maneira: primeiramente é iniciado a câmera (linha 8) e é definida algumas configurações iniciais, tal como a rotação
da imagem a ser capturada (linha 9) e a resolução da mesma (linha 10). Após isso o código é dividido em duas partes, uma referente a captura da imagem e a outra re-
ferente a captura do vídeo. Para a captura da imagem foi mostrado a pré-vizualização da imagem que a câmera iria capturar, adicionado do nome dos integrantes do gru-
po, (linhas 14 e 15) e após dois segundos foi capturada a imagem (linhas 16 e 17), finalizando a pré-vizualização da imagem (linha 18).

Já para a captura do vídeo os passos são semelhantes, alterando somente a função utilizada para a captura. Assim, é iniciado a captura do vídeo e após cinco segun-
dos o vídeo é encerrado e salvo (linhas 25, 26 e 27). Vale ressaltar que tanto as imgens capturadas quanto os vídeos são salvos nos diretórios passados como parâme-
tros para as funções de captura. Os resultados obtidos com este códgio podem ser vistos nos arquivos "ImagemCamera.jpg" e "VideoCamera.h264".

# Explicação Referente ao Códgio Clima.py

Foram utilzadas as bibliotecas json, requests e pprint. Da requests foi utilizada a função get, responsável por adquirir os dados presentes nos servidores, e da pprint
foi usada a função pprint, responsável por printar os dados adquiridos de maneira organizada.

O funcionamento do código ocorre da seguinte maneira: primeiramente obtemos a URL em que contém os dados relacionados ao clima obtido pela estação de ID 966583 e guar-
damos o mesmo em uma variável (linha 9). Após isso obtemos esses dados em formato json e armazenamos em outra variável (linha 11). Estes dados obtidos são printados
utilizando a função pprint (linha 12). O resultado obtido com este código pode ser visto no arquivo "clima.jpg".
