from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Amenities, Hotel, HotelBooking
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Welcome, Signup Successful!')
            return redirect('signin')
        else:
            messages.error(request, 'Username or Email already exists.')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_data = authenticate(request, username=username, password=password)
        if user_data:
            login(request, user_data)
            messages.success(request, f'{user_data.username} signed in successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('index')


def check_booking(uid, room_count, start_date, end_date):
    qs = HotelBooking.objects.filter(hotel__id=uid).filter(
        Q(start_date__gte=start_date, end_date__lte=end_date) |
        Q(start_date__lte=start_date, end_date__gte=end_date)
    )
    return False if qs.count() >= room_count else True


def index(request):
    amenities = Amenities.objects.all()
    hotels = Hotel.objects.all()
    total_hotels = len(hotels)
    search = request.GET.get('searchInput') or ''
    sort_by = request.GET.get('sortSelect') or ''
    price = request.GET.get('price') or ''
    startdate = request.GET.get('startDate') or ''
    enddate = request.GET.get('endDate') or ''
    selected_amenities = request.GET.getlist('selectAmenity')

    if selected_amenities:
        hotels = hotels.filter(amenities__amenity_name__in=selected_amenities).distinct()

    if search:
        hotels = hotels.filter(
            Q(hotel_name__icontains=search) |
            Q(description__icontains=search) |
            Q(amenities__amenity_name__icontains=search)
        ).distinct()

    if sort_by == 'low_to_high':
        hotels = hotels.order_by('hotel_price')
    elif sort_by == 'high_to_low':
        hotels = hotels.order_by('-hotel_price')

    if price:
        hotels = hotels.filter(hotel_price__lte=int(price))

    if startdate and enddate:
        unbooked = []
        for h in hotels:
            if check_booking(h.id, h.room_count, startdate, enddate):
                unbooked.append(h)
        hotels = unbooked

    context = {
        'hotels': hotels,
        'total_hotels': total_hotels,
        'amenities': amenities,
        'selected_amenities': selected_amenities,
        'sort_by': sort_by,
        'search': search,
        'price': price,
        'startdate': startdate,
        'enddate': enddate,
        'date': datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, 'index.html', context)


@login_required
def book_hotel(request, hotel_id):
    if request.method == 'POST':
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        booking_type = request.POST.get('booking_type')

        # Validate dates
        if start_date >= end_date:
            messages.error(request, "End date must be after start date.")
            return redirect('index')

        # Check room availability
        if not check_booking(hotel.id, hotel.room_count, start_date, end_date):
            messages.error(request, "No rooms available for selected dates.")
            return redirect('index')

        # Create the booking with status 'Pending'
        HotelBooking.objects.create(
            hotel=hotel,
            user=request.user,
            start_date=start_date,
            end_date=end_date,
            booking_type=booking_type,
            status='Pending'
        )
        messages.success(request, "Booking submitted successfully. Awaiting approval.")
        return redirect('index')

    return redirect('index')


@login_required
def profile(request):
    user = request.user
    bookings = HotelBooking.objects.filter(user=user).select_related('hotel').order_by('-start_date')
    
    return render(request, 'profile.html', {
        'user': user,
        'bookings': bookings
    })
