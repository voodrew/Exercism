def hey(message):
    message = message.strip()
    if not message:
        return "Fine. Be that way!"
    if message.endswith("?"):
        if message.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if message.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'






