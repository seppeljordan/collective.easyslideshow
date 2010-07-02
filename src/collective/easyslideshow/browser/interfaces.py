from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.easyslideshow')


class IEasySlideshowBrowserLayer(Interface):
    """ Browser layer marker interface
    """

class IEasyslideshowConfiguration(Interface):
    """ This interface defines the configlet for the slideshows. """

    slideshow_width = schema.Int(
        title=_(u"label_slideshow_width", default=u'Width of the Slideshow'),
        description=_(u"help_slideshow_width",
                      default=u"Enter a whole number for width in pixels. "
                      "All images should be this width."),
        required=True,
        default=500
    )

    slideshow_height = schema.Int(
        title=_(u"label_slideshow_height", default=u'Height of the Slideshow'),
        description=_(u"help_slideshow_height",
                      default=u"Enter a whole number for height in pixels. "
                      "All images should be this height."),
        required=True,
        default=333
    )

    slide_timeout = schema.Int(
        title=_(u"label_slide_timeout", default=u'Slide Time'),
        description=_(
            u"help_slide_timeout",
            default=u"Enter a number in milliseconds (5000 = 5 seconds). "
            "Entering '0' will set the slideshow to only be "
            "manually operated using the navigation."
        ),
        required=True,
        default=7000
    )

    transition = schema.Choice(
        title=_(u"label_transition", default=u'Transition'),
        description=_(u"help_transition",
                      default=u''),
        values=("blindX", "blindY", "blindZ", "cover", "curtainX", "curtainY",
                "fade", "fadeZoom", "growX", "growY", "scrollUp", "scrollDown",
                "scrollLeft", "scrollRight", "scrollHorz", "scrollVert",
                "shuffle", "slideX", "slideY", "turnUp", "turnDown",
                "turnLeft", "turnRight", "uncover", "wipe", "zoom"),
        default="fade"
    )

    transition_speed = schema.Int(
        title=_(u"label_transition_speed", default=u'Transition Time'),
        description=_(
            u"help_transition_speed",
            default=u'Enter a number in milliseconds (1000 = 1 second).'
        ),
        required=True,
        default=1000
    )

    pause_hover = schema.Bool(
        title=_(u"label_pause_hover", default=u'Pause on Hover'),
        description=_(
            u"help_pause_hover",
            default=u"If checked, the slideshow will pause when cursor "
            "is hovering over the slideshow"
        ),
        required=False,
        default=False
    )

    display_nav = schema.Bool(
        title=_(u"label_display_nav", default=u'Display Navigation'),
        description=_(u"help_display_nav",
                      default=u''),
        required=True,
        default=True
    )

    display_caption = schema.Bool(
        title=_(u"label_display_caption", default=u'Display Caption'),
        description=_(u"help_display_caption",
                      default=u''),
        required=True,
        default=True
    )

class IEasySlideshowLiteBrowserLayer(Interface):
    """ Browser layer marker interface for the lite version
    """

class IEasySlideshowView(Interface):
    """ View class for the Slideshow
    """

    def getImages(slideshowfolderid):
        """ Get the images for the slideshow based of the given ID
        """

    def getPortletImages(slideshowfolderuid):
        """ Get the images for the slideshow based of the given UID
        """
