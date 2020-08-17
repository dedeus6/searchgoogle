import googlesearch
from time import time
from selenium import webdriver

def busca(tema):
    start_time = time()
    for resultado in googlesearch.search(f'"{tema}" youtube', stop=1):
        url = resultado
    end_time = time()
    tempo_execucao = (end_time - start_time) * 1000
    with open('log.txt', 'a+', newline="") as file:
        file.write(f'O tempo da busca foi: {tempo_execucao:.2f}ms\n')
    return url

def janela(url):
    browser = webdriver.Firefox(executable_path=r'C:\Users\filip\driver\geckodriver.exe')
    browser.get(url)


if __name__ == '__main__':
    tema = input('Diga algo para pesquisa no youtube:  ')
    link = busca(tema)
    janela(link)
