from django.contrib import admin
from .models import City,DailyFeed,Clipping,DailySpecialAkola,DailySpecialBuldhana,TopAdds,BottomAdds,AdvertisementForm

# Register your models here.
admin.site.register(City)
admin.site.register(DailyFeed)
admin.site.register(Clipping)
admin.site.register(DailySpecialAkola)
admin.site.register(DailySpecialBuldhana)
admin.site.register(TopAdds)
admin.site.register(BottomAdds)
admin.site.register(AdvertisementForm)