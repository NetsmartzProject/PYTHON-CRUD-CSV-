import pandas as pd
import os

def add_student_details():
    name = input("Enter student name: ")
    lastname = input("Enter the last name of Student: ")
    degree = input("Enter degree: ")
    score = float(input("Enter score: "))

    # Create a DataFrame to store the data
    student_data = pd.DataFrame({'Name': [name], 'Lastname': [lastname], 'Degree': [degree], 'Score': [score]})

    # Check if the CSV file already exists
    if os.path.exists('student_data.csv'):
        existing_data = pd.read_csv('student_data.csv')
        print(existing_data,"existing_data")
        updated_data = pd.concat([existing_data, student_data], ignore_index=True)
        print(updated_data,"updated_data")

    else:
        updated_data = student_data
    # Save the updated data to the CSV file
    updated_data.to_csv('student_data.csv', index=False)

if __name__ == "__main__":
    add_student_details()
