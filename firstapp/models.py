from django.db import models

# Create your models here.

class StateMaster(models.Model):
	name = models.CharField(max_length = 120)
	lastDateTimeModified = models.DateTimeField()
	lastModifiedBy = models.CharField(max_length = 120)

	class meta:
		db_table = 'statemaster'

	def __str__(self):
		return '%s  %s' %(self.id,self.name)


class CityMaster(models.Model):
	state_name = models.ForeignKey(StateMaster,null  = True, blank = True)
	name = models.CharField(max_length = 120)
	lastDateTimeModified = models.DateTimeField()
	lastModifiedBy = models.CharField(max_length = 120)

	class meta:
		db_table = 'citymaster'

	def __str__(self):
		return '%s  %s' %(self.id,self.name)


class CreateOrder(models.Model):
	username = models.CharField(max_length = 25,null = True, blank = True)
	name = models.CharField(max_length = 100)
	mobile = models.BigIntegerField(null = True, blank = True)
	no_of_cloths = models.IntegerField(null = True, blank = True)
	state = models.ForeignKey(StateMaster,null  = True, blank = True)
	city = models.ForeignKey(CityMaster,null  = True, blank = True)
	house_no = models.CharField(max_length = 250)
	pin_code = models.BigIntegerField()

	class meta:
		db_table = 'creteorder'

	def __str__(self):
		return '%s  %s' %(self.id,self.name)