import random
import csv
import os
#import datetime

def main():
    ...
    

def welcome_page():
    print("Welcome to My Bank\n\nYour App for Empowering you Financial Freedom\n Your Money, Your Way\n Press the corresponding Number to start:\n 1.My Profile\n 2.My History\n 3.My Loans\n 4.My Card\n 5.My Fx account\n 6.help")

def my_profile():
    print("Please Enter your data to createa profile with us")
    customer_id = random.randint(12322, 99999)
    customer_title = input("Title (Mrs/Mr): ").lower()
    customer_first_name = input("First Name (include any middle names): ").lower()
    customer_last_name = input("Last Name: ").lower()
    customer_dob = input("Date of birth(DD.MM.YYYY): ")
    customer_address = input("Country of Residence: ").lower()
    customer_nationality = input("Nationality: ").lower()
    customer_email = input("E-mail: ") #^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

    customer_phone = input("Phone(include country code): ")
    customer_agreement = input("Do you agree to processing your data by MyBank as per international regulations (yes/no): ").lower()

    if customer_agreement == "yes" or customer_agreement == "y":
        print("Welcome to My Bank", customer_title, customer_last_name, "\nPlease discover our wide range of services")
        return welcome_page()

    elif customer_agreement == "no" or customer_agreement == "n":
        print("Unfortunately", customer_title, customer_last_name, " we cannot offer you our services without your consent to processing your data. \n Please type exit to abandon the process or yes to agree to our TandC: ")
        if customer_agreement == "yes" or customer_agreement == "y":
            return welcome_page()
        elif customer_agreement == "exit":
            print("Sad to see you go ", customer_title, customer_last_name)
        else:
            print("Invalid Choice, Kindly enter Yes or Exit")
    else:
        print("Invalid Choice, Kindly enter Yes or No")



    if not os.path.isfile("customerdata.csv"):
        with open("customerdata.csv", "w") as file:
            
            writer = csv.writer(file)
            writer.writerow(["customer_id",
                             "customer_title",
            "customer_first_name",
            "customer_last_name",
            "customer_dob",
            "customer_address",
            "customer_nationality",
            "customer_email",
            "customer_phone"])


    with open("customerdata.csv", "a") as results_file:
        writer = csv.writer(results_file)
        writer.writerow([
            customer_id,
            customer_title,
            customer_first_name,
            customer_last_name,
            customer_dob,
            customer_address,
            customer_nationality,
            customer_email,
            customer_phone
        ])

def my_history():
    print(" Below is your transaction history ")
def my_loans():
    print("Our Selection of available loans is below \n Press the corresponding Number:\n 1.Home Loan\n 2.Car Loan\n 2.Business Loan")
def my_transactions():
    print("What Type of operations you would like to make \n Press the corresponding Number:\n 1.Deposit\n 2.Withdrawal\n")
def my_fx_account():
    print("Below are the updates rates from NYSE \n Press the corresponding Number:\n 1.Currencies\n 2.Cryptocurrencies\n")
def help_section():
    print("Please Enter your data: ")
my_profile()