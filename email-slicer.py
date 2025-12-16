#clareokoye@gmail.com

def form():
    print('This is an email slicer')
    print("")

    email_input = input("please provide your email address: ")

    if "@" in email_input:
        (username, domain) = email_input.split("@")
        (domain, ext) = domain.split(".")

        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print("Extension = ", ext)
        print("")
    else:
        print("Please provide a valid email address")
        quit()
while True:
    form()
"""

while True:
    try:
        form()
    except ValueError:
        quit()
"""

