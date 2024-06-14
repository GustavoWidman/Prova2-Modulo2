# face-detector (Prova2-Modulo2)

## Descrição

Esse projeto é uma CLI que detecta faces em um vídeo e desenha um retângulo em volta de cada face detectada. A CLI foi feita em Python e utiliza a biblioteca OpenCV para a detecção de faces.

![usage](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/3f921dcd-c729-4b06-af65-9204cbdd9b3d)

## Perguntas Técnicas

### 1. Descreva o funcionamento do método de detecção escolhido

O método de detecção escolhido foi o Haar Cascade. O Haar Cascade é um método de detecção de objetos em imagens digitais que utiliza um classificador em cascata para detectar objetos em imagens. O classificador em cascata é treinado a partir de um grande número de imagens positivas e negativas.

### 2. Ordene HAAR Cascade, CNN, NN Linear e Filtros de correlação cruzada em termos de viabilidade técnica

1. Haar Cascade
2. Filtros de correlação cruzada
3. CNN
4. NN Linear

Coloquei o Haar Cascade em primeiro lugar porque ele é um método de detecção de objetos em imagens digitais que é muito eficiente e rápido. Ele é muito utilizado para detecção de faces em imagens e vídeos. Os filtros de correlação cruzada são um método de detecção de objetos em imagens digitais que é muito eficiente e rápido. Eles são muito utilizados para detecção de objetos em imagens e vídeos. As CNNs são um método de detecção de objetos em imagens digitais que são muito eficientes e rápidas. Elas são muito utilizadas para detecção de objetos em imagens e vídeos. As NNs lineares são um método de detecção de objetos em imagens digitais que são muito eficientes e rápidas. Elas são muito utilizadas para detecção de objetos em imagens e vídeos.

### 3. Classifique os mesmos métodos mas levando em consideração a detecção de emoções

1. CNN
2. Filtros de correlação cruzada
3. Haar Cascade
4. NN Linear

Coloquei as CNNs em primeiro lugar porque elas são muito eficientes e rápidas para detecção de emoções em imagens digitais. Existe um dataset chamado `fer2013` que é muito utilizado para treinar CNNs para detecção de emoções em imagens digitais e poderia facilmente ser utilizado aqui. Os filtros de correlação cruzada são um método de detecção de objetos em imagens digitais que é muito eficiente e rápido. Eles são muito utilizados para detecção de objetos em imagens e vídeos. O Haar Cascade é um método de detecção de objetos em imagens digitais que é muito eficiente e rápido. Ele é muito utilizado para detecção de faces em imagens e vídeos. As NNs lineares são um método de detecção de objetos em imagens digitais que são muito eficientes e rápidas. Elas são muito utilizadas para detecção de objetos em imagens e vídeos.

### 4. Alguma das técnicas tem a capacidade de considerar variações de um frame para o outro?

Sim, CNNs são capazes de considerar variações de um frame para o outro. CNNs são muito eficientes e rápidas para detecção de objetos em imagens digitais e podem ser utilizadas para detectar objetos em vídeos. Elas são capazes de considerar variações de um frame para o outro porque elas são capazes de aprender padrões em imagens digitais e podem ser treinadas para detectar objetos em vídeos. Isso também pode ser feito com filtros de correlação cruzada, mas CNNs são mais eficientes e rápidas.

### 5. Quem vai ganhar a bola de ouro 2024?

Mbappé vai ganhar a bola de ouro 2024. Certeza absoluta.

## Dependencias

As dependencias necessárias para rodar a CLI são:

- [rich](https://pypi.org/project/rich/) v13.7.1
- [typer](https://pypi.org/project/typer/) v0.12.3
- [inquirer](https://pypi.org/project/inquirer/) v3.2.4
- [yaspin](https://pypi.org/project/yaspin/) v3.0.2
- [opencv-python](https://pypi.org/project/opencv-python/) v4.10.0.82

Também é necessário ter o dataset `alt` do Haar Cascade para detecção de faces. Ele vem incluso com esse repositório, mas você pode baixar ele [aqui](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml). Coloque-o no diretório `data` desses repositório com o nome `haarcascade_frontalface_alt.xml`.

## Instalação e Utilização

Para rodar a CLI, basta rodar o script `src/main.py` com o python, porem, nao esqueca de criar um ambiente virtual e instalar as dependencias antes de rodar o script. Você pode fazer isso com os seguintes comandos:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Depois de instalar as dependencias, você consultar a mensagem de ajuda da CLI com o seguinte comando:

```bash
$ python3 src/main.py --help

 Usage: main.py [OPTIONS] INPUT OUTPUT

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    input       FILE  The input file path [default: None] [required]                                                                      │
│ *    output      PATH  The output file path. [default: None] [required]                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                    │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                             │
│ --help                        Show this message and exit.                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Esse comando mostrara a utilização básica da CLI.

## Demonstração

Segue o video de demonstração da CLI, além do video de entrada e saída utilizados no video de demonstração.

![la_cabra](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/aada0b73-63b4-4cbf-836f-4c73a621d902)

![usage](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/3f921dcd-c729-4b06-af65-9204cbdd9b3d)

![output](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/e3c98487-4de4-423d-b92f-3f59e7ef4e24)

## Exemplos

Aqui estão alguns exemplos de como você pode usar a CLI:

```bash
# Percorre todos os frames do video e desenha um retângulo em volta de cada face detectada

$ python3 src/main.py la_cabra.mp4 la_cabra_recog.mp4
```

## License

Esse projeto é licenciado sob a licença CC0 1.0 Universal - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
[usage.webm](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/bb43e404-4eb8-4859-854f-8226944e29d0)
![usage](https://github.com/GustavoWidman/Prova2-Modulo2/assets/123963822/51a98c07-3ba8-44ce-bfb0-8b46eabf498e)
