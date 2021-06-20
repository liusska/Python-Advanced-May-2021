from exercises.email_validator.exceptions_custom import MustContainAtSymbolError, InvalidDomainError, NameTooShort

VALID_DOMAINS = ("com", "bg", "org", "net")


def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) <= 4:
        raise NameTooShort("Name must be more than 4 characters")

    print("Email is valid")


while True:
    data = input()
    if data == "End":
        break
    valid_email(data)
