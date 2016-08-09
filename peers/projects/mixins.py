
class ProjectMixin(object):

    def project_of_owner(self, user):
        return self.filter(owner=user)


class CreditsAchievedMixin(object):
    pass


class StrategyMixin(object):
    pass


class ProjectQuestionMixin(object):
    pass


class StrategyQuestionMixin(object):
    pass


class CreditsValueMappingMixin(object):
    pass


class ProjectPlantMappingMixin(object):
    pass


class ElectricityPlantUnitMixin(object):
    pass


class ProjectElectricityPlantMixin(object):
    pass


class CreditsKeywordMixin(object):
    pass
