def generate_test_cases():
    test_cases = []

    # Basic Test Case 1
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Alice'),
        (2, 'Bob'),
        (3, 'Charlie');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (101, 'Mathematics', 300.00),
        (102, 'English Literature', 250.00),
        (103, 'Computer Science', 500.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 101),
        (2, 2, 103),
        (3, 3, 102);
        """,
        "output": """
        | course_name      | fee    |
        |------------------|--------|
        | Computer Science | 500.00 |
        """
    })

    # Basic Test Case 2
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'David'),
        (2, 'Emma'),
        (3, 'Frank');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (201, 'Biology', 400.00),
        (202, 'Chemistry', 350.00),
        (203, 'Physics', 450.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 201),
        (2, 2, 203),
        (3, 3, 202);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Physics     | 450.00 |
        """
    })

    # Basic Test Case 3
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'George'),
        (2, 'Helen'),
        (3, 'Ian');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (301, 'History', 200.00),
        (302, 'Geography', 220.00),
        (303, 'Political Science', 240.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 301),
        (2, 2, 302),
        (3, 3, 303);
        """,
        "output": """
        | course_name       | fee    |
        |-------------------|--------|
        | Political Science | 240.00 |
        """
    })

    # Basic Test Case 4
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Jane'),
        (2, 'John'),
        (3, 'Doe');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (401, 'Art', 150.00),
        (402, 'Music', 180.00),
        (403, 'Dance', 170.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 401),
        (2, 2, 402),
        (3, 3, 403);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Music       | 180.00 |
        """
    })

    # Edge Test Case 1
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Anna'),
        (2, 'Elsa'),
        (3, 'Olaf');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (501, 'Physics', 1000.00),
        (502, 'Chemistry', 800.00),
        (503, 'Biology', 900.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 501),
        (2, 2, 502),
        (3, 3, 503);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Physics     | 1000.00 |
        """
    })

    # Edge Test Case 2
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Tom'),
        (2, 'Jerry'),
        (3, 'Spike');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (601, 'Economics', 600.00),
        (602, 'Finance', 700.00),
        (603, 'Accounting', 650.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 601),
        (2, 2, 602),
        (3, 3, 603);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Finance     | 700.00 |
        """
    })

    # Boundary Test Case 1
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Arthur'),
        (2, 'Martha'),
        (3, 'George');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (701, 'Law', 100.00),
        (702, 'Medicine', 200.00),
        (703, 'Engineering', 300.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 701),
        (2, 2, 702),
        (3, 3, 703);
        """,
        "output": """
        | course_name   | fee    |
        |---------------|--------|
        | Engineering   | 300.00 |
        """
    })

    # Boundary Test Case 2
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Mark'),
        (2, 'Luke'),
        (3, 'John');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (801, 'History', 150.00),
        (802, 'Geography', 250.00),
        (803, 'Political Science', 350.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 801),
        (2, 2, 802),
        (3, 3, 803);
        """,
        "output": """
        | course_name       | fee    |
        |-------------------|--------|
        | Political Science | 350.00 |
        """
    })
    
    # Corner Test Case 1
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Andrew'),
        (2, 'Bella'),
        (3, 'Chris');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (901, 'Philosophy', 500.00),
        (902, 'Sociology', 450.00),
        (903, 'Anthropology', 475.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 901),
        (2, 2, 902),
        (3, 3, 903);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Philosophy  | 500.00 |
        """
    })
    
    # Corner Test Case 2
    test_cases.append({
        "input": """
        -- Create Students table
        CREATE TABLE Students (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50)
        );

        -- Create Courses table
        CREATE TABLE Courses (
            course_id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            fee DECIMAL
        );

        -- Create Enrollments table
        CREATE TABLE Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        -- Insert data into Students table
        INSERT INTO Students (student_id, student_name) VALUES 
        (1, 'Sam'),
        (2, 'Dean'),
        (3, 'Castiel');

        -- Insert data into Courses table
        INSERT INTO Courses (course_id, course_name, fee) VALUES 
        (1001, 'Astronomy', 725.00),
        (1002, 'Astrophysics', 750.00),
        (1003, 'Cosmology', 800.00);

        -- Insert data into Enrollments table
        INSERT INTO Enrollments (enrollment_id, student_id, course_id) VALUES 
        (1, 1, 1001),
        (2, 2, 1003),
        (3, 3, 1002);
        """,
        "output": """
        | course_name | fee    |
        |-------------|--------|
        | Cosmology   | 800.00 |
        """
    })
    
    return test_cases

# Print the test cases
for i, test_case in enumerate(generate_test_cases()):
    print(f"### Test Case {i+1}")
    print("**Input:**")
    print(f"```sql\n{test_case['input']}\n```")
    print("**Expected Output:**")
    print(f"{test_case['output']}")
    print("\n")