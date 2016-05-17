from crowdsourcing.serializers.dynamic import DynamicFieldsModelSerializer
from crowdsourcing.models import Qualification, QualificationItem, WorkerAccessControlEntry, \
    RequesterAccessControlGroup


class QualificationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'name', 'description')

    def create(self, owner, *args, **kwargs):
        return Qualification.objects.create(owner=owner, **self.validated_data)


class QualificationItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = QualificationItem
        fields = ('id', 'expression')

    def create(self, qualification, *args, **kwargs):
        return QualificationItem.objects.create(qualification_id=qualification, **self.validated_data)


class RequesterACGSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = RequesterAccessControlGroup
        fields = ('id', 'requester', 'is_global', 'type', 'name')

    def create(self, requester, *args, **kwargs):
        return RequesterAccessControlGroup.objects.create(requester=requester, **self.validated_data)


class WorkerACESerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WorkerAccessControlEntry
        fields = ('id', 'worker', 'group', 'created_timestamp')

    def create(self, *args, **kwargs):
        return WorkerAccessControlEntry.objects.create(**self.validated_data)
