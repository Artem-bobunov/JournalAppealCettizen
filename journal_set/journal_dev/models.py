from django.db import models

class Signature(models.Model):
    numberInput = models.IntegerField('Номер Входящий',null=True,blank=True)
    user = models.CharField('Подпись пользователя',blank=True,null=True,max_length=2000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)
# Create your models here.
class journal(models.Model):
    signature = models.ForeignKey(Signature,on_delete=models.CASCADE,null=True, blank=True)

    npp = models.IntegerField('№ п/п', null=True,blank=True,max_length=10000)
    dateInput = models.DateField('Дата поступления заявления', null=True,blank=True)
    content = models.CharField('Краткое содержание заявления', null=True,blank=True,max_length=10000)
    executor = models.CharField('ФИО исполнителя',null=True,blank=True,max_length=10000)
    datePeredachi = models.DateField('Дата передачи исполнителю', null=True,blank=True)
    controlPeriod = models.DateField('Контрольный срок', null=True,blank=True)
    painting = models.CharField('Роспись исполнителя',null=True,blank=True,max_length=10000)
    mark = models.CharField('Отметка об исполнении',null=True,blank=True,max_length=10000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)
