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
    menu_types = models.ManyToManyField('MenuType')

    def items(self):
        return self.menuitem_set.all()

    # this displays as string on site
    def __unicode__(self):
        parent_menus = ', '.join([menu.name for menu in self.menu_types.all()])
        return "%s (in %s)" % (self.name, parent_menus)


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
                                  help_text="What time the menu is available to be served. Format: 1 pm is 13:00:00")
    end_time = models.TimeField(blank=False,
                                help_text="What time the the menu is no longer served. Format: 1 pm is 13:00:00")

    def categories(self):
        """ Get the MenuItems that have this MenuType """
        return self.menucategory_set.all().order_by('order_affinity')

    def __unicode__(self):
      if self.description: return "%s : %s" % (self.name, self.description)
      else: return self.name
        

class ItemOption(models.Model):
    """Description and Price option for a MenuItem.
    * Allows one Item to have multiple options with individual pricing

    eg.  Build-it Burger             
            Plain                         7
            Cheese                        8
                Swiss, Cheddar, or Jack
            Add Bacon                     +1
            Add Avocado                   +1  

    Could be made of a Burger MenuItem, and 5 Options that have
    the burger as their parent item """
    description = models.CharField(max_length=255,
                                   blank=True,
                                   help_text="The description text"
                                   )

    price = models.DecimalField(blank=True,
                                null=True,
                                max_digits=6,
                                decimal_places=2,
                                help_text="How much the item costs"
                                )
    price_prefix = models.CharField(max_length=10,
                                    blank=True,
                                    help_text="Text to be displayed after price"
                                   )
    parent_item = models.ForeignKey('MenuItem')

    def __unicode__(self): 
      if self.price: return "%s - %s" % (self.description, self.price)
      else: return self.description

class MenuItem(models.Model):
    """ An item on a menu"""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a menu item, eg. Lobster Bisque"
                            )
    
    price = models.DecimalField(blank=True,
                                null=True,
                                max_digits=6,
                                decimal_places=2,
                                help_text="How much the item costs"
                                )
    price_prefix  = models.CharField(max_length=10,
                                    blank=True,
                                    help_text="Text to be displayed after price"
                                    )

    image = models.ImageField(blank=True,
                              height_field="height",
                              width_field="width",
                              help_text="Please upload an image of the dish"
                              )

    menu_category = models.ManyToManyField('MenuCategory')

    published = models.BooleanField(default=True)

    def options(self):
        """ Get all of the options associated with this item """
        return self.itemoption_set.all()

    def __unicode__(self):
       # = ', '.join(self.options()
      # if self.options(): return "%s ,%f : %s" % (self.name, self.price, self.options())
      # else: return "%s , $%d" % (self.name, self.price)
      print "P: ",self.price
      categories = ", ".join([ unicode(cat) for cat in self.menu_category.all()])
      if self.price: return "%s, $%d : %s" % (self.name, self.price, categories)
      else: return "%s : %s" % (self.name, categories)


class SliderImage(models.Model):
    """ Images for the front page slider, all images not associated with a MenuItem"""
    name = models.CharField(max_length=50,
                            blank=False,
                            help_text="The name of a image"
                            )
    caption = models.TextField(blank=True,
                               help_text="The caption to be displayed overlaying the image"
                               )
    width = models.IntegerField(default=1024,
                                help_text="Suggested keep 16:9 aspect ratio for width:height")
    height = models.IntegerField(default=576,
                                 help_text="Ideally, height is 9/16(width) naturally; it will be stretched to this ratio automatically")

    image = models.ImageField(blank=False,
                              help_text="An image to be displayed in the slider",
                              width_field='width',
                              height_field='height',
                              upload_to="image-slider"
                              )
    link = models.URLField(blank=True,
                           help_text="Please provide a link to the part of the site the image is representing"
                           )
    order_affinity = models.PositiveSmallIntegerField(default=5,
                                                      help_text="Please specify how far the down the slider it should be rendered, starting at 1"
                                                      )

    published = models.BooleanField(default=True)

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

class FrontPageBlurb(models.Model):
    """ Featurette Blurbs for the front page"""
    heading = models.CharField(max_length=50,
                             blank=False,
                             help_text="The title to appear at the top of the blurb"
                             )
    comment = models.CharField(max_length=50,
                             blank=True,
                             help_text="An afterthought to appear next to the heading at the top of the blurb"
                             )
    content = models.TextField(blank=True,
                               help_text="The main content of the blurb"
                               )
    width = models.IntegerField(default=500,
                                help_text="You don't need to change this (it adjusts automatically)")
    height = models.IntegerField(default=500,
                                 help_text="You don't need to change this (it adjusts automatically)")
    image = models.ImageField(blank=False,
                              help_text="An image to be displayed in the featurette",
                              width_field='width',
                              height_field='height',
                              upload_to="featurette-images"
                              )
    published = models.BooleanField(default=True)
    order_affinity = models.PositiveSmallIntegerField(default=5,
                                                      help_text="Please specify how far the down the page it should be rendered, starting at 1"
                                                      )

    def __unicode__(self):
        return "%s %s" % (self.heading, self.comment)