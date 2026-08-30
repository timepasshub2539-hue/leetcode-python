def can_access(user, resource):
    if user.role == "admin":
        return True
    return user.id == resource.owner_id

# missing: user.is_active check
# a disabled admin account still gets in
