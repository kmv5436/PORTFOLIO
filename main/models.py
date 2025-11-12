from django.db import models

class Specialization(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    icon = models.CharField(max_length=50, default='fas fa-stethoscope', verbose_name="Иконка")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        ordering = ['order']

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    duration = models.CharField(max_length=50, blank=True, verbose_name="Продолжительность")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Учебное заведение")
    degree = models.CharField(max_length=200, verbose_name="Степень/Квалификация")
    years = models.CharField(max_length=50, verbose_name="Годы обучения")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
        ordering = ['-years']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пациента")
    condition = models.CharField(max_length=100, verbose_name="Диагноз/Проблема")
    content = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(
        default=5, 
        choices=[(i, i) for i in range(1, 6)],
        verbose_name="Рейтинг"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
    
class PatientReview(models.Model):
    RATING_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Имя пациента")
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name="Оценка")
    review_text = models.TextField(verbose_name="Текст отзыва")
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв пациента"
        verbose_name_plural = "Отзывы пациентов"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"    