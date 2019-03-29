from django.urls import path, re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^contacts/$', mainapp.contacts, name='contacts'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.category, name='category'),
    # альтернативный вариант
    # path('<int:pk>/', mainapp.category, name='category'),
    re_path(r'^catalog/$', mainapp.catalog, name='catalog'),
]
