from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from poem.models import Poem
from .forms import PoemForm


# Create your views here.


@login_required()
def cpanel(request):
    return render(request, 'admin.html',{})

class PoemList(ListView):
    model = Poem
    template_name = 'poem/poem_edit.html'
    context_object_name = "poem"  
    paginate_by = 10


class PoemCreate(CreateView):
	model = Poem
	template_name = 'poem/poem.html'
	success_url = reverse_lazy('poem_edit')
	form_class = PoemForm
	context_object_name = "poem"  


class PoemUpdate(UpdateView):
	model = Poem
	template_name = 'poem/poem_update_form.html'
	success_url = reverse_lazy('poem_edit')
	form_class = PoemForm
	context_object_name = "poem"  

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		if "cancel" in request.POST:
			return redirect('delete_poem', pk=self.object.pk)
		else:
			return super(PoemUpdate, self).post(request, *args, **kwargs)


class PoemDelete(DeleteView):
    model = Poem
    template_name = 'poem/delete_confirm.html'
    success_url = reverse_lazy('poem_edit')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(PoemDelete, self).post(request, *args, **kwargs)