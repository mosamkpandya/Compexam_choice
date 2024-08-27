from django.shortcuts import render, redirect
from .forms import UserDataForm
# Create your views here.


def CompExamChoice(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            # Save data to session instead of database for preview
            request.session['form_data'] = form.cleaned_data
            return redirect('preview')
    else:
        form = UserDataForm()
    return render(request, 'compexamchoice.html', {'form': form})
def preview(request):
    form_data = request.session.get('form_data', None)
    if not form_data:
        return redirect('submit_user_data')  # Redirect back if no data

    if request.method == 'POST':
        # If confirmed, save to the database
        form = UserDataForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('success')

    return render(request, 'user_form/preview.html', {'form_data': form_data})


def success(request):
    return render(request, 'success.html')
