from django.shortcuts import render
from django.core.mail import send_mail


def homepage(requset):
	return render(requset, 'homepage.html' , {})

def contact(requset):
	if requset.method == 'POST':
		namename = requset.POST['namename']
		emailemail= requset.POST['emailemail']
		message = requset.POST['message']

		send_mail(
			namename ,
			message ,
			emailemail ,
			['abbbas.mirzaei@gmail.com'],
			fail_silently = False ,

			)

		return render(requset, 'contact.html' , {'namename' : namename ,'message':message}  )
			
	else :
		return render(requset, 'contact.html' , {})

def catagory(requset):
	return render(requset, 'catagory.html' , {})

def single(requset):
	return render(requset, 'single-post.html' , {})

def video(requset):
	return render(requset, 'video-post.html' , {})
