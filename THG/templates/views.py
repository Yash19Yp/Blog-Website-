from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Exam, BlogComment, Contact
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from THG.templatetags import extras
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# For Password generator tool we use this below modules random, string and re
import random
import string
import re
# ListView = List of all posts
# DetailView = Detail inside the post

# List category wise posts
def technology_posts(request):
    allTechPosts = Post.objects.filter(category="Technology")
    params = {'allPosts': allTechPosts, 'post_category':'Technology'}
    return render(request, "category_post/category_wise_post.html", params)

def design_posts(request):
    allDesignPosts = Post.objects.filter(category="Design")
    params = {'allPosts': allDesignPosts, 'post_category':'Design'}
    return render(request, "category_post/category_wise_post.html", params)

def database_posts(request):
    allDatabasePosts = Post.objects.filter(category="Database")
    params = {'allPosts': allDatabasePosts, 'post_category':'Database'}
    return render(request, "category_post/category_wise_post.html", params)

def security_posts(request):
    allSecurityPosts = Post.objects.filter(category="Security")
    params = {'allPosts': allSecurityPosts, 'post_category':'Security'}
    return render(request, "category_post/category_wise_post.html", params)

def hacking_posts(request):
    allHackingPosts = Post.objects.filter(category="Hacking")
    params = {'allPosts': allHackingPosts, 'post_category':'Hacking'}
    return render(request, "category_post/category_wise_post.html", params)

def cybersecurity_posts(request):
    allCybersecPosts = Post.objects.filter(category="Cyber Security")
    params = {'allPosts': allCybersecPosts, 'post_category':'Cyber Security'}
    return render(request, "category_post/category_wise_post.html", params)

def contact(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact(name=name, email=email, phone=phone, desc=desc).save()
        messages.success(request, "Thank you for your response. We will be in touch with you as soon as possible.")
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/")
                messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset/password_reset.html", context={"password_reset_form":password_reset_form})

def grammer_checking(request):
    return render(request, 'grammer_checking.html')
def grammer_check(request):
    from gingerit.gingerit import GingerIt
    import streamlit as st
    GrammerChecking = request.POST.get('GrammerChecking','off')
    text = request.POST.get('text','default')
    if GrammerChecking=='on':
        parser = GingerIt()
        if text == '':
            st.write("Please enter text for checking")
        else:
            result_dict = parser.parse(text)
            res = st.markdown('**Corrected Sentence - **'+ str(result_dict['result']))
            params = {'result':res}
    else:
        pass
    return render(request, 'grammer.html', params)


def textutils(request):
    return render(request, 'textutils_tool.html')

def analyze_text(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    purpose = ''

    if(removepunc=="on"):
        purpose = 'Remove Punctuations'
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps=="on"):
        purpose = purpose + ' + Change To Uppercase'
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(newlineremover == "on"):
        purpose = purpose + ' + New Line Remover'
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(extraspaceremover == "on"):
        purpose = purpose + ' + Extra Space Remover'
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzed_text.html', params)
    
    if(charactercounter == "on"):
        purpose = purpose + ' + Character Counter'
        count = 0
        analyzed = 0
        for char in djtext:
            count = count + 1
        analyzed = count
        params = {'purpose': purpose, 'analyzed_text':f'Total Characters in your content: {analyzed}', 'djtext':djtext}
        djtext=analyzed
    
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charactercounter!='on'):
        return HttpResponse("For utilizing the text you have to on button.")
    
    return render(request, 'analyzed_text.html', params)

def password_generate(request):
    return render(request, 'password_generator_tool.html')

def password_generator(request):
    password_len = request.POST.get('pwdlen', 'default')
    try:
        password_len = int(password_len)
        if password_len<1:
            return HttpResponse("<center><h2 style='color:red;margin-top:5%;'>Please enter the length greater than 0!!</h2></center>")
    except:
        return HttpResponse("<center><h2 style='color:red;margin-top:5%;'>Error! You didn't enter the number. Please Enter the number!!</h2></center>")
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    print(s4)
    s = []

    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    special_characters=request.POST.get('special_characters','off')
    digit=request.POST.get('digit','off')

    if uppercase=='on':
        s.extend(list(s2))
    if lowercase=='on':
        s.extend(list(s1))
    if special_characters=='on':
        s.extend(list(s4))
    if digit=='on':
        s.extend(list(s3))
    random.shuffle(s)
    password = "".join(s[0:password_len])

    lower, upper, dgts, spec_char = 0, 0, 0, 0
    for pwd in password:
        if pwd in s1:
            lower+=1
        if pwd in s2:
            upper+=1
        if pwd in s3:
            dgts+=1
        if pwd in s4:
            spec_char+=1
        else:
            continue
    chrs = f"\nYour Password Length is: {len(password)}\n\nTotal Lowercase Characters: {lower}\nTotal Uppercase Characters: {upper}\nTotal digits: {dgts}\nTotal Special Symbols: {spec_char}\n"


    risks=''
    risks = risks + chrs
    lowerreg = re.compile(r'[a-z]')
    upperreg = re.compile(r'[A-Z]')
    digreg = re.compile(r'[\d]')
    ptrn = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    speccharreg = re.compile(r"[\W]")

    lwr = lowerreg.search(password)
    upr = upperreg.search(password)
    dgtt = digreg.search(password)
    specs = speccharreg.search(password)
    print(upr, dgtt, specs)
    if len(password)<6:
        risks = risks + 'Your password length is too small: ' + str(len(password)) + '\n'
    
    if lwr and upr==None and dgtt==None and specs==None:
        if len(password)<8:
            risks = risks + '\nYour password contain Lower case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Weak'
        elif len(password)>8 and len(password)<15:
            print(password)
            risks = risks + '\nYour password contain Lower case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Average'
        else:
            risks = risks + '\nYour password contain Lower case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Good'

    elif upr and lwr==None and dgtt==None and specs==None:
        if len(password)<8:
            risks = risks + '\nYour password contain Upper case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Weak'
        elif len(password)>8 and len(password)<15:
            risks = risks + '\nYour password contain Upper case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Average'
        else:
            risks = risks + '\nYour password contain Upper case letters only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Good'

    elif dgtt and upr==None and lwr==None and specs==None:
        
        if len(password)<8:
            risks = risks + '\nYour password contain Digits only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Weak'
        elif len(password)>8 and len(password)<15:
            risks = risks + '\nYour password contain Digits only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Average'
        else:
            risks = risks + '\nYour password contain Digits only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Good'

    elif specs and upr==None and dgtt==None and lwr==None:
        if len(password)<8:
            risks = risks + '\nYour password contain Special Symbols only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Weak'
        elif len(password)>8 and len(password)<15:
            risks = risks + '\nYour password contain Special Symbols only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Average'
        else:
            risks = risks + '\nYour password contain Special Symbols only. \nFor Increasing strength of Password please select two or more options\nPassword Strength : Good'
    
    elif(lowerreg.search(password) and upperreg.search(password) and digreg.search(password) and speccharreg.search(password)):
        if len(password)<8:
            risks = risks + '\nYour password contain Lowercase, Uppercase, Digits, and Special Symbols all. You have to increase your password length\nPassword Strength : Average'
        elif len(password)>8 and len(password)<14:
            risks = risks + '\nYour password contain Lowercase, Uppercase, Digits, and Special Symbols all.\nPassword Strength : Strong'
        else:
            risks = risks + '\nYour password contain Lowercase, Uppercase, Digits, and Special Symbols all.\nPassword Strength : Hacker will be Confuse! Very Strong'
    else:
        if len(password)>10 and len(password)<25:
            risks = risks + '\nYour Password strength is : GOOD'
        elif len(password)>=25 and len(password)<=30:
            risks = risks + '\nYour Password Strength is : Very Good!'
        elif len(password)>30:
            risks = risks + '\nYour Password Strength is : Excellent!'
    
    print(risks)
    params = {'password':password, 'risks':risks}
    return render(request, 'password.html', params)

def binary_text_converter(request):
    return render(request, 'binary_text_converter.html')

def converting_text_binary(request):
    text = request.POST.get("text")
    recieve_T_B = request.POST.get("select","")
    if recieve_T_B == "binary_to_text":
        ptrn = '(2|3|4|5|6|7|8|9|[a-z]|[A-Z]|\W)+'
        mtch = re.search(ptrn, text)
        if mtch:
            return HttpResponse("<center><h2 style='color:red;margin-top:3%;'>Hey! Don't try to be start. Enters only 0 or 1 if you want to convert binary to text.</center>")
        else:
            
            if " " in text:
                ptrn1 = re.compile(r'\s+')
                text = re.sub(ptrn1, '', text)
            def BinaryToDecimal(binary):
                binary1 = binary
                decimal, i, n = 0, 0, 0
                while(binary != 0):
                    dec = binary % 10
                    decimal = decimal + dec * pow(2, i)
                    binary = binary//10
                    i += 1
                return (decimal)
            str_data =' '
            for i in range(0, len(text), 8):
                temp_data = int(text[i:i + 8])
                decimal_data = BinaryToDecimal(temp_data)
                str_data = str_data + chr(decimal_data)
            params = {'purpose':'Binary To Text:','converted_data' : str_data}
            return render(request, 'converted_data_t_b.html', params)
     
    elif recieve_T_B == "text_to_binary": 
        res = ' '.join(format(ord(i), '08b') for i in text)
        params = {'purpose':'Text To Binary:','converted_data' : res}
        return render(request, 'converted_data_t_b.html', params)
    
    elif recieve_T_B == '-':
        return HttpResponse(request, "You didn't selected the method!!")

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for erroneous inputs
        if len(username) > 22:
            messages.error(request, "Username must be under 22 characters")
            return redirect("home")
        if not username.isalnum():
            messages.warning(request, "Only contains letters and numbers")
            return redirect("home")
        if pass1 != pass2:
            messages.warning(request, "password don't match")
            return redirect("home")


        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Tech Hack Gyan (THG) account has been successfully created :)")
        return redirect('/')

    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("/")

    return HttpResponse("404 - Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/")

def search(request):
    query = request.GET['query']
    if query == "":
        messages.warning(request, "For finding stuff please enter query")
        return redirect('/')
    if len(query)>80:
        allPosts = Post.objects.none()
    else:
        # allPosts = Post.objects.all()
        allPosts= Post.objects.filter( Q(title__icontains=query) | Q(content__icontains=query))
        # allPostsContent = Post.objects.filter(content__icontains=query)
        # allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'search.html', params)

def tech_quiz(request):
    techQuiz = Exam.objects.filter(category="Technology")
    params = {'exam':techQuiz, 'quiz_category': 'Technology Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def design_quiz(request):
    designQuiz = Exam.objects.filter(category="Design")
    params = {'exam': designQuiz, 'quiz_category': 'Design Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def db_quiz(request):
    dbQuiz = Exam.objects.filter(category="Database")
    params = {'exam':dbQuiz, 'quiz_category': 'Database Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def security_quiz(request):
    securityQuiz = Exam.objects.filter(category="Security")
    params = {'exam':securityQuiz, 'quiz_category': 'Security Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def hacking_quiz(request):
    hackingQuiz = Exam.objects.filter(category="Hacking")
    params = {'exam':hackingQuiz, 'quiz_category': 'Hacking Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def cybersecurity_quiz(request):
    cybersecurityQuiz = Exam.objects.filter(category="Cyber Security")
    params = {'exam':cybersecurityQuiz, 'quiz_category': 'Cyber Security Quiz'}
    return render(request, 'category_quiz/quiz.html', params)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(title=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/{post.slug}")

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

def PostDetailView(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'post_detail.html', context)   