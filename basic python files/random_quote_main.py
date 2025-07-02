from quote_utils import get_random_quote as gr
from quote_utils import read_file as rf

try:
    FileName = input("Enter the filename : ")
    quotes = rf(FileName)
    if len(quotes)>0:
        for i in range(5):
             print(gr(quotes))

    else:
        print("File exists but has no contet")
except FileNotFoundError:
    print("The FileName enterred is incorrect. Please input a valid filename")
