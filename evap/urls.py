import django.contrib.auth.views
from django.conf import settings
from django.urls import include, path, re_path

urlpatterns = [
    path("", include('evap.evaluation.urls')),
    path("staff/", include('evap.staff.urls')),
    path("results/", include('evap.results.urls')),
    path("student/", include('evap.student.urls')),
    path("contributor/", include('evap.contributor.urls')),
    path("rewards/", include('evap.rewards.urls')),
    path("grades/", include('evap.grades.urls')),

    path("logout", django.contrib.auth.views.LogoutView.as_view(next_page="/"), name="django-auth-logout"),
    re_path(r'^oidc/', include('mozilla_django_oidc.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('development/', include('evap.development.urls'))]

    if settings.ENABLE_DEBUG_TOOLBAR:
        # pylint does not correctly evaluate this if, so it will raise an import-error on
        # GitHub actions and a useless-suppression on a vagrant setup. Ignore both cases.
        import debug_toolbar  # pylint: disable=import-error, useless-suppression
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
