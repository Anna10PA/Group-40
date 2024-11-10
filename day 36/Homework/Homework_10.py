'''10. დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მასში მხოლოდ მარტივ რიცხვებს. '''

user_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = []

# ბატონ გაბრიელს როგორც უნდოდა 
def check(num):
    for a in range(len(num)):
        if num[a] >= 2:
            for i in range(2, num[a]):
                if num[a] % i == 0:
                    break
            else:
                new_list.append(num[a])
    return new_list 
print(check(user_number_list))








# 1
def check(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

for num in user_number_list:
    if check(num) == True:
        new_list.append(num)
print(new_list)
