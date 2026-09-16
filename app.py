# import streamlit as st
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model="gemini-3.6-flash"
# )

# st.title("Knowledge-Based AI Assistant")

# question = st.text_input("Ask something")

# if st.button("Ask"):
#     if question.strip():
#         response = model.invoke(question)
#         st.write(response.content[0]["text"])


import streamlit as st
from rag import ask_question


st.title("Knowledge-Based AI Assistant")

question = st.text_input("Ask a question about the document")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Finding the answer..."):
            answer = ask_question(question)

        st.write(answer)