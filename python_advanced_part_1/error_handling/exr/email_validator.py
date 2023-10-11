def validator(valid_dom, email):
    for dom in valid_dom:
        if dom in email:
            return True
    return False


email = input().split()
valid_domains = ['.com', '.bg', '.net', '.org']


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if 5 > len(email.split('@')[0]):
        raise NameTooShortError("Email is valid")

    if not validator(valid_domains, email):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    email = input()

print("Email is valid")
