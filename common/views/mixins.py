from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendView:
    multi_serializer_class = None
    serializer_class = None
    permission_classes = []
    multi_permissions_classes = None

    def get_serializer_class(self):
        assert self.multi_serializer_class or self.serializer_class, (
                '"%s" must define a "multi_serializer_class"'
                ' and "serializer_class", "get_serializer_class()".'
                % self.__class__.__name__
        )
        if not self.multi_serializer_class:
            return self.serializer_class

        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method
        return self.multi_serializer_class.get(action) or self.serializer_class

    def get_permissions(self):
        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method

        if self.multi_permissions_classes:
            permissions = self.multi_permissions_classes.get(action)
            if permissions:
                return [permission() for permission in permissions]

        return [permission() for permission in self.permission_classes]


class ExtendedGenericViewSetMixin(ExtendView, GenericViewSet):
    pass


class CreateViewMixin(ExtendedGenericViewSetMixin, mixins.CreateModelMixin):
    pass


class CRUMixin(
    ExtendedGenericViewSetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    pass


class LCRUDMixin(
    CRUMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
):
    pass
