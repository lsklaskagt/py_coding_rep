from validator import is_positive

def average_positive(numbers):
    sum = 0
    cnt = 0
    for num in numbers:
        if is_positive(num):
            sum += num
            cnt += 1
    return sum / cnt


