from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileUserForm, ProfileForm, TicketForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket

from .otp import generate_otp


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            otp = generate_otp()

            request.session['register_otp'] = otp

            request.session['register_data'] = request.POST.dict()

            return redirect('accounts:register_otp')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


def register_otp(request):

    if request.method == 'POST':

        user_otp = request.POST.get('otp')
        correct_otp = request.session.get('register_otp')

        try:
            user_otp = int(user_otp)
        except (TypeError, ValueError):
            user_otp = None

        if user_otp and correct_otp:

            if user_otp == correct_otp:

                register_data = request.session.get(
                    'register_data'
                )

                form = RegisterForm(register_data)

                if form.is_valid():
                    form.save()

                request.session.pop(
                    'register_otp',
                    None
                )

                request.session.pop(
                    'register_data',
                    None
                )

                return redirect('accounts:login')

        return render(
            request,
            'accounts/otp.html',
            {
                'error': 'OTP is incorrect.',
                'purpose': 'register'
            }
        )

    return render(
        request,
        'accounts/otp.html',
        {
            'purpose': 'register'
        }
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            otp = generate_otp()

            request.session['login_user_id'] = user.id

            request.session['login_otp'] = otp

            return redirect('accounts:login_otp')

        return render(
            request,
            'accounts/login.html',
            {
                'error':
                    'Username or password is incorrect.'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )


def login_otp(request):

    if request.method == 'POST':

        user_otp = request.POST.get('otp')
        correct_otp = request.session.get('login_otp')

        try:
            user_otp = int(user_otp)
        except (TypeError, ValueError):
            user_otp = None

        if user_otp and correct_otp:

            if user_otp == correct_otp:

                user_id = request.session.get(
                    'login_user_id'
                )

                user = User.objects.get(
                    id=user_id
                )

                login(request, user)

                request.session.pop(
                    'login_otp',
                    None
                )

                request.session.pop(
                    'login_user_id',
                    None
                )

                return redirect('website:index')

        return render(
            request,
            'accounts/otp.html',
            {
                'error': 'OTP is incorrect.',
                'purpose': 'login'
            }
        )

    return render(
        request,
        'accounts/otp.html',
        {
            'purpose': 'login'
        }
    )
def resend_otp(request):

    purpose = request.POST.get('purpose')

    if purpose == 'register':

        register_data = request.session.get('register_data')

        if not register_data:
            return redirect('accounts:register')

        otp = generate_otp()

        request.session['register_otp'] = otp

        return redirect('accounts:register_otp')


    elif purpose == 'login':

        user_id = request.session.get('login_user_id')

        if not user_id:
            return redirect('accounts:login')

        otp = generate_otp()

        request.session['login_otp'] = otp

        return redirect('accounts:login_otp')


    return redirect('accounts:login')

@login_required
def profile(request):

    if request.method == 'POST':

        user_form = ProfileUserForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile
        )

        if (
            user_form.is_valid()
            and profile_form.is_valid()
        ):

            user_form.save()
            profile_form.save()

            return redirect('accounts:profile')

    else:

        user_form = ProfileUserForm(
            instance=request.user
        )

        profile_form = ProfileForm(
            instance=request.user.profile
        )

    return render(
        request,
        'accounts/profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )


def logout_view(request):

    logout(request)

    return redirect('website:index')


@login_required
def create_ticket(request):

    if request.method == 'POST':

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.sender = request.user

            ticket.save()

            return redirect('accounts:ticket-list')

    else:

        form = TicketForm()

    return render(
        request,
        'tickets/create_ticket.html',
        {
            'form': form
        }
    )



@login_required
def ticket_list(request):

    tickets = Ticket.objects.filter(
        sender=request.user
    ).order_by('-created_at')

    return render(
        request,
        'tickets/ticket_list.html',
        {
            'tickets': tickets
        }
    )


@login_required
def ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        sender=request.user
    )

    return render(
        request,
        'tickets/ticket_detail.html',
        {
            'ticket': ticket
        }
    )