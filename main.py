"""report_dict is a dictionary in which the key is the group number and the
value is the number of clients.
"""
n = int(input())
n_from = int(input())

sum_ = lambda x: sum(map(int, list(str(x))))

def report_from_zero(n_customers):
    report_dict = {}
    for i in range(0, n_customers):
        number = sum_(i)
        report_dict[number] = report_dict.get(number, 0) + 1
    return report_dict


def report_from_any(n_first_id, n_customers):
    report_dict = {}
    for i in range(n_first_id, n_first_id + n_customers):
        number = sum_(i)
        report_dict[number] = report_dict.get(number, 0) + 1
    return report_dict


print(report_from_zero(n))
print(report_from_any(n_from, n))
