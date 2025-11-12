from django.contrib import admin
from .models import Specialization, Service, Education, Contact, Testimonial
from .models import PatientReview

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration']
    list_filter = ['price']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'years']
    search_fields = ['institution', 'degree']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'phone']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'condition', 'rating', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['name', 'condition', 'content']
    list_editable = ['is_active']

@admin.register(PatientReview)
class PatientReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_published', 'created_at']
    list_filter = ['rating', 'is_published', 'created_at']
    search_fields = ['name', 'review_text']
    list_editable = ['is_published']
    readonly_fields = ['created_at']