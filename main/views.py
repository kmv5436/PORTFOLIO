from django.shortcuts import render, redirect
from .models import Specialization, Service, Education, Testimonial, PatientReview
from .forms import ContactForm, PatientReviewForm

def home(request):
    specializations = Specialization.objects.all().order_by('order')
    services = Service.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    
    # Инициализируем обе формы
    contact_form = ContactForm()
    review_form = PatientReviewForm()
    
    if request.method == 'POST':
        # Проверяем, какая форма была отправлена
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('home')
            # Если форма невалидна, оставляем review_form пустой
            review_form = PatientReviewForm()
        elif 'review_submit' in request.POST:
            review_form = PatientReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                return redirect('home')
            # Если форма невалидна, оставляем contact_form пустой
            contact_form = ContactForm()
    
    return render(request, 'home.html', {
        'specializations': specializations,
        'services': services,
        'education': education,
        'testimonials': testimonials,
        'contact_form': contact_form,
        'review_form': review_form,
    })