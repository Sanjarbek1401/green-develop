from django.contrib import admin
from event.models import Event_speaker,About,Sponsor, Authors, Partner, Link
admin.site.register(Event_speaker)
admin.site.register(About)
admin.site.register(Sponsor)
admin.site.register(Authors)
admin.site.register(Partner)
admin.site.register(Link)

# Register your models here.
