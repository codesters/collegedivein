from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cdi.forms import SettingsForm

from django.contrib.auth.models import User

@login_required
def settings(request):
    form = None
    u = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=u)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, ('Your settings have been saved'))
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = SettingsForm(instance=u)
    return render_to_response('settings.html', {'form': form}, context_instance=RequestContext(request))

