from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'feedback/create_feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('list-of-feedbacks')
    success_message = "{f_name} {l_name}"

    def get_success_message(self, cleaned_data):
        message = self.success_message + ', ' + 'your feedback was submitted '

        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class FeedbackListView(ListView):
    template_name = 'feedback/list-of-feedbacks.html'
    model = Feedback
    context_object_name = 'all_feedbacks'


class FeedbackUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    template_name = 'feedback/update-feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('list-of-feedbacks')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ', ' + 'your feedback form has been updated succesfully!'
        return message.format(f_name=self.object.first_name,l_name=self.object.last_name)


class FeedbackDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'feedback/delete_feedback.html'
    model = Feedback
    success_url = reverse_lazy('list-of-feedbacks')


class FeedbackDetailView(LoginRequiredMixin, DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback


