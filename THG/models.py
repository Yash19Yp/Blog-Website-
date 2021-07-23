from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Exam(models.Model):
    category = models.CharField(max_length=50, default="")
    Question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    corrans = models.CharField(max_length=100)

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # User will point on user record.
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # If post delete comment will also delete
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # Point to comment or reply to comment.
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:20] + "..." + "by " + self.user.username

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)   # Search on google = django model field reference.
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name