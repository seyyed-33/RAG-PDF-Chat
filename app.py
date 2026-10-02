import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import tempfile
import os

# ============================================
# تنظیمات صفحه
# ============================================
st.set_page_config(
    page_title="چت‌بات PDF",
    page_icon="📚",
    layout="centered"
)

st.title("📚 چت‌بات هوشمند PDF")
st.write("PDF خود را وارد کنید و سوال بپرسید")

# ============================================
# آپلود PDF
# ============================================
uploaded_file = st.file_uploader("PDF خود را اینجا وارد کنید", type="pdf")

if uploaded_file is not None:
    # ذخیره موقت فایل
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # لود PDF
    with st.spinner("reading PDF..."):
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

    # Chunking
    with st.spinner("cutting..."):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=100,
            separators=["\n\n", "\n", "。", "،", ".", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)

    # Embedding
    with st.spinner("embedding..."):
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        vectorstore = FAISS.from_documents(chunks, embeddings)

    st.success(f"PDF وارد شد ✅ , {len(documents)} صفحه و {len(chunks)} تکه")

    # ============================================
    # پرسش و پاسخ
    # ============================================
    st.subheader("💬 سوال خود را بپرسید")

    question = st.text_input("سوال خود را اینجا وارد کنید : ")

    if question:
        with st.spinner("loading answer..."):
            # LLM
            llm = ChatGroq(
                api_key="###########",
                model="openai/gpt-oss-20b",
                temperature=0,
                max_tokens=1000,
                max_retries=2,
            )

            # پرامپت
            prompt = PromptTemplate.from_template(
                "شما یک دستیار هوشمند هستید. بر اساس متن زیر به سوال کاربر پاسخ بده.\n\n"
                "متن مرجع:\n{context}\n\n"
                "سوال کاربر: {question}\n\n"
                "دستورالعمل:\n"
                "- اگر پاسخ در متن بود، به صورت روان و فارسی جواب بده\n"
                "- اگر متن شامل کلمات کلیدی سوال بود اما پاسخ صریح نبود، سعی کن با تحلیل خودت جواب بده\n"
                "- اگر واقعاً متن هیچ ربطی به سوال نداشت، بگو «اطلاعاتی پیدا نکردم»\n\n"
                "پاسخ:"
            )

            chain = prompt | llm | StrOutputParser()

            # جستجو
            docs = vectorstore.similarity_search(question, k=7)
            context = "\n\n".join([d.page_content for d in docs])

            # جواب
            response = chain.invoke({"context": context, "question": question})

            st.write("### 📝 جواب : ")
            st.write(response)

    # پاک کردن فایل موقت
    os.unlink(tmp_path)