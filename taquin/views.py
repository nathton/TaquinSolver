from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'taquin/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'taquin/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'taquin/results.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'taquin/index.html', context)

# # Leave the rest of the views (detail, results, vote) unchanged

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'taquin/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'taquin/results.html', {'question': question})

def vote(request, question_id):
    import pdb; pdb.set_trace()
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'taquin/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('taquin:results', args=(question.id,)))

def voteq(request):
    import pdb; pdb.set_trace()
    return request.POST        