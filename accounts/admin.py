from django.contrib import admin
from .models import RegistrationRequest
from django.contrib.auth import get_user_model


User = get_user_model()

class RegistrationRequestAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "created_at", "updated_at"]
    search_fields = ["user__username", "user__email", "user__first_name", "user__last_name", "status", "created_at", "updated_at"]

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
    
    def has_add_permission(self, request):
        return False
    
# Register your models here.
admin.site.register(User)
admin.site.register(RegistrationRequest, RegistrationRequestAdmin)