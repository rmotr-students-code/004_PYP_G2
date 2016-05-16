users = ['u1', 'u2', 'u3']

mutable_old_enough_to_drink(users)

print(users)

###

old_enough_users = immutable_old_enough_to_drink(users)
print(old_enough_users)

for u in users:
    users.append('a')