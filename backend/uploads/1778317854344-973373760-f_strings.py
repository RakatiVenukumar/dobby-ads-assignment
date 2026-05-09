# use of f'strings()

age = int(input("enter your current age :"))

years_left = 90 - age
a = years_left*365 # where a = days_left
b = years_left*52 # where b = weeks_left
c = years_left*12 # where c = months_left

print(f"you have {years_left} years , {a} days , {b} weeks , {c} months left to live 90 years")