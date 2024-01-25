from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendedGenericViewSetMixin(GenericViewSet):
    pass


class CRUMixin(
    ExtendedGenericViewSetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    pass


class CRUDMixin(
    CRUMixin,
    mixins.DestroyModelMixin
):
    pass
