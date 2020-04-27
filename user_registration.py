def registration():

    name=input("enter your full name ")
    print(name)

    age = input("enter your age")
    print(age)

    cell_number=input("enter your cell number")
    print(cell_number)

    location=input("enter your current location")
    print(location)

    medical_history_lifestyle_disease=("living with lifestyle disease")
    print(medical_history_lifestyle_disease)

registration()
name=input("enter your full name ")
print(name)

age = input("enter your age")
print(age)

cell_number=input("enter your cell number")
print(cell_number)

location=input("enter your current location")
print(location)

medical_history_lifestyle_disease = input("living with lifestyle disease,enter True or False")
print(medical_history_lifestyle_disease)



vulnerable_group=0 #older than 50 years old,living with lifestyle disease

semi_vulnerable_group=0 #younger than 50 years old but with a lifestyle disease

carrier_group=0 #have tested positive,not showing any symptoms so far and are not vulnerable

home_care_group=0 #have tested positive,not in vulnerable age group,showing symptoms but not living with any lifestyle disease

safe_group=0

COVID_19_symptomps=False


test_result = False
def home_test_kit():
    if test_result == False and int(age) <=40 and medical_history_lifestyle_disease== False :
        safe_group=+1
        print(name + " you are COVID_19 negative,stay home,")

    elif test_result == True and int(age) >=41 and medical_history_lifestyle_disease==True :
        vulnerable_group=+1
        print(name +"you are positive and in a very vulnerable age bracket,we will contact you and admit you in a medical facility")


    elif test_result ==True and medical_history_lifestyle_disease==False and COVID_19_symptomps==False:
        carrier_group=+1
        print(name +"C0VID_19 positive but you are a carrier,please confine yourself in a room at home and take daily assessment ")

    elif test_result ==False and medical_history_lifestyle_disease==True and int(age) >=40 :
        semi_vulnerable_group=+1
        print(name +"you are negative but you are in the vulnerable group,please please stay home and follow WHO directives")

    else:
        print("follow World Health Organization directives")
home_test_kit()
