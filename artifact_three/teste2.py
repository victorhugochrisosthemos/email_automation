import tkinter as tk
from tkinter import ttk
import unicodedata
import string
import pandas as pd
import sys
import io

# Configura o stdout para UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dados = pd.read_csv(
    'tabela.csv',
    sep=';',        
    encoding='latin-1'
)

def limpar_texto(text):
    if not isinstance(text, str):
        return ""

    # Converter para minúsculas
    text = text.lower()

    # Remover pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))

    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

    # Remover todos os espaços (adicionar no final da função)
    text = text.replace(" ", "")

    text = text.replace("\n", "")

    if isinstance(text, str):
        texto = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
        return texto

    return ' '.join(text)



def analisar_texto():
    texto = campo_a.get("1.0", "end-1c")  # Pega todo o texto do Campo A
    

    #--------------------- Processamento aqui ------------------------------------
    
    # Monta a resposta
    #resposta = f"Texto analisado:\n\n"

    resposta = ""

    processado = limpar_texto(texto)

    # Variáveis para armazenar o produto e setor encontrados
    produto_encontrado = []
    setor_encontrado = []
    fila_encontrado = []

    # Procurar por cada produto no texto
    for _, linha in dados.iterrows():
        produto = str(linha['Produto'])
        produto_limpo = limpar_texto(produto)  # Limpa o nome do produto da mesma forma
        
        # Verifica se o produto limpo está contido no texto limpo
        if produto_limpo and produto_limpo in processado:
            produto_encontrado.append(linha['Produto']) 
            setor_encontrado.append(linha['Setor'])
            fila_encontrado.append(linha['filas'])
            #break  # Para no primeiro encontro
    
    resposta += f'Produto foi encontrado? ' 

    if(not produto_encontrado):
        resposta += 'NÃO\n'
        resposta += '\n'
        resposta += 'E-mail sugerido de resposta:\n'
        resposta += 'Prezado cliente!\nAgradecemos o seu contato e para darmos continuidade a sua solicitação vou precisar de mais algumas informações\n'
        resposta += 'Por gentileza, informe especificamente qual produto Intelbras precisa de suporte.'
    else:
        resposta += 'SIM\n'
        resposta += '\n'
        resposta += f"PRODUTO = {produto_encontrado}\n"
        resposta += f"SETOR = {setor_encontrado}\n"
        resposta += f"FILA = {fila_encontrado}\n"
        '''
        resposta += "\n---------------------------------------------\n"
        resposta += f"\nTexto processado:\n{processado}\n"


        num_caracteres = len(texto)
        resposta += f"Número de caracteres: {num_caracteres}\n"

        num_palavras = len(texto.split())
        resposta += f"Número de palavras: {num_palavras}\n"
        '''

    #-----------------------------------------------------------------------------
    
    # Limpa e insere a resposta no Campo B
    campo_b.config(state="normal")
    campo_b.delete("1.0", "end")
    campo_b.insert("1.0", resposta)
    campo_b.config(state="disabled")

def limpar_campos():
    """Limpa o conteúdo dos campos A e B"""
    campo_a.delete("1.0", "end")  # Limpa campo A
    campo_b.config(state="normal")
    campo_b.delete("1.0", "end")  # Limpa campo B
    campo_b.config(state="disabled")

# Cria a janela principal
root = tk.Tk()
root.title("Analisador de E-mail's")
root.geometry("600x400")
root.configure(bg="#13ec1e")  # Cor de fundo da janela principal

# Estilo para os widgets ttk
style = ttk.Style()
style.configure('TFrame', background="#1e7a26")
style.configure('TLabel', background="#5bd84f", foreground='#333333', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10), background='#4CAF50', foreground='#1e7a26')
style.map('TButton', background=[('active', '#45a049')])

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Rótulo e Campo A (entrada)
ttk.Label(main_frame, text="Digite seu texto:").pack(anchor="w")
campo_a = tk.Text(main_frame, height=8, wrap="word", bg='white', fg='#333333',
                 insertbackground='#333333', selectbackground="#0d5e14")
campo_a.pack(fill="x", pady=(0, 10))

# Botão Analisar
btn_analisar = ttk.Button(main_frame, text="Analisar", command=analisar_texto)
btn_analisar.pack(pady=5)

# Botão Limpar
btn_limpar = ttk.Button(main_frame, text="Limpar", command=limpar_campos)
btn_limpar.pack(pady=5)

# Rótulo e Campo B (saída)
ttk.Label(main_frame, text="Resultado:").pack(anchor="w")
campo_b = tk.Text(main_frame, height=10, wrap="word", state="disabled",
                 bg="#e9e9e9", fg='#333333')
campo_b.pack(fill="both", expand=True)

# Inicia o loop principal
root.mainloop()