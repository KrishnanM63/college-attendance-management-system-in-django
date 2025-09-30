from django.urls import reverse
from django.shortcuts import redirect

class RedirctAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        paths_to_redirct = []   
        if request.user.is_authenticated:
            paths_to_redirct =[reverse("login_page"),reverse("registerpage")]
        if request.path in paths_to_redirct:
            return redirect(reverse("dashbort"))
        
        response = self.get_response(request)
        return response
                
            
        
        