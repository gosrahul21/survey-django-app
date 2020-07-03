from django.contrib import admin
from django.urls import path,include,reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('post/',include('post.urls')),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)