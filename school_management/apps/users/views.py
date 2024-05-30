from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm, RoleForm
from .models import CustomUser, Role, UserActivityLog

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'templates/users/signup.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'templates/users/profile.html'

class UserListView(generic.ListView):
    model = CustomUser
    template_name = 'templates/users/user_list.html'
    context_object_name = 'users'

class UserDetailView(generic.DetailView):
    model = CustomUser
    template_name = 'templates/users/user_detail.html'

class UserUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'templates/users/user_form.html'
    success_url = reverse_lazy('user_list')

class RoleCreateView(generic.CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'templates/users/role_form.html'
    success_url = reverse_lazy('role_list')

class RoleListView(generic.ListView):
    model = Role
    template_name = 'templates/users/role_list.html'
    context_object_name = 'roles'

class UserActivityLogListView(generic.ListView):
    model = UserActivityLog
    template_name = 'templates/users/user_activity_log_list.html'
    context_object_name = 'logs'
