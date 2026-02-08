from datetime import datetime
from LLMService import LLMService

class Document:
    def __init__(self, text, filename=None):
        self.text = text
        self.filename = filename
        self.uploaded_time = datetime.now()
        self.llm = LLMService()

    def summarize(self, lang="English"):
        # Only support Chinese, English, and Japanese summaries
        allowed_langs = ["Chinese", "English", "Japanese"]
        if lang not in allowed_langs:
            raise ValueError(f"Language '{lang}' not supported. Choose from: {', '.join(allowed_langs)}.")
        word_count = len(self.text.split())

        # Summary is limited to documents with up to 8000 words
        if word_count > 8000:
            raise ValueError(f"Document too long: {word_count} words. Maximum supported is 8000.")
        user_prompt = f"Summarize the following document in {lang}:\n{self.text}"
        system_prompt = "You are professional translator"

        return self.llm.chat(system_prompt=system_prompt, user_prompt=user_prompt)

# Example usage
if __name__ == "__main__":
    doc_text = "The Hong Kong Polytechnic University (PolyU) is a leading university in Hong Kong, known for its innovative research, strong industry partnerships, and commitment to professional education. PolyU offers a wide range of programs and is recognized for its contributions to science, engineering, business, and design."
    doc = Document(doc_text, filename="polyu.txt")
    print(f"Filename: {doc.filename}")
    print(f"Uploaded time: {doc.uploaded_time}")
    summary = doc.summarize(lang="Chinese")
    print("Summary:", summary)
