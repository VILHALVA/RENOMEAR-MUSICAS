# RENOMEAR MUSICAS
🎈RENOMEIE AS MÚSICAS GLOBALMENTE.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
Este projeto permite que você renomeie facilmente arquivos de músicas em um diretório selecionado. Ele adiciona um nome universal seguido de um número sequencial aos nomes dos arquivos. Isso é útil quando você tem uma pasta com músicas que possuem nomes diferentes e deseja padronizá-los.
Por exemplo, suponha que você tenha um diretório com as seguintes músicas:
```
1. Song A.mp3
2. Track B.mp3
3. Music C.mp3
```

Após executar o projeto, as músicas seriam renomeadas para:
```
1. FAIXA 01.mp3
2. FAIXA 02.mp3
3. FAIXA 03.mp3
```

Isso garante que todas as músicas tenham o mesmo nome inicial (nesse caso, "FAIXA") seguido de um número sequencial, facilitando a organização e a identificação das faixas.

## EXECUTANDO O PROJETO:
1. Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python CODIGO.py
```
2. Isso abrirá uma janela do aplicativo "RENOMEAR MÚSICAS".
3. Clique no botão "SELECIONAR" para escolher o diretório onde estão localizadas suas músicas.
4. Digite um nome universal desejado no campo "NOME UNIVERSAL".
5. Clique no botão "RENOMEAR" para iniciar o processo de renomeação das músicas no diretório selecionado.
6. Aguarde até que o processo seja concluído. Quando terminar, a mensagem "Renomeação concluída!" será exibida na janela.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)



