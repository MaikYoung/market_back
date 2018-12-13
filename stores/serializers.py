from rest_framework import serializers

from admins.models import Admin
from stores.models import Store


class StoreListSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    is_closed = serializers.SerializerMethodField()
    adress = serializers.SerializerMethodField()
    schedule_open = serializers.SerializerMethodField()
    schedule_close = serializers.SerializerMethodField()

    class Meta:
        Model = Store
        fields = (
            'id', 'name', 'is_closed', 'adress', 'schedule_open', 'schedule_close',
        )

    def get_id(self, obj):
        return obj.id

    def get_name(self, obj):
        return obj.name

    def get_is_closed(self, obj):
        return obj.is_closed

    def get_adress(self, obj):
        return obj.adress

    def get_schedule_open(self, obj):
        return obj.schedule_open

    def get_schedule_close(self, obj):
        return obj.schedule_close


class StoreDetailSerializer(serializers.Serializer):
    store = serializers.SerializerMethodField()

    class Meta:
        Model = Store
        fields = ('store')

    def get_store(self, obj):
        store = {
            'manager': obj.manager.id,
            'manager_name': obj.manager.username,
            'name': obj.name,
            'lat': obj.lat,
            'lng': obj.lng,
            'adress': obj.adress,
            'postal_code': obj.postal_code,
            'schedule_open': obj.schedule_open,
            'schedule_close': obj.schedule_close,
            'work_days':  obj.work_days,
            'is_closed': obj.is_closed,
            'twitter': obj.twitter,
            'facebook': obj.facebook,
            'instagram': obj.instagram
        }
        return dict(store)
