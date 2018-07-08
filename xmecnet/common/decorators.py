from django.core.exceptions import PermissionDenied

def is_logged_in(function):
    def wrap(request, *args, **kwargs):

        if (request.session.get('logged_in',False) == True):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
