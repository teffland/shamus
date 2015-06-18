from django.db import models

class MenuCategory(models.Model):
    """ A Category of menu items, eg Salads/Soups, Entrees, etc."""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a menu category, eg. Appetizers, Salads, or Sandwiches"
                            )
    description = models.TextField(blank=True,
                                   help_text="The description to be displayed on the menu"
                                   )
    # how the items are to be displayed on the menu
    #display_type = models
    order_affinity = models.PositiveSmallIntegerField(default=5,
                                                      help_text="Please specify how far down the menu it should be rendered, starting at 1"
                                                      )
    # this displays as string on site
    def __unicode__(self):
        return "%s : %s" % (self.name, self.description)


class MenuType(models.Model):
    """ Seperate Menus, eg lunch, Dinner"""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a menu type, eg. Lunch, Dinner"
                            )
    description = models.TextField(blank=True,
                                   help_text="The description to be displayed when scrolling over the menu"
                                   )
    start_time = models.TimeField(blank=False,
                                  help_text="What time the menu is available to be served")
    end_time = models.TimeField(blank=False,
                                help_text="What time the the menu is no longer served")

    def __unicode__(self):
        return "%s : %s" % (self.name, self.description)

class MenuItem(models.Model):
    """ An item on a menu"""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a menu item, eg. Lobster Bisque"
                            )
    description = models.TextField(blank=True,
                                   help_text="The description to be displayed when scrolling over the item"
                                   )
    price = models.DecimalField(blank=False,
                                max_digits=6,
                                decimal_places=2,
                                help_text="How much the item costs")
    image = models.ImageField(blank=True,
                              height_field="height",
                              width_field="width",
                              help_text="Please upload an image of the dish")
    menu_types = models.ManyToManyField('MenuType')
    menu_category = models.ForeignKey('MenuCategory')

    def __unicode__(self):
        return "%s : %s" % (self.name, self.description)

class SliderImage(models.Model):
    """ Images for the front page slider, all images not associated with a MenuItem"""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a image"
                            )
    caption = models.TextField(blank=True,
                               help_text="The caption to be displayed overlaying the image"
                               )
    image = models.ImageField(blank=False,
                              height_field="height",
                              width_field="width",
                              help_text="An image to be displayed in the slider"
                              )
    link = models.URLField(blank=True,
                           help_text="Please provide a link to the part of the site the image is representing"
                           )
    order_affinity = models.PositiveSmallIntegerField(default=5,
                                                      help_text="Please specify how far the down the slider it should be rendered, starting at 1"
                                                      )

    def __unicode__(self):
        return "%s : %s" % (self.name, self.caption)

class StaticPage(models.Model):
    """ Plain pages that should be editable from admin"""
    title = models.CharField(max_length=50,
                             blank=False,
                             help_text="The title to appear at the top of the page"
                             )
    content = models.TextField(blank=True,
                               help_text="The page content you wish to display"
                               )
    url = models.CharField(max_length=50,
                           primary_key=True,
                           blank=False,
                           help_text="The url to be matched.  Eg. 'about-us/'.  Be sure to include the trailing / "
                           )
    template = models.CharField(max_length=50,
                                null=False,
                                default='staticpage.html',
                                help_text='If using a different template, you can override it with this'
                                )

    def __unicode__(self):
        return "%s : %s" % (self.title, self.url)