# Import necessary libraries
import datetime

# Sample database of vaccines (In a real application, this would be a proper database)
vaccines = {
    "BCG": {"disease": "Tuberculosis", "schedule": "At birth"},
    "HepB": {"disease": "Hepatitis B", "schedule": "At birth, 6 weeks, 6 months"},
    "OPV": {"disease": "Polio", "schedule": "At birth, 6 weeks, 10 weeks, 14 weeks"},
    # Add more vaccines as needed
}

# Sample data storage for children (In a real application, use a database)
children_records = {}

# Function to display vaccine information
def display_vaccine_info():
    print("\nVaccine Information:")
    for vaccine, details in vaccines.items():
        print(f"Vaccine: {vaccine}\nDisease: {details['disease']}\nSchedule: {details['schedule']}\n")

# Function to add a child’s record
def add_child_record():
    child_name = input("Enter the child's name: ")
    dob = input("Enter the child's date of birth (YYYY-MM-DD): ")
    
    children_records[child_name] = {
        "dob": dob,
        "vaccination_history": [],
        "appointments": []
    }
    print(f"Record added for {child_name}.")

# Function to update vaccination history
def update_vaccination_history(child_name, vaccine):
    if child_name in children_records:
        children_records[child_name]["vaccination_history"].append({
            "vaccine": vaccine,
            "date": datetime.date.today().strftime("%Y-%m-%d")
        })
        print(f"{vaccine} vaccination updated for {child_name}.")
    else:
        print("Child not found!")

# Function to schedule an appointment
def schedule_appointment(child_name, date):
    if child_name in children_records:
        children_records[child_name]["appointments"].append(date)
        print(f"Appointment scheduled for {child_name} on {date}.")
    else:
        print("Child not found!")

# Function to display a child’s record
def display_child_record(child_name):
    if child_name in children_records:
        print(f"\nRecord for {child_name}:")
        print(f"Date of Birth: {children_records[child_name]['dob']}")
        print("Vaccination History:")
        for vaccine in children_records[child_name]["vaccination_history"]:
            print(f"Vaccine: {vaccine['vaccine']}, Date: {vaccine['date']}")
        print("Appointments:")
        for appointment in children_records[child_name]["appointments"]:
            print(f"Date: {appointment}")
    else:
        print("Child not found!")

# Main Menu
def main():
    while True:
        print("\n1. Display Vaccine Information")
        print("2. Add Child Record")
        print("3. Update Vaccination History")
        print("4. Schedule Appointment")
        print("5. Display Child Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_vaccine_info()
        elif choice == '2':
            add_child_record()
        elif choice == '3':
            child_name = input("Enter the child's name: ")
            vaccine = input("Enter the vaccine name: ")
            update_vaccination_history(child_name, vaccine)
        elif choice == '4':
            child_name = input("Enter the child's name: ")
            date = input("Enter the appointment date (YYYY-MM-DD): ")
            schedule_appointment(child_name, date)
        elif choice == '5':
            child_name = input("Enter the child's name: ")
            display_child_record(child_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
