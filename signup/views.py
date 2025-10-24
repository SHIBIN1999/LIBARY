from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserAccount  # Import your model

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        if not username or not email or not password:
            messages.error(request, 'All fields are required!')
            return redirect('signup')

        # Check if email already exists
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        # Save user to database
        UserAccount.objects.create(name=username, email=email, password=password)

        messages.success(request, f'Account created successfully for {username}!')
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # using same field name from form
        password = request.POST.get('password')

        try:
            user = UserAccount.objects.get(email=email, password=password)
            messages.success(request, f'Welcome back, {user.name}!')
            return redirect('list') 
        except UserAccount.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')



def logout_view(request):
    # Clear all session data
    request.session.flush()
    
    # Add success message
    messages.success(request, 'You have been logged out successfully.')
    
    # Create response with cache headers
    response = redirect('login')
    
    return response