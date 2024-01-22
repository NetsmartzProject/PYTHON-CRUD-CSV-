#### STUDENT  MANAGEMENT SYSTEM  

This is a simple Student Management System implemented in Python using the Pandas library for data handling. The system allows users to perform basic operations such as adding, fetching, updating, and deleting student records stored in a CSV file.

### Instructions

Add Student Details :- 

### Choose option 1 to add new student details.

Enter the student's name, last name, degree, and score when prompted.

### Fetch Student Details by Name
Choose option 2 to search for student details by name.
### Enter the name you want to search for.
Update Student Records by Name

Choose option 3 to update existing student records.
#### Enter the name, last name, degree, and score of the student whose record you want to update.
Provide the updated information when prompted.
Delete Student Records by Name

### Choose option 4 to delete student records by name.
Enter the name of the student whose records you want to delete.
Quit

Choose option 5 to exit the program.

### USAGE 
Run the script in a Python environment.

Follow the on-screen prompts to interact with the Student Management System.
Note
The student records are stored in a CSV file named student_data.csv.

If the CSV file doesn't exist initially, it will be created when the first student record is added.
The system handles file not found errors gracefully and provides appropriate messages.

Feel free to use, modify, or enhance this system for your specific needs.



### Multithreading and Multiprocessing Example


This Python script demonstrates the concepts of multithreading and multiprocessing by performing square and cube calculations concurrently. The program uses both threading and multiprocessing to showcase the difference between these parallelization approaches.

### Multithreading
Threaded Calculation of Squares and Cubes
Threaded Square Calculation

The calc_square function calculates the square of numbers in a threaded manner.
A separate thread (t1) is created to execute the square calculation concurrently.
Threaded Cube Calculation

The calc_cube function calculates the cube of numbers in another thread (t2).
Both threads (t1 and t2) run concurrently.
Execution

Threads are started using t1.start() and t2.start().
t1.join() and t2.join() ensure that the main program waits for the threads to finish before proceeding.
Result Display

The total time taken for both threaded operations is printed at the end.

### Multiprocessing
Multiprocessing Square Calculation
Multiprocessing Square Calculation

The calc_square function calculates the square of numbers in a multiprocessing manner.
A separate process (t1) is created to execute the square calculation concurrently.
Execution

The process is started using t1.start() and t1.join() ensures that the main program waits for the process to finish before proceeding.
Result Display

The total time taken for the multiprocessing operation is printed at the end.
Note
The script uses a shared square_list to store square values in both the multithreading and multiprocessing examples.
The program calculates squares and cubes for the array [2, 3, 8, 9].
Usage
Run the script in a Python environment.
Observe the concurrent execution of square and cube calculations using multithreading and multiprocessing.
Feel free to experiment with the code, adjust the input array, and explore the differences in performance between multithreading and multiprocessing.












