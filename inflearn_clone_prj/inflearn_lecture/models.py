from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class myText(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    #board_text = RichTextField(null=True)
    board_text = RichTextUploadingField(null=True)

    category = models.CharField(max_length=200, null=True)


    lecture_title1 = models.CharField(max_length=200, null=True)
    lecture_video1 = models.CharField(max_length=800, null=True)
    lecture_title2 = models.CharField(max_length=200, null=True)
    lecture_video2 = models.CharField(max_length=800, null=True)
    lecture_title3 = models.CharField(max_length=200, null=True)
    lecture_video3 = models.CharField(max_length=800, null=True)
    lecture_title4 = models.CharField(max_length=200, null=True)
    lecture_video4 = models.CharField(max_length=800, null=True)



    def __str__(self):
        return self.title
    
    def publish(self):
        self.save()


class Comment(models.Model):

    lecture = models.ForeignKey(myText, on_delete=models.CASCADE)
    rate = models.CharField(max_length=200, null=True)
    writer = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    def publish(self):
        self.save()