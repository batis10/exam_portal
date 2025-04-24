

# from django.contrib import admin 
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('/users',include('users.urls')),
# ]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/courses/', include('courses.urls')),  # includes enrollments
    path('api/exams/', include('exams.urls')),
    path('api/questions/', include('questions.urls')),
    path('api/attempts/', include('attempts.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/certificates/', include('certificates.urls')),
    path('questions/', include('questions.template_urls')),
]

