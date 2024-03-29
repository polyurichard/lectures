
- [Java Spring](#java-spring)
  - [What is Spring Boot?](#what-is-spring-boot)
  - [Creating a Spring Boot Project](#creating-a-spring-boot-project)
- ["Hello World" program](#hello-world-program)
- [Defining a REST API for Book Service](#defining-a-rest-api-for-book-service)
  - [Defining the Book Model](#defining-the-book-model)
  - [Service Layer](#service-layer)
  - [Repository for Persistent Data Storage](#repository-for-persistent-data-storage)
  - [Database Configuration](#database-configuration)
  - [Introduction to ORM in Spring Boot with JPA](#introduction-to-orm-in-spring-boot-with-jpa)
- [Dependency Injection in Spring](#dependency-injection-in-spring)
  - [Overview](#overview)
  - [Types of Dependency Injection in Spring](#types-of-dependency-injection-in-spring)
    - [Field Injection](#field-injection)
    - [Constructor Injection](#constructor-injection)
    - [Setter Injection](#setter-injection)
  - [Case Study: MessageService](#case-study-messageservice)
- [Extending the REST API for Book Service](#extending-the-rest-api-for-book-service)
  - [Overview](#overview-1)
  - [Create a New Book](#create-a-new-book)
  - [Get a Single Book](#get-a-single-book)
  - [Update a Book](#update-a-book)
  - [Delete a Book](#delete-a-book)
- [References](#references)

# Java Spring

## What is Spring Boot?
Spring Boot is a Java framework for building web applications and microservices. 
- It is built on top of the Java Spring framework and provides a simplified way to create Spring-powered applications.
- Dependency injection: Spring Boot provides a powerful dependency injection mechanism that allows us to easily manage dependencies in our application. It allows us to decouple the creation of objects from the objects themselves, making the code more flexible and maintainable. 
- In Java Spring, beans are objects that are instantiated, assembled, and managed by the Spring IoC (Inversion of Control) container .
- The Application Context is the IoC container that contains all the beans (objects) in the application.


**Use cases of Spring Boot**

Which web frameworks developer  you use?
<img src="image.png" alt="Alt text" width="80%"><br/>
*Reference: [Java Dev Ecosystem 2023](https://www.jetbrains.com/lp/devecosystem-2023/java/)*

- **Web Applications**: 
  - A web application is a client-server application that runs in a web browser. Spring Boot provides a rich framework for building web applications using the MVC (Model-View-Controller) pattern.

  - We can implement web applications using different approaches:
    - Apps where the backend provides the fully prepared view in response to a client’s request. The browser directly interprets the data received from the backend and displays this information to the user in these apps. 
  
  <img src="image-3.png" alt="Alt text" width="90%">
  
  - Apps using frontend-backend separation: The backend only serves raw data. The browser runs a separate frontend app that gets the backend responses, processes the data, and instructs the browser what to display.
  
  <img src="image-2.png" alt="Alt text" width="90%">

- **REST APIs**: 
    In Software Engineering, an API (Application Programming Interface) is a set of functions and procedures that allow the creation of applications that access the features of an application, or other service. 

    API allows programs to communicate with each other:
    ![Alt text](image-7.png)

    REST API is a popular type of API 
    - Uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations. 
    - Applications can communicate with each other over the internet using the HTTP protocol (e.g., GET, POST, PUT, DELETE methods).
    - It often returns data in format like JSON or XML. 
      - JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.
    - REST API should return the appropriate HTTP status codes to indicate the status of the request.
      - 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error)...

    <img src="image-4.png" alt="Alt text" width="80%">

- **Microservices**: 
  - A microservice is a small, independently deployable service that performs a specific task. 
  - Microservices are typically used to build large applications using a collection of small services.

  <img src="image-5.png" alt="Alt text" width="80%">

## Creating a Spring Boot Project

**Spring Initializr** 

-  A web-based tool for generating Spring Boot projects. It allows us to select the dependencies and build tools for our project. 
-  Allows us to download the project as a zip file or generate a Maven project.

<img src="image-1.png" alt="Alt text" width="70%"> <br/>
*URL: [Spring Initializr](https://start.spring.io)*



The Tree Structure of a Spring Boot Project for a BookStore REST API project:

```text
my-spring-boot-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           └── bookstore/
│   │   │               ├── BookstoreApplication.java
│   │   │               ├── controller/
│   │   │               │   └── BookController.java
│   │   │               ├── model/
│   │   │               │   └── Book.java
│   │   │               ├── repository/
│   │   │               │   └── BookRepository.java
│   │   │               └── service/
│   │   │                   └── BookService.java
│   │   └── resources/
│   │       ├── application.properties
│   │       ├── static/
│   │       └── templates/
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   └── bookstore/
│                       ├── BookstoreApplicationTests.java
│                       ├── controller/
│                       ├── repository/
│                       └── service/
├── target/
├── mvnw
├── mvnw.cmd
├── pom.xml
└── README.md
````

Description of Key Components:
- **`src/`**: Contains the source code for the application.
  - **`main/java/com/example/bookstore/`**: Main Java package for the application.
    - **`BookstoreApplication.java`**: Main Spring Boot application class.
    - **`controller/`**: Controllers to handle HTTP requests.
    - **`model/`**: Domain model entities.
    - **`repository/`**: Data access layer with JPA repositories.
    - **`service/`**: Service layer with business logic.
  - **`resources/`**: Application configurations and other resources. E.g. `application.properties` file.
- **`test/`**: Test code
- **`target/`**: Contains the compiled output and other artifacts generated by Maven.
- **`mvnw` and `mvnw.cmd`**: Maven wrapper scripts for building the project without a pre-installed Maven.
- **`pom.xml`**: Maven Project Object Model file for project configurations and dependencies.
- **`README.md`**: Project documentation in markdown format.

In Java Spring, the Main Application Class is located in the `src/main/java` directory.
- It contains the `main()` method, which is the starting point of the application.
- The `BookstoreApplication`  class is annotated with `@SpringBootApplication`. This annotation is used to mark the class as a Spring Boot application.

```java
@SpringBootApplication
public class BookstoreApplication {
    public static void main(String[] args) {
        SpringApplication.run(BookstoreApplication.class, args);
    }

}
```

# "Hello World" program

In this section, we will create a simple Spring Boot application that prints "Hello World!" when we send a `GET /` request to the application.

**REST Controllers**: In Spring Boot, REST controllers are used to handle incoming web requests and returning responses using HTTP.

Here is an example of creating a Basic REST Controller that print "Hello World!"

```java
@RestController
public class HelloController {
    @GetMapping("/")
    public String index() {
        return "Hello World!";
    }
}
```

In Java, an annotation is a form of syntactic metadata that can be added to Java source code.
- `@RestController` is a class-level annotation that marks the class as a REST controller 
- `@GetMapping("/")` is a method-level annotation which indicates that the `index()` method should handle HTTP GET requests for the root ("/") path.

To start the Spring app, we can run the following command in the terminal:

```bash
mvn spring-boot:run
```

Here is the sample output of the Rest API when send a `GET /` request to the Spring App:

```text
"Hello World!"
```

# Defining a REST API for Book Service
In this section, we will define a REST API for a simple Book Service. The Book Service will be used to store and retrieve books from a database. The Book Service will expose a REST API that allows clients to perform CRUD operations on books.   

## Defining the Book Model

In Spring Boot , model classes represent the data in the application.

Here is the sample code for a simple model class for a book:

```java
package com.example.helloworld;

public class Book {
    private int bookid;
    private String title;
    private String author;

    // No-argument constructor 
    public Book() {
    }

    // Constructor with fields
    public Book(int bookid, String title, String author) {
        this.bookid = bookid;
        this.title = title;
        this.author = author;
    }

    // Getters and Setters
    public int getBookid() {
        return bookid;
    }

    public void setBookid(int bookid) {
        this.bookid = bookid;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
}
```

Explanation of Sample Code: 
- The `Book` class defines three properties (`bookid`, `title`, and `author`), a no-argument constructor, a parameterized constructor, and getters and setters for each property. 
- Model classes like `Book` can be used as return types in controller methods, where Spring Boot automatically converts them into JSON for RESTful responses.

Example:

```java
@RestController
public class BookController {
    @GetMapping("/book")
    public Book getBook() {
        return new Book(1, "The Alchemist", "Paulo Coelho");
    }
}
```

Explanation of Sample Code:
- The `BookController` class defines a `getBook()` method that returns a `Book` object.
- When the `getBook()` method is invoked, Spring Boot automatically converts the `Book` object into JSON and sends it back to the client as the HTTP response body.


Here is a sample HTTP request to create a new book:
```http
GET /book HTTP/1.1
```

Here is the sample HTTP response:
```http
HTTP/1.1 200
Content-Type: application/json

{
    "bookid": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho"
}
```

---

If we want to return a list of books, we can use the `List` interface:

```java
@RestController
public class BookController {
    @GetMapping("/books")
    public List<Book> getBooks() {
        List<Book> books = new ArrayList<>();
        books.add(new Book(1, "Spring in Action", "Craig Walls"));
        books.add(new Book(2, "Effective Java", "Joshua Bloch"));
        books.add(new Book(3, "Java Concurrency in Practice", "Brian Goetz"));
        return books;
    }
}
```

Here is the sample output of the Rest API when send a `GET /books` request to the Spring App:
    
```json
[
    {
        "bookid": 1,
        "title": "Spring in Action",
        "author": "Craig Walls"
    },
    {
        "bookid": 2,
        "title": "Effective Java",
        "author": "Joshua Bloch"
    },
    {
        "bookid": 3,
        "title": "Java Concurrency in Practice",
        "author": "Brian Goetz"
    }
]
```

The JSON response is a list of books, where each book is represented as a JSON object. 
- The bracket notation (`[]`) indicates that the response is a JSON array. 
- The curly braces (`{}`) represent a JSON object. 
- The book properties (`bookid`, `title`, and `author`) are mapped to the JSON object properties.

## Service Layer

In Spring Boot, the service layer is used to encapsulate the business logic of the application and is typically used to interact with the data source. In this section, we will introduce the service layer by refining the Book Service example from the previous section.

Let's define the class `BookService` to encapsulate the business logic of the Book Service.
- The `BookService` class acts as the intermediary between the controller (`BookController`) and the data source (in this case, a collection of books). 
- It handles the business logic, such as creating, retrieving, updating, and deleting books.

Sample Code:

```java
@Service
public class BookService {
    // Keeps a Collection of books
    private final Set<Book> books;

    // Constructor
    public BookService() {
        books = new HashSet<>();
        books.add(new Book(1, "Spring in Action", "Craig Walls"));
        books.add(new Book(2, "Effective Java", "Joshua Bloch"));
        books.add(new Book(3, "Java Concurrency in Practice", "Brian Goetz"));
    }

    // Returns all books in the collection
    public Set<Book> findAllBooks() {
        return books;
    }
}
```

Explanation of Sample Code:
- The `@Service` annotation marks `BookService` as a Spring-managed service bean. This means that Spring will automatically create an instance of `BookService` and inject it into `BookController` when needed.
- In the constructor, we initialize the `BookService` with a set of sample books. This mimics a data source in a simplified manner.
- The `findAllBooks()` method returns all books in the collection. It's a simple representation of a "read" operation in CRUD.

The `BookService` class is now responsible for managing the books, while the `BookController` class is responsible for handling web requests and delegating business logic to the service layer.

Here is how the `BookController` class looks like after the introduction of the service layer:

```java
@RestController
public class BookController {
    @autoWired
    private BookService bookService;    

    // Returns all books in the collection
    @GetMapping("/books")
    public Set<Book> getBooks() {
        return bookService.findAllBooks();
    }
}
```

##  Repository for Persistent Data Storage

In our previous example, we used a collection of books as the data source. However, in real-world applications, we need a persistent data storage solution.  

The following diagram illustrate the architecture of a typical Spring Boot application with a persistent data storage solution. 

<img src="image-8.png" alt="Alt text" width="80%">

*Remark: In Java Spring, the *Application Context* is a container that contains all the beans (objects) in the application.*

In Spring Boot,
-  A **repository** is responsible for data access and manipulation, typically interacting with a relational database. In this section, we will integrate a repository into our Book Service example.
- An **entity** is a model class that represents a database table. 

We first define the `Book` model as an entity class.

```java
    @Entity
    public class Book {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private int bookid;
        private String title;
        private String author;

        // Define the Constructors, getters, setters, toString() ...

    }
```

Explanation:
- The `@Entity` annotation marks the `Book` class as an entity class, which will be mapped to a database table in relational databases.
- The `@Id` annotation indicates the primary key of the entity
- The `@GeneratedValue` annotation indicates that the primary key is automatically generated
- The `@GeneratedValue(strategy = GenerationType.IDENTITY)` annotation indicates that the primary key is generated using an identity column (e.g., auto-increment in MySQL)

For the `Book` entity class, we should also define the constructor, getters, setters, and `toString()` methods...

---
Next, we will define the `BookRepository` interface, which extends `JpaRepository` to provide CRUD methods for `Book` entities.

The following is the sample code for the `BookRepository` interface:
- The `BookRepository` interface extends `JpaRepository` and provides CRUD (Create, Read, Update, and Delete) methods for `Book` entities in relational databases.
- The `BookRepository `class  provide an abstraction layer to perform database operations without writing explicit SQL queries.
- JpaRepository<Book,Integer> is a generic interface that takes two parameters: 
  - The first parameter is the entity class (`Book`), and 
  - The second parameter is the type of the primary key (`Integer`) for the Book entity.

```java

```java
public interface BookRepository extends JpaRepository<Book, Integer> {
}
```

The Spring Framework will create the following table in relationship databases based on the `Book` entity class:
| Column | Type    | Key       |
|--------|---------|-----------|
| id     | Integer | Primary   |
| title  | String  |           |
| author | String  |           |

> *Remark:*
> - JPA stands for Java Persistence API. It is a specification for accessing, persisting, and managing data between Java objects and relational databases. 
> - Spring Framework can use Hibernate as its JPA implementation to perform database operations.  Hibernate is a Java-based ORM (Object-Relational Mapping) framework that maps Java objects to database tables.

You can customize the `BookRepository` interface to support additional custom queries. For example, to support the operation find books by author, we can define the following method in the `BookRepository` interface:

```java
public interface BookRepository extends JpaRepository<Book, Integer> {
    List<Book> findByAuthor(String author); // Find books by author
}
```


Here is the sample code for the `BookService` class after integrating the `BookRepository`:

```java
@Service
public class BookService {
    @Autowired
    private final BookRepository repo;

    public Set<Book> findAllBooks() {
        return new HashSet<>(repo.findAll());
    }
}
```
Explanation:
- The `@Autowired` annotation is used in the Spring framework to automatically inject dependencies into a class. In this case, Spring will automatically inject an instance of `BookRepository` into `BookService`.
- The `findAllBooks()` method returns all books in the database using the `findAll()` method provided by `BookRepository`.

With the changes, our Spring app will now return all books from the database when we send a `GET /books` request to the app.  

## Database Configuration

There are two ways to configure the database in Spring Boot:
1. **Using `application.properties`**: We can configure the database in the `application.properties` file. For example, we can specify the JDBC URL, username, and password in the `application.properties` file.
2. **Include the MySQL JDBC driver in your `pom.xml`**: We can also configure the database by including the MySQL JDBC driver in the `pom.xml` file. For example, we can specify the JDBC URL, username, and password in the `pom.xml` file.

Example: Configure DataSource in `application.properties`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/mydatabase
spring.datasource.username=myusername
spring.datasource.password=mypassword
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

Explanation:
- The `spring.datasource.url` property specifies the JDBC URL of the MySQL database.
- The `spring.datasource.username` and `spring.datasource.password` properties specify the credentials for the MySQL database.
- The `spring.jpa.hibernate.ddl-auto` property specifies the Hibernate DDL auto (e.g., update, create, none). This is used to automatically create the database tables based on the entity classes (e.g., `Book`) in the application when the application starts.
- The `spring.datasource.driver-class-name` property specifies the MySQL JDBC driver class.- 

## Introduction to ORM in Spring Boot with JPA

Object-Relational Mapping (ORM) in Spring Boot, facilitated by JPA (Java Persistence API), allows seamless mapping of Java objects to relational database tables. This approach bridges the gap between the object-oriented domain model and the relational database.

Let's consider the scenario where we have two entities: `Book` and `Author`. Suppose that a book can only be written by one author, but an author can write multiple books. In this case, we have a one-to-many relationship between `Book` and `Author`.

The following code define the `Book` entity class to respesent a book in the database:
- Represents the `Book` table in the database.
- The @GeneratedValue annotation indicates that the primary key is automatically generated.
- The `@ManyToOne` annotation indicates that the relationship is many-to-one. The `@JoinColumn` annotation indicates that the `author_id` column in the `Book` table is a foreign key referencing the `Author` table.

```java
@Entity
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;

    @ManyToOne // Many books can be written by one author
    @JoinColumn(name = "author_id", nullable = false)
    private Author author;

    // Getters and setters...
}
```

The following code define the `Author` entity class to respesent an author in the database:
- Represents the `Author` table in the database.
- The `@OneToMany` annotation indicates that the relationship is one-to-many. The `mappedBy` attribute indicates that the relationship is mapped by the `author` field in the `Book` class.


```java
@Entity
public class Author {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedBy = "author") // One author can write many books
    private Set<Book> books;

    // Getters and setters...
}
```

When the Spring App is started, the Hibernate ORM framework will automatically create the `Book` and `Author` tables in the database based on the entity classes. 
- **Book Table**:
   - Columns: `id`, `title`, `author_id`
   - The `author_id` column is a foreign key referencing the `Author` table.

-  **Author Table**:
   - Columns: `id`, `name`

It will also automatically create the foreign key constraints to maintain the relationship between the two tables.

Here is an example of Database Tables with sample data


**Author Table**

| id | name        |
|----|-------------|
|  1 | John Doe    |
|  2 | Jane Smith  |

**Book Table**

| id | title             | author_id |
|----|-------------------|-----------|
|  1 | Spring in Action  |  1        |
|  2 | JPA for Beginners |  1        |
|  3 | Hibernate Basics  |  2        |


The following `BookService` class  illustrates how to create a new book and link up with an author from the database.
- The `createBook()` method takes the ID of the author and the book to be created as parameters.
- It first retrieves the author by its ID using the `findById()` method provided by `AuthorRepository`. If the author exists, it sets the author of the book using the `setAuthor()` method provided by `Book`. The `setAuthor()` method is created by the `@ManyToOne` annotation in the `Book` class.
- The `createBook()` method then saves the book to the database using the `save()` method provided by `BookRepository`.

```java
@Service
public class BookService {
    // Autowired repositories...
    public Book createBook(Long authorId, Book book) {
        Author author = authorRepository.findById(authorId).orElseThrow();
        book.setAuthor(author);
        return bookRepository.save(book);
    }
    // Additional methods...
}
```

ORM with JPA in Spring Boot simplifies managing relational data in an object-oriented manner. 
- By defining entities and their relationships, developers can interact with the database using Java objects, abstracting away complex SQL queries. 
- There is no need to write SQL queries to perform CRUD operations.


# Dependency Injection in Spring

## Overview

Spring Framework supports three primary methods of dependency injection to manage and inject dependencies into classes: Constructor Injection, Setter Injection, and Field Injection. These approaches provide flexibility in how dependencies are provided to an object. 

##  Types of Dependency Injection in Spring

### Field Injection

**Field Injection **involves injecting dependencies directly into fields.
- The `bookService` field is annotated with `@Autowired`.
- **Advantages**: Reduces boilerplate code, simpler to write.


  ```java
  @RestController
  public class BookController {
      @Autowired
      private BookService bookService;
  }
  ```

 

### Constructor Injection

**Constructor Injection** involves injecting dependencies through the class constructor. 
- The `@Autowired` annotation on the constructor is optional.
- When Spring creates `BookController`, it injects an instance of `BookService`.
- **Advantages**: Ensures that required dependencies are not null, allowing for immutability of dependencies (i.e. the dependencies cannot be changed after the object is instantiated).
  
```java
  @RestController
  public class BookController {
      private final BookService bookService;

      @Autowired
      public BookController(BookService bookService) {
          this.bookService = bookService;
      }
  }
```


### Setter Injection

**Setter Injection** involves injecting dependencies through setter methods.
- The `setBookService` method is annotated with `@Autowired`, telling Spring to inject `BookService` when creating `BookController`.
- Dependencies can be set at any time before the actual usage. This is useful when a class has optional dependencies that can be injected after the object is instantiated.

```java
@RestController
public class BookController {
    private BookService bookService;

    @Autowired
    public void setBookService(BookService bookService) {
        this.bookService = bookService;
    }
}
```

## Case Study: MessageService 
In this section, we will demonstrate how to use Dependency Injection in a Spring Boot application.

We will define the followin classes:
- `EmailMessageService`: Sends messages via email
- `SMSMessageService`: Sends messages via SMS
- The `MessageService` interface is implemented by both `EmailMessageService` and `SMSMessageService`. 
- The client class `NotificationService`  uses the `MessageService` interface to send messages.


<img src="image-6.png" alt="Alt text" width="80%">


The `MessageService` interface defines the contract for sending messages. It includes a method to send messages to a specified recipient.

```java
public interface MessageService {
    void sendMessage(String message, String recipient);
}
```

We now create the following implementation classes for the `MessageService` interface:


Here is the sample code for the `EmailMessageService` class:
- The `@Component` annotation marks the class as a Spring-managed bean (In Java Spring, a bean is an object that is instantiated, assembled, and managed by the Spring IoC container).

```java
@Component
public class EmailMessageService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("Sending email to " + recipient + ": " + message);
    }
}
```

Here is the sample code for the `SMSMessageService` class:

```java
@Service
public class SMSMessageService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("Sending SMS to " + recipient + ": " + message);
    }
}
```

We will now define the client class  `NotificationService`, which uses the `MessageService` to send messages. 
- The `NotificationService` class is also annotated with `@Component`, which marks it as a Spring-managed bean.
- In the code below, the `sendNotification()` method takes the message and recipient as parameters. It calls the `sendMessage()` method provided by `MessageService` to send the message to the recipient.

```java
@Component
public class NotificationService {
    @Autowired
    private final MessageService messageService;

    public void sendNotification(String message, String recipient) {
        messageService.sendMessage(message, recipient);
    }
}
```



When the Spring app is started, Spring will automatically create an instance of `NotificationService` and inject an implementation of `MessageService` into it. 
- In our example, there are two implementations of `MessageService`: `EmailMessageService` and `SMSMessageService`. 
- There is an ambiguity in selecting the implementation of `MessageService` to be injected into `NotificationService`. The IoC container has no idea which implementation to inject into `NotificationService`. 

---
Here are the possible ways to resolve this ambiguity:
1. Use of `@Qualifier` Annotation
2. Marking a Bean as `@Primary`
3. Configurations in `application.properties`

**Option 1**: Use of `@Qualifier` Annotation 

We can explicitly specify the bean to be used for autowiring using the `@Qualifier` annotation. In the code below, the `NotificationService` class is annotated with `@Qualifier("emailMessageService")`, which tells Spring to inject the `EmailMessageService` implementation.

```java
@Component
@Qualifier("emailMessageService")
public class NotificationService {
    @Autowired
    private final MessageService messageService;

    public void sendNotification(String message, String recipient) {
        messageService.sendMessage(message, recipient);
    }
}
```

**Option 2**: Marking a Bean as `@Primary`

We can designate one of the implementations as the primary bean. In the code below, the `EmailMessageService` class is annotated with `@Primary`, which tells Spring to give preference to the primary bean when resolving the dependency.

```java
@Component
@Primary
public class EmailMessageService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("Sending email to " + recipient + ": " + message);
    }
}
```

**Option 3**: Configurations in `application.properties` 
- We can also configure the application to select the implementation of `MessageService` to be injected into `NotificationService`. 
- **Advantage:** Easily switch implementations in different environments (e.g. development, production, testing) by changing the property value in the configuration file without chaning the code.

In the code below, the `application.properties` file is configured to inject the `EmailMessageService` implementation.
1. **Define a Property in `application.properties`**:
   - Set a property in `application.properties` that determines which implementation to use. For example:
    ```
    messaging.service.type=email
    ```
2. **Conditional Bean Creation in Configuration Class**:
   - Use the `@ConditionalOnProperty` annotation in your Java configuration class to create beans conditionally based on the property value.
   - Example:
    ```java
    @Configuration
    public class MessagingConfig {

        @Bean
        @ConditionalOnProperty(name = "messaging.service.type", havingValue = "email")
        public MessageService emailMessageService() {
            return new EmailMessageService();
        }

        @Bean
        @ConditionalOnProperty(name = "messaging.service.type", havingValue = "sms")
        public MessageService smsMessageService() {
            return new SMSMessageService();
        }
    }
    ```
3. **Injecting the Selected Implementation**:
   - In your service or controller where `MessageService` is required, simply autowire the `MessageService`. Spring will automatically inject the correct implementation based on the configuration.

   ```java
   @Service
   public class NotificationService {
        @Autowired
        private final MessageService messageService;
   }
   ```



In this section, we demonstrated how to use Dependency Injection in Spring Boot applications.
- By using DI, there is no need for developer to create the dependencies manually. The dependencies are automatically injected into the object by the IoC container.
- **Loose coupling:** DI allows us to easily change the dependencies of an object. This reduces the coupling between objects, making the code more maintainable and testable.
- **Flexible code: **DI allows us to easily switch the dependencies of an object (e.g. by changing the configuration file). This makes the code more flexible.
- **Testable code**: 
  - DI allows us to easily test the object in isolation by injecting mock dependencies. 
    - E.g., during unit testing, spring can inject mock dependencies for the interface `MessageService`. 
  - This allows us to test the `NotificationService` class in isolation.

# Extending the REST API for Book Service 

## Overview
The current implementation of our `Book` Service can retrieve all books from the database. However, to enhance its functionality and make it a comprehensive tool for managing books, we may  extend the REST API to support full CRUD (Create, Read, Update, Delete) operations.

The following table summarizes the REST API endpoints for the Book Service:

| Operation         | HTTP Method | Endpoint          | Request Body                                  | Success Response        | Failure Response       |
|-------------------|-------------|-------------------|-----------------------------------------------|-------------------------|------------------------|
| Create a new book | POST        | `/api/books`      | JSON object with book details                 | 201 (Created) with book details | 400 (Bad Request) if input is invalid |
| Read all books    | GET         | `/api/books`      | N/A                                           | 200 (OK) with list of books | 500 (Internal Server Error) |
| Read a single book| GET         | `/api/books/{id}` | N/A                                           | 200 (OK) with book details | 404 (Not Found) if book ID doesn't exist |
| Update a book     | PUT         | `/api/books/{id}` | JSON object with updated book details        | 200 (OK) with updated book details | 404 (Not Found) if book ID doesn't exist |
| Delete a book     | DELETE      | `/api/books/{id}` | N/A                                           | 204 (No Content) | 404 (Not Found) if book ID doesn't exist |



## Create a New Book
To support the creation of a new book, we may extend our `BookService` class with a `createBook()` method. In the code below, 
- the `createBook()` method takes the book to be created as a parameter. It calls the `save()` method provided by `BookRepository` to create a new book.

```java
@Service
public class BookService {
    @Autowired
    private final BookRepository repo;

    // existing code ...

    // Create a new book
    public Book createBook(Book book) {
        return repo.save(book);
    }
}
```

We should also update the `BookController` class to handle the `POST /api/books` request. - In the code below, the `createBook()` method takes the book to be created as a parameter. It calls the `createBook()` method in `BookService` to create a new book. 
- If the book is created successfully, it returns the newly created book with the HTTP status code `201 (Created)`. 

```java
@RestController
public class BookController {
    @Autowired
    private BookService bookService;

    // existing code ...

    // Create a new book
    @PostMapping("/api/books")
    public ResponseEntity<Book> createBook(@RequestBody Book book) {
        Book newBook = bookService.createBook(book);
        return new ResponseEntity<>(newBook, HttpStatus.CREATED);
    }
}
```
In the sample code:
- The `@PostMapping("/api/books")` annotation indicates that the `createBook()` method should handle the `POST /api/books` request.
- The `@RequestBody` annotation indicates that the `book` parameter should be retrieved from the request body.
- The `createBook()` method calls the `createBook()` method in `BookService` to create a new book.
- The `ResponseEntity` class is a generic class that represents an HTTP response. It allows us to set the HTTP status code and the response body. The `createBook()` method returns a `ResponseEntity` object with the newly created book and the HTTP status code `201 (Created)`.

Here is a sample HTTP request to create a new book:

```http
POST /api/books HTTP/1.1
Content-Type: application/json

{
    "title": "The Alchemist",
    "author": "Paulo Coelho"
}
```

Here is the sample HTTP response:

```http
HTTP/1.1 201
Content-Type: application/json

{
    "bookid": 4,
    "title": "The Alchemist",
    "author": "Paulo Coelho"
}
```


## Get a Single Book

Our Book API currently supports retrieving all books from the database. However, we may also want to retrieve a specific book by its ID. In this section, we will extend the Book API to support retrieving a single book by its ID.

We may extend our `BookService` class with a `getBookById()` method. 
- In the code below, the `getBookById()` method takes the ID of the book to be retrieved as a parameter. 
- It first checks if the book exists in the database using the `existsById()` method provided by `BookRepository`. If the book exists, it retrieves the book using the `getBookById()` method provided by `BookService`.
- The findBookById() method returns the book if the book exists. Otherwise, it returns null.

```java
@Service
public class BookService {
    @Autowired
    private final BookRepository repo;

    // existing code ...

    // Get a book by ID
    public Book getBookById(Long id) {
        return repo.findById(id).orElse(null);
    }
}
```

We should also update the `BookController` class to handle the `GET /api/books/{id}` request. 
- In the code below, the `getBookById()` method takes the ID of the book to be retrieved as a parameter. 
- It first checks if the book exists in the database using the `existsById()` method provided by `BookRepository`. If the book exists, it retrieves the book using the `getBookById()` method provided by `BookService`.

```java
@RestController
public class BookController {
    @Autowired
    private BookService bookService;

    // existing code ...

    // Get a book by ID
    @GetMapping("/api/books/{id}")
    public ResponseEntity<Book> getBookById(@PathVariable Long id) {
        // Call the getBookById() method in the bookService and return the book
        Book book = bookService.getBookById(id);

        // If the book exists, return the book
        if (book != null) {
            return new ResponseEntity<>(book, HttpStatus.OK); // 200 (OK)
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND); // 404 (Not Found)
        }
    }
}
```

In the sample code, 
- The `@GetMapping("/api/books/{id}")` annotation indicates that the `getBookById()` method should handle the `GET /api/books/{id}` request.
- The `@PathVariable` annotation indicates that the `id` parameter should be retrieved from the path variable.
- The `getBookById()` method calls the `getBookById()` method in `BookService` to retrieve a book by its ID.
- The `ResponseEntity` class is a generic class that represents an HTTP response. It allows us to set the HTTP status code and the response body. The `getBookById()` method returns a `ResponseEntity` object with the retrieved book and the HTTP status code `200 (OK)` if the book exists. Otherwise, it returns a `ResponseEntity` object with the HTTP status code `404 (Not Found)`.
  

Retrieving the details of a specific book is done via the `GET /api/books/{id}` endpoint. For instance, to retrieve the details of the book with ID 1, we can send a `GET /api/books/1` request to the Book API.

Here is a sample HTTP request to retrieve the details of a book with ID 1:
    
```http
GET /api/books/1 HTTP/1.1
```

Here is the sample HTTP response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "bookid": 1,
    "title": "1984",
    "author": "George Orwell"
}
```

## Update a Book


Updating a book involves modifying its details like title or author. This is achieved through the `PUT /api/books/{id}` endpoint.

We should extend our `BookService` class with an `updateBook()` method. In the code below, the `updateBook()` method takes two parameters: `id` and `bookDetails`. The `id` parameter is the ID of the book to be updated, and the `bookDetails` parameter is the updated book details.

```java
@Service
public class BookService {
    @Autowired
    private final BookRepository repo;

    // existing code ...

    // Update a book
    public Book updateBook(Long id, Book bookDetails) {
        // Get the book by ID from the database
        Book book = repo.findById(id).orElse(null);

        // If the book exists, update the book details and save the changes
        if (book != null) {
            book.setTitle(bookDetails.getTitle());
            book.setAuthor(bookDetails.getAuthor());
            return repo.save(book);
        }
        return null;
    }
}
```
Explanation:
- The `updateBook()` method takes two parameters: `id` and `bookDetails`. The `id` parameter is the ID of the book to be updated, and the `bookDetails` parameter is the updated book details.
- The `updateBook()` method first retrieves the book by its ID using the `findById()` method provided by `BookRepository`. If the book exists, it updates the book details and saves the changes to the database using the `save()` method provided by `BookRepository`.
- The `updateBook()` method returns the updated book if the book exists. Otherwise, it returns `null`.
- The `updateBook()` method is called by the `updateBook()` method in `BookController`.
  

We should also update the `BookController` class to handle the `PUT /api/books/{id}`. 
- In the code below, the `updateBook()` method takes the ID of the book to be updated as a parameter. 
- It first checks if the book exists in the database using the `existsById()` method provided by `BookRepository`. If the book exists, it updates the book using the `updateBook()` method provided by `BookService`.

```java
@RestController
public class BookController {
    @Autowired
    private BookService bookService;

    // existing code ...

    // Update a book
    @PutMapping("/api/books/{id}")
    public ResponseEntity<Book> updateBook(@PathVariable Long id, @RequestBody Book bookDetails) {
        // Call the updateBook() method in the bookService and return the updated book
        Book updatedBook = bookService.updateBook(id, bookDetails);

        // If the book exists, return the book
        if (updatedBook != null) {
            return new ResponseEntity<>(updatedBook, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
```

Here is the sample HTTP request and response to update the details of a book with ID 1:

```http
PUT /api/books/1 HTTP/1.1
Content-Type: application/json

{
    "title": "1984",
    "author": "George Orwell"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "bookid": 1,
    "title": "1984",
    "author": "George Orwell"
}
```

## Delete a Book

To delete a book, we can extend our `BookService` class with a `deleteBook()` method. In the code below, the `deleteBook()` method takes the ID of the book to be deleted as a parameter. It first checks if the book exists in the database using the `existsById()` method provided by `BookRepository`. If the book exists, it deletes the book using the `deleteById()` method provided by `BookRepository`.

```java
@Service
public class BookService {
    @Autowired
    private final BookRepository repo;

    // existing code ...

    // Delete a book
    public boolean deleteBook(Long id) {
        if (repo.existsById(id)) {
            repo.deleteById(id);
            return true;
        }
        return false;
    }
}
```

We should also update the `BookController` class to handle the `DELETE /api/books/{id}` request. In the code below, the `deleteBook()` method takes the ID of the book to be deleted as a parameter. It first checks if the book exists in the database using the `existsById()` method provided by `BookRepository`. If the book exists, it deletes the book using the `deleteBook()` method provided by `BookService`.

```java
@RestController
public class BookController {
    @Autowired
    private BookService bookService;

    // existing code ...

    // Delete a book
    @DeleteMapping("/api/books/{id}")
    public ResponseEntity<HttpStatus> deleteBook(@PathVariable Long id) {
        // Call the deleteBook() method in the bookService and return the HTTP status code
        if (bookService.deleteBook(id)) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT); // 204 (No Content)
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND); // 404 (Not Found)
        }
    }
}
```


# References
- [Spring Guide](https://spring.io/guides)
- Laurentiu Spilca, Spring Start Here, Manning Publications, 2021.

