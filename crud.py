import pandas as pd

# Function to add student details to the CSV file
def add_student_details():
    name = input("Enter student name: ")
    lastname=input("Enter the last name of Student ")
    degree = input("Enter degree: ")
    score = float(input("Enter score: "))

    # Create a DataFrame to store the data
    student_data = pd.DataFrame({'Name': [name], 'Lastname':[lastname],'Degree': [degree], 'Score': [score]})

    # Check if the CSV file already exists
    try:
        existing_data = pd.read_csv('student_data.csv')
        updated_data = pd.concat([existing_data, student_data], ignore_index=True)
    except FileNotFoundError:
        updated_data = student_data
        print(updated_data,"updated_data")

    # Save the updated data to the CSV file
    updated_data.to_csv('student_data.csv', index=False)
    print("Student details added and saved to CSV.")

# Function to fetch student details by name
def fetch_student_details_by_name():
    name = input("Enter the name to search: ")
    try:
        student_data = pd.read_csv('student_data.csv')
        print(student_data,"student_data")
        result = student_data[student_data['Name'] == name]
        print(result,"Result",result.empty)
        if not result.empty:
            print("\nStudent details found:")
            print(result)
        else:
            print("\nStudent not found in the database.")
    except FileNotFoundError:
        print("CSV file not found. No data to search.")

# Function to delete student records by name
def delete_student_by_name():
    name = input("Enter the name to delete: ")
    try:
        student_data = pd.read_csv('student_data.csv')
        filtered_data = student_data[student_data['Name'] != name]
        print(filtered_data,"filtered_data","length of student_data",len(student_data))
        if len(filtered_data) < len(student_data):
            filtered_data.to_csv('student_data.csv', index=False)
            print(f"\nStudent records for {name} deleted.")
        else:
            print(f"\nStudent with name {name} not found in the database.")
    except FileNotFoundError:
        print("CSV file not found. No data to delete.")

# Function to update student records by name
def update_student_by_name():
    name = input("Enter the name to update: ")
    lastname = input("Enter the lastname to update: ")
    score =float(input('Enter the Score '))
    degree = input("Enter the Degree to update:")
    try:
        student_data = pd.read_csv('student_data.csv')
        result = student_data[(student_data['Name'] == name) & (student_data['Lastname'] == lastname) & (student_data['Score'] == score) & (student_data['Degree'] == degree)]
        if not result.empty:
            print("\nExisting student details:")
            print(result)
            new_name = input("Enter updated name: ")
            new_lastname = input("Enter the updated lastname:")
            new_degree = input("Enter updated degree: ")
            new_score = float(input("Enter updated score: "))
           
            student_data.loc[student_data['Name'] == name, 'Name'] = new_name
            student_data.loc[student_data['Lastname'] == lastname, 'Lastname'] = new_lastname
            student_data.loc[student_data['Degree'] == degree, 'Degree'] = new_degree
            student_data.loc[student_data['Score'] == score, 'Score'] = new_score
            student_data.to_csv('student_data.csv', index=False)
            print(f"\nStudent records for {name} updated.")
        else:
            print(f"\nStudent with name {name} not found in the database.")
    except FileNotFoundError:
        print("CSV file not found. No data to update.")
# Main function
def main():
    while True:
        print("\n1. Add student details")
        print("2. Fetch student details by name")
        print("3. Update student records by name")
        print("4. Delete student records by name")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student_details()
        elif choice == '2':
            fetch_student_details_by_name()
        elif choice == '3':
            update_student_by_name()
        elif choice == '4':
            delete_student_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
