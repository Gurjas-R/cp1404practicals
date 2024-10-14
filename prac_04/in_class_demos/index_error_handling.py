friends = ['Gurjas', 'John', 'Lindsy', 'Osmond']
query_number = int(input('Which record from "friends" 0-3: '))
try:
    print(friends[query_number])
except IndexError:
    print("Invalid")
