def build_profile(first, last, **user_info):
    # 任意将剩余实参封装到字典中，**kwargs
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
print(user_profile)
