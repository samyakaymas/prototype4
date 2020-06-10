from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView,CreateView, UpdateView,DetailView
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    return HttpResponse("saved")

class TheoryCreateView(CreateView):
    model=Theory
    form_class=TheoryTagForm
    success_url='/theory'
    def form_valid(self, form):
            userId=self.request.user.id
            self.object = form.save(commit=False)
            self.object.userId = userId
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
class TheoryListView(ListView):
    model=Theory
    def get_queryset(self):
        userId = self.request.user.id
        print(userId)
        return Theory.objects.filter(userId=userId)
class TheoryDetailView(DetailView):
    model = Theory

class TheoryUpdateView(UpdateView):
    model = Theory
    pk_url_kwarg = 'pk'
    success_url = 'theory/'
    fields = '__all__'


def loadSubConcepts(request):
    conceptId = request.GET.get('concept')
    subConcepts=SubConcept.objects.filter(concept=Concept.objects.get(pk=conceptId))
    return render(request,"theoryTag/sub_concept_dropdown_list.html",{'subConcepts':subConcepts})

def loadConcepts(request):
    userChapter = get_user_model().objects.get(pk=request.user.id).chapter.id
    chapterId = request.GET.get('chapter',userChapter)
    concepts=Concept.objects.filter(chapter=Chapter.objects.get(pk=chapterId))
    return render(request,"theoryTag/concept_dropdown_list.html",{'concepts':concepts})

def loadSubConceptName(request):
    subConceptId=request.GET.get('subConcept')
    subConcept=SubConcept.objects.get(pk=subConceptId)
    data={"subConceptName":subConcept.name}
    return JsonResponse(data)