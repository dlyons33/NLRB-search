from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields