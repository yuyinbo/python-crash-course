guests = ['Keqing', 'Ganyu', 'Ayaka', 'Yoimia', 'Nilou', 'Dehya', 'Jean',
          'Eula']
for guest in guests:
    print('Dear ' + guest + ", you are cordially invited to dinner.")
print('Jean is unable to attend the dinner due to overtime work.')
guests.remove('Jean')
guests.append('Amber')
print('Dear ' + guests[-1] + ", you are cordially invited to dinner.")
print('*' * 50)
print('I find a bigger dining table.')
print('Cancel sending them.')
guests.insert(0, 'Yelan')
guests.insert(3, 'Raiden Shogun')
guests.append('Lisa')
# 在开头，第4位和结尾加上三个人
for guest in guests:
    print('Dear ' + guest + ", you are cordially invited to dinner.")

print("I have invited " + str(len(guests)) + " guests.")
