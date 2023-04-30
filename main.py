import statistics

first = int(input("There are 5 numbers. Pick the first number: "))
second = int(input("There are 5 numbers. Pick the second number: "))
third = int(input("There are 5 numbers. Pick the third number: "))
fourth = int(input("There are 5 numbers. Pick the fourth number: "))
fifth = int(input("There are 5 numbers. Pick the fifth number: "))

num_list = [first, second, third, fourth, fifth]

mode = statistics.mode([first, second, third, fourth, fifth])
mean = statistics.mean([first, second, third, fourth, fifth])
median = statistics.median([first, second, third, fourth, fifth])
Range = max(num_list)-min(num_list)
harmonic_mean = round(statistics.harmonic_mean([first, second, third, fourth, fifth]), 2)

print(f"The mode is: {mode}")
print(f"The mean is: {mean}")
print(f"The median is: {median}")
print(f"The range is: {Range}")
print(f"The harmonic mean is: {harmonic_mean}")
