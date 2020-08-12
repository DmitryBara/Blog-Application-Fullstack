from django import forms
from .models import Article
from django.core.files.images import get_image_dimensions


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'image', 'hiden')


    def __init__(self, *args, **kwargs):
        # Need article_id for check in clean_title
        self.article_id = kwargs.pop('article_id', None)
        super(ArticleForm, self).__init__(*args, **kwargs)


    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea, min_length=15)
    image = forms.ImageField()
    hiden = forms.BooleanField(required=False)

    #Set Attributes
    title.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название статьи', 'autocomplete': 'off'})	
    text.widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст статьи'})
    image.widget.attrs.update({'class': 'input-file', 'name': 'inpFile', 'id': 'inpFile'})

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        try:
            article = Article.objects.get(title=title)
            if self.article_id != article.id:
                raise forms.ValidationError('Статья с таким названием уже существует')
        except Article.DoesNotExist:
            pass
        return title

    
    def clean_text(self):
        text = self.cleaned_data.get('text')
        return text


    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('Изображение не загружено')
        else:
            w, h = get_image_dimensions(image)
            if w<200 or h<200:
                raise forms.ValidationError('Минимальное разрешение изображения 200x200')
            if image.size > 5242880:
                raise forms.ValidationError('Максимальный допустимый рамер фаила 5 MB')
        return image







    #Need 2 methods because my default save() method has been changed.
    #It was possible to do another. Check my answer on:
    #https://stackoverflow.com/questions/39399547/django-form-creates-new-instance-instead-updating-a-existing-one
    # def save(self, *args, **kwargs):
    #     new_article = Article.objects.create(
    #         	title=self.cleaned_data['title'],
    #         	text=self.cleaned_data['text'],
    #         	image=self.cleaned_data['image'],
    #         	# author_id=author_id
    #         )
    #     return new_article

    # def update(self, article_id, *args, **kwargs):
    #     old_article = Article.objects.get(id=article_id)
    #     # super(ArticleForm, self).save(*args, **kwargs)
        
    #     old_article.hiden = self._hiden
    #     old_article.save()
        
    #     return old_article


        

