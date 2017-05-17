from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
	return render(request,'home.html')


def homepage(request):
	return render(request,'home1.html')

def createorders(request):
	if request.method == 'POST':
		form = request.POST
		name = form["name"]
		phone = form['phone']
		number = form['number']
		state = StateMaster.objects.get(name = form['state'])
		city = CityMaster.objects.get(name = form['city'])
		address = form['full_address']
		pincode = form['pincode']
		latestUserId = CreateOrder.objects.latest('id').id
		par = "PAR" + str(1000000+latestUserId+1)

		orders = CreateOrder.objects.get_or_create(
			username = par,
			name = name,
			mobile = phone,
			no_of_cloths = number,
			state = state,
			city = city,
			house_no = address,
			pin_code = pincode,

			)
		return redirect('/orderplaced/')

	else:
		return redirect('/home/')

def orderplaced(request):
	objec = CreateOrder.objects.latest('id').username
	return render(request,'complete1.html',{'objec':objec})

def aboutus(request):
	return render(request,'about.html')

def front(request):
	return render(request,'front.html')

def register(request):
	return render(request,'register.html')

def trackorder(request):

	# objects = CreateOrder.objects.all()
	if request.method == 'POST':
		form = request.POST

		orderObject = CreateOrder.objects.get(name = form['trackid'])

		return render(request,'home.html',{'orderObject':orderObject})

	else:
		return redirect('/home/')
def explore(request):
	return render(request,'explore.html')
	

