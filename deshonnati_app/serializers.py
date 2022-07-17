from rest_framework import serializers
from deshonnati_app.models import DailyFeed,DailySpecialBuldhana,DailySpecialAkola,City,AdvertisementForm



class DailyFeedSerializer(serializers.ModelSerializer):

    city = serializers.CharField(source='city.name', read_only=True)
    class Meta :
        model = DailyFeed
        fields = ('id','city','page1','page2','page3','page4','page5','page6','page7','page8')

class DailySpecialAkolaSerializer(serializers.ModelSerializer):


    class Meta :
        model = DailySpecialAkola
        fields = ('id','specialakola1','specialakola2','specialakola3','specialakola4','specialakola5','specialakola6','specialakola7','specialakola8')

class DailyFeedSpecialBuldhanaSerializer(serializers.ModelSerializer):

    class Meta :
        model = DailySpecialBuldhana
        fields = ('buldhanaid','specialbuldhana1','specialbuldhana2','specialbuldhana3','specialbuldhana4','specialbuldhana5','specialbuldhana6','specialbuldhana7','specialbuldhana8')

class AdvertisementFormSerializer(serializers.ModelSerializer):

    class Meta :
        model = AdvertisementForm
        fields = '__all__'