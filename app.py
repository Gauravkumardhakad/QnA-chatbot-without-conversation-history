## import the libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING"]="true"
os.environ["LANGCHAIN_PROJECT"]="simple Q&A chatbot"

# prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant, please answer the following quesries"),
        ("user","Question:{question}")
    ]
)


def generate_response(input,engine,temperature,max_token):
    llm=Ollama(model=engine)
    output_parse=StrOutputParser()
    chain=prompt|llm|output_parse
    answer=chain.invoke({'question':input})
    return answer


## streamlit app
st.title("QnA chatbot with open source models")

## Select the OpenAI model
engine=st.sidebar.selectbox("Select Open AI model", ["gemma:2b"])
## Adjust response parameter
temperature=st.sidebar.slider("Temperature", min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)
## MAin interface for user input
st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide the query")
