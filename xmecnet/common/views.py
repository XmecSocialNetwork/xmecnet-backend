from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from .models import User

import random
import datetime
import json

# To be removed.
@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            print(data)
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

@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))


            print(data)
            if User.objects.filter(email=data['email']).exists():
                try:
                    user = User.login(data['email'], data['password'])
                    print(user)
                    if user:
                        request.session['logged_in'] = True
                        print (user)
                        return JsonResponse({'Success': True})
                    else:
                        return JsonResponse({'Error': 'Invalid password'}, status=403)
                except Exception as e:
                    # To be changed during production
                    print(e)
                    return JsonResponse({'Error': 'Could not log in'}, status=403)
            else:
                return JsonResponse({'Error': 'User not registered'}, status=400)
        except Exception as e:
            # To be changed during production
            print(e)
            return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
    else:
        return JsonResponse({'Error': 'Invalid request'}, status=403)

@csrf_exempt
def otp(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        request.session["otp"]=random.randint(1001,9999)
        send_mail(
        'OTP from Xmec Network',
        'Hello Mecian,We are glad to see you back.Enter this Verification code '+str(request.session["otp"])+'in the app to continue ',
        'jeswincyriac.k@gmail.com',
        [data["email"]],
        fail_silently=False,
        )

        return JsonResponse({'OTPsenttomail ': True})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
