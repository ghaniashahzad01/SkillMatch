from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm


@login_required
def create_job(request):
    if not request.user.is_employer:
        return redirect('login')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer-dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})
