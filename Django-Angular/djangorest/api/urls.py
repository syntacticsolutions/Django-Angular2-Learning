from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 
from rest_framework.authtoken.views import obtain_auth_token # add this import

urlpatterns = {
    url(r'^$', CreateView.as_view(), name="api"),
    # url(r'^auth/', include('rest_framework.urls',
    #                        namespace='rest_framework')),
    # url(r'^users/$', UserView.as_view(), name="users"),
    # url(r'users/(?P<pk>[0-9]+)/$',
    #     UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token), # Add this line
}

urlpatterns = format_suffix_patterns(urlpatterns)