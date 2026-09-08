import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# define UI
image_path = "https://img.freepik.com/premium-photo/chatbot-3d-illustration-concept-web-app-using-nlp-engage-conversation_1995-873.jpg?w=2000"
st.image(image_path, width=100)

st.title(" 🤖 My AI Chatbot")
input_text = st.text_input("Enter your message :")
st.button("Search")

# define LLM model
llm=Ollama(model='gemma:2b')

# define prompts
prompt=ChatPromptTemplate.from_messages(
    [("system", "Act as my Personal AI Assistant - help me think, create, plan, analyze, and execute."),
     ("human","{input_text}")])

# Chain to generate the response
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# generate response
if input_text:
    with st.spinner("Generating response..."):
     response = chain.invoke({"input_text": input_text})
    st.write("Bot_Response", response)

