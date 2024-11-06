# name = "wagwan boiiii"
# print(name)

# first_name = str(input("Enter first"))





# print("Hello, Welcome to our terminal Bank")

# response =str(input("What woud you like to do today?\n1. Transfer\n2. Create account\n3. Airtime\n4. Balance\n>>")).lower()

# if response == "1" or response == "transfer":
#     reply_1 = str(input("Enter account number\n>>"))
#     if reply_1 and len (reply_1)==10:
#         reply_2 = str(input("enter account name\n>>")).upper()
#         print("Account found and valid")

#     else:
#         print("Inavlid account details")

#         elif response == "2" or response == "create account":
#      reply_1 = str(input("Enter First name\n>>"))
#     if reply_1:
#         reply_2 = str(input("Enter Last Name\n>>"))
#         if reply_2:
#         reply_3 = str(input("Enter Phone number\n>>")).upper()
#         print("Account created\n Thanks for banking with us...")
#         else:
#             print("Account Creation error")

            
# elif response =="2" or response == "create account":
#     first_name = str(input("Enter your first name\n>>")).upper()
#     last_name = str(input("Enter your Last name\n>>")).upper()
#     phone_number = str(input("Enter your Phone number\n>>"))
#     print(f"Dear {first_name} {last_name} thank you for creating an account\nwith us, yout account number is {phone_number}")

# else:
#     print("UNKNOWN DIALING CODE")









def main():
    total_bill = float(input("Total bill (₦): "))
    num_friends = int(input("Number of friends: "))
    option = input("Payment method (1: One account, 2: Split with tip): ")

    if option == '1':
        print(f"Total bill of ₦{total_bill} will be transferred.")
    elif option == '2':
        print(f"Each pays: ₦{(total_bill * 1.05) / num_friends}")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()

















# import requests

# import requests

# response = requests.get('https://dummyjson.com/products')
# products = response.json()


# for product in products['products']:
#     if product['price'] < 5:
#         print(f"{product['title']} is {product['price']}")

