from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from django.http import Http404
from main.form import InfoForm
from main.models import *
from main.serializer import *


class InfoView(APIView):
    def get(self, request):
        info = Info.objects.last()
        ser = InfoSerializer(info)

        return Response(ser.data)


class SliderView(APIView):

    def get(self, request):
        slider = Slider.objects.all().order_by('-id')[0:5]
        ser = SliderSerializer(slider, many=True)

        return Response(ser.data)


class ProjectsView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        ser = ProjectsSerializer(projects, many=True)

        return Response(ser.data)


class TechnoparkView(APIView):
    def get(self, request):
        technopark = Technopark.objects.all()[0:6]
        ser = TechnoparkSerializer(technopark, many=True)

        return Response(ser.data)


class SectionView(RetrieveAPIView):

    def retrieve(self, request, pk):
        section = Section.objects.get(id=pk)
        sec = SectionSerializer(section)
        return Response(sec.data)

class Postalservicesview(APIView):

    def get(self, request):
        pochta = Postalservices.objects.all().order_by('-id')
        ser = PostalservicesSerializer(pochta, many=True)

        return Response(ser.data)


class BoglanishView(APIView):
    def post(self, request):
        fullname = request.data['fullname']
        phone = request.data['phone']
        text = request.data['text']
        Boglanish.objects.create(fullname=fullname,phone=phone,text=text)

        return Response('отправлено ваша смс')


class MobileoperatorsView(APIView):

    def get(self, request):
        operator = Mobileoperators.objects.all().order_by('-id')
        ser = MobileoperatorsSerializer(operator, many=True)

        return Response(ser.data)


class InternetprovidersView(APIView):

    def get(self, request):
        providers = Internetproviders.objects.all().order_by('-id')
        ser = InternetprovidersSerializer(providers, many=True)

        return Response(ser.data)


class OurAudienceView(APIView):

    def get(self, request):
        audience = OurAudience.objects.all().order_by('-id')[0:5]
        ser = OurAudienceSerializer(audience, many=True)

        return Response(ser.data)

class PercentageView(APIView):

    def get(self, request):
        percentage = Percentage.objects.all().order_by('-id')[0:4]
        ser = PercentageSerializer(percentage, many=True)

        return Response(ser.data)

class ResidentsView(APIView):

    def get(self, request):
        residents = Residents.objects.all().order_by('-id')[0:5]
        ser = ResidentsSerializer(residents, many=True)

        return Response(ser.data)

class TeamView(APIView):

    def get(self, request):
        team = Team.objects.last()
        ser = TeamSerializer(team)

        return Response(ser.data)


class CoworkingView(APIView):
    def get(self, request):
        coworking = Coworking.objects.all().order_by('-id')[0:2]
        ser = CoworkingSerializer(coworking, many=True)

        return Response(ser.data)

class InfrastructureSliderView(APIView):
    def get(self, request):
        infrastructure = InfrastructureSlider.objects.all().order_by('-id')[0:6]
        ser = InfrastructureSliderSerializer(infrastructure, many=True)

        return Response(ser.data)

class StudyDirectionsView(APIView):

    def get(self, request):
        study = StudyDirections.objects.all().order_by('-id')[0:5]
        ser = StudyDirectionsSerializer(study, many=True)

        return Response(ser.data)

class ItAcademyView(APIView):

    def get(self, request):
        it_academy = ItAcademy.object.all().order_by('-id')[0:5]
        ser = ItAcademySerializer(it_academy, many=True)

        return Response(ser.data)

class StartupDirectionsView(ListAPIView):
    queryset = StartupDirections.objects.all()
    serializer_class = StartupDirectionsSerializer

    def list(self, request):
        incub = StartupDirections.objects.all().order_by("-id")[0:6]
        inc = StartupDirectionsSerializer(incub, many=True)
        return Response(inc.data)


class IncubationCentersView(ListAPIView):
    queryset = IncubationCenters.objects.all()
    serializer_class = IncubationCentersSerializer

    def list(self, request):
        incub = IncubationCenters.objects.all().order_by("-id")[0:4]
        inc = IncubationCentersSerializer(incub, many=True)
        return Response(inc.data)


class RaqamlashtirishxizmalariView(ListAPIView):
    queryset = Raqamlashtirishxizmalari.objects.all()
    serializer_class = RaqamlashtirishxizmalariSerializer

    def list(self, request):
        incub = Raqamlashtirishxizmalari.objects.all().order_by("-id")[0:4]
        inc = RaqamlashtirishxizmalariSerializer(incub, many=True)
        return Response(inc.data)

class ContactPost(APIView):

    def post(self, request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response(contact.data, status=status.HTTP_201_CREATED)
        return Response(contact.errors, status=status.HTTP_400_BAD_REQUEST)


class XizmatTuriView(ListAPIView):
    queryset = XizmatTuri.objects.all()
    serializer_class = XizmatTuriSerializer

    def list(self, request):
        incub = XizmatTuri.objects.all().order_by("-id")[0:3]
        inc = XizmatTuriSerializer(incub, many=True)
        return Response(inc.data)


class XizmatlarPost(APIView):

    def post(self, request):
        xizmat = XizmatlarSerializer(data=request.data)
        if xizmat.is_valid():
            xizmat.save()
            return Response(xizmat.data, status=status.HTTP_201_CREATED)
        return Response(xizmat.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationPost(APIView):

    def post(self, request):
        applicication = ApplicationSerializer(data=request.data)
        if applicication.is_valid():
            applicication.save()
            return Response(applicication.data, status=status.HTTP_201_CREATED)
        return Response(applicication.errors, status=status.HTTP_400_BAD_REQUEST)


def Home(request):
    return render(request, 'home.html')

def Table(request):
    return render(request, 'table.html')

def InfoTemplate(request):
    info = Info.objects.all()
    context = {
    'info':info,
    }
    return render(request, 'info.html', context)

def InfoFormView(request):
    info = Info.objects.all()
    context = {
        "infoform": InfoForm
    }
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'infocreate.html', context)


def EditTemplate(request, pk):
    info = Info.objects.get(id=pk)
    context = {
        "info": info
    }
    if request.method == "POST":
        logo = request.FILES['logo']
        short_phone = request.POST.get('short_phone')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address_ru = request.POST.get('address_ru')
        address_en = request.POST.get('address_en')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        
    return render(request, 'edit.html')

def DeleteInfo(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return redirect('info')


def SliderTemp(request):
    slider = Slider.objects.all()
    context = {
        'slider':slider,
    }
    return render(request, 'slider.html', context)


def ProjectsTemp(reqeust):
    projects = Projects.objects.all()
    context = {
        "projects":projects
    }
    return render(reqeust, "projects.html", context)


def TechnoparkTemp(reqeust):
    technopark = Technopark.objects.all()
    context = {
        "technopark":technopark
    }
    return render(reqeust, "technopark.html", context)


def SectionTemp(reqeust):
    section = Section.objects.all()
    context = {
        "section":section
    }
    return render(reqeust, "section.html", context)

