# Object-Oriented Design for a Modern Notes App
*How OO, Interfaces, and Layered Architecture Build Flexibility and Power*

---

## 1. Procedural Beginnings: Simple Functions and Data

Let’s start with a bare-bones notes app. Notes are simple dictionaries:

```python
note = {
    'id': 'n1',
    'owner': 'alice',
    'title': 'Team Sync',
    'content': 'Discuss Q1 planning.',
    'type': 'text'
}
```

Need to rename a note?

```python
def rename_note(note, new_title):
    note['title'] = new_title
```
**Problem:**  
There's a rule: "Title must not exceed 20 characters."  
However, anyone can break this rule anywhere in the code, and duplicate checks are easy to forget.

You could scatter validation everywhere:
```python
def rename_note(note, new_title):
    if len(new_title) > 20:
        raise Exception('Title too long!')
    note['title'] = new_title
```

But with procedural code, someone will still do:

```python
note['title'] = "A very very very very loooooong title"
```
There’s no way to **guarantee** rules are always followed.

![alt text](image-23.png)

---

## 2. Object-Oriented Approach: Notes as Classes

Object-oriented design models notes as classes that bundle data and behavior:

- **Data:** Represents the note's properties, such as `id`, `owner`, `title`, and `content`.
- **Behavior:** Includes methods like `rename()`, `save()`, `export()`, etc.

![alt text](image-15.png)

---
## 3. Encapsulation: Data and Rules Together

Object-oriented code groups data and behavior. All rules are enforced in one clear location:

```python
class Note:
    def __init__(self, id, owner, title, content):
        if len(title) > 20:
            raise Exception("Title too long!")
        self.id = id
        self.owner = owner
        self.title = title
        self.content = content
    
    def rename(self, new_title):
        if len(new_title) > 20:
            raise Exception("Title too long!")
        self.title = new_title
```

Now, you can only update the title through a method that **always** enforces the rule.

![alt text](image-1.png)

**Private vs. Public in UML Diagrams:**
- `-` (minus) means private (internal use only)
- `+` (plus) means public (accessible from outside)

To achieve encapsulation, we make attributes private and provide public methods to interact with them. This ensures that the internal state of the object can only be changed in controlled ways, enforcing any necessary rules or validations.

---
---

## 4. Interfaces: Contracts for Consistency and Reuse

**Abstract interfaces** (in Python, via `ABC`) ensure all note types have common actions:

```python
from abc import ABC, abstractmethod

class NoteInterface(ABC):
    @abstractmethod
    def rename(self, new_title):
        pass
```

Any subclass (including future types) must implement this method, guaranteeing consistency across your codebase.

![alt text](image-24.png)

---
## 5. Inheritance: Growing Flexible Note Types

Want to support **audio** and **video** notes? Inherit from `Note`:

```python
class AudioNote(Note):
    def __init__(self, id, owner, title, audio_file_path, duration_seconds):
        super().__init__(id, owner, title, content=None)
        self.audio_file_path = audio_file_path
        self.duration_seconds = duration_seconds

class VideoNote(Note):
    def __init__(self, id, owner, title, video_file_path, duration_seconds, thumbnail_path=None):
        super().__init__(id, owner, title, content=None)
        self.video_file_path = video_file_path
        self.duration_seconds = duration_seconds
        self.thumbnail_path = thumbnail_path
```

The title validation "just works" for every kind of note.

![alt text](image-2.png)

---
## 6. Polymorphism and Special Capabilities with Playable Interface

Some notes can be "played"—like audio or video. Define a `Playable` interface:

```python
class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

class AudioNote(Note, Playable):
    def play(self):
        print(f"Playing audio: {self.audio_file_path} ({self.duration_seconds}s)")

class VideoNote(Note, Playable):
    def play(self):
        print(f"Playing video: {self.video_file_path} ({self.duration_seconds}s)")
```

Now, you can uniformly operate on **any** playable note:

```python
notes = [Note(...), AudioNote(...), VideoNote(...)]
for note in notes:
    if isinstance(note, Playable):
        note.play()  # Will work for audio and video notes
```

![alt text](image-3.png)

![alt text](image-19.png)

---
## 7. Coupling and Cohesion: Building Well-Structured Code

### Cohesion:

- **Each class or module serves a single, focused purpose.**
- `Note`/`AudioNote`/`VideoNote` handle **only note data and logic**.
- `NoteRepository` handles **only storage**.
- `Playable` defines playback only for the right classes.

### Coupling:

- **Classes/modules know as little about each other as possible**—they communicate via interfaces, not implementation details.
- When `NoteService` wants to save notes, it only cares that it has a `NoteRepository`—not which database it uses.
- High cohesion and loose coupling make the app **robust, adaptable, and easy to change**.

![alt text](image-25.png)


---
---

## 8. SOLID Principles Illustrated

- **Single Responsibility:** Each class does one job: note logic, storage, or playback.
- **Open/Closed:** Add new note types or backends by subclassing—not by rewriting core classes.

![alt text](image-46.png)

- **Liskov Substitution:** All subclasses of `NoteInterface` or implementers of `Playable` work wherever those APIs are needed.
- **Interface Segregation:** Only "playable" notes implement `play()`, keeping interfaces minimal.
- **Dependency Inversion:** High-level logic does not depend on details—repositories and services communicate only through interfaces.


---
---

## 9. Dependency Inversion & Injection: Database Example

**Problem:** Hard dependencies between high-level app code and low-level database code make switching databases painful.

![alt text](image-21.png)

*High-level app code should rely only on abstractions, not concrete DB code.*

**What we want:**

![alt text](image-26.png)

### Step 1: The Repository Interface

```python
class NoteRepository(ABC):
    @abstractmethod
    def get_by_id(self, note_id):
        pass
    
    @abstractmethod
    def save(self, note):
        pass
```

### Step 2: Implementations for Each Database

```python
class MySQLNoteRepository(NoteRepository):
    def get_by_id(self, note_id):
        print("Loading note from MySQL...")
        # SQL query
    
    def save(self, note):
        print("Saving note to MySQL...")
        # SQL command

class MongoNoteRepository(NoteRepository):
    def get_by_id(self, note_id):
        print("Loading note from MongoDB...")
        # MongoDB query
    
    def save(self, note):
        print("Saving note to MongoDB...")
        # MongoDB command

    def get_by_id(self, note_id):
        print("Loading note from PostgreSQL...")
        # PostgreSQL query
    
    def save(self, note):
        print("Saving note to PostgreSQL...")
        # PostgreSQL command
```

### Step 3: Service Layer Depends ONLY on the Interface

```python
class NoteService:
    def __init__(self, repository: NoteRepository):
        self.repository = repository
    
    def save_note(self, note):
        self.repository.save(note)
```

### Step 4: Swap Implementations via Dependency Injection

At runtime:

```python
# Use MySQL
repo = MySQLNoteRepository()
service = NoteService(repo)
service.save_note(note)  # "Saving note to MySQL..."

# Switch to MongoDB
repo = MongoNoteRepository()
service = NoteService(repo)
service.save_note(note)  # "Saving note to MongoDB..."

# Or PostgreSQL
repo = PostgresNoteRepository()
service = NoteService(repo)
service.save_note(note)  # "Saving note to PostgreSQL..."
```

Everywhere else in your code stays the same!  
This is true dependency inversion, putting power and flexibility in your architecture.

![alt text](image-6.png)

![alt text](image-13.png)

![alt text](image-27.png)

---

## 10. Controller-Service-Repository (CSR) Pattern

The Controller-Service-Repository (CSR) pattern organizes backend code into three layers for better separation of concerns, maintainability, and testability.

In web frameworks such as Spring Boot, Django, or Flask, the CSR pattern helps structure code by dividing responsibilities:

### Controller Layer

Controllers handle incoming HTTP requests, validate inputs, and return responses. They act as entry points, delegating logic without implementing business rules.

![alt text](image-20.png)

![alt text](image-44.png)


### Service Layer

Services contain core business logic, orchestrating operations like calculations or validations. They coordinate between controllers and repositories, often managing transactions.

![alt text](image-45.png)

### Repository Layer

Repositories abstract data access, encapsulating database queries, CRUD operations, and persistence logic. This hides storage details from upper layers.

![alt text](image-17.png)

**Coding to Contract:**

![alt text](image-18.png)

### Model Role

Models define the data schema, such as user profiles or products, typically as classes or ORM entities. Repositories interact with these models for CRUD operations, keeping data access abstracted.

![alt text](image-22.png)

![alt text](image-43.png)

### Example Flow (Sequence Diagram)

![alt text](image-28.png)

![alt text](image-14.png)

![alt text](image-42.png)

![alt text](image-12.png)


![alt text](image-29.png)

![alt text](image-16.png)

![alt text](image-30.png)

![alt text](image-31.png)

---

## 11. Dependency Inversion in Practice

### Dependency Inversion Principle

![alt text](image-32.png)

### Defining the Contract

![alt text](image-33.png)

### Adapter: The Concrete Implementation

![alt text](image-34.png)

![alt text](image-35.png)

![alt text](image-36.png)

### Dependency Injection: Wiring at Runtime

![alt text](image-37.png)

### Benefits

**Flexibility:**

![alt text](image-38.png)

**Testability:**

![alt text](image-39.png)

**Maintainability:**

![alt text](image-40.png)

![alt text](image-41.png)

---

## 12. UML Diagram Notations

![alt text](image-5.png)

### Composition

Filled diamond indicates a strong ownership relationship where the contained object cannot exist independently of the container.

![alt text](image-7.png)

### Aggregation

Open diamond indicates a weaker relationship where the contained object can exist independently of the container.

![alt text](image-9.png)


