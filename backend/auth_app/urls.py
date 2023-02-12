from django.urls import path
from backend.auth_app.views import user_views
from backend.auth_app.views.jwt_views import MyTokenObtainPairView
from backend.auth_app.views.user_views import ProfileView

urlpatterns = (
    path("users/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/register/", user_views.UserRegisterView.as_view(), name="user_register"),
    path("users/profile/", ProfileView.as_view(), name="profile"),
    # path("auth_app/profile/delete/<int:pk>", DeleteProfileView.as_view(), name="delete-profile"),
    # path("auth_app/logout/", UserLogoutView.as_view(), name="logout"),
    # path("auth_app/logout/confirmation", UserLogoutConfirmationView.as_view(), name="logout-confirm"),
    # path("auth_app/farewell/", FarewellView.as_view(), name="farewell"),
    # path("auth_app/password_change/", ChangeUserPasswordView.as_view(), name="password_change"),
    # path("auth_app/password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    # path("auth_app/success/", SuccessPassChangeView.as_view(), name="success-url")

)