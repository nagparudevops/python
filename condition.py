# Conditions in python
# if, else, else if or elif

# How to accept input from user
# The return datatype of input function is string
# environment = input("Enter your environment: ")
# print(environment, type(environment))

# num = int(input("Enter a number: "))
# print(num + 123)

# If the provided environment PROD, a change ticket is necessary
# For all other non-prod environments, it is not necessary to provide a change ticket
# For staging environment, user need to login with his credentials
# To debug issues on the PROD environment that are reported by the users, an incident ticket is necessary

# Indentation in python is very important
# It can be either a tab or 4 spaces 

environment = input("Enter your environment: ")

environment = environment.upper()

chg_tkt = False
inc_tkt = False
is_issue = "No"

if environment == "PROD":
    is_issue = input("Issue reported by user (Yes/No)? ")
    if is_issue == "Yes":
        inc_tkt = input("Please enter your incident ticket: ")
        if len(inc_tkt) > 0:
            print("Please proceed with resolving the incident")
        else:
            print("Please enter a valid incident ticket number")
    else:
        chg_tkt = input("Please enter your change ticket: ")
        if len(chg_tkt) > 0:
            chg_tkt = True
        if chg_tkt:
            print("Please proceed with your release activity")
        else:
            print("A change ticket for this release activity is necessary")
elif environment == "STAGING":
    print("Please login with your credentials and proceed")
else:
    print("You are in non-prod environment")