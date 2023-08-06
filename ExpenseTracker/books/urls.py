from django.urls import path
from . import views
import ExpenseTracker.settings as settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Import_Excel, name='Import_excel'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)