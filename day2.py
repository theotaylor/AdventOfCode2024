data = []
with open('inputday2.txt', 'r') as file:
    data = [[int(x) for x in line.split()] for line in file]


def find_num_safe_reports(data):
    total_safe = 0

    for report in data:
        if is_safe_report(report):
            total_safe += 1
        else:
            for i in range(len(report)):
                reportCopy = report[:i] + report[i+1:]
                if is_safe_report(reportCopy):
                    total_safe += 1
                    break
    print(total_safe)


def is_safe_report(report):
    unsafe = False
    increasing = None
    for i in range(1, len(report)):
        prev = report[i-1]
        curr = report[i]
        score = curr - prev
        if score > 3 or score < -3 or score == 0:
            unsafe = True
            break

        if increasing is None:
            increasing = score > 0
        elif increasing and score < 0:
            unsafe = True
            break
        elif not increasing and score > 0:
            unsafe = True
            break
    return not unsafe


        



data1 = [[55, 56, 59, 62, 61], [68, 70, 71, 74, 75, 76, 78, 78], [52, 55, 56, 58, 62], [28, 28, 27, 25, 25, 19], [90, 94, 96, 97, 94], [63, 63, 67, 68, 69, 66], [68, 68, 66, 65, 60, 59, 58, 51], [92, 92, 86, 85, 82, 80, 76], [26, 27, 24, 25, 26, 25], [73, 78, 84, 86, 88, 91, 91], [42, 44, 43, 40, 42, 40, 40], [40, 41, 42], [4, 3, 2]]
find_num_safe_reports(data)





