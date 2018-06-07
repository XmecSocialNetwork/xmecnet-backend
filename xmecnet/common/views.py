from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

from .models import User


# To be removed.
@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = request.body.decode("utf-8")
            if not User.objects.filter(email=data['email']).exists():
                try:
                    user = User.objects.create(email=data['email'],
                                               name=data['name'],
                                               roll_no=data['roll_no'],
                                               password=make_password(data['password']),
                                               date_of_birth=data['dob'],
                                               branch=data['branch'])

                    
                    return JsonResponse({'Success': True})

                except Exception as e:
                    return JsonResponse({'Error': 'Invalid data'},
                                        status=400)

            else:
                return JsonResponse({'Error': 'User already registered'},
                                    status=400)
        except Exception as e:
            return JsonResponse({'Error': 'Something unexpected happened'},
                                status=500)
    else:
        return JsonResponse({'Error': 'Invalid request'}, status=405)

# TODO: Write endpoint for login and to setSession.