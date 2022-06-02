from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


# Bu url saytni sliderini get qlb beradi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/info/', InfoView.as_view()),
    path('api/slider/', SliderView.as_view()),
    path('api/porjects/', ProjectsView.as_view()),
    path('api/technopark/', TechnoparkView.as_view()),
    path('api/section/<int:pk>/', SectionView.as_view()),
    path('api/postalservice/', Postalservicesview.as_view()),
    path('api/boglanish/', BoglanishView.as_view()),
    path('api/mobileoperator/', MobileoperatorsView.as_view()),
    path('api/internetproviders/', InternetprovidersView.as_view()),
    path('api/audince/', OurAudienceView.as_view()),
    path('api/percentage/', PercentageView.as_view()),
    path('api/residents/', ResidentsView.as_view()),
    path('api/team/', TeamView.as_view()),
    path('api/coworking/', CoworkingView.as_view()),
    path('api/infrastructure/', InfrastructureSliderView.as_view()),
    path('api/studydirection/', StudyDirectionsView.as_view()),
    path('api/itacademy/', ItAcademyView.as_view()),
    path('api/startupdirections/', StartupDirectionsView.as_view()),
    path('api/incubationcenters/', IncubationCentersView.as_view()),
    path('api/raqamlashtirishxizmalari/', RaqamlashtirishxizmalariView.as_view()),
    path('api/contact/', ContactPost.as_view()),
    path('api/xizmatturi/', XizmatTuriView.as_view()),
    path('api/xizmatlar/', XizmatlarPost.as_view()),
    path('api/application/', ApplicationPost.as_view()),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

