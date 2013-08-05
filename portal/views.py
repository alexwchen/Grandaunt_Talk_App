from django.shortcuts import render_to_response
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from portal.models import main_page


"""
If users are authenticated, direct them to the main page. Otherwise, take
them to the login page.
"""
def portal_main_page(request):
    """
    div1_1 = main_page.objects.filter(div_id = 1) 
    div1_2 = []
    for i in div1_1:
        i.encode = "#00CCFF"
        div1_2.append(i)

    div = main_page.objects.filter(div_id = 2) 
    c = main_page.objects.filter(div_id = 3) 
    d = main_page.objects.filter(div_id = 4) 
    """
    
    return render_to_response('portal/portal.html',
    {
    })


