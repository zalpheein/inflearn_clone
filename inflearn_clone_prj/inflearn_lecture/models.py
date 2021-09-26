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


    def __str__(self):
        return self.title
    
    def publish(self):
        self.save()
