from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.admin_user.forms import UserRegistrationForm
from apps.admin_user.models import AdminUser


class SingUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/sign_up.html"

    class Meta:
        model = AdminUser
        fields = (
            "username",
            "avatar",
        )


class UserUpdateView(UpdateView):
    model = AdminUser
    fields = (
        "username",
        "avatar",
    )
    template_name = "accounts/user_update_form.html"
    template_name_suffix = "_update_form.html"
    success_url = reverse_lazy("homepage:index")
