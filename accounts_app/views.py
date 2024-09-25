from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



# registraion 
def fun_register(request):
	if request.method=="POST":
		var_username=request.POST['reg_username'] 
		var_email=request.POST['reg_email']
		var_password=request.POST['reg_password']
		var_confirm_password=request.POST['reg_confirm_password']

		if var_password==var_confirm_password:
			if  User.objects.filter(username="var_username").exists():
				print("Username already exits")
				return redirect('go_register')
			else:
				user = User.objects.create_user(username=var_username, email=var_email, password=var_password)
				user.save() #send the data to the database: table:user
				return redirect('go_login')
		else:
			print("Passwords does not match")
			return redirect('go_register')
	else:
		return render(request,'accounts/register.html',{'template':"REGISTER"})

# login
def fun_login(request):
	if request.method=="POST":
		var_username=request.POST["login_username"]
		var_password=request.POST["login_password"]
		user=auth.authenticate(username=var_username, password=var_password)

		if User is not None:
			auth.login(request,user)
			print('Login Successful')
			return redirect ('home')
		else:
			print("Invalid Credentials")
			return redirect('login')
	else:
		return render(request,'accounts/login.html',{'template':"LOGIN"})


#logout
def fun_logout(request):
	if request.method == 'POST':
		auth.logout(request)
		print("Logout from website")
		return redirect('go_login')

