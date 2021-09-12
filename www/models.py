from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from markdown import markdown

from almalinux.settings import LANGUAGES
from commons.uploads import segmented_upload_to


class Backer(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    display_name: models.CharField = models.CharField(
        max_length=100,
        null=False,
        help_text='Name of the backer'
    )

    logo: models.FileField = models.FileField(
        null=False,
        upload_to=segmented_upload_to,
        help_text='Logo of the backer. MUST be a zero-margin SVG file!',
        validators=[FileExtensionValidator(['svg'])]
    )

    url: models.URLField = models.URLField(
        null=False,
        help_text='URL of the backer'
    )

    priority: models.PositiveIntegerField = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text='Absolute priority of the backer relative to other backers. The higher the priority, the earlier '
                  'the backer will appear.'
    )

    def __str__(self) -> str:
        return self.display_name


class CommercialSupportVendor(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    display_name: models.CharField = models.CharField(
        max_length=100,
        null=False,
        help_text='Name of the vendor'
    )

    logo: models.FileField = models.FileField(
        null=False,
        upload_to=segmented_upload_to,
        help_text='Logo of the vendor. MUST be a zero-margin SVG file!',
        validators=[FileExtensionValidator(['svg'])]
    )

    url: models.URLField = models.URLField(
        null=False,
        help_text='URL of the vendor'
    )

    priority: models.PositiveIntegerField = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text='Absolute priority of the vendor relative to other vendors. The higher the priority, the earlier '
                  'the vendor will appear.'
    )

    def __str__(self) -> str:
        return self.display_name


class PressArticle(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    priority: models.PositiveIntegerField = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text='Absolute priority of the article relative to other articles. The higher the priority, the earlier '
                  'the article will appear.'
    )

    publication: models.CharField = models.CharField(
        max_length=255,
        null=False,
        help_text='Name of the publication'
    )

    excerpt: models.TextField = models.TextField(
        help_text='Excerpt or quote from the article to display in the page'
    )

    url: models.URLField = models.URLField(
        null=False,
        help_text='URL to the news article'
    )

    def __str__(self) -> str:
        return '%s [%s]' % (self.publication, self.excerpt)


# noinspection DuplicatedCode
class Page(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    published: models.BooleanField = models.BooleanField(
        default=True,
        help_text='Uncheck to make draft. Drafts are not visible to public.'
    )

    date: models.DateTimeField = models.DateTimeField(
        verbose_name='Publication date',
        help_text='Date of publication. Will be displayed to public AFTER this date.'
    )

    lang: models.CharField = models.CharField(
        max_length=7,
        choices=LANGUAGES,
        db_index=True,
        default='en',
        verbose_name='Content language'
    )

    title: models.CharField = models.CharField(
        max_length=255
    )

    slug: models.SlugField = models.SlugField(
        max_length=255,
        blank=True,
        verbose_name='Canonical title (slug)',
        help_text='Optional - leave empty to set automatically from Title.'
    )

    content_md: models.TextField = models.TextField(
        verbose_name='Content (Markdown)',
        help_text='Markdown content of the page content',
        blank=True,
    )

    content_html: models.TextField = models.TextField(
        editable=False,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:  # type: ignore
        if 0 == len(self.slug):
            # noinspection PyTypeChecker
            self.slug = slugify(self.title, allow_unicode=False)

        self.content_html = markdown(self.content_md, extensions=['extra'])

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


# noinspection DuplicatedCode
class BlogPost(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    published: models.BooleanField = models.BooleanField(
        default=True,
        help_text='Uncheck to hide'
    )

    date: models.DateTimeField = models.DateTimeField(
        help_text='Date of publication. Will be displayed to public AFTER this date.'
    )

    lang: models.CharField = models.CharField(
        max_length=7,
        choices=LANGUAGES,
        db_index=True,
        default='en',
        verbose_name='Content language'
    )

    featured_image: models.ImageField = models.ImageField(
        null=False,
        upload_to=segmented_upload_to,
        help_text='Feature image - any web-safe format',
        blank=True
    )

    title: models.CharField = models.CharField(
        max_length=255
    )

    slug: models.SlugField = models.SlugField(
        max_length=255,
        blank=True,
        verbose_name='Canonical title (slug)',
        help_text='Optional - leave empty to set automatically from Title.'
    )

    excerpt: models.TextField = models.TextField(
        help_text='An excerpt to display in the article list view of the blog index.'
    )

    content_md: models.TextField = models.TextField(
        verbose_name='Content (Markdown)',
        help_text='Markdown content of the blog entry',
        blank=True,
    )

    content_html: models.TextField = models.TextField(
        editable=False,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:  # type: ignore
        if 0 == len(self.slug):
            # noinspection PyTypeChecker
            self.slug = slugify(self.title, allow_unicode=False)

        self.content_html = markdown(self.content_md, extensions=['extra'])

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


# noinspection DuplicatedCode
class FAQEntry(models.Model):
    class Meta:
        verbose_name_plural = 'FAQ entries'

    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    lang: models.CharField = models.CharField(
        max_length=7,
        choices=LANGUAGES,
        db_index=True,
        default='en',
        verbose_name='Content language'
    )

    priority: models.PositiveIntegerField = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text='Absolute priority of the question relative to other questions in the same language. '
                  'The higher the priority, the earlier the question will appear.'
    )

    question: models.CharField = models.CharField(
        max_length=255
    )

    answer: models.TextField = models.TextField()

    def __str__(self) -> str:
        return self.question


class ShowcaseFeature(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )

    lang: models.CharField = models.CharField(
        max_length=7,
        choices=LANGUAGES,
        db_index=True,
        default='en',
        verbose_name='Content language'
    )

    title: models.CharField = models.CharField(
        max_length=255,
        null=False,
        help_text='Feature title'
    )

    description: models.TextField = models.TextField(
        null=False,
        help_text='Feature description'
    )

    screenshot: models.ImageField = models.ImageField(
        null=False,
        upload_to=segmented_upload_to,
        help_text='Feature screenshot',
    )

    priority: models.PositiveIntegerField = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text='Absolute priority of the feature relative to other features. The higher the priority, the earlier '
                  'the feature will appear.'
    )

    def __str__(self) -> str:
        return self.title
