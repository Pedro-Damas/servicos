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
token = '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'
commit_message = 'Update CSV file'

st.set_page_config(
    page_title = "HOME",
    layout="wide"
)


def ler_data_base():
    data_base = pd.read_csv('data_base.csv')
    data_base['CODIGO UNICO'] = data_base['CODIGO UNICO'].apply(lambda x: str(x))
    data_base['DATA ESTIMADA'] = data_base['DATA ESTIMADA'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    data_base['HORA ESTIMADA'] = data_base['HORA ESTIMADA'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))
    return data_base

data_base = ler_data_base()

#-------------------------------------------------------------------------------- Filtros
st.header('EDITAR ORDEM DE SERVIÇO', divider='red')


col1, col2 =st.columns(2)
if col1.checkbox(label='Apenas com data para o dia atual'):
    CHAMDOS = data_base[(data_base['DATA ESTIMADA'] == datetime.today().strftime('%Y-%m-%d')) & (data_base['IDENTIFICADOR'].isnull() == False) ]
else: 
    CHAMDOS = data_base[(data_base['IDENTIFICADOR'].isnull() == False) ]

if col2.checkbox(label='Apenas chamados abertos') & (CHAMDOS.empty == False):
    CHAMDOS = CHAMDOS[CHAMDOS['STATUS'] == False]['IDENTIFICADOR']
else: 
    CHAMDOS = CHAMDOS['IDENTIFICADOR']



if CHAMDOS.empty== True:
    st.error(f'Não existem chamados comas caracteristicas definida', icon="🚨")
else:
    CHAMDO = st.selectbox(label='ESCOLHA O CHAMDO',
                options= list(CHAMDOS))

    st.divider() #-----------------------------------------------------------------

    LINHA_SELECIONADA = data_base[(data_base['IDENTIFICADOR'] == CHAMDO)]

    STATUS_EDITED = st.checkbox('Concluido',value=LINHA_SELECIONADA['STATUS'].iloc[0])

    col1, col2= st.columns([0.6,0.2])
    CLIENTE_EDITED = str(col1.text_input(label='Cliente', value=LINHA_SELECIONADA['CLIENTE'].iloc[0]))
    CODIGO_UNICO_EDITED = str(col2.text_input(label='Codigo Unico', value=LINHA_SELECIONADA['CODIGO UNICO'].iloc[0]))


    col1, col2, col3 =st.columns([0.6, 0.2, 0.2])
    SERVICO_EDITED = str(col1.text_input(label='SERVIÇO', value=LINHA_SELECIONADA['SERVIÇO'].iloc[0]))
    DATA_ESTIMADA_EDITED = col2.date_input(label='Data Estiamda', value=LINHA_SELECIONADA['DATA ESTIMADA'].iloc[0])
    HORA_ESTIMADA_EDITED = col3.time_input(label='Hora Estimada', value=LINHA_SELECIONADA['HORA ESTIMADA'].iloc[0])
    DESCRICAO_EDITED = str(st.text_area(label= 'Descrição', value=LINHA_SELECIONADA['DESCRIÇÃO'].iloc[0]))
    st.write('Selecione as etapas que já ocorreram:')

    col1, col2, col3, col4, col5 = st.columns(5)
    ETAPA_1_EDITED = col1.checkbox(label='Etapa 1',value= LINHA_SELECIONADA['ETAPA 1'].iloc[0])
    ETAPA_2_EDITED = col2.checkbox(label='Etapa 2',value= LINHA_SELECIONADA['ETAPA 2'].iloc[0])
    ETAPA_3_EDITED = col3.checkbox(label='Etapa 3',value= LINHA_SELECIONADA['ETAPA 3'].iloc[0])
    ETAPA_4_EDITED = col4.checkbox(label='Etapa 4',value= LINHA_SELECIONADA['ETAPA 4'].iloc[0])
    ETAPA_5_EDITED = col5.checkbox(label='Etapa 5',value= LINHA_SELECIONADA['ETAPA 5'].iloc[0])

    if col1.button(label='SALVAR ALTERAÇÕES', type="primary"): #Botao Salvar
        #---------------------------------------------------------------------------------------1
        if (ETAPA_1_EDITED == True) & (LINHA_SELECIONADA['ETAPA 1'].iloc[0]== False):
            ETAPA_1_DT = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (ETAPA_1_EDITED == False) & (LINHA_SELECIONADA['ETAPA 1'].iloc[0]== True):
            ETAPA_1_DT = np.nan
        else:
            ETAPA_1_DT = LINHA_SELECIONADA['ETAPA 1 TIME'].iloc[0]
        #---------------------------------------------------------------------------------------2

        if (ETAPA_2_EDITED == True) & (LINHA_SELECIONADA['ETAPA 2'].iloc[0]== False):
            ETAPA_2_DT = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (ETAPA_2_EDITED == False) & (LINHA_SELECIONADA['ETAPA 2'].iloc[0]== True):
            ETAPA_2_DT = np.nan
        else:
            ETAPA_2_DT = LINHA_SELECIONADA['ETAPA 2 TIME'].iloc[0]
            #---------------------------------------------------------------------------------------3

        if (ETAPA_3_EDITED == True) & (LINHA_SELECIONADA['ETAPA 3'].iloc[0]== False):
            ETAPA_3_DT = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (ETAPA_3_EDITED == False) & (LINHA_SELECIONADA['ETAPA 3'].iloc[0]== True):
            ETAPA_3_DT = np.nan
        else:
            ETAPA_3_DT = LINHA_SELECIONADA['ETAPA 3 TIME'].iloc[0]
            #---------------------------------------------------------------------------------------4

        if (ETAPA_4_EDITED == True) & (LINHA_SELECIONADA['ETAPA 4'].iloc[0]== False):
            ETAPA_4_DT = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (ETAPA_4_EDITED == False) & (LINHA_SELECIONADA['ETAPA 4'].iloc[0]== True):
            ETAPA_4_DT = np.nan
        else:
            ETAPA_4_DT = LINHA_SELECIONADA['ETAPA 4 TIME'].iloc[0]
            #---------------------------------------------------------------------------------------5

        if (ETAPA_5_EDITED == True) & (LINHA_SELECIONADA['ETAPA 5'].iloc[0]== False):
            ETAPA_5_DT = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (ETAPA_5_EDITED == False) & (LINHA_SELECIONADA['ETAPA 5'].iloc[0]== True):
            ETAPA_5_DT = np.nan
        else:
            ETAPA_5_DT = LINHA_SELECIONADA['ETAPA 5 TIME'].iloc[0]

    #--------------------------------------------------------------------------------------- Hora abertura e fechamento
        if (STATUS_EDITED == False) & (LINHA_SELECIONADA['STATUS'].iloc[0]== True):
            HORA_FECHAMENTO = datetime.now().strftime("%d/%m/%Y %H:%M")
        elif (STATUS_EDITED == True) & (LINHA_SELECIONADA['STATUS'].iloc[0]== False):
            HORA_FECHAMENTO = np.nan
        else:
            HORA_FECHAMENTO = LINHA_SELECIONADA['STATUS'].iloc[0]

        data_base = pd.read_csv('data_base.csv')
        data_base[(data_base['IDENTIFICADOR'] == CHAMDO)] = [CODIGO_UNICO_EDITED, 
                                                            CLIENTE_EDITED, 
                                                            SERVICO_EDITED, 
                                                            DESCRICAO_EDITED,
                                                            DATA_ESTIMADA_EDITED, 
                                                            HORA_ESTIMADA_EDITED, 
                                                            ETAPA_1_EDITED,
                                                            ETAPA_1_DT, 
                                                            ETAPA_2_EDITED, 
                                                            ETAPA_2_DT, 
                                                            ETAPA_3_EDITED, 
                                                            ETAPA_3_DT, 
                                                            ETAPA_4_EDITED, 
                                                            ETAPA_4_DT, 
                                                            ETAPA_5_EDITED, 
                                                            ETAPA_5_DT, 
                                                            STATUS_EDITED,
                                                            LINHA_SELECIONADA['DATA ABERTURA'].iloc[0],
                                                            HORA_FECHAMENTO,
                                                            f'{CLIENTE_EDITED} - {SERVICO_EDITED} - {CODIGO_UNICO_EDITED}']
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

        st.toast('Alterações salvas com sucesso!', icon='✅')

    with st.expander("Visão Avançada de registros"):
        st.data_editor(ler_data_base(), use_container_width=True)
