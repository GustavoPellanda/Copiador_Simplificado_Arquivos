import tkinter as tk
from tkinter import filedialog
from ftplib import FTP
import shutil

def arquivo_origem():
    origem_busca = filedialog.askopenfilename(initialdir = "/", title = "Select file")
    origem_caminho.set(origem_busca)

def pasta_destino():
    destino_busca = filedialog.askdirectory(initialdir = "/", title = "Select folder")
    destino_caminho.set(destino_busca)

def pasta_destino1():
    destino_busca1 = filedialog.askdirectory(initialdir = "/", title = "Select folder")
    destino_caminho1.set(destino_busca1)

def pasta_destino2():
    destino_busca2 = filedialog.askdirectory(initialdir = "/", title = "Select folder")
    destino_caminho2.set(destino_busca2)

def pasta_destino3():
    destino_busca3 = filedialog.askdirectory(initialdir = "/", title = "Select folder")
    destino_caminho3.set(destino_busca3)

def pasta_destino4():
    destino_busca4 = filedialog.askdirectory(initialdir = "/", title = "Select folder")
    destino_caminho4.set(destino_busca4)

def copia():
    origem = origem_caminho.get()
    destinos = [
        destino_caminho.get(), 
        destino_caminho1.get(), 
        destino_caminho2.get(), 
        destino_caminho3.get(), 
        destino_caminho4.get()
    ]
    
    for destino in destinos:
        if destino and destino.startswith("ftp://"):
            upload_ftp(origem, destino)
        elif destino:
            shutil.copy(origem, destino)

def upload_ftp(local_file_path, ftp_url):
    # Extrai o nome do arquivo a partir do caminho local do arquivo
    nome_arquivo = local_file_path.split('/')[-1]

    # Extrai os componentes da URL FTP
    partes_ftp = ftp_url[6:].split('/', 1)
    servidor_ftp = partes_ftp[0]
    diretorio_ftp = partes_ftp[1] if len(partes_ftp) > 1 else ''

    # Conecta ao servidor FTP
    ftp = FTP(servidor_ftp)
    ftp.login()

    # Verifica se há um subdiretório no caminho FTP
    if diretorio_ftp:
        # Altera para o diretório desejado
        ftp.cwd(diretorio_ftp)

    # Abre o arquivo local no modo binário
    with open(local_file_path, 'rb') as arquivo:
        # Envia o arquivo para o servidor FTP
        ftp.storbinary('STOR ' + nome_arquivo, arquivo)

    # Fecha a conexão FTP
    ftp.quit()

root = tk.Tk()
root.title("Copiador Simplificado de Arquivos")
root.geometry("550x380")

origem_caminho = tk.StringVar()
origem_texto = tk.Label(root, text="Origem do Arquivo:", borderwidth=20)
origem_texto.grid(row=0, column=0)
origem_barra = tk.Entry(root, textvariable=origem_caminho, width=50)
origem_barra.grid(row=0, column=1)
origem_botao = tk.Button(root, text="Buscar...", command=arquivo_origem)
origem_botao.grid(row=0, column=2)

destino_caminho = tk.StringVar()
#destino_default = r"C:\Users\ adicionar default aqui"
#destino_caminho.set(destino_default)
destino_texto = tk.Label(root, text="Destino do Arquivo:", borderwidth=20)
destino_texto.grid(row=1, column=0)
destino_barra = tk.Entry(root, textvariable=destino_caminho, width=50)
destino_barra.grid(row=1, column=1)
destino_botao = tk.Button(root, text="Buscar...", command=pasta_destino)
destino_botao.grid(row=1, column=2)

destino_caminho1 = tk.StringVar()
destino_texto1 = tk.Label(root, text="Destino do Arquivo:", borderwidth=20)
destino_texto1.grid(row=2, column=0)
destino_barra1 = tk.Entry(root, textvariable=destino_caminho1, width=50)
destino_barra1.grid(row=2, column=1)
destino_botao1 = tk.Button(root, text="Buscar...", command=pasta_destino1)
destino_botao1.grid(row=2, column=2)

destino_caminho2 = tk.StringVar()
destino_texto2 = tk.Label(root, text="Destino do Arquivo:", borderwidth=20)
destino_texto2.grid(row=3, column=0)
destino_barra2 = tk.Entry(root, textvariable=destino_caminho2, width=50)
destino_barra2.grid(row=3, column=1)
destino_botao2 = tk.Button(root, text="Buscar...", command=pasta_destino2)
destino_botao2.grid(row=3, column=2)

destino_caminho3 = tk.StringVar()
destino_texto3 = tk.Label(root, text="Destino do Arquivo:", borderwidth=20)
destino_texto3.grid(row=4, column=0)
destino_barra3 = tk.Entry(root, textvariable=destino_caminho3, width=50)
destino_barra3.grid(row=4, column=1)
destino_botao3 = tk.Button(root, text="Buscar...", command=pasta_destino3)
destino_botao3.grid(row=4, column=2)

destino_caminho4 = tk.StringVar()
destino_texto4 = tk.Label(root, text="Destino do Arquivo:", borderwidth=20)
destino_texto4.grid(row=5, column=0)
destino_barra4 = tk.Entry(root, textvariable=destino_caminho4, width=50)
destino_barra4.grid(row=5, column=1)
destino_botao4 = tk.Button(root, text="Buscar...", command=pasta_destino4)
destino_botao4.grid(row=5, column=2)

copia_botao = tk.Button(root, text="Copiar Arquivo", command=copia)
copia_botao.grid(row=6, column=1)

root.mainloop()
