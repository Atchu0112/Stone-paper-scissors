from datetime import datetime

def calculate_age(birthdate):
    today=datetime.today()
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    return age
birthdate_input=input("Enter your birthdate(DD-MM-yyyy):")
birthdate=datetime.strptime(birthdate_input,"%d-%m-%Y")
age=calculate_age(birthdate)
print(f"YOUR AGE IS:{age}")