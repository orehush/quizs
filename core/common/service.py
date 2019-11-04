from django.utils.functional import cached_property


class ModelService:
    def __init__(self, instance):
        self.instance = instance

    @classmethod
    def create_from(cls, instance):
        return cls(instance)


class ModelServiceMixin:
    service_class = None  # type: ModelService

    def get_service_class(self):
        msg = 'Does not specified service_class'
        assert type(self.service_class) is type, msg
        return self.service_class

    @cached_property
    def service(self):
        return self.get_service_class().create_from(self)
