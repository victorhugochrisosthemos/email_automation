import pandas as pd
import sys
import io

# Configura o stdout para UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dados = pd.read_csv(
    'C:/Users/Victor/Desktop/Intelbras/teste_emails/artifact_two/tabela_transferencia.csv',
    sep=';',        
    encoding='latin-1'
)

pd.set_option('display.max_columns', None)  # Mostra todas as colunas
#pd.set_option('display.expand_frame_repr', False)  # Evita quebra de linha
pd.set_option('display.max_rows', None)  # Mostra todas as linha


print(dados.columns.tolist())

'''
Exemplo de E-mail para teste

Prezados, bom dia!
Entro em contato para solicitar o firmware do tip 1001D.
Preciso dele porque acredito que seja esse o problema de não funcionar minha conta da VIVO nele.
Estou precisando com urgência.

Desde já, agradeço a atenção!

'''