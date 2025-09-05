import sys
import os
# ocr_config.py
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Add the parent directory (project root) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.document_loader import load_document




import streamlit as st


from src.chunker import chunk_text
from src.embedding_indexer import EmbeddingIndexer
from src.qa_pipeline import answer_question
from src.summarizer import summarize_text
from src.action_item_extractor import extract_action_items

st.title("📄 Intelligent Document Analyzer")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "png", "jpg"])

if uploaded_file:
    # Extract file extension from uploaded file name
    file_extension = os.path.splitext(uploaded_file.name)[1]
    temp_filename = f"temp_file{file_extension}"

    # Save uploaded file with correct extension
    with open(temp_filename, "wb") as f:
        f.write(uploaded_file.read())

    # Load and process the document
    raw_text = load_document(temp_filename)
    st.subheader("Extracted Text")

    # Let user control preview length
    max_preview_chars = st.slider(
        "Select number of characters to preview", 
        min_value=100, 
        max_value=min(len(raw_text), 10000), 
        value=600, 
        step=100
    )
    st.text_area("Document Preview", raw_text[:max_preview_chars], height=300)

    # Chunking and indexing
    chunks = chunk_text(raw_text)
    indexer = EmbeddingIndexer()
    indexer.build_index(chunks)

    # Question-answering
    question = st.text_input("Ask a question about the document")
    if question:
        context = " ".join(indexer.query(question))
        answer = answer_question(context, question)
        st.success(f"Answer: {answer}")

    # Summarization
    if st.button("Summarize Document"):
        summary = summarize_text(raw_text[:1500])  # You can increase this if needed
        st.info(summary)

    # Action item extraction
    if st.button("Extract Action Items"):
        items = extract_action_items(raw_text[:1500])  # Increase if model supports more
        st.warning(items)

    # Optional: clean up temp file
    os.remove(temp_filename)
