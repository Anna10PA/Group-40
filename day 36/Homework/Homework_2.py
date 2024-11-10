'''2.    დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი.'''

user_number = int(input("Enter number: "))

def if_this_number_is_even(answer):
    if answer % 2 == 0:
        return "ლუწია"
    else:
        return "კენტი"

print(if_this_number_is_even(user_number))
