import random 

def read_file (filename):
    quote_list =[]
    with open (filename,"r") as file:
        for line in file:
            quote_list.append(line.strip())
    return quote_list

def get_random_quote(quote_list):
    return random.choice(quote_list)


