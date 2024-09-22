# WAF to print the elements of a list in a single line. (list is the parameter)

def elem_list(list):
    for el in list:
        print(el, end=" ")

countries = ["USA", "Canada", "UK", "Australia", "New ealand"]
elem_list(countries)