"""
user = get_user_from_db(email)  # User or None

if user and user.is_active:
    # do something
    pass
"""

name, email, password

#if name == '' or email == '' or password == '':
if not all([name, email, password])
    raise ErrorFormException()