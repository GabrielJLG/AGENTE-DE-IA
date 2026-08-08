from groq import Groq
import streamlit as st 
import time
import os



# pip install groq 




client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


st.title("Conversa com o Piloto") 
pergunta  = st.text_input('pergunta:')


if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=0.2,


        messages=[
        {
        'role':'system',
        'content':"Você será um assistente onde irá ajudar a solucionar os problemas dos usuários com computadores até encontrar o erro! de pergunta em pergunta você irá solucionando os problemas! de forma rápida e objetiva!"
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )


        st.text(reposta.choices[0].message.content)
        time.sleep(0)
        



