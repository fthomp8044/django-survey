from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.forms.formsets import formset_factory
from django.urls import reverse
from .forms import QuestionForm, ChoiceFormSet
from .models import Question, Choice
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'surveys/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

class CreateView(generic.CreateView):
    template_name = 'surveys/create.html'
    model = Question
    form_class = QuestionForm
    success_url = 'surveys/index/'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = QuestionForm(self.request.POST)
            context['formset'] = ChoiceFormSet(self.request.POST)
        else:
            context['form'] = QuestionForm()
            context['formset'] = ChoiceFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context ['formset']
        if all ([form.is_valid(), formset.is_valid()]):
            form.instance.created_by = self.request.user
            question = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = question
                    choice.save()
        return HttpResponseRedirect(reverse('surveys:index',))

class ResultsView(generic.DetailView):
    template_name = 'surveys/results.html'
    model = Question


class DetailView(generic.DetailView):
    template_name = 'surveys/detail.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('surveys:results', args=(question.id,)))
