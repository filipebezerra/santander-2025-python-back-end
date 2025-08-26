# Entrada do usuário
email = input().strip()


# TODO: Verifique as regras do e-mail:
def validate_email(email: str) -> str:
    # Validates if is empty
    if not email:
        return "E-mail inválido"

    # Validates if contains any space
    if " " in email:
        return "E-mail inválido"

    # Validates if first or last character is @
    if email[0] == "@" or email[-1] == "@":
        return "E-mail inválido"

    # Validates if there's a single @
    if not email.count("@") == 1:
        return "E-mail inválido"

    domain = email.split("@")[-1]
    valid_domains = ["gmail.com", "outlook.com"]

    # Validates if contains a domain
    if not domain in valid_domains:
        return "E-mail inválido"

    return "E-mail válido"


if __name__ == "__main__":
    output = validate_email(email)
    print(output)
