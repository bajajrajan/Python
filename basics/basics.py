# Count of 10.0 in a list
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))
# Ans: 3

# lowercase
username='Python3'
print(username.lower())
# Ans: python3

# Dictionary - items(all), key:value
student_grade = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(student_grade.values())
# Ans: dict_values([9.1, 8.8, 7.5])
print(student_grade.keys())
# Ans: dict_keys(['Marry', 'Sim', 'John'])

# Tuple - are immutable while lists are mutable
monday_temp = (1, 23, 33)
print(monday_temp)
# Ans: (1, 23, 33)

# # Reverse list printing - pending
# list1 = [1.2, 2.3, 3.4, 4.5, 5.6]
# print(list1[-1])
# for item in list1:
#     print(item[-1])

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1,2,3,4,5]))

# if condition for checking type() of input
def mean1(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

print(mean1({"Marry": 9.1, "Sim": 8.9}))
print(mean1([1,2,3,4,5]))

# isinstance instead of type 
def mean1(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

print(mean1({"Marry": 9.1, "Sim": 8.9}))
print(mean1([1,2,3,4,5]))




