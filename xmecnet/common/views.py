from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from .models import User
from .decorators import is_logged_in
import random
import datetime
import json

# To be removed.
@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            #print(data)
            print(request.session["otp"])
            print(data['otp'])
            if 'roll_no' not in data:
                data['roll_no'] = None
                #print(request.session["otp"])
                #print(data['otp'])
            if (str(request.session["otp"]) == data['otp']):
                print("im in")
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

                        request.session["logged_in"]=True
                        request.session['email'] = data['email']
                        return JsonResponse({'status': "success"})

                    except Exception as e:
                        print(e)
                        return JsonResponse({'status': 'Invalid data'},
                                            status=400)

                else:
                    print("why iam i here")
                    return JsonResponse({'status': 'User already registered'},
                                        status=400)
            else:
                    print("why iam i here")
                    return JsonResponse({'status': 'otp not correct'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'Something unexpected happened'},
                                status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=405)


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
                        request.session['email'] = data['email']
                        print (user)
                        return JsonResponse({'status': "success"})
                    else:
                        return JsonResponse({'status': 'Invalid password'}, status=403)
                except Exception as e:
                    # To be changed during production
                    print(e)
                    return JsonResponse({'status': 'Could not log in'}, status=403)
            else:
                return JsonResponse({'status': 'User not registered'}, status=400)
        except Exception as e:
            # To be changed during production
            print(e)
            return JsonResponse({'status': 'Something unexpected happened'}, status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=403)

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
        print("reached here")
        return JsonResponse({'status': "Success"})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)

@csrf_exempt
def isloggedin(request):
    try:
        print(request.session["logged_in"])
        return JsonResponse({"logged_in":request.session["logged_in"]})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)

@csrf_exempt
@is_logged_in
def logout(request):
    try:
        request.session["logged_in"]=False
        request.session.flush()
        return JsonResponse({"status":"logoutsuccessfull"})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)

@csrf_exempt
@is_logged_in
def search(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        return JsonResponse({"status":"successfull"})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'status': 'Failed'}, status=500)





@csrf_exempt
def trying(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        print(request.session['logged_in'])
        return JsonResponse({'tryingreceived ': True})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)

@csrf_exempt
def trying2(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        print(request.session['hai'])
        return JsonResponse({'tryingreceived ': True})
    except Exception as e:
        # To be changed during production
        print(e)
        return JsonResponse({'Error': 'Something unexpected happened'}, status=500)
