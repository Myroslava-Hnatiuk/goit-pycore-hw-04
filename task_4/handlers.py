def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return 'Invalid input'

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        return 'Invalid input. Example: add Tom 11111111'
  

def change_contact(args, contracts):
    try:
        name, phone = args
        if name in contracts:
            contracts[name] = phone
            return "Contact updated."
        else:
            return "Contact is not found"
    except:
        return 'Invalid input. Example: change Tom 11111111'

def show_phone(args, contacts): 
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact is not found"
    except:
        return 'Invalid input. Example: phone Tom'

def show_all(contacts): 
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)