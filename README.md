# keylogger-simples-python
Este projeto é um exemplo de um keylogger simples em Python que usa a biblioteca pynput para capturar eventos de teclado e registrar os pressionamentos de tecla em um arquivo de texto.

## 🎯 Objetivo
O código monitora o teclado e grava as teclas pressionadas, incluindo caracteres alfanuméricos e teclas especiais (como Enter, Space, Backspace, etc.), em um arquivo de texto com a data atual no nome. O propósito é demonstrar o uso da biblioteca pynput para capturar entradas do teclado e registrar eventos de forma prática.

## 🔧 Dependências
Para executar este código, você precisa da biblioteca pynput. Além disso, o código utiliza as bibliotecas padrão do Python re e datetime.

## 💾 Instalação das Dependências
 1. Instalar a Biblioteca pynput:

 2. Abra o terminal e execute o seguinte comando:
`pip install pynput`

## 🚀 Como Usar
Preparar o Ambiente:

Certifique-se de que você tenha a biblioteca pynput instalada.
Verifique no código se o caminho do arquivo onde o log será gravado (fileLog) é válido e que o diretório existe. Exemplo: `C:/Users/Usuário/Desktop/keylogger-simples-python/text.txt`

## 👨‍💻 Executar o Código:
Salve o código Python em um arquivo, por exemplo, `main.py`
Abra o terminal, navegue até o diretório onde o arquivo está localizado e execute o código com o comando:
`python main.py`

O código iniciará o monitoramento do teclado e registrará os eventos em um arquivo de texto com a data atual.

## 📥 Verificar o Arquivo de Log:
O arquivo de log será salvo no diretório especificado com o nome no formato text.txtYYYY-MM-DD.txt (por exemplo, `text.txt2024-09-02.txt`).
Abra o arquivo para revisar as teclas registradas.

## 🔍 Observações
Permissões: Certifique-se de que você tem permissões adequadas para criar e gravar arquivos no diretório especificado.
Segurança e Privacidade: Use este código com responsabilidade e apenas em sistemas que você tem permissão para monitorar. O uso inadequado pode violar leis de privacidade e ética.

## 🤝 Contribuições
Se você deseja melhorar este código ou adicionar novas funcionalidades, sinta-se à vontade para criar um pull request ou abrir uma issue.
