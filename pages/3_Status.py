import streamlit as st
import numpy as np
import datetime
import pandas as pd
#from streamlit_extras.let_it_rain import rain


def ler_data_base():
    data_base = pd.read_csv('pages/status/data_base.csv')
    data_base['CODIGO UNICO'] = data_base['CODIGO UNICO'].apply(lambda x: str(x))

    return data_base

data_base = ler_data_base()

st.header('RASTREIO DO SERVIÇO', divider='red')
CODIGO_UNICO = str(st.text_input(label='Código da ordem de serviços', autocomplete="on"))

if CODIGO_UNICO in list(data_base['CODIGO UNICO']):
    data_base_filtrado = data_base[(data_base['CODIGO UNICO'] == CODIGO_UNICO)]

    if data_base_filtrado['ETAPA 5'].iloc[0] == True:
        st.success(f'Sua ordem {CODIGO_UNICO} está concluida!', icon="✅")
        #rain(emoji="🎉", font_size=54, falling_speed=4, animation_length=1)

elif CODIGO_UNICO =='':
    st.info('Digite o código da ordem de serviços que você recebeu', icon="ℹ️")
else:
    st.error(f'Código {CODIGO_UNICO} não encontrado', icon="🚨")
    CODIGO_UNICO = ''


if CODIGO_UNICO == '':
    st.markdown('')
else:
    st.divider()

    if data_base_filtrado['ETAPA 1 TIME'].isnull().iloc[0] == False:
        DATA_1 = data_base_filtrado['ETAPA 1 TIME'].iloc[0].split(' ')
        DATA_1 = ' - '.join(DATA_1) 
    else:
        DATA_1 = ''
    
    if data_base_filtrado['ETAPA 2 TIME'].isnull().iloc[0] == False:
        DATA_2 = data_base_filtrado['ETAPA 2 TIME'].iloc[0].split(' ')
        DATA_2 = ' - '.join(DATA_2) 
    else:
        DATA_2 = ''

    if data_base_filtrado['ETAPA 3 TIME'].isnull().iloc[0] == False:
        DATA_3 = data_base_filtrado['ETAPA 3 TIME'].iloc[0].split(' ')
        DATA_3 = ' - '.join(DATA_3) 
    else:
        DATA_3 = ''

    if data_base_filtrado['ETAPA 4 TIME'].isnull().iloc[0] == False:
        DATA_4 = data_base_filtrado['ETAPA 4 TIME'].iloc[0].split(' ')
        DATA_4 = ' - '.join(DATA_4) 
    else:
        DATA_4 = ''
    
    if data_base_filtrado['ETAPA 5 TIME'].isnull().iloc[0] == False:
        DATA_5 = data_base_filtrado['ETAPA 5 TIME'].iloc[0].split(' ')
        DATA_5 = ' - '.join(DATA_5) 
    else:
        DATA_5 = ''

    CLIENTE = data_base_filtrado['CLIENTE'].iloc[0]
    SERVICO = data_base_filtrado['SERVIÇO'].iloc[0]
    DESCRCAO = data_base_filtrado['DESCRIÇÃO'].iloc[0]
    st.markdown(f':red[_Cliente:_] {CLIENTE}')
    st.markdown(f':red[_Serviço:_] {SERVICO}')
    st.markdown(f':red[_Descrição:_] {DESCRCAO}')
    st.divider()

    if ((data_base_filtrado['ETAPA 1'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 2'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 3'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 5'].iloc[0] == True)):

        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_1}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_2}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_3}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_4}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_5}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")

    
    elif ((data_base_filtrado['ETAPA 1'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 2'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 3'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)):

        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_1}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_2}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_3}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_4}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
    
    elif ((data_base_filtrado['ETAPA 1'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 2'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 3'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)):

        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_1}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_2}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_3}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")

    elif ((data_base_filtrado['ETAPA 1'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 2'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 3'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)):

        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_1}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")
        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_2}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")

    elif ((data_base_filtrado['ETAPA 1'].iloc[0] == True)&
        (data_base_filtrado['ETAPA 2'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 3'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)&
        (data_base_filtrado['ETAPA 4'].iloc[0] == False)):

        with st.chat_message("user", avatar='✔️'):
            st.write(f"Em fabricação - {DATA_1}")
            st.write("Seu produto já se encontra em nossas linhas de frabricação")



