from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenge = {
    
    "January": "January month will be displayed",
    "febuary": "Febuaray month will be displayed this all is possible due to dynamic segements feature of django",
    "march": "March will be displayed and urls is also modified by adding a placeholder",
    "april": "april will be displayed",
    "may": "may wll be displayed",
    "june": "June will be displayed here",
    "july": "July will be displayed here we created a dictonary",
    "august": "August will be displayed",
    "september": "september will be displaye",
    "october": "october will be displayed",
    "november": "november will be displayed",
    "december": "december will be displayed"
    
}
# Create your views here.
# def january(request):
#     return HttpResponse("DJANGO APP 1")


# def febuary(request):
#     return HttpResponse("February app using django using views.py")




def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenges", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)  
    
    
    return render(request ,"challenges/index.html" , {
        
        "months": months
    })
  

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request , month):
    try:
       challenge_text = monthly_challenge[month]
       return render(request, "challenges/challenge.html" , {
           
            "text": challenge_text,
            "month_place": month
       })
    #    response_data = render_to_string("challenges/challenge.html")
    #    return HttpResponse(response_data)   
    except:
        return HttpResponseNotFound("<h1>This Month is not supported<h1>")
