guests = ['ally', 'winston', 'schmidt', 'cece']
print(guests[0].title() + ", will you and " + guests[1].title() + " please join me for dinner on January 30th?")
print(guests[2].title() + ", I would be honored if you and " + guests[3].title() + " would join us too.")

print("\t " + guests[0].title() + " will be unable to join the dinner.")

guests[0] = "jess"
print(guests)

guests.insert(0, "outside dave")
guests.insert(3, "nick")
guests.append("nadia")

print(guests)

print("\nI will only be able to invite two people now, as the table will not arrive in time.")

guests.pop()
print(guests)

guests.sort()
print(guests)
