from groq import Groq
import streamlit as st 
import time
import os



# pip install groq 




client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


st.title("Conversa com o DevGuard") 
pergunta  = st.text_input('pergunta:')


if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=0.8,


        messages=[
        {
        'role':'system',
        'content':"Você é um agente onde irá solucionar problemas de códigos e irá dar sugestões de melhorisa e falar se aquilo é um código desnecesário ou não. e quando estiver o código errado, dar uma sugestão de melhorias."
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )


        st.text(reposta.choices[0].message.content)
        time.sleep(0)
        



