from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.utils.text import slugify
# Create your models here.

class Units(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Слаг')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:unit_detail',args=[self.slug])
    class Meta:
        verbose_name_plural='Структура'
        verbose_name='Структура'
class Block(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название блока')
    units=models.ForeignKey(Units,on_delete=models.CASCADE,verbose_name='Структура')

    slug=models.SlugField(max_length=255,verbose_name='Слаг')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Блок '
        verbose_name_plural='Блок'
class Position(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название должность')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Должность'
        verbose_name_plural='Должность'
class City(models.Model):

    name=models.CharField(max_length=255,verbose_name='Название города')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Город'
        verbose_name_plural='Город'
class Departaments(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Слаг')
    block=models.ForeignKey(Block,on_delete=models.CASCADE,verbose_name='Блок')
    units=models.ForeignKey(Units,on_delete=models.CASCADE,verbose_name='Структура')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:departament_detail',args=[self.slug])
    class Meta:
        verbose_name='Подразделеия'
        verbose_name_plural='Подразделеия'

class Departament_block(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    deps = models.ForeignKey(Departaments, on_delete=models.CASCADE, verbose_name='Подразделение')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:departament_block_detail',args=[self.slug])
    class Meta:
        verbose_name='Отделы подразделение'
        verbose_name_plural='Отделы подразделение'

class Workers(models.Model):
    firstname=models.CharField(max_length=255,verbose_name='Фамилия')
    secondname=models.CharField(max_length=255,verbose_name='Имя')
    lastname=models.CharField(max_length=255,verbose_name='Отчество')

    slug=models.SlugField(max_length=255,verbose_name='Слаг')
    deps=models.ForeignKey(Departaments,on_delete=models.CASCADE,verbose_name='Подразделение',blank=True,null=True)
    deps_block=models.ForeignKey(Departament_block,on_delete=models.CASCADE,verbose_name='Отделы подразделение',blank=True,null=True)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,related_name='position_workers',verbose_name='Должность')
    room=models.CharField(max_length=4,verbose_name='Кабинет')
    ip_number=models.CharField(max_length=16,verbose_name='Ip адрес')
    city=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='Город',related_name='city_workers')
    mobile_phone=models.CharField(max_length=12,verbose_name='Телефонный номер')
    def __str__(self):
        return '{} {} {}'.format(self.firstname,self.secondname,self.lastname)
    def full_name(self):
        return '{} {} {}'.format(self.firstname,self.secondname,self.lastname)
    class Meta:
        verbose_name='Сотрудники'
        verbose_name_plural='Сотрудники'