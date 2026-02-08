import pytest
from unittest.mock import Mock
from datetime import datetime
from example2 import Document

class MockLLMService:
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        return "This is a mocked summary."

def test_summarize_with_mock_llm():
    doc_text = "Test document content."
    mock_llm = MockLLMService()
    document = Document(doc_text, mock_llm, filename="test.txt")
    summary = document.summarize(lang="English")
    assert summary == "This is a mocked summary."

def test_unsupported_language():
    doc_text = "Test document content."
    mock_llm = MockLLMService()
    document = Document(doc_text, mock_llm, filename="test.txt")
    with pytest.raises(ValueError):
        document.summarize(lang="Spanish")

def test_document_too_long():
    long_text = "word " * 8001
    mock_llm = MockLLMService()
    doc_long = Document(long_text, mock_llm, filename="long.txt")
    with pytest.raises(ValueError):
        doc_long.summarize(lang="English")
