guests = ['Keqing', 'Ganyu', 'Ayaka', 'Yoimia', 'Nilou', 'Dehya', 'Jean',
          'Eula']
for guest in guests:
    print('Dear ' + guest + ", you are cordially invited to dinner.")
print('Jean is unable to attend the dinner due to overtime work.')
guests.remove('Jean')
guests.append('Amber')
print('Dear ' + guests[-1] + ", you are cordially invited to dinner.")
print('*'*50)
print('I find a bigger dining table.')
print('Cancel sending them.')
guests.insert(0, 'Yelan')
guests.insert(3, 'Raiden Shogun')
guests.append('Lisa')
for guest in guests:
    print('Dear ' + guest + ", you are cordially invited to dinner.")
print('*'*50)
print('The table is broken.')
while len(guests) > 3:
    removed_guest = guests.pop()
    print("Dear " + removed_guest + ", I am sorry I can't invite you to "
                                    "dinner.")
# 删除列表元素直到只剩三个人
for guest in guests:
    print('Dear ' + guest + ", you are still invited to dinner.")

del guests[:]
# 清空列表
print(guests)
