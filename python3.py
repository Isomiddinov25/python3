def multi_table(number):
    a = ''
    for i in range(1, 11):
        a += f"{i} * {number} = {i*number}\n"
    return a[:-1]