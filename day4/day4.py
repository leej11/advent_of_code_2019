test = '111111'
test2 = '223450'
test3 = '123789'

start = '264793'
stop = '803935'


def password_checker(password):

    pass_score = 0
    double_counter = 0
    double_counter_2 = 0
    double_ints = []

    for i in range(1,6):

        if password[i] > password[i-1]:
            pass_score += 1

        elif password[i] == password[i-1]:
            pass_score += 1
            double_counter += 1
            double_ints.append(password[i])

    if (pass_score == 5) and (double_counter == 1):
        result = password

    elif (pass_score ==5) and (double_counter > 1):

        for i in double_ints:
            if double_ints.count(i) == 1:
                double_counter_2 += 1

        if double_counter_2 >= 1:
            result = password

        else:
            result = ''

    else:
        result = ''

    return result


def pass_generator(rng):

    pwd_list = []

    for pwd in rng:

        if password_checker(pwd) == '':
            continue

        else:
            pwd_list.append(pwd)

    return pwd_list

my_list = map(str, range(264793, 803935))
output = pass_generator(my_list)
print(len(output))