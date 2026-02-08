---

## 1. What is a Unit Test?

A **unit test** is a small, automated program that checks if a specific function ("unit") of your code works correctly, *in isolation*.

**Key ideas:**
- Tests *just your code*, not external systems
- Should be *fast* and *repeatable*
- Run frequently, such as on every commit or before every deployment

### Why Unit Tests Matter

- Catch bugs early, before they affect users
- Make refactoring safer and faster
- Serve as live documentation of what the code should do

---

## 2. The Problem: Dependencies

Most real software does more than pure computation. It:
- Reads or writes files (`open("file.txt")`)
- Connects to databases (`cursor.execute(...)`)
- Calls APIs on the network (`requests.get(...)`)
- Talks to hardware or system resources

**When writing unit tests**, if you actually access these dependencies:
- The tests become slow (they wait for IO, networks, or DBs)
- They can fail for reasons outside your code (network flakiness, API downtime, permissions issues, etc.)
- Developers and continuous integration systems need specific setup just to run tests

---

## 3. Why Dependencies Make Tests Flaky

A **flaky test** is one where:
- *Sometimes* the test passes, *sometimes* it fails, *even if* you haven't changed your code.
- The underlying cause? Unpredictable external things (network, disk, clock, random numbers).

**Example:**
```python
def test_google_homepage():
    import requests
    resp = requests.get("https://www.google.com/")
    assert resp.status_code == 200
```
This test will:
- Pass if your network works and Google's up
- Fail otherwise—regardless of your code's correctness!

---

## 4. The Solution: Isolation and Mocking

To make unit tests **fast and reliable**, you need to:
- Design your code so the "real work" (like file access, DB, APIs) happens in one spot
- In your tests, *replace* (mock) that spot with a controllable fake—called a *mock* or *stub*

This approach means your unit tests never actually touch the disk, network, or real APIs.

---

## 5. Using a Service Class for External APIs

When using things like the OpenAI API, encapsulate the API access in a *service class*.
- Keeps your business logic clean (no deep API chains everywhere)
- Makes mocking straightforward

**Example:**
Consider the following class that wraps OpenAI' LLM API to provide text summarization.

```python
# llm_service.py
class LLMService:
    def __init__(self, client):
        self.client = client

    def summarize(self, text):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Summarize this:"},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
```

---

## 6. Writing Testable Business Logic

Your main logic should *accept* this service as a parameter. This is **dependency injection**—making it easy to substitute mocks in tests.

```python
# business_logic.py
def summarize_text(text, llm_service, max_words=8000):
    if not text.strip():
        return "ERROR: No input text provided."
    if len(text.split()) > max_words:
        return f"ERROR: Input exceeds {max_words} words."
    try:
        return llm_service.summarize(text)
    except Exception as exc:
        return f"ERROR: {exc}"
```

---

## 7. How to Write Fast, Reliable Unit Tests with Mocked LLMService

**Why this structure avoids flaky tests:**
- Your tests do **not** call OpenAI or any live API—no network needed, no per-test cost, no API rate limits!
- You control exactly what the LLMService does in tests.

#### The Mock Service

```python
# test_business_logic.py
class MockLLMService:
    def __init__(self, summary="MOCK SUMMARY", should_error=False):
        self.summary = summary
        self.should_error = should_error
    def summarize(self, text):
        if self.should_error:
            raise Exception("Simulated error from LLMService")
        return self.summary
```

#### Pytest Fixtures and Test Suite

```python
import pytest
from business_logic import summarize_text

@pytest.fixture
def happy_llm():
    return MockLLMService("FAKE SUMMARY")

@pytest.fixture
def error_llm():
    return MockLLMService(should_error=True)

def test_successful_summary(happy_llm):
    result = summarize_text("Explain pytest.", happy_llm)
    assert result == "FAKE SUMMARY"

def test_too_long_input(happy_llm):
    text = "foo " * 8001
    result = summarize_text(text, happy_llm)
    assert result.startswith("ERROR: Input exceeds")

def test_empty_input(happy_llm):
    for blank in ["", "   ", "\n"]:
        assert summarize_text(blank, happy_llm) == "ERROR: No input text provided."

def test_when_service_errors(error_llm):
    result = summarize_text("Hello", error_llm)
    assert result == "ERROR: Simulated error from LLMService"
```

---

## 1. Why Unit Testability Depends on Class Design

When writing unit tests, your code should be easy to test *in isolation*—without calling real APIs, networks, or external services. This is only possible if your classes are designed for testability.

---

## 2. Example: Why example1.py Is Hard to Test

Let's look at example1.py:

```python
from datetime import datetime
from LLMService import LLMService

class Document:
    def __init__(self, text, filename=None):
        self.text = text
        self.filename = filename
        self.uploaded_time = datetime.now()
        self.llm = LLMService()  # Directly creates the real service

    def summarize(self, lang="English"):
        # ...validation code...
        return self.llm.chat(system_prompt=system_prompt, user_prompt=user_prompt)
```

**What's the problem?**
- The Document class *always* creates a real LLMService.
- You can't substitute a mock or fake service in tests.
- Unit tests will always call the real OpenAI API, making them slow, flaky, and expensive.

---

## 3. Refactoring for Testability: example2.py

Now see example2.py:

```python
from datetime import datetime
from LLMService import LLMService

class Document:
    def __init__(self, text, llm_service, filename=None):
        self.text = text
        self.filename = filename
        self.uploaded_time = datetime.now()
        self.llm = llm_service  # Accepts service as a parameter

    def summarize(self, lang="English"):
        # ...validation code...
        return self.llm.chat(system_prompt=system_prompt, user_prompt=user_prompt)
```

**Why is this better?**
- The Document class *accepts* the LLMService as a parameter (dependency injection).
- In production, you pass the real LLMService.
- In tests, you pass a mock or fake service.
- Unit tests are now fast, reliable, and don't require network or API keys.

---

## 4. How to Write Unit Tests with Dependency Injection

With this design, your tests can use a mock service:

```python
class MockLLMService:
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        return "This is a mocked summary."

def test_summarize_with_mock_llm():
    doc_text = "Test document content."
    mock_llm = MockLLMService()
    document = Document(doc_text, mock_llm, filename="test.txt")
    summary = document.summarize(lang="English")
    assert summary == "This is a mocked summary."
```

---

## 5. Key Takeaways

- **Direct instantiation of dependencies (example1.py) makes testing hard.**
- **Dependency injection (example2.py) makes testing easy and reliable.**
- Always design your classes to accept external services as parameters.
- This lets you substitute mocks in tests, avoiding real API calls and making tests fast and robust.

---

## 6. Summary

Refactor your code to use dependency injection for all external services. This is the foundation of testable, maintainable, and reliable Python code.

---

## 7. Visualizing the Difference: Class Diagram

Below is a Mermaid class diagram showing the difference between example1.py and example2.py:

```
classDiagram
    class Document1 {
        -text
        -filename
        -uploaded_time
        -llm : LLMService
        Document1(text, filename)
        summarize(lang)
    }
    class LLMService
    Document1 --> LLMService : creates

    class Document2 {
        -text
        -filename
        -uploaded_time
        -llm : LLMService
        Document2(text, llm_service, filename)
        summarize(lang)
    }
    Document2 --> LLMService : injected
```

---

### Diagram Explanation

- **Document1 (example1.py):**
  - Directly creates an instance of LLMService inside its constructor.
  - This means Document1 is tightly coupled to LLMService and cannot easily be tested with a mock.

- **Document2 (example2.py):**
  - Receives LLMService as a constructor parameter (dependency injection).
  - This makes Document2 flexible and testable, as you can inject a mock or real service as needed.

The diagram visually highlights how dependency injection (Document2) decouples your business logic from external services, making unit testing easier and more reliable.

---

## 8. Designing Extensible and Testable Classes with Interfaces and Dependency Injection

### What is an Interface?
An interface is a programming construct that defines a set of methods a class must implement, but does not specify how those methods work. In Python, interfaces are typically defined using abstract base classes (ABCs) from the `abc` module. This allows you to write code that works with any class implementing the interface, regardless of its internal details.

#### How to Define an Interface in Python
You use the `ABC` class and the `@abstractmethod` decorator:

```python
from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def save(self, filename, data):
        pass
```

Any class inheriting from `StorageInterface` must implement the `save` method, or Python will raise an error if you try to instantiate it.

---

### Why Are Interfaces Important?
- **Flexibility:** Your code can work with any implementation of the interface, making it easy to swap out components (e.g., switch from local storage to cloud storage).
- **Extensibility:** You can add new implementations (e.g., new LLM providers, new storage backends) without changing your business logic.
- **Testability:** You can easily replace real services with mocks or fakes in tests, avoiding slow or flaky tests.
- **Maintainability:** Business logic stays clean and decoupled from provider details, making code easier to update and extend.

---

### Example 1: LLMService Interface

Suppose you want your Document class to work with different LLM providers (OpenAI, Gemini, etc.):

```python
from abc import ABC, abstractmethod

class LLMServiceInterface(ABC):
    @abstractmethod
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        pass
```

Now, you can implement this interface for OpenAI, Gemini, or a mock:

```python
class OpenAILLMService(LLMServiceInterface):
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        # OpenAI implementation
        ...

class GeminiLLMService(LLMServiceInterface):
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        # Gemini implementation
        ...

class MockLLMService(LLMServiceInterface):
    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        return "This is a mocked summary."
```

Your Document class can now depend on LLMServiceInterface:

```python
class Document:
    def __init__(self, text, llm_service: LLMServiceInterface, filename=None):
        self.text = text
        self.llm = llm_service
        ...
```

---

### Example 2: Storage Interface

Suppose you want to save documents or summaries to different locations (local disk, AWS S3, Vercel, or various databases):

```python
from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def save(self, filename, data):
        pass
```

Now, you can implement this interface for different storage backends:

```python
class LocalStorage(StorageInterface):
    def save(self, filename, data):
        with open(filename, 'w') as f:
            f.write(data)

class S3Storage(StorageInterface):
    def save(self, filename, data):
        # Save to AWS S3
        ...

class DatabaseStorage(StorageInterface):
    def save(self, filename, data):
        # Save to a database
        ...
```

Your Document class can now depend on StorageInterface:

```python
class Document:
    def __init__(self, text, llm_service: LLMServiceInterface, storage: StorageInterface, filename=None):
        self.text = text
        self.llm = llm_service
        self.storage = storage
        self.filename = filename
        ...
    def save(self):
        self.storage.save(self.filename, self.text)
```

---

By designing your classes to depend on interfaces, you make your codebase robust, modular, and ready for future integrations and changes. Interfaces are the foundation of flexible, extensible, and testable software.
