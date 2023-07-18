def check_diet(diet, breakfast, lunch):
    if not diet and not breakfast and not lunch:
        return ""

    remaining_food = []  # List to store characters remaining in the diet after meals
    extra_food = []  # List to store characters eaten in excess or not present in the diet
    diet = set(diet)  

    for char in diet:
        if char in breakfast:
            breakfast = breakfast.replace(char, '', 1)  # Remove character from breakfast once eaten
        elif char in lunch:
            lunch = lunch.replace(char, '', 1)  # Remove character from lunch once eaten
        else:
            remaining_food.append(char)  # Character not eaten

    extra_food = list(breakfast + lunch)  # Combine remaining breakfast and lunch as extra_chars

    if extra_food:
        return "CHEATER"  # If there are extra_chars, it means the diet was violated
    else:
        return ''.join(sorted(remaining_food))

num_test_cases = int(input())
results = []

for _ in range(num_test_cases):
    diet = input()
    breakfast = input()
    lunch = input()
    results.append(check_diet(diet, breakfast, lunch))

for result in results:
    print(result)