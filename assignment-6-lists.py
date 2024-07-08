user_input = input("Enter a sequence of numbers each seperated by a space: ")
user_list = []
user_input_errors = []
for value in user_input.split():
        try:
            user_list.append(int(value))
        except ValueError:
            user_input_errors.append(value)            

if user_list != []:
    if user_input_errors != []:
        print(f'{user_input_errors} is not a number and will not be included in the sequence')
    print(f'List of numbers is as follows: {user_list}')
    user_list.reverse()
    print(f'and the list reversed is: {user_list}')
    user_list.sort()
    print(f'and sorted: {user_list}.')
    print(f'List has {len(user_list)} number of elements.')
    print(f'Smallest number in list is: {min(user_list)} while largest number is: {max(user_list)}.')
    print(f'The sum of the list is {sum(user_list)} and the average of it is {sum(user_list) / len(user_list):.2f}')

else:
    print("No numbers entered")