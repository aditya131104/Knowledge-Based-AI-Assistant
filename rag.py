# from pypdf import PdfReader


# def load_pdf(file_path):
#     reader = PdfReader(file_path)

#     text = ""

#     for page in reader.pages:
#         page_text = page.extract_text()

#         if page_text:
#             text += page_text + "\n"

#     return text


# if __name__ == "__main__":
#     file_path = "documents/Smart_PrepResearchGate.pdf"

#     text = load_pdf(file_path)

#     print(text[:3000])



# 2
# from pypdf import PdfReader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from dotenv import load_dotenv

# load_dotenv()


# def load_pdf(file_path):
#     reader = PdfReader(file_path)

#     text = ""

#     for page in reader.pages:
#         page_text = page.extract_text()

#         if page_text:
#             text += page_text + "\n"

#     return text


# def split_text(text):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100
#     )

#     chunks = splitter.split_text(text)

#     return chunks


# def create_embeddings():
#     embeddings = GoogleGenerativeAIEmbeddings(
#         model="gemini-embedding-001"
#     )

#     return embeddings

# if __name__ == "__main__":
#     file_path = "documents/Smart_PrepResearchGate.pdf"

#     text = load_pdf(file_path)

#     chunks = split_text(text)

#     embeddings = create_embeddings()

#     vector_store = FAISS.from_texts(
#         chunks,
#         embedding=embeddings
#     )

#     print("Number of chunks:", len(chunks))
#     print("FAISS vector store created!")

#     question = "What is Smart Prep?"

#     results = vector_store.similarity_search(
#         question,
#         k=3
#     )

#     print("\nRetrieved chunks:\n")

#     for result in results:
#         print(result.page_content)
#         print("\n-----------------\n")

# 2
# if __name__ == "__main__":
#     file_path = "documents/Smart_PrepResearchGate.pdf"

#     text = load_pdf(file_path)

#     chunks = split_text(text)

#     embeddings = create_embeddings()

#     vector_store = FAISS.from_texts(
#         chunks,
#         embedding=embeddings
#     )

#     vector_store.save_local("faiss_index")

#     print("Number of chunks:", len(chunks))
#     print("FAISS vector store created and saved!")

# 3
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from dotenv import load_dotenv

# load_dotenv()


# def create_embeddings():
#     embeddings = GoogleGenerativeAIEmbeddings(
#         model="gemini-embedding-001"
#     )

#     return embeddings


# if __name__ == "__main__":
#     embeddings = create_embeddings()

#     vector_store = FAISS.load_local(
#         "faiss_index",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

#     question = "What is Smart Prep?"

#     results = vector_store.similarity_search(
#         question,
#         k=3
#     )

#     print("FAISS index loaded!")
#     print("\nRetrieved chunks:\n")

#     for result in results:
#         print(result.page_content)
#         print("\n-----------------\n")

# 4
# from langchain_google_genai import (
#     GoogleGenerativeAIEmbeddings,
#     ChatGoogleGenerativeAI
# )
# from langchain_community.vectorstores import FAISS
# from dotenv import load_dotenv

# load_dotenv()


# def create_embeddings():
#     embeddings = GoogleGenerativeAIEmbeddings(
#         model="gemini-embedding-001"
#     )

#     return embeddings


# def generate_answer(question, results):
#     context = "\n\n".join(
#         result.page_content for result in results
#     )

#     model = ChatGoogleGenerativeAI(
#         model="gemini-3.6-flash"
#     )

#     prompt = f"""
# Answer the question using only the information provided in the context.

# Context:
# {context}

# Question:
# {question}

# If the answer is not present in the context, say:
# "I could not find this information in the document."
# """

#     response = model.invoke(prompt)

#     return response.content[0]["text"]


# if __name__ == "__main__":
#     embeddings = create_embeddings()

#     vector_store = FAISS.load_local(
#         "faiss_index",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

#     question = "What is Smart Prep?"

#     results = vector_store.similarity_search(
#         question,
#         k=3
#     )

#     answer = generate_answer(question, results)

#     print("\nAnswer:\n")
#     print(answer)


from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


def create_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )


def load_vector_store():
    embeddings = create_embeddings()

    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def generate_answer(question, results):
    context = "\n\n".join(
        result.page_content for result in results
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I could not find this information in the document."
"""

    response = model.invoke(prompt)

    return response.content[0]["text"]


def ask_question(question):
    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        question,
        k=3
    )

    answer = generate_answer(question, results)

    return answer