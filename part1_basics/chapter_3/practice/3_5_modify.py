guests = ['Keqing', 'Ganyu', 'Ayaka', 'Yoimia', 'Nilou', 'Dehya', 'Jean',
          'Eula']
for guest in guests:
    print('Dear ' + guest + ", you are cordially invited to dinner.")
print('Jean is unable to attend the dinner due to overtime work.')
# 琴因为加班来不了了
guests.remove('Jean')
# 删掉琴加上安柏
guests.append('Amber')
print('Dear ' + guests[-1] + ", you are cordially invited to dinner.")
