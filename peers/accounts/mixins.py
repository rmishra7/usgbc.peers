
class ProfileMixin(object):
    """
    mixin for user model with queryset methods
    """
    def get_user_by_email(self, email):
        return self.get(email=email)

    def get_user_by_username(self, username):
        return self.get(username=username)

    def get_user_by_emaillist(self, emails):
        return self.filter(email__in=emails)
