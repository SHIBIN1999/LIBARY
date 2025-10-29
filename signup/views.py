from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserAccount  
from django.shortcuts import get_object_or_404
from subapp.models import student
from django.utils import timezone
from datetime import timedelta

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


def logout_view(request):
    # Clear all session data
    request.session.flush()
    
    # Add success message
    messages.success(request, 'You have been logged out successfully.')
    
    # Create response with cache headers
    response = redirect('login')
    
    return response


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserAccount.objects.get(email=email, password=password)
            # Store user info in session
            request.session['user_id'] = user.id  # ADD THIS
            request.session['username'] = user.name  # ADD THIS
            
            if user.is_Admin:
                messages.success(request, f'Welcome back, {user.name}!')
                return redirect('list') 
            else:
                messages.success(request, f'Welcome back, {user.name}!')
                return redirect('books')  # No pk needed anymore
        except UserAccount.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')


def books_view(request):
    # Get user from session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    if request.method == 'POST':
        # Handle booking here
        book_id = request.POST.get('book_id')
        if book_id:
            try:
                book = student.objects.get(id=book_id)
                user = UserAccount.objects.get(id=user_id)  # Get the user object
                current_date = timezone.now().date() 
                book.user = user  # Assign the user to the book
                book.starting_date = current_date
                book.ending_date = current_date + timedelta(days=30)
                book.is_booked = True
                book.save()
                messages.success(request, f'Successfully booked "{book.title}"!')
            except student.DoesNotExist:
                messages.error(request, 'Book not found!')
            except UserAccount.DoesNotExist:
                messages.error(request, 'User not found!')
    
    s = student.objects.all()
    return render(request, 'books.html', {'s': s})



def unbook_view(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            try:
                book = student.objects.get(id=book_id)
                book.user = None  # Clear the user assignment
                book.is_booked = False
                book.starting_date = None  # Clear the dates
                book.ending_date = None
                book.save()
                messages.success(request, f'Successfully unbooked "{book.title}"!')
            except student.DoesNotExist:
                messages.error(request, 'Book not found!')
    return redirect('books')