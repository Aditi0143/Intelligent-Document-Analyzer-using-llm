# 📄 Intelligent Document Analysis using LLM

<div align="center">
  <h3>AI-Powered Document Processing and Analysis Platform</h3>
  <p>Extract insights, answer questions, and analyze documents using state-of-the-art Language Models</p>
</div>

---

## 🚀 Project Overview

This project is an intelligent document analysis system that leverages Large Language Models (LLMs) to process, analyze, and extract meaningful insights from various document formats. The system provides a user-friendly web interface for document upload, text extraction, question-answering, summarization, and action item extraction.

## ✨ Key Features

- **📁 Multi-format Document Support**: PDF, DOCX, TXT, PNG, JPG, JPEG
- **🔍 Intelligent Text Extraction**: OCR support for images and PDFs
- **❓ Question-Answering System**: Ask questions about your documents
- **📝 Automatic Summarization**: Generate concise summaries
- **✅ Action Item Extraction**: Identify tasks, assignees, and deadlines
- **🔗 Semantic Search**: Find relevant content using embeddings
- **🌐 Web Interface**: Streamlit-based user-friendly UI

## 🏗️ Project Architecture

```
Intelligent_Document_Analysis_using_LLM/
├── 📁 data/
│   └── 📁 sample_docs/          # Sample documents for testing
├── 📁 models/
│   └── 📄 custom_prompt_templates.py  # Custom prompt templates
├── 📁 src/
│   ├── 📄 action_item_extractor.py    # Action item extraction logic
│   ├── 📄 chunker.py                  # Text chunking utilities
│   ├── 📄 document_loader.py          # Document loading and processing
│   ├── 📄 embedding_indexer.py        # Vector embeddings and search
│   ├── 📄 qa_pipeline.py             # Question-answering pipeline
│   └── 📄 summarizer.py              # Text summarization
├── 📁 ui/
│   └── 📄 app.py                     # Streamlit web application
├── 📄 requirements.txt               # Python dependencies
└── 📄 README.md                     # Project documentation
```

## 🛠️ Core Components

### 1. Document Loader (`src/document_loader.py`)
Handles loading and text extraction from multiple file formats:
- **PDF**: Uses PyMuPDF for text extraction
- **DOCX**: Uses python-docx for Word document processing
- **Images**: Uses Tesseract OCR for text extraction from images
- **TXT**: Direct text file reading

### 2. Text Chunker (`src/chunker.py`)
Splits large documents into manageable chunks for processing:
- Configurable chunk size (default: 512 words)
- Word-based splitting for better context preservation

### 3. Embedding Indexer (`src/embedding_indexer.py`)
Creates vector embeddings for semantic search:
- Uses sentence-transformers/all-MiniLM-L6-v2 model
- FAISS indexing for fast similarity search
- Supports querying with top-k results

### 4. Question-Answering Pipeline (`src/qa_pipeline.py`)
Provides intelligent question-answering capabilities:
- Uses deepset/roberta-base-squad2 model
- Context-aware answer generation

### 5. Text Summarizer (`src/summarizer.py`)
Generates concise document summaries:
- Uses T5-base model for summarization
- Configurable summary length

### 6. Action Item Extractor (`src/action_item_extractor.py`)
Identifies actionable items from documents:
- Uses google/flan-t5-small model
- Extracts tasks, assignees, and deadlines

### 7. Web Interface (`ui/app.py`)
Streamlit-based user interface featuring:
- File upload functionality
- Document preview with adjustable length
- Interactive question-answering
- One-click summarization and action item extraction

## 📦 Dependencies

### Core Libraries
- **PyMuPDF** - PDF document processing and text extraction
- **pytesseract** - OCR for image text extraction
- **Pillow** - Image processing and manipulation
- **python-docx** - Microsoft Word document processing

### Machine Learning & AI
- **faiss-cpu** - Efficient similarity search and clustering
- **torch** - PyTorch deep learning framework
- **transformers** - Hugging Face transformers library for pre-trained models

### Web Interface
- **streamlit** - Web application framework

### Model Dependencies
- **sentence-transformers** - For text embeddings
- **t5-base** - For text summarization
- **roberta-base-squad2** - For question-answering
- **flan-t5-small** - For action item extraction

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR installed on your system

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Intelligent_Document_Analysis_using_LLM
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR**
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get install tesseract-ocr
   ```
   
   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Update the path in `document_loader.py` and `ui/app.py`

4. **Run the application**
   ```bash
   streamlit run ui/app.py
   ```

## 🎯 Usage

### Web Interface
1. Launch the Streamlit app
2. Upload a document (PDF, DOCX, PNG, JPG)
3. Preview the extracted text
4. Ask questions about the document
5. Generate summaries and extract action items

### Programmatic Usage
```python
from src.document_loader import load_document
from src.chunker import chunk_text
from src.embedding_indexer import EmbeddingIndexer
from src.qa_pipeline import answer_question
from src.summarizer import summarize_text
from src.action_item_extractor import extract_action_items

# Load document
text = load_document("path/to/document.pdf")

# Process document
chunks = chunk_text(text)
indexer = EmbeddingIndexer()
indexer.build_index(chunks)

# Answer questions
answer = answer_question(" ".join(indexer.query("Your question")), "Your question")

# Generate summary
summary = summarize_text(text)

# Extract action items
actions = extract_action_items(text)
```

## 🔧 Configuration

### Model Configuration
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **QA Model**: `deepset/roberta-base-squad2`
- **Summarization Model**: `t5-base`
- **Action Extraction Model**: `google/flan-t5-small`

### Customization
- Modify chunk size in `chunker.py`
- Update prompt templates in `models/custom_prompt_templates.py`
- Adjust model parameters in respective pipeline files

## 📊 Performance Considerations

- **Memory Usage**: Models are loaded on-demand to optimize memory usage
- **Processing Speed**: Uses CPU-optimized FAISS for fast similarity search
- **Text Limits**: Summarization and action extraction limited to 1500 characters for optimal performance
- **Chunking**: Large documents are automatically chunked for efficient processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For issues and questions:
1. Check the existing issues
2. Create a new issue with detailed description
3. Include error logs and system information

## 🔮 Future Enhancements

- [ ] Support for more document formats (PPTX, XLSX)
- [ ] Batch processing capabilities
- [ ] Advanced OCR with layout analysis
- [ ] **Improved JPEG text extraction efficiency** - Current OCR performance on JPEG files needs optimization
- [ ] Multi-language support
- [ ] API endpoints for integration
- [ ] Docker containerization
- [ ] Cloud deployment options

---

<div align="center">
  <p>Built with ❤️ using Python, Streamlit, and Hugging Face Transformers</p>
</div>
