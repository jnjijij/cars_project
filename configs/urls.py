from django.urls import include, path
from django.conf.urls.static import static

from configs import settings

urlpatterns = [
    path('auth', include('apps.all_users.auth.urls')),
    path('cars', include('apps.cars_details.cars.urls')),
    path('car_views', include('apps.cars_details.car_views.urls')),
    path('brand_models', include('apps.cars_details.brand_models.urls')),
    # path('cars_model', include('apps.cars_details.car_model.urls')),
    # path('car_dealership', include('apps.partners.car_dealership.urls')),
    # path('car_dealership_admin', include('apps.partners.car_dealership_admin.urls')),
    # path('car_dealership_manager', include('apps.partners.car_dealership_manager.urls')),
    # path('car_dealership_mechanic', include('apps.partners.car_dealership_mechanic.urls')),
    # path('car_dealership_sales', include('apps.partners.car_dealership_sales.urls'))
    # path('sellers', include('apps.all_users.sellers.urls')),
    # path('premium_sellers', include('apps.all_users.premium_sellers.urls')),
    # path('sale_announcement', include('apps.sale_announcement')),
    # path('visitors', include('apps.all_users.visitors.urls')),
    path('info', include('apps.info.urls')),
    path('managers', include('apps.all_users.managers.urls')),
    path('admins', include('apps.all_users.admins.urls')),
    path('users', include('apps.all_users.users.urls')),
    # path('accounts', include('apps.all_users.accounts.urls')),
    # path('send_message', include('apps.messages.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
