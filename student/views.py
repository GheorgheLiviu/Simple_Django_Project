from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent


# Create your views here.

# PermissonRequiredMixin - verificam daca userul logat are permisiunea respectiva, daca user ul logat NU ARE permisiune
# respectiv va fi redirectionat catre pagina 403
# CreateView -> fololsit pentru a genera un formular pe baza modelului si pentru a salva datele in baza de date
# SuccessMessageMixin -> folosit pentru a afisa un mesaj de success in
# momentul in care actiunea a fost realizata cu succes


class StudentCreateView(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    success_message = "{f_name} {l_name}"
    permission_required = 'student.add_student'
    def get_success_message(self, cleaned_data):
        if self.object.gender == 'male':
            message = self.success_message + '' + 'a fost adaugat cu succes!'
        else:
            message = self.success_message + '' + 'a fost adaugata cu succes!'

        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.last_name = new_student.last_name.title()
            new_student.email = new_student.email.lower()
            new_student.save()

            get_current_id = self.request.user.id
            get_current_username = User.objects.get(id=get_current_id).username

            get_message = f'Noul student {new_student.first_name} {new_student.last_name} a fost creat de catre {get_current_username}'

            HistoryStudent.objects.create(message=get_message, active=new_student.active, user_id=get_current_id)

            # self reprezinta instanta curenta a clasei respective
            # self este utilizat pentru a accesa diverse atribute si metoda ale instantei

            # self.request.user.id -> reprezinta obiectul userului curent asociat cu cererea HTTP.
            # Este un obiect de tip USER(care apartine clasei user) care contine informatii depre userul autentificat

        return redirect('list-of-students')


# ListView -> folosim pentru a afisa inregistrarile din tablea student_student

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'  # Students.objects.all() Django va face asta in spate
    permission_required = 'student.view_list_of_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)


# UpdateView -> folosim pentru a actualiza datele unui student

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView, SuccessMessageMixin):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')
    success_message = "{f_name} {l_name}"
    permission_required = 'student.change_student'

    def get_success_message(self, cleaned_data):
        if self.object.gender == 'male':
            message = self.success_message + '' + 'a fost modificat cu succes!'
        else:
            message = self.success_message + '' + 'a fost modificata cu succes!'

        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


@login_required()
def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        students = Student.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
    else:
        students = Student.objects.all()

    return render(request, 'student/list_of_students.html', {'all_students': students})
