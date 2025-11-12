from django.core.management.base import BaseCommand
from main.models import Specialization, Service, Education, Testimonial

class Command(BaseCommand):
    help = 'Create sample medical data'

    def handle(self, *args, **options):
        # Специализации
        specializations = [
            {
                'title': 'Сахарный диабет',
                'description': 'Диагностика, подбор терапии, обучение самоконтролю, профилактика осложнений',
                'icon': 'fas fa-syringe',
                'order': 1
            },
            {
                'title': 'Щитовидная железа',
                'description': 'Лечение гипотиреоза, гипертиреоза, тиреоидитов, узловых образований',
                'icon': 'fas fa-thyroid',
                'order': 2
            },
            {
                'title': 'Ожирение и метаболизм',
                'description': 'Комплексное лечение избыточного веса, метаболический синдром',
                'icon': 'fas fa-weight',
                'order': 3
            },
        ]

        for spec_data in specializations:
            Specialization.objects.get_or_create(**spec_data)

        # Услуги
        services = [
            {
                'title': 'Первичная консультация',
                'description': 'Комплексный осмотр, сбор анамнеза, постановка предварительного диагноза',
                'price': 2500,
                'duration': '60 минут'
            },
            {
                'title': 'Повторная консультация',
                'description': 'Анализ результатов обследования, коррекция лечения',
                'price': 2000,
                'duration': '40 минут'
            },
        ]

        for service_data in services:
            Service.objects.get_or_create(**service_data)

        # Образование
        education = [
            {
                'institution': 'Первый МГМУ им. И.М. Сеченова',
                'degree': 'Врач-лечебник',
                'years': '2005-2011',
                'description': 'Диплом с отличием'
            },
            {
                'institution': 'Клиническая ординатура',
                'degree': 'Врач-эндокринолог',
                'years': '2011-2013',
                'description': 'Специализация по эндокринологии'
            },
        ]

        for edu_data in education:
            Education.objects.get_or_create(**edu_data)

        self.stdout.write(
            self.style.SUCCESS('Successfully created medical data')
        )