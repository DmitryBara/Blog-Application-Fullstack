from django import forms
from django.core.files.images import get_image_dimensions
from .models import Article



class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'image', 'hiden')


    def __init__(self, *args, **kwargs):
        # Need article_id for check in clean_title, clean_image
        # self,atticle_id is only on existing article
        self.article_id = kwargs.pop('article_id', None)
        super(ArticleForm, self).__init__(*args, **kwargs)


    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea, min_length=15)
    image = forms.ImageField()
    hiden = forms.BooleanField(required=False)


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
        if not self.article_id:
            w, h = get_image_dimensions(image)
            if w<200 or h<200:
                raise forms.ValidationError('Минимальное разрешение изображения 200x200')
            if image.size > 5242880:
                raise forms.ValidationError('Максимальный допустимый рамер фаила 5 MB')
        return image


        

