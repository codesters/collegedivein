from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cdi.forms import UserForm, StudentForm

from django.contrib.auth.models import User
from student.models import Student

@login_required
def settings(request):
    form1 = None
    form2 = None
    u = User.objects.get(email=request.user.email)
    s = Student.objects.get(user=u)
    if request.method == 'POST':
        form1 = UserForm(request.POST, instance=u)
        form2 = StudentForm(request.POST, instance=s)
        if all([form1.is_valid(), form2.is_valid()]):
            messages.add_message(request, messages.SUCCESS, ('Your settings have been saved'))
            form1.save()
            form2.save()
            return HttpResponseRedirect(reverse('account_settings'))
    else:
        form1 = UserForm(instance=u)
        form2 = StudentForm(instance=s)
    return render_to_response('settings.html', {'form1': form1, 'form2': form2}, context_instance=RequestContext(request))

