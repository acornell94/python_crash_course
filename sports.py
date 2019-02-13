high_school_sports = ['soccer', 'football', 'baseball', 'hockey', 'tennis']
print(high_school_sports[0:3])
print(high_school_sports[:3])
print(high_school_sports[:-2])

print("\nThe following are the most popular sports among local schools: ")
for sport in high_school_sports[1:4]:
    print(sport.title())

college_sports = high_school_sports[:]
college_sports.append('rugby')
college_sports.remove('hockey')

print("\nColleges often offer the following:")
for sport2 in college_sports:
    print(sport2.title())