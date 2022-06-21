from django.contrib import admin

# Register your models here.
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        "first_name",
        "last_name",
        "email_address",
    )
    # Ordering in admin
    ordering = ("id",)


admin.site.register(Profile, ProfileAdmin)
