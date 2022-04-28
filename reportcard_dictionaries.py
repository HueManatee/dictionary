import operator
gradesList = {}
print('')
print('Welcome to your grade compiler!')

name = input('What is your name? ')

gradesList['Math'] = float(input('What is your Math grade? '))
gradesList['Science'] = float(input('What is your Science grade? '))
gradesList['Technology'] = float(input('What is your Technology grade? '))
gradesList['Social Studies'] = float(input('What is your Social Studies grade? '))
gradesList['English'] = float(input('What is your English grade? '))

#print(gradesList.items())

dictgradeslist = dict(sorted(gradesList.items(), key=operator.itemgetter(1)))

lastint = min(dictgradeslist, key=dictgradeslist.get)
firstint = max(dictgradeslist, key=dictgradeslist.get)

#print(dictgradeslist)

print('Hello ' + name + '!')

print('Here are your grades from high to low: ' + str(dictgradeslist))

print('Here is your highest grade: ' + str(dictgradeslist[firstint]))

print('Here is your lowest grade that is being dropped: ' + str(dictgradeslist[lastint]))
del dictgradeslist[lastint]
print('So here are your new grades: ' + str(dictgradeslist))
dictgradeslist[lastint] = float(0)
average = (int((dictgradeslist.get('Math') + dictgradeslist.get('Science') + dictgradeslist.get('Technology') + dictgradeslist.get('Social Studies') + dictgradeslist.get('English') - dictgradeslist.get(lastint)))/4)

print('Here is your new grade average: ' + str(average))



