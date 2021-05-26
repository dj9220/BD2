from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from .views import view, add_to_cart, remove_from_cart, checkout, all_orders
from shop import views as shopviews
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/$', view, name = 'view_cart'),
    url(r'^cart/(?P<id>\d+)/$', add_to_cart, name='update_cart'),
    url(r'^cart/(?P<id>\d+)/$',remove_from_cart , name='remove_from_cart'),
url(r'^checkout/$', checkout, name = 'checkout'),
    path('all_orders/', all_orders, name = 'all_orders'),

   ]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
