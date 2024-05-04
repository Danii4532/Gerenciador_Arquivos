import tkinter
import os
from tkinter import filedialog,messagebox
import shutil
dic = {}

caminho = filedialog.askdirectory()
if not caminho:
    print('Nenhum caminho selecionado')
    exit()
os.chdir(caminho)

for pasta in os.listdir():
    if os.path.isdir(pasta):
        arquivos = os.path.abspath(pasta)
        if len(os.listdir(arquivos)) == 0:
            os.rmdir(arquivos)
        else:
            pass

salvar = messagebox.askyesno('ATENÇÃO', 'Deseja separar algum arquivo importante')
if salvar:
    arquivo_separar = filedialog.askopenfilenames()
    if arquivo_separar:
        os.mkdir('ProjetoImportante(10)')
        c = os.path.abspath('ProjetoImportante(10)')
        for cada in arquivo_separar:
            shutil.move(cada, c)
        print(f'Os arquivos importantes foram salvos em: {os.path.abspath("ArquivosImportantes(10)")}')
else:
    pass

lista = list(os.listdir(caminho))
if 'ProjetoImportante(10)' in lista:
    lista.remove('ProjetoImportante(10)')
lista_extensoes = set()
for cada in lista:
    extensao = cada.split('.')[-1]
    lista_extensoes.add(extensao)

#for cada in lista_extensoes:
#    os.mkdir(cada)
for cada_extensao in lista_extensoes:
    os.mkdir(cada_extensao)
    file = os.path.abspath(cada_extensao)
    dic[cada_extensao] = file

for cada in os.listdir():
    if os.path.isdir(os.path.abspath(cada)) == False:
        extensao = cada.split('.')[-1]
        if extensao in list(dic.keys()):
            caminho = dic[extensao]
            shutil.move(cada,caminho)
    else:
        pass