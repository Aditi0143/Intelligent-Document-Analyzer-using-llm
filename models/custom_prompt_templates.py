# src/models/custom_prompt_templates.py

def get_action_item_prompt():
    return """
You are a smart assistant analyzing corporate documents like meeting transcripts, legal contracts, or business reports.

Your task is to extract actionable items in the following format:
1. Task description
2. Responsible person or team (if any)
3. Deadline (if mentioned)

Text:
{text}

Respond with a clear list of action items:
"""

def get_summarization_prompt():
    return """
You are a professional summarizer. Summarize the following document clearly and concisely.

Document:
{text}

Summary:
"""

def get_qa_prompt():
    return """
You are an AI assistant. Based on the following context, answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""
