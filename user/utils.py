def has_permission(provider_user, user):
    return provider_user == user or user.is_superuser