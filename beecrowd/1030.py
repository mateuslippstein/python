# The Josephus' problem is known because of the Flavius Josephus' legend, a Jewish historian living in the 1st century. According to Josephus' account of the siege of Yodfat, he and his 40 comrade soldiers were trapped in a cave, the exit of which one was blocked by Romans. They chose suicide over capture and decided that they would form a circle and start killing themselves skipping three in three. Josephus says that, by luck or maybe by the hand of God, he remained the last and gave up to the Romans.”
# Input

# There are NC (1 ≤ NC ≤ 30 ) test cases. In each input test case there will be a pair of positive integer numbers n (1 ≤ n ≤ 10000 ) and k (1 ≤ k ≤ 1000). The number n represents the quantity of people in the circle, numbered from 1 to n. The number k represents the size of step between two men in the circle.

# Follow an example with 5 men and step 2: In this example the remaining element is 3.


# The data must be read from standard input.
# Output

# For each test case we will have an output line, presenting in the following format: Case n: m always with a space before n and m.





NC = int(input())  # Enter the number of test cases

test_cases = []
for case in range(NC):
    n, k = map(int, input().split())  # Enter the values of n and k for case
    test_cases.append((n, k))

results = []
for case, (n, k) in enumerate(test_cases):
    circle = list(range(1, n + 1))
    index = 0

    while len(circle) > 1:
        index = (index + k - 1) % len(circle)
        circle.pop(index)

    remaining = circle[0]
    results.append((case, remaining))

for case, remaining in results:
    print("Case {}: {}".format(case + 1, remaining))
