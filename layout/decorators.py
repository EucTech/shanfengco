from django.shortcuts import redirect


def is_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            value = request.session.get('is_admin', False)
            return view_func(request, *args, **kwargs)
        else:
            # Handle the case where the user is not authenticated (e.g., redirect to login)
            return redirect('admin_login')

    return _wrapped_view

