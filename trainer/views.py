from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from feedback.models import Feedback
from student.models import Student
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home-page')
    permission_required = 'trainer.add_trainer'


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainer'


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-of-trainers')
    success_message = "{f_name} {l_name}"
    permission_required = 'trainer.view_trainer'

    def get_success_message(self, clean_data):
        return self.success_message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class TrainerDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    permission_required ='trainer.delete_trainer'


class TrainerDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer
    permission_required = 'trainer.view_trainer'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # se poate regasi si ca data = super().get_context_data(**kwargs)
        now = datetime.now()  # preluam data si ora curenta
        context[
            'current_datetime'] = now  # adaugam in dict context, cheia current_datetime pt a afisa data si ora curenta

        current_trainer_id = self.kwargs["pk"]  # Accesam id-ul trainerului selectat

        students_current = Student.objects.filter(
            trainer_id=current_trainer_id)  # realizam un query prin care luam toti studentii asignati trainerului selectat
        context[
            'students'] = students_current  # adaugam in dict context, cheia students pt a afisa o tabela cu studentii trainerului

        feedback_current = Feedback.objects.filter(trainer_id=current_trainer_id)
        context['feedbacks'] = feedback_current

        return context

    # Get Context Data(get_context_data) este o metoda folosita in clasele de View-uri(ListView, TemplateView, UpdateView, etc)
    # este utilitaza pentru a returna sau pentru a construi si a retuna un dictionar de date de context care vor fi afisate in paginile de HTML
