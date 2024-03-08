# QuizMaster: Python Quiz Creation and Solving

QuizMaster is a Python project designed for quiz creation and solving. The application features a command-line interface that supports functionalities such as quiz creation, question addition, and interactive quiz-solving.

## Key Features

- **Quiz Creation:** Users can create quizzes based on difficulty levels, specifying the number of questions and saving the quiz to a file.

- **Question Management:** The master question list allows users to add questions with details such as text, choices, correct answers, and difficulty levels.

- **Quiz Solving:** The program guides users through interactive quiz-solving, presenting questions one by one and calculating scores based on difficulty levels.

## Implementation Highlights

- **Layered Architecture:** Utilizes a layered architecture with distinct modules for Repository, Controller, and UI, promoting code modularity and maintainability.

- **File Handling:** Implements robust file handling to read and write quiz and master question list files, ensuring data persistence.

- **Scalability:** Supports scalability by dynamically selecting questions from the master list for quiz creation, accommodating various difficulty levels.

## Non-functional Requirements

- **User-Friendly Commands:** The application gracefully handles user commands, providing clear error messages and preventing crashes regardless of input.

- **Command Examples:**
  - `create hard 6 hardquiz.txt`
  - `add 5;Which of the following numbers is prime?;5;56;75;5;easy`
  - `start myquiz.txt`

## Testing and Documentation

- **Specification:** Provides specifications for non-trivial methods in the Repository and Controller layers, ensuring a clear understanding of the codebase.

- **Tests:** Includes comprehensive tests to validate the functionality of key components, promoting code reliability.

This QuizMaster 2000 project demonstrates proficiency in Python programming, file handling, and the implementation of a layered architecture. The user-friendly interface and robust functionalities make it an engaging tool for quiz enthusiasts and learners alike.

