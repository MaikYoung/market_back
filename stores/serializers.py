from requests.compat import basestring
from rest_framework import serializers
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

    @staticmethod
    def get_store(obj):
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


class StoreCustomSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    name = serializers.CharField()
    adress = serializers.CharField()
    postal_code = serializers.IntegerField()
    schedule_open = serializers.IntegerField()
    schedule_close = serializers.IntegerField()
    work_days = serializers.ListField(child=serializers.IntegerField())
    twitter = serializers.CharField(required=False)
    facebook = serializers.CharField(required=False)
    instagram = serializers.CharField(required=False)

    class Meta:
        model = Store
        fields = '__all__'

    def validate_name(self, data):
        if data is None:
            raise serializers.ValidationError('StoreNameError')
        return data

    def validate_adress(self, data):
        if data is None:
            raise serializers.ValidationError('StoreAdressError')
        return data

    def validate_postal_code(self, data):
        regex = '^([1-9]{2}|[0-9][1-9]|[1-9][0-9])[0-9]{3}$'
        if data is None or len(str(data)) != 5:
            raise serializers.ValidationError('StorePostalCodeError')
        elif str(data) != regex:
            raise serializers.ValidationError('PostalCodeNoRegexMatch')
        else:
            return data

    def validate_schedule_open(self, data):
        if data is None:
            raise serializers.ValidationError('StoreScheduleOpenError')
        return data

    def validate_schedule_close(self, data):
        if data is None or isinstance(data, basestring):
            raise serializers.ValidationError('StoreScheduleCloseError')
        return data

    def validate_work_days(self, data):
        if data is None:
            raise serializers.ValidationError('StoreWorKDaysError')
        elif data != isinstance(data, list):
            raise serializers.ValidationError('WordDaysNotList')
        else:
            return data

    def validate(self, data):
        return data

    def create(self, validated_data):
        store = super(StoreCustomSerializer, self).create(validated_data)
        try:
            Store.objects.create(store)
            return store
        except:
            return 'algo ha ido mal al crear store'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.adress = validated_data.get('adress')
        instance.postal_code = validated_data.get('postal_code')
        instance.schedule_open = validated_data.get('schedule_opne')
        instance.schedule_close = validated_data.get('schedule_close')
        instance.work_days = validated_data.get('work_days')
        instance.twitter = validated_data.get('twitter')
        instance.facebook = validated_data.get('facebook')
        instance.instagram = validated_data.get('instagram')
        instance.save()
        return instance
