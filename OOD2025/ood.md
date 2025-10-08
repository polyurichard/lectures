# Object-Oriented Design

## 1) Classes & Objects

**Concept:**
A class is like a blueprint for creating objects. It describes what data (attributes) and actions (methods) the objects will have. An object is a specific thing created from that blueprint.

**Example:**
A Cat class describes what all cats have (name, age, color, etc.) and what they can do (eat, sleep, meow). Each cat you create is an object.

### Python

```python
class Cat:
    def __init__(self, name, sex, age, weight, color, texture):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color
        self.texture = texture

    def breathe(self):
        print(f"{self.name} is breathing.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def run(self, destination):
        print(f"{self.name} is running to {destination}.")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")

    def meow(self):
        print(f"{self.name} says: Meow!")


# Create objects and use attributes/methods
oscar = Cat("Oscar", "male", 3, 7, "brown", "striped")
luna = Cat("Luna", "female", 2, 5, "gray", "plain")

# Mutate attributes
oscar.name = "Oscar II"
oscar.weight = 8
luna.color = "white"
luna.age = 3

print("\nOscar's attributes:")
print(f"Name: {oscar.name}")
print(f"Weight: {oscar.weight} kg")

print("\nLuna's attributes:")
print(f"Name: {luna.name}")
print(f"Color: {luna.color}")

print("Oscar:")
oscar.meow()
oscar.eat("fish")

print("\nLuna:")
luna.run("toy")
luna.sleep(2)
```

### Java

```java
class Cat {
    private String name, sex, color, texture;
    private int age;
    private double weight;

    public Cat(String name, String sex, int age, double weight, String color, String texture) {
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.weight = weight;
        this.color = color;
        this.texture = texture;
    }

    public void breathe() { System.out.println(name + " is breathing."); }
    public void eat(String food) { System.out.println(name + " is eating " + food + "."); }
    public void run(String destination) { System.out.println(name + " is running to " + destination + "."); }
    public void sleep(int hours) { System.out.println(name + " is sleeping for " + hours + " hours."); }
    public void meow() { System.out.println(name + " says: Meow!"); }

    // Getters/Setters (only those we need in the demo)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getWeight() { return weight; }
    public void setWeight(double weight) { this.weight = weight; }
    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
    public void setAge(int age) { this.age = age; }
}

public class Main {
    public static void main(String[] args) {
        Cat oscar = new Cat("Oscar", "male", 3, 7, "brown", "striped");
        Cat luna = new Cat("Luna", "female", 2, 5, "gray", "plain");

        oscar.setName("Oscar II");
        oscar.setWeight(8);
        luna.setColor("white");
        luna.setAge(3);

        System.out.println("\nOscar's attributes:");
        System.out.println("Name: " + oscar.getName());
        System.out.println("Weight: " + oscar.getWeight() + " kg");

        System.out.println("\nLuna's attributes:");
        System.out.println("Name: " + luna.getName());
        System.out.println("Color: " + luna.getColor());

        System.out.println("Oscar:");
        oscar.meow();
        oscar.eat("fish");

        System.out.println("\nLuna:");
        luna.run("toy");
        luna.sleep(2);
    }
}
```

**Practice Questions:**
Q1. What is the difference between a class and an object?
<details><summary>Show Answer</summary>A class is a blueprint defining state (attributes) and behavior (methods). An object is an instance of a class created at runtime.</details>

Q2. In Python, how do you define a constructor?
<details><summary>Show Answer</summary>With the special method __init__(self, ...), which initializes attributes of the object.</details>

Q3. In Java, what keyword is used to create an object from a class?
<details><summary>Show Answer</summary>The new keyword, e.g. Cat c = new Cat();.</details>

**Practice Question:**
What is the difference between a class and an object?
<details>
<summary>Show Answer</summary>
A class is a template or blueprint; an object is a specific instance created from that template.
</details>

---

## 2) Inheritance

**Concept:**
Inheritance lets you create a new class based on an existing class. The new class (child) gets all the features of the old class (parent), and you can add more features or change how things work.

**Example:**
A Cat and a Dog are both Animals. They share things like name and age, but each has its own special actions (meow, bark).

### Python

```python
class Animal:
    def __init__(self, name, sex, age, weight, color):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color

    def breathe(self): print(f"{self.name} is breathing.")
    def eat(self, food): print(f"{self.name} is eating {food}.")
    def run(self, destination): print(f"{self.name} is running to {destination}.")
    def sleep(self, hours): print(f"{self.name} is sleeping for {hours} hours.")

class Cat(Animal):
    def __init__(self, name, sex, age, weight, color, is_nasty):
        super().__init__(name, sex, age, weight, color)
        self.__is_nasty = is_nasty  # "private" by convention (name-mangled)

    def meow(self): print(f"{self.name} says: Meow!")

class Dog(Animal):
    def __init__(self, name, sex, age, weight, color, best_friend):
        super().__init__(name, sex, age, weight, color)
        self.__best_friend = best_friend

    def bark(self): print(f"{self.name} says: Woof!")


cat = Cat("Whiskers", "Female", 3, 4.5, "Tabby", False)
dog = Dog("Buddy", "Male", 5, 15.2, "Golden", "John")
cat.meow(); cat.eat("fish")
dog.bark(); dog.run("park")
```

### Java

```java
class Animal {
    protected String name, sex, color;
    protected int age;
    protected double weight;

    public Animal(String name, String sex, int age, double weight, String color) {
        this.name = name; this.sex = sex; this.age = age;
        this.weight = weight; this.color = color;
    }
    public void breathe() { System.out.println(name + " is breathing."); }
    public void eat(String food) { System.out.println(name + " is eating " + food + "."); }
    public void run(String dest) { System.out.println(name + " is running to " + dest + "."); }
    public void sleep(int hours) { System.out.println(name + " is sleeping for " + hours + " hours."); }
}

class Cat extends Animal {
    private boolean isNasty;
    public Cat(String name, String sex, int age, double weight, String color, boolean isNasty) {
        super(name, sex, age, weight, color);
        this.isNasty = isNasty;
    }
    public void meow() { System.out.println(name + " says: Meow!"); }
}

class Dog extends Animal {
    private String bestFriend;
    public Dog(String name, String sex, int age, double weight, String color, String bestFriend) {
        super(name, sex, age, weight, color);
        this.bestFriend = bestFriend;
    }
    public void bark() { System.out.println(name + " says: Woof!"); }
}

public class Demo {
    public static void main(String[] args) {
        Cat cat = new Cat("Whiskers", "Female", 3, 4.5, "Tabby", false);
        Dog dog = new Dog("Buddy", "Male", 5, 15.2, "Golden", "John");
        cat.meow(); cat.eat("fish");
        dog.bark(); dog.run("park");
    }
}
```

**Practice Questions:**
Q4. What does inheritance achieve in OO design?
<details><summary>Show Answer</summary>It promotes reusability by allowing subclasses to inherit and extend attributes/methods of a superclass.</details>

Q5. Give an example of a real-world “is-a” relationship.
<details><summary>Show Answer</summary>Lion is an Animal; hence Lion inherits from Animal.</details>

Q6. Can Python support multiple inheritance?
<details><summary>Show Answer</summary>Yes, Python supports multiple inheritance; Java does not for classes (but allows multiple interfaces).</details>

**Practice Question:**
Why do we use inheritance?
<details>
<summary>Show Answer</summary>
To avoid repeating code and to show relationships between things (like a Cat is an Animal).
</details>

---

## 3) Encapsulation (Privacy, Getters/Setters)

**Concept:**
Encapsulation means hiding the details of how something works inside a class. You protect the data by making it private, and provide special methods to get or change it (getters and setters).

**Example:**
A Robot keeps its battery level private. You can only check or change it using special methods.

### Python

```python
class Robot:
    def __init__(self, name):
        self.__name = name           # name-mangled attribute
        self.__battery_level = 100

    def recharge(self):
        self.__battery_level = 100
        print(f"{self.__name} is recharging.")

    def get_battery_level(self):
        return self.__battery_level

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 5:
            self.__name = name
        else:
            print("Name must be more than 5 characters")
```

### Java

```java
class Robot {
    private String name;
    private int batteryLevel = 100;

    public Robot(String name) { this.name = name; }

    public void recharge() {
        batteryLevel = 100;
        System.out.println(name + " is recharging.");
    }

    public int getBatteryLevel() { return batteryLevel; }

    public String getName() { return name; }
    public void setName(String name) {
        if (name != null && name.length() > 5) this.name = name;
        else System.out.println("Name must be more than 5 characters");
    }
}
```

**Practice Questions:**
Q7. What is encapsulation?
<details><summary>Show Answer</summary>The principle of hiding internal state and providing controlled access via getters/setters.</details>

Q8. In Java, how do you make an attribute private?
<details><summary>Show Answer</summary>By declaring it with the private modifier.</details>

Q9. In Python, how can you indicate a private attribute?
<details><summary>Show Answer</summary>By prefixing with double underscores __attribute, which triggers name mangling.</details>

**Practice Question:**
Why do we make some attributes private?
<details>
<summary>Show Answer</summary>
To protect the data and control how it is changed, making programs safer and easier to fix.
</details>

---

## 4) Interfaces & Abstract Classes

**Concept:**
An interface or abstract class is like a promise: it says what methods a class must have, but not how they work. This lets you create different classes that all follow the same rules.

**Example:**
SocialLogin is an interface. FacebookLogin and GoogleLogin must have an authenticate method.

### Python (Abstract Base Class)

```python
from abc import ABC, abstractmethod

class SocialLogin(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class FacebookLogin(SocialLogin):
    def authenticate(self):
        print("Authenticating with Facebook.")

class GoogleLogin(SocialLogin):
    def authenticate(self):
        print("Authenticating with Google.")
```

### Java (Interface)

```java
interface SocialLogin {
    void authenticate();
}

class FacebookLogin implements SocialLogin {
    public void authenticate() {
        System.out.println("Authenticating with Facebook.");
    }
}

class GoogleLogin implements SocialLogin {
    public void authenticate() {
        System.out.println("Authenticating with Google.");
    }
}
```

**Practice Questions:**
Q10. What is the purpose of an interface (Java) or abstract base class (Python)?
<details><summary>Show Answer</summary>They define a contract (methods) without implementation, enabling polymorphism and reducing coupling.</details>

Q11. What keyword is used in Java to declare an abstract method?
<details><summary>Show Answer</summary>abstract.</details>

Q12. In Python, which module supports abstract classes?
<details><summary>Show Answer</summary>The abc module (from abc import ABC, abstractmethod).</details>

**Practice Question:**
What is the purpose of an interface?
<details>
<summary>Show Answer</summary>
To make sure different classes have the same methods, so you can use them in the same way.
</details>

---

## 5) Polymorphism

**Concept:**
Polymorphism means you can use different classes in the same way if they share an interface or base class. The actual action depends on which class you use.

**Example:**
You can call login() with FacebookLogin, GoogleLogin, or InstagramLogin, and each will do its own thing.

### Python

```python
def login(social_login: SocialLogin):
    social_login.authenticate()

facebook_login = FacebookLogin()
google_login = GoogleLogin()
login(facebook_login)
login(google_login)

class InstagramLogin(SocialLogin):
    def authenticate(self):
        print("Authenticating with Instagram.")

login(InstagramLogin())
```

### Java

```java
class Auth {
    static void login(SocialLogin s) {
        s.authenticate();
    }
    public static void main(String[] args) {
        login(new FacebookLogin());
        login(new GoogleLogin());
        login(new SocialLogin() { // or a concrete InstagramLogin class
            public void authenticate() { System.out.println("Authenticating with Instagram."); }
        });
    }
}
```

**Practice Questions:**
Q13. Define polymorphism in object-oriented programming.
<details><summary>Show Answer</summary>The ability for different classes to provide different implementations of the same interface/abstract method.</details>

Q14. Example: If FacebookLogin and GoogleLogin both implement SocialLogin.authenticate(), what does calling authenticate() on a SocialLogin variable achieve?
<details><summary>Show Answer</summary>It dynamically invokes the correct implementation (Facebook or Google) at runtime.</details>

**Practice Question:**
How does polymorphism make code flexible?
<details>
<summary>Show Answer</summary>
You can write code that works with many types of objects, as long as they follow the same interface.
</details>

---

## 6) Coupling & OO Relationships

**Concept:**
Coupling is about how closely classes are connected. Loose coupling means classes work together but are not tightly linked, making code easier to change. There are different ways classes relate: association (uses-a), aggregation (has-a, but parts can exist alone), composition (has-a, parts belong to whole), inheritance (is-a).

**Example:**
A Student uses a Course (association). A Book has an Author (aggregation). A House has Rooms (composition). A Lion is an Animal (inheritance).

### Association — “uses-a”

#### Python

```python
class Student:
    def __init__(self, name): self.name = name
    def study(self, course): print(f"{self.name} is studying {course.name}")

class Course:
    def __init__(self, name): self.name = name
```

#### Java

```java
class Student {
    private String name;
    public Student(String name) { this.name = name; }
    public void study(Course course) { System.out.println(name + " is studying " + course.getName()); }
}
class Course {
    private String name;
    public Course(String name) { this.name = name; }
    public String getName() { return name; }
}
```

### Aggregation — “has-a” (parts can outlive whole)

#### Python

```python
class Author:
    def __init__(self, name): self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # aggregation
    def display_info(self):
        print(f"'{self.title}' by {self.author.name}")
```

#### Java

```java
class Author { 
    private String name;
    public Author(String name) { this.name = name; }
    public String getName() { return name; }
}
class Book {
    private String title;
    private Author author; // aggregation
    public Book(String title, Author author) { this.title = title; this.author = author; }
    public void displayInfo() { System.out.println("'" + title + "' by " + author.getName()); }
}
```

### Composition — “has-a” (parts bound to whole)

#### Python

```python
class Room:
    def __init__(self, name): self.name = name

class House:
    def __init__(self): self.rooms = []
    def add_room(self, room_name):
        room = Room(room_name)      # lifecycle owned by House
        self.rooms.append(room)
```

#### Java

```java
class Room { 
    private String name;
    public Room(String name) { this.name = name; }
}
class House {
    private java.util.List<Room> rooms = new java.util.ArrayList<>();
    public void addRoom(String name) { rooms.add(new Room(name)); } // composition
}
```

### Inheritance — “is-a” (tighter coupling)

#### Python

```python
class Animal:
    def __init__(self, name): self.name = name
    def move(self): print(f"{self.name} is moving.")

class Lion(Animal):
    def roar(self): print(f"{self.name} roars!")
```

#### Java

```java
class Animal2 {
    protected String name;
    public Animal2(String name) { this.name = name; }
    public void move() { System.out.println(name + " is moving."); }
}
class Lion extends Animal2 {
    public Lion(String name) { super(name); }
    public void roar() { System.out.println(name + " roars!"); }
}
```

**Practice Questions:**
Q15. Differentiate between aggregation and composition.
<details><summary>Show Answer</summary>Both are “has-a” relationships: in aggregation, parts can exist independently (e.g., Book has an Author); in composition, parts are bound to the whole’s lifecycle (e.g., House has Room).</details>

Q16. Which relationship describes “uses-a”?
<details><summary>Show Answer</summary>Association.</details>

**Practice Question:**
What is the difference between aggregation and composition?
<details>
<summary>Show Answer</summary>
Aggregation: parts can exist without the whole (e.g., Author and Book). Composition: parts belong to the whole and are created/destroyed with it (e.g., Room and House).
</details>

---

## 7) SOLID & Dependency Management with Databases

**Concept:**
If your app depends directly on a specific database, it’s hard to change later. SOLID principles say you should depend on interfaces, not details, so you can swap things easily.

**Example:**
MyApp uses MySQLDatabase directly (tight coupling). Better: MyApp uses a Database interface, so you can use MySQL or MongoDB.

### Problem (Tight Coupling)

#### Python

```python
class MySQLDatabase:
    def connect(self): print("Connecting to MySQL database")
    def save(self, data): print(f"Saving data to MySQL: {data}")
    def close(self): print("Closing MySQL connection")

class MyApp:
    def __init__(self, data: dict):
        self.data = data
    def save_to_db(self):
        db = MySQLDatabase()
        db.connect(); db.save(self.data); db.close()

data = {"name": "John Doe", "age": 30}
app = MyApp(data)
app.save_to_db()
```

#### Java

```java
class MySQLDatabase {
    public void connect() { System.out.println("Connecting to MySQL database"); }
    public void save(java.util.Map<String, Object> data) { System.out.println("Saving data to MySQL: " + data); }
    public void close() { System.out.println("Closing MySQL connection"); }
}
class MyApp {
    private java.util.Map<String, Object> data;
    public MyApp(java.util.Map<String, Object> data) { this.data = data; }
    public void saveToDb() {
        MySQLDatabase db = new MySQLDatabase();
        db.connect(); db.save(data); db.close();
    }
}
```

### Solution: Program to an Interface (OCP, DIP)

#### Python — Interface & Implementations

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def save(self, data): pass
    @abstractmethod
    def close(self): pass

class MySQLDatabase(Database):
    def connect(self): print("Connecting to MySQL database")
    def save(self, data): print(f"Saving data to MySQL: {data}")
    def close(self): print("Closing MySQL connection")

class MongoDB(Database):
    def connect(self): print("Connecting to MongoDB database")
    def save(self, data): print(f"Saving data to MongoDB: {data}")
    def close(self): print("Closing MongoDB connection")

class MyApp:
    def __init__(self, data: dict):
        self.data = data
    def save_to_db(self, db: Database):  # method injection here
        db.connect(); db.save(self.data); db.close()

data = {"name": "John Doe", "age": 30}
app = MyApp(data)
app.save_to_db(MySQLDatabase())
app.save_to_db(MongoDB())
```

#### Java — Interface & Implementations

```java
interface Database {
    void connect();
    void save(java.util.Map<String, Object> data);
    void close();
}
class MySQLDatabaseImpl implements Database {
    public void connect() { System.out.println("Connecting to MySQL database"); }
    public void save(java.util.Map<String, Object> data) { System.out.println("Saving data to MySQL: " + data); }
    public void close() { System.out.println("Closing MySQL connection"); }
}
class MongoDBImpl implements Database {
    public void connect() { System.out.println("Connecting to MongoDB database"); }
    public void save(java.util.Map<String, Object> data) { System.out.println("Saving data to MongoDB: " + data); }
    public void close() { System.out.println("Closing MongoDB connection"); }
}
class MyApp2 {
    private java.util.Map<String, Object> data;
    public MyApp2(java.util.Map<String, Object> data) { this.data = data; }
    public void saveToDb(Database db) {
        db.connect(); db.save(data); db.close();
    }
}
```

**Practice Questions:**
Q17. Which SOLID principle suggests “Depend on abstractions, not concrete implementations”?
<details><summary>Show Answer</summary>Dependency Inversion Principle (DIP).</details>

Q18. Which SOLID principle is about making classes open for extension but closed for modification?
<details><summary>Show Answer</summary>Open/Closed Principle (OCP).</details>

**Practice Question:**
Why is programming to an interface better than programming to a concrete class?
<details>
<summary>Show Answer</summary>
It makes your code flexible and easier to change or test, because you can swap implementations without changing the rest of your code.
</details>

---

## 8) Dependency Injection & Factories

**Concept:**
Dependency injection means giving an object what it needs (like a database) from the outside, instead of creating it inside. This makes code easier to test and change.

**Example:**
You can give MyApp a database using the constructor, a setter method, or a method parameter.

### Constructor Injection

#### Python

```python
class MyAppCtor:
    def __init__(self, data: dict, db: Database):
        self.data = data
        self.db = db
    def save_to_db(self):
        self.db.connect(); self.db.save(self.data); self.db.close()

data = {"name": "John Doe", "age": 30}
app_mysql = MyAppCtor(data, MySQLDatabase())
app_mysql.save_to_db()
app_mongo = MyAppCtor(data, MongoDB())
app_mongo.save_to_db()
```

#### Java

```java
class MyAppCtor {
    private java.util.Map<String, Object> data;
    private Database db;
    public MyAppCtor(java.util.Map<String, Object> data, Database db) {
        this.data = data; this.db = db;
    }
    public void saveToDb() { db.connect(); db.save(data); db.close(); }
}
```

### Setter Injection

#### Python

```python
class MyAppSetter:
    def __init__(self, data: dict):
        self.data = data
        self.db: Database | None = None
    def set_database(self, db: Database): self.db = db
    def save_to_db(self):
        if self.db is None: raise ValueError("Database instance is not set")
        self.db.connect(); self.db.save(self.data); self.db.close()

app = MyAppSetter({"name": "John Doe", "age": 30})
app.set_database(MySQLDatabase()); app.save_to_db()
app.set_database(MongoDB()); app.save_to_db()
```

#### Java

```java
class MyAppSetter {
    private java.util.Map<String, Object> data;
    private Database db;
    public MyAppSetter(java.util.Map<String, Object> data) { this.data = data; }
    public void setDatabase(Database db) { this.db = db; }
    public void saveToDb() {
        if (db == null) throw new IllegalStateException("Database instance is not set");
        db.connect(); db.save(data); db.close();
    }
}
```

### Method Injection (already shown in §7 Java’s `MyApp2.saveToDb`)

**Practice Questions:**
Q19. What is dependency injection?
<details><summary>Show Answer</summary>A design technique where a class receives its dependencies from external sources (constructor, setter, or method) rather than creating them internally.</details>

Q20. How does the factory pattern improve object creation?
<details><summary>Show Answer</summary>It centralizes and abstracts object creation, allowing clients to request objects by type without coupling to specific class constructors.</details>

**Practice Question:**
What is the benefit of dependency injection?
<details>
<summary>Show Answer</summary>
It makes code more flexible and testable, because you can easily swap or mock dependencies.
</details>

---

## 9) Factory for Object Creation

**Concept:**
A factory is a special class or method that creates objects for you. It hides the details of how objects are made, so you don’t have to change your code if the way you create them changes.

**Example:**
DatabaseFactory creates a MySQLDatabase or MongoDB for you, based on a string.

### Python

```python
class DatabaseFactory:
    @staticmethod
    def create_database(db_type: str) -> Database:
        if db_type == "mysql": return MySQLDatabase()
        elif db_type == "mongodb": return MongoDB()
        else: raise ValueError(f"Unknown database type: {db_type}")

class MyAppFactory:
    def __init__(self, db: Database): self.db = db
    def save_to_db(self, data: dict):
        self.db.connect(); self.db.save(data); self.db.close()

data = {"name": "John Doe", "age": 30}
mysql_db = DatabaseFactory.create_database("mysql")
MyAppFactory(mysql_db).save_to_db(data)

mongodb = DatabaseFactory.create_database("mongodb")
MyAppFactory(mongodb).save_to_db(data)
```

### Java

```java
class DatabaseFactory {
    public static Database createDatabase(String type) {
        return switch (type.toLowerCase()) {
            case "mysql" -> new MySQLDatabaseImpl();
            case "mongodb" -> new MongoDBImpl();
            default -> throw new IllegalArgumentException("Unknown database type: " + type);
        };
    }
}

class MyAppFactory {
    private final Database db;
    public MyAppFactory(Database db) { this.db = db; }
    public void saveToDb(java.util.Map<String, Object> data) {
        db.connect(); db.save(data); db.close();
    }
}

class DemoFactory {
    public static void main(String[] args) {
        var data = new java.util.HashMap<String, Object>();
        data.put("name", "John Doe"); data.put("age", 30);

        Database mysql = DatabaseFactory.createDatabase("mysql");
        new MyAppFactory(mysql).saveToDb(data);

        Database mongo = DatabaseFactory.createDatabase("mongodb");
        new MyAppFactory(mongo).saveToDb(data);
    }
}
```

**Practice Question:**
Why use a factory to create objects?
<details>
<summary>Show Answer</summary>
To keep creation logic in one place, making code easier to change and maintain.
</details>

---

## 10) Programming to an Interface (Recap)

**Why it matters:**
- You can swap implementations without touching client code (Open/Closed Principle).
- High-level modules depend on abstractions, not details (Dependency Inversion Principle).
- Improves testability (you can mock interfaces in unit tests).

**Minimal Java example:**

```java
// Database interface remains the same.
class MyService {
    private final Database db;
    public MyService(Database db) { this.db = db; } // constructor injection
    public void doWork(java.util.Map<String, Object> data) {
        db.connect(); db.save(data); db.close();
    }
}
```

**Practice Question:**
How does programming to an interface help with testing?
<details>
<summary>Show Answer</summary>
You can easily replace real implementations with fake ones (mocks) for testing, without changing your main code.
</details>
