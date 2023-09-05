import streamlit as st
import numpy as np
import datetime
import pandas as pd
from datetime import datetime
from github import Github
import requests

repo_owner = 'Pedro-Damas'
repo_name = 'servicos'
file_path = 'data_base.csv'
token = st.secrets["TOKEN_SECRET"]
commit_message = 'Update CSV file'

st.set_page_config(
    page_title = "HOME",
    layout="wide"
)

def ler_data_base():
    data_base = pd.read_csv('data_base.csv')
    data_base['CODIGO UNICO'] = data_base['CODIGO UNICO'].apply(lambda x: str(x))
    data_base['DATA ESTIMADA'] = data_base['DATA ESTIMADA'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    return data_base

data_base = ler_data_base()

st.header('CRIAR ORDEM DE SERVIÇO', divider='red')

col1, col2 = st.columns([0.6,0.4])
CLIENTE = str(col1.text_input(label='CLIENTE'))
CODIGO_UNICO = str(col2.text_input(label='CODIGO UNICO',disabled=True ,value= CLIENTE[:2].upper() + datetime.now().strftime("%d%m%Y") + str(data_base.index[-1] + 1)))

col1, col2, col3 =st.columns([0.6, 0.2, 0.2])
SERVICO = str(col1.text_input(label='SERVIÇO'))
DATA_ESTIMADA = col2.date_input(label='DATA ESTIMADA')
HORA_ESTIMADA = col3.time_input(label='HORA ESTIMADA')
DESCRICAO = str(st.text_area(label= 'DESCRIÇÃO'))

st.write('Selecione as etapas que já ocorreram:')
col1, col2, col3, col4, col5 = st.columns(5)

ETAPA_1 = col1.checkbox(label='ETAPA 1')
ETAPA_2 = col2.checkbox(label='ETAPA 2')
ETAPA_3 = col3.checkbox(label='ETAPA 3')
ETAPA_4 = col4.checkbox(label='ETAPA 4')
ETAPA_5 = col5.checkbox(label='ETAPA 5')

st.divider()
col1, col2 = st.columns(2)

if col1.button(label='CRIAR ORDEM DE SERVIÇO'):
    data_base = pd.read_csv('data_base.csv')
    new_row = pd.DataFrame({'CODIGO UNICO': CODIGO_UNICO, 
                            'CLIENTE': CLIENTE, 
                            'SERVIÇO': SERVICO, 
                            'DESCRIÇÃO': DESCRICAO,
                            'DATA ESTIMADA': DATA_ESTIMADA, 
                            'HORA ESTIMADA': HORA_ESTIMADA, 
                            'ETAPA 1': ETAPA_1, 
                            'ETAPA 1 TIME': np.nan,
                            'ETAPA 2': ETAPA_2, 
                            'ETAPA 2 TIME': np.nan,
                            'ETAPA 3': ETAPA_3,
                            'ETAPA 3 TIME': np.nan, 
                            'ETAPA 4': ETAPA_4, 
                            'ETAPA 4 TIME': np.nan,
                            'ETAPA 5': ETAPA_5,
                            'ETAPA 5 TIME': np.nan,
                            'STATUS': True,
                            'DATA ABERTURA': datetime.now().strftime("%d/%m/%Y %H:%M"),
                            'DATA FECHAMENTO': np.nan,
                            'IDENTIFICADOR': f'{CLIENTE} - {SERVICO} - {CODIGO_UNICO}'}, index=[0])
    data_base = pd.concat([new_row,data_base.loc[:]]).reset_index(drop=True)
    data_base.to_csv("data_base.csv", index=False)
    ler_data_base()

    github = Github(token)
    repo = github.get_user(repo_owner).get_repo(repo_name)

    url = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}'
    response = requests.get(url)

    content = repo.get_contents(file_path)

    with open('data_base.csv', 'rb') as f:
        contents = f.read()


    repo.update_file(file_path, commit_message, contents, content.sha)
    st.toast('Ordem de serviços criada com sucesso!', icon='✅')



