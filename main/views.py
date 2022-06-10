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



def InfoTemplate(request):
    info = Info.objects.all()
    context = {
    'info':info,
    }
    return render(request, 'info.html', context)

def InfoCreate(request):
    info = Info.objects.all()
    context = {
        "info":info,
    }
    if request.method == "POST" and request.FILES:
        data = request.POST
        Info.objects.create(
            logo = request.FILES['logo'],
            short_phone = data.get('short_phone'),
            phone = data.get('phone'),
            email = data.get('email'),
            address = data.get('address'),
            address_ru = data.get('address_ru'),
            address_en = data.get('address_en'),
            lat = data.get('lat'),
            lng = data.get('lng')
        )
        return redirect('info')
    return render(request, 'infocreate.html', context)


def InfoEdit(request, pk):
    info = Info.objects.get(id=pk)
    if request.method == "POST":
        info = Info.objects.get(id=pk)
        if 'logo' in request.FILES:
            info.logo = request.FILES['logo']
        
        info.short_phone = request.POST.get('short_phone')
        info.phone = request.POST.get('phone')
        info.email = request.POST.get('email')
        info.address = request.POST.get('address')
        info.address_ru = request.POST.get('address_ru')
        info.address_en = request.POST.get('address_en')
        info.lat = request.POST.get('lat')
        info.lng = request.POST.get('lng')
        info.save()
        return redirect('info')
    context = {
        "info": info
    }
    return render(request, 'infoedit.html', context)

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

def SliderCreate(request):
    slider = Slider.objects.all()
    context = {
        "slider":slider,
    }
    if request.method == "POST":
        data = request.POST
        Slider.objects.create(
            video = request.FILES['video'],
            title = data.get('title'),
            title_ru = data.get('title_ru'),
            title_en = data.get('title_en'),
        )
        return redirect('slider')
    return render(request, 'slidercreate.html', context)


def SliderEdit(request, pk):
    slider = Slider.objects.get(id=pk)
    if request.method == "POST":
        slider = Slider.objects.get(id=pk)
        if 'logo' in request.FILES:
            slider.video = request.FILES['logo']
        else:
            slider.video = request.POST.get('video')
        slider.title = request.POST.get('title')
        slider.title_ru = request.POST.get('title_ru')
        slider.title_en = request.POST.get('title_en')
        slider.save()
        return redirect('slider')
    context = {
        "slider": slider
    }
    return render(request, 'slideredit.html', context)

def DeleteSlider(request, pk):
    slider = Slider.objects.get(id=pk)
    slider.delete()
    return redirect('slider')

def ProjectsTemp(request):
    projects = Projects.objects.all().order_by('-id')
    context = {
        "projects":projects
    }
    return render(request, "projects.html", context)

def ProjectsCreate(request):
    projects = Projects.objects.all()
    context = {
        "projects":projects,
    }
    if request.method == "POST":
        data = request.POST
        Projects.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
        )
        return redirect('projects')
    return render(request, 'projectscreate.html', context)

def ProjectsEdit(request, pk):
    if request.method == "POST":
        projects = Projects.objects.get(id=pk)
        projects.image = request.FILES['image']
        projects.text = request.POST.get('text')
        projects.text_en = request.POST.get('text_en')
        projects.text_ru = request.POST.get('text_ru')
        projects.save()
        return redirect('projects')
    projects = Projects.objects.get(id=pk)
    context = {
        "projects": projects
    }
    return render(request, 'projectsedit.html', context)

def DeleteProjects(request, pk):
    projects = Projects.objects.get(id=pk)
    projects.delete()
    return redirect('projects') 
  

def TechnoparkTemp(request):
    technopark = Technopark.objects.all().order_by('-id')
    context = {
        "technopark":technopark
    }
    return render(request, "technopark.html", context)

def TechnoparkCreate(request):
    technopark = Technopark.objects.all()
    context = {
        "technopark":technopark,
    } 
    if request.method == "POST":
        data = request.POST
        Technopark.objects.create(
            icon = request.FILES['icon'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
            number = data.get('number'),
        )
        return redirect('technopark')
    return render(request, 'technoparkcreate.html', context)

def TechnoparkEdit(request, pk):
    if request.method == "POST":
        technopark = Technopark.objects.get(id=pk)
        technopark.icon = request.FILES['icon']
        technopark.text = request.POST.get('text')
        technopark.text_en = request.POST.get('text_en')
        technopark.text_ru = request.POST.get('text_ru')
        technopark.number = request.POST.get('number')
        technopark.save()
        return redirect('technopark')
    technopark = Technopark.objects.get(id=pk)
    context = {
        "technopark": technopark
    }
    return render(request, 'technoparkedit.html', context)

def DeleteTechnopark(request, pk):
    technopark = Technopark.objects.get(id=pk)
    technopark.delete()
    return redirect('technopark')


def SectionTemp(request):
    section = Section.objects.all().order_by('-id')
    context = {
        "section":section
    }
    return render(request, "section.html", context)

def DeleteSection(request, pk):
    section = Section.objects.get(id=pk)
    section.delete()
    return redirect("section")

def SectionCreate(request):
    if request.method == "POST":
        data = request.POST
        Section.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
            name = data.get('name'),
            name_en = data.get('name_en'),
            name_ru = data.get('name_ru')
        )
        return redirect('section')

    return render(request, 'sectioncreate.html')


def SectionEdit(request, pk):
    section = Section.objects.get(id=pk)
    if request.method == "POST":
        section = Section.objects.get(id=pk)
        if 'logo' in request.FILES:
            section.image = request.FILES['logo']
        else:
            section.image = request.POST.get('image')
        section.name = request.POST.get('name')
        section.name_ru = request.POST.get('name_ru')
        section.name_en = request.POST.get('name_en')

        section.text = request.POST.get('text')
        section.text_ru = request.POST.get('text_ru')
        section.text_en = request.POST.get('text_en')
        section.save()
        return redirect('section')
    context = {
        "section": section
    }
    return render(request, 'sectionedit.html', context)

def PostalservicesEdit(request,pk):
    postalservices = Postalservices.objects.get(id=pk)
    if request.method == "POST":
        postalservices = Postalservices.objects.get(id=pk)
        if 'logo' in request.FILES:
            postalservices.logo = request.FILES['logo']
        else:
            postalservices.logo = request.POST.get('image')
        postalservices.save()
        return redirect('postalservices')
    context = {
        "postalservices": postalservices
    }
    return render(request, 'postalservicesedit.html', context)


def PostalservicesCreate(request):
    if request.method == "POST":
        data = request.POST
        Postalservices.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('postalservices')

    return render(request, 'postalservicescreate.html')

def PostalservicesTemp(request):
    postalservices = Postalservices.objects.all().order_by('-id')
    context = {
        "postalservices":postalservices
    }

    return render(request, 'postalservices.html', context)


def DeletePostal(request, pk):
    postal = Postalservices.objects.get(id=pk)
    postal.delete()
    return redirect("postalservices")


def BoglanishTemp(request):
    boglanish = Boglanish.objects.all().order_by('-id')
    context = {
        "boglanish":boglanish
    }

    return render(request, 'boglanish.html', context)



def DeleteBoglanish(request, pk):
    boglanish = Boglanish.objects.get(id=pk)
    boglanish.delete()
    return redirect("boglanish")


def MobileoperatorTemp(request):
    mobileoperator = Mobileoperators.objects.all().order_by('-id')
    context = {
        "mobileoperator":mobileoperator
    }

    return render(request, 'mobileoperator.html', context)

def MobileoperatorsEdit(request,pk):
    mobileoperator = Mobileoperators.objects.get(id=pk)
    if request.method == "POST":
        mobileoperator = Mobileoperators.objects.get(id=pk)
        if 'logo' in request.FILES:
            mobileoperator.logo = request.FILES['logo']
        else:
            mobileoperator.logo = request.POST.get('image')
        mobileoperator.save()
        return redirect('mobileoperator')
    context = {
        "mobileoperators": mobileoperator
    }
    return render(request, 'mobileoperatoredit.html', context)

def MobileoperatorCreate(request):
    if request.method == "POST":
        Mobileoperators.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('mobileoperator')

    return render(request, 'mobileoperatorcreate.html')

def DeleteMobiloperator(request, pk):
    mobileoperator = Mobileoperators.objects.get(id=pk)
    mobileoperator.delete()
    return redirect("mobileoperator")


def InternetprovidersTemp(request):
    internetproviders = Internetproviders.objects.all().order_by('-id')
    context = {
        "internetproviders":internetproviders
    }

    return render(request, 'internetproviders.html', context)

def InternetprovidersEdit(request,pk):
    internetproviders = Internetproviders.objects.get(id=pk)
    if request.method == "POST":
        internetproviders = Internetproviders.objects.get(id=pk)
        if 'logo' in request.FILES:
            internetproviders.logo = request.FILES['logo']
        else:
            internetproviders.logo = request.POST.get('image')
        internetproviders.save()
        return redirect('internetproviders')
    context = {
        "internetproviders": internetproviders
    }
    return render(request, 'internetprovidersedit.html', context)

def DeleteInternetproviders(request, pk):
    internetproviders = Internetproviders.objects.get(id=pk)
    internetproviders.delete()
    return redirect("internetproviders")

def CreateInternetproviders(request):
    if request.method == "POST":
        Internetproviders.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('internetproviders')

    return render(request, 'createinternetproviders.html')

def OurAudienceEdit(request, pk):
    ouraudience = OurAudience.objects.get(id=pk)
    if request.method == "POST":
        ouraudience = OurAudience.objects.get(id=pk)
        if 'logo' in request.FILES:
            ouraudience.image = request.FILES['logo']
        else:
            ouraudience.image = request.POST.get('image')
        ouraudience.name = request.POST.get('name')
        ouraudience.name_ru = request.POST.get('name_ru')
        ouraudience.name_en = request.POST.get('name_en')
        
        ouraudience.text = request.POST.get('text')
        ouraudience.text_ru = request.POST.get('text_ru')
        ouraudience.text_en = request.POST.get('text_en')
        ouraudience.save()
        return redirect('ouraudience')
    context = {
        "ouraudience": ouraudience
    }
    return render(request, 'ouraudienceedit.html', context)

def OuraudienCereate(request):
    ouraudience = OurAudience.objects.all()
    context = {
        "ouraudience":ouraudience,
    }
    if request.method == "POST":
        data = request.POST
        OurAudience.objects.create(
            image = request.FILES['image'],
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),

            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
            
        )
        return redirect('ouraudience')
    return render(request, 'ouraudiencecreate.html', context)

def OurAudienceTemp(request):
    ouraudience = OurAudience.objects.all().order_by('-id')
    context = {
        "ouraudience":ouraudience
    }

    return render(request, 'ouraudience.html', context)


def DeleteOurAudience(request, pk):
    ouraudience = OurAudience.objects.get(id=pk)
    ouraudience.delete()
    return redirect("ouraudience")


def PercentageTemp(request):
    percentage = Percentage.objects.all().order_by('-id')
    context = {
        "percentage": percentage
    }
    return render(request, 'percentage.html', context)

def PercentageCreate(request):
    percentage = Percentage.objects.all()
    context = {
        "percentage":percentage,
    } 
    if request.method == "POST":
        data = request.POST
        Percentage.objects.create(
            percent = data.get('percent'),
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),
        )
        return redirect('percentage')
    return render(request, 'percentagecreate.html', context)

def PercentageEdit(request, pk):
    if request.method == "POST":
        percentage = Percentage.objects.get(id=pk)
        percentage.percent = request.POST.get('percent')
        percentage.name = request.POST.get('name')
        percentage.name_ru = request.POST.get('name_ru')
        percentage.name_en = request.POST.get('name_en')
        percentage.save()
        return redirect('percentage')
    percentage = Percentage.objects.get(id=pk)
    context = {
        "percentage": percentage
    }
    return render(request, 'percentageedit.html', context)

def DeletePercentage(request, pk):
    percentage = Percentage.objects.get(id=pk)
    percentage.delete()
    return redirect("percentage")


def ResidentsTemp(request):
    residents = Residents.objects.all().order_by('-id')
    context = {
        "residents": residents
    }
    return render(request, 'residents.html', context)

def ResidentsCreate(request):
    residents = Percentage.objects.all()
    context = {
        "residents":residents,
    } 
    if request.method == "POST":
        data = request.POST
        Residents.objects.create(
            image = request.FILES['image'],
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('residents')
    return render(request, 'residentscreate.html', context)

def ResidentsEdit(request, pk):
    residents = Residents.objects.get(id=pk)
    if request.method == "POST":
        residents = Residents.objects.get(id=pk)
        if 'logo' in request.FILES:
            residents.image = request.FILES['logo']
        else:
            residents.image = request.POST.get('image')
        residents.text = request.POST.get('text')
        residents.text_ru = request.POST.get('text_ru')
        residents.text_en = request.POST.get('text_en')
        residents.save()
        return redirect('residents')
    context = {
        "residents": residents
    }
    return render(request, 'residentsedit.html', context)

def DeleteResidents(request, pk):
    residents = Residents.objects.get(id=pk)
    residents.delete()
    return redirect("residents")


def TeamTemp(request):
    team = Team.objects.all().order_by('-id')
    context = {
        "team": team
    }
    return render(request, 'team.html', context)


def TeamCreate(request):
    team = Team.objects.all()
    context = {
        "team":team,
    } 
    if request.method == "POST":
        data = request.POST
        Team.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('team')
    return render(request, 'teamcreate.html', context)

def TeamEdit(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == "POST":
        team = Team.objects.get(id=pk)
        if 'image' in request.FILES:
            team.image = request.FILES['image']
        else:
            team.image = request.POST.get('image')
        team.text = request.POST.get('text')
        team.text_ru = request.POST.get('text_ru')
        team.text_en = request.POST.get('text_en')
        team.save()
        return redirect('team')
    context = {
        "team": team
    }
    return render(request, 'teamedit.html', context)

def DeleteTeam(request, pk):
    team = Team.objects.get(id=pk)
    team.delete()
    return redirect("team")


def CoworkingTemp(request):
    coworking = Coworking.objects.all().order_by('-id')
    coimages = Coimages.objects.all().order_by('-id')
    context = {
        "coimages": coimages,
        "coworking": coworking
    }
    return render(request, 'coworking.html', context)

def CoworkingCreate(request):
    coworking = Coworking.objects.all()
    coimages = Coimages.objects.all()
    context = {
        "coworking":coworking,
        "coimages":coimages,
    } 
    if request.method == "POST":
        data = request.POST
        images = []
        for img in request.POST:
            
            if img.split("-")[0] == 'img':
                id = img.split("-")[1]
                images.append(Coimages.objects.get(id=id))
        print(images)
        a = Coworking.objects.create(
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        a.image.set(images)
        
        return redirect('coworking')
    return render(request, 'coworkingcreate.html', context)

def CoworkingEdit(request, pk):
    coworking = Coworking.objects.get(id=pk)
    if request.method == "POST":
        coworking = Coworking.objects.get(id=pk)
        if 'image' in request.FILES:
            coworking.image = request.FILES['image']
        else:
            coworking.image = request.POST.get('image')
        coworking.text = request.POST.get('text')
        coworking.text_ru = request.POST.get('text_ru')
        coworking.text_en = request.POST.get('text_en')
        coworking.save()
        return redirect('coworking')
    context = {
        "coworking": coworking
    }
    return render(request, 'coworkingedit.html', context)

def CoimagesCreate(request):
    coimages = Coimages.objects.all()
    context = {
        "coimages":coimages,
    } 
    if request.method == "POST":
        Coimages.objects.create(
            image = request.FILES['image'],
        )
        return redirect('coworking')
    return render(request, 'coimagescreate.html', context)

def CoimagesEdit(request, pk):
    coimages = Coimages.objects.get(id=pk)
    context = {
        "coimages":coimages,
    } 
    if request.method == "POST":
        coimages = Coimages.objects.get(id=pk)
        if 'image' in request.FILES:
            coimages.image = request.FILES['image']
        else:
            coimages.image = request.POST.get('image')
        Coimages.objects.create(
            image = request.FILES['image']
        )
        return redirect('coworking')
    return render(request, 'coimagesedit.html', context)

def DeleteCoimage(request, pk):
    coimage = Coimages.objects.get(id=pk)
    coimage.delete()
    return redirect('coworking') 

def DeleteCoworking(request, pk):
    coworking = Coworking.objects.get(id=pk)
    coworking.delete()
    return redirect('coworking')

def InfrastructureSliderTemp(request):
    infra = InfrastructureSlider.objects.all().order_by('-id')
    context = {
        'infra':infra,
    }
    return render(request, 'infrastructureslider.html', context)

def InfrastructureCreate(request):
    infra = InfrastructureSlider.objects.all()
    context = {
        "infra":infra,
    } 
    if request.method == "POST":
        data = request.POST
        Team.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('infrastructureslider')
    return render(request, 'infrastructureslider.html', context)


def InfrastructureEdit(request, pk):
    infrastructureslider = InfrastructureSlider.objects.get(id=pk)
    if request.method == "POST":
        infrastructureslider = InfrastructureSlider.objects.get(id=pk)
        if 'image' in request.FILES:
            infrastructureslider.image = request.FILES['image']
        else:
            infrastructureslider.image = request.POST.get('image')
        infrastructureslider.text = request.POST.get('text')
        infrastructureslider.text_ru = request.POST.get('text_ru')
        infrastructureslider.text_en = request.POST.get('text_en')
        infrastructureslider.save()
        return redirect('infrastructureslider')
    context = {
        "infrastructureslider": infrastructureslider
    }
    return render(request, 'infrastructureslideredit.html', context)


def InfrastructureDelete(request, pk):
    infra = InfrastructureSlider.objects.get(id=pk)
    infra.delete()
    return redirect("team")
