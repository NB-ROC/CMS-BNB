from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from datetime import date
from modelcluster.models import ParentalKey

class BlogIndexPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("description")]

class BlogPostPage(Page):
    date = models.DateField("Post date", default=date.today)
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("date"),
                                            FieldPanel("intro"),
                                            FieldPanel("body"),
                                            InlinePanel("gallery_images", label="Gallery images")]


class BlogPageImageGallery(Orderable):
    page = ParentalKey(BlogPostPage, related_name="gallery_images",
                       on_delete=models.CASCADE)
    image = models.ForeignKey("wagtailimages.Image",
                              on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(max_length=255, blank=True)
    panels = [FieldPanel("image"), FieldPanel("caption")]

