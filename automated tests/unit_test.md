
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
