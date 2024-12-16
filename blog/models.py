from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class blogpost(models.Model):
	
	title = models.CharField(max_length = 300)
	blog_post_content = RichTextField()

	url = models.SlugField(null=True,blank=True)


	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		self.url = slugify(self.title)

		super(blogpost, self).save(*args, **kwargs)