from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

from .models import User

import datetime
import json

# To be removed.
@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            
            if 'roll_no' not in data:
                data['roll_no'] = None

            if not User.objects.filter(email=data['email']).exists():
                try:
                    user = User.create(email=data['email'],
                                       name=data['name'],
                                       password=make_password(data['password']),
                                       dobday=data['dobday'],
                                       dobmonth=data['dobmonth'],
                                       dobyear=data['dobyear'],
                                       branch=data['branch'],
                                       roll_no = data['roll_no']
                                     )
            
                    
                    return JsonResponse({'Success': True})

                except Exception as e:
                    print(e)
                    return JsonResponse({'Error': 'Invalid data'},
                                        status=400)

            else:
                return JsonResponse({'Error': 'User already registered'},
                                    status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'Error': 'Something unexpected happened'},
                                status=500)
    else:
        return JsonResponse({'Error': 'Invalid request'}, status=405)

# TODO: Write endpoint for login and to setSession.
