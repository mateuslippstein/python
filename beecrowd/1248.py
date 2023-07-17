def check_diet(diet, breakfast, lunch):
    if not diet and not breakfast and not lunch:
        return ""

    remaining_chars = set(diet) - (set(breakfast) | set(lunch))
    extra_chars = set(breakfast - diet) - set(lunch - diet)

    if extra_chars or not remaining_chars:
        return "CHEATER"
    else:
        return ''.join(sorted(remaining_chars))


num_test_case = int(input())
results = []

for _ in range(num_test_case):
    diet = input()
    breakfast = input()
    lunch = input()
    results.append(check_diet(diet, breakfast, lunch))

for result in results:
    print(result)