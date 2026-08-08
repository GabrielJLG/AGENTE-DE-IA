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
        # temperature=0.8,


        messages=[
        {
        'role':'system',
        'content':"Você agora é um Assistente de jogos, onde qualquer jogo que um usuário mencionar, ou quiser criar, vc irá dar ideias sobre aquele projeto. e seja sempre educado!"
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )


        st.text(reposta.choices[0].message.content)
        time.sleep(0)
        



