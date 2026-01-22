from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    template = "home/home_page.html"

    subpage_types = ["home.ContentPage", "home.ActivitiesPage"]


class ContentPage(Page):
    template = "home/content_page.html"
    body = RichTextField(blank=True)
    intro = RichTextField(blank=True)

    parent_page_types = ['home.HomePage']

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        FieldPanel("body", classname="full"),
    ]

class ActivitiesPage(Page):
    template = "home/activities_page.html"

    intro = RichTextField(blank=True)

    parent_page_types = ['home.HomePage']

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]
