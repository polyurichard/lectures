Certainly! Here's a **refined, comprehensive tutorial on Object-Oriented Design (OOD)** incorporating all the concepts you requested: **attributes, properties, methods, encapsulation, abstraction, interfaces, inheritance, and polymorphism**, illustrated with the `Document` class and its specialized subclasses for different file types.

---

# Object-Oriented Design (OOD) Tutorial with Interfaces and Inheritance

---

## 1. Introduction to Object-Oriented Design

OOD is a programming paradigm that models software as *objects* which combine **state (data)** and **behavior (methods)**. It promotes **modularity**, **reusability**, and **extensibility**.

---

## 2. Core Concepts Illustrated in a `Document` Example

### Base Class: `Document`

- Has **attributes** (like `text`, `filename`, and a dependency: `llm_service`).
- Implements **methods** (e.g., `summarize`, `save`).
- Shows **properties** (computed, read-only attribute).
- Encapsulates internal details.

---

## 3. Defining Interfaces for Loose Coupling

Use an interface to define a contract that any **LLM service provider** must follow. This enables easily swapping implementations and improving testability.

```python
from abc import ABC, abstractmethod

class LLMServiceInterface(ABC):
    @abstractmethod
    def chat(self, system_prompt: str, user_prompt: str, temperature: float = 1.0, top_p: float = 1.0) -> str:
        """Generate a response from the language model."""
        pass
```

---

## 4. Implementing a Concrete LLM Service (Example)

```python
class OpenAILLMService(LLMServiceInterface):
    def chat(self, system_prompt: str, user_prompt: str, temperature: float = 1.0, top_p: float = 1.0) -> str:
        # Integration with an actual API would go here
        return f"Fake summary of: {user_prompt[:30]}..."
```

---

## 5. The Base `Document` Class

```python
class Document:
    def __init__(self, text: str, llm_service: LLMServiceInterface, filename: str = None):
        self.text = text                   # Attribute: document content
        self.llm = llm_service             # Attribute: LLM service instance (dependency injected)
        self.filename = filename           # Optional filename attribute

    @property
    def word_count(self) -> int:
        """Property: computed attribute that counts words in the document."""
        return len(self.text.split())

    def summarize(self) -> str:
        """Method: generates a summary using the LLM service."""
        system_prompt = "Summarize this text."
        user_prompt = self.text
        return self.llm.chat(system_prompt, user_prompt)

    def save(self):
        """Default save method saves plain text to a file."""
        if not self.filename:
            raise ValueError("Filename not set.")
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.text)
        print(f"Saved plain text: {self.filename}")
```

---

## 6. Extending `Document` with Inheritance for File Types

Subclasses extend `Document` by:

- **Adding unique attributes** related to the file type.
- **Overriding** `save()` to implement file-type specific saving.
- Still **inheriting** common behavior like `summarize()`.

---

### 6.1 `DocxDocument` subclass

```python
class DocxDocument(Document):
    def __init__(self, text: str, llm_service: LLMServiceInterface, filename: str = None, template_style: str = 'Normal'):
        super().__init__(text, llm_service, filename)
        self.template_style = template_style   # Additional DOCX-specific attribute

    def save(self):
        if not self.filename or not self.filename.endswith(".docx"):
            raise ValueError("Filename must end with .docx")
        print(f"Saving DOCX file with template '{self.template_style}' to {self.filename}")
        # Integration with python-docx would go here
```

---

### 6.2 `PdfDocument` subclass

```python
class PdfDocument(Document):
    def __init__(self, text: str, llm_service: LLMServiceInterface, filename: str = None, page_size: str = 'A4'):
        super().__init__(text, llm_service, filename)
        self.page_size = page_size             # PDF-specific attribute

    def save(self):
        if not self.filename or not self.filename.endswith(".pdf"):
            raise ValueError("Filename must end with .pdf")
        print(f"Saving PDF file with page size '{self.page_size}' to {self.filename}")
        # Integration with PDF libraries would go here
```

---

### 6.3 `PptxDocument` subclass

```python
class PptxDocument(Document):
    def __init__(self, text: str, llm_service: LLMServiceInterface, filename: str = None, slide_layout: int = 5):
        super().__init__(text, llm_service, filename)
        self.slide_layout = slide_layout       # PPTX-specific attribute

    def save(self):
        if not self.filename or not self.filename.endswith(".pptx"):
            raise ValueError("Filename must end with .pptx")
        print(f"Saving PPTX file with slide layout {self.slide_layout} to {self.filename}")
        # Integration with python-pptx would go here
```

---

## 7. Polymorphism in Action

All subclasses share the same interface (`summarize()`, `save()`), allowing you to work with these objects interchangeably:

```python
documents = [
    DocxDocument("Docx content", llm_service, "doc.docx", template_style="Heading1"),
    PdfDocument("Pdf content", llm_service, "file.pdf", page_size="Letter"),
    PptxDocument("Pptx content", llm_service, "slide.pptx", slide_layout=2),
]

for doc in documents:
    print(f"Word count: {doc.word_count}")
    print(doc.summarize())
    doc.save()
```

---

## 8. Summary of Key Concepts

| Concept        | Explanation & Example                                                  |
|----------------|------------------------------------------------------------------------|
| **Attribute**  | Data stored in the object, e.g., `self.text`, `self.filename`           |
| **Property**   | Computed attribute, e.g., `word_count` property                         |
| **Method**     | Object behavior, e.g., `summarize()`, `save()`                         |
| **Encapsulation** | Bundling attributes and methods; hiding inner details (`doc.summarize()` hides LLM details) |
| **Abstraction** | Exposing a simple interface hiding complex logic                      |
| **Interface**  | Contract (abstract base class) defining expected behavior (`LLMServiceInterface`) |
| **Inheritance**| Subclassing `Document` to create `DocxDocument`, `PdfDocument`, etc.   |
| **Method Overriding** | Customized `save()` method in each subclass                      |
| **Polymorphism**| Same interface for different types allows interchangeable usage        |
| **Dependency Injection** | Injecting `llm_service` to decouple LLM implementation         |

---

## 9. Benefits of This Design

- **Modular & Extensible:** Easily add new document types.
- **Reusable:** Common behaviors share code in base class.
- **Testable:** Mock/fake LLM services by implementing `LLMServiceInterface`.
- **Maintainable:** Clear separation between document logic and external services.

---

## 10. Complete Minimal Example

```python
from abc import ABC, abstractmethod

class LLMServiceInterface(ABC):
    @abstractmethod
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        pass

class OpenAILLMService(LLMServiceInterface):
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        return f"Fake summary: {user_prompt[:30]}..."

class Document:
    def __init__(self, text, llm_service, filename=None):
        self.text = text
        self.llm = llm_service
        self.filename = filename

    @property
    def word_count(self):
        return len(self.text.split())

    def summarize(self):
        system_prompt = "Summarize this text."
        user_prompt = self.text
        return self.llm.chat(system_prompt, user_prompt)

    def save(self):
        if not self.filename:
            raise ValueError("Filename not set.")
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.text)
        print(f"Saved plain text: {self.filename}")

class DocxDocument(Document):
    def __init__(self, text, llm_service, filename=None, template_style="Normal"):
        super().__init__(text, llm_service, filename)
        self.template_style = template_style

    def save(self):
        if not self.filename or not self.filename.endswith(".docx"):
            raise ValueError("Filename must end with .docx")
        print(f"Saving DOCX with template '{self.template_style}' to {self.filename}")

class PdfDocument(Document):
    def __init__(self, text, llm_service, filename=None, page_size="A4"):
        super().__init__(text, llm_service, filename)
        self.page_size = page_size

    def save(self):
        if not self.filename or not self.filename.endswith(".pdf"):
            raise ValueError("Filename must end with .pdf")
        print(f"Saving PDF with page size '{self.page_size}' to {self.filename}")

class PptxDocument(Document):
    def __init__(self, text, llm_service, filename=None, slide_layout=5):
        super().__init__(text, llm_service, filename)
        self.slide_layout = slide_layout

    def save(self):
        if not self.filename or not self.filename.endswith(".pptx"):
            raise ValueError("Filename must end with .pptx")
        print(f"Saving PPTX with slide layout {self.slide_layout} to {self.filename}")

# Example use:
llm_service = OpenAILLMService()

documents = [
    DocxDocument("This is DOCX content.", llm_service, "report.docx", template_style="Formal"),
    PdfDocument("This is PDF content.", llm_service, "summary.pdf", page_size="Letter"),
    PptxDocument("This is PPTX content.", llm_service, "slides.pptx", slide_layout=2),
]

for doc in documents:
    print(f"Words: {doc.word_count}")
    print(doc.summarize())
    doc.save()
```

---

If you want, I can help you integrate actual file generation libraries or demonstrate unit testing with mock LLM services!