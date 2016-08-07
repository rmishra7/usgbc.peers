
class ProjectMixin(object):

    def project_of_owner(self, user):
        return self.filter(owner=user)
