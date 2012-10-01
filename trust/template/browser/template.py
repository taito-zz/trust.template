from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from five import grok
from plone.app.layout.globals.interfaces import IViewView
from trust.template.browser.interfaces import ITrustTemplateLayer
from zope.component import getMultiAdapter


grok.templatedir('templates')


class PloneSiteRootView(grok.View):
    """View for Plone Site Root"""
    grok.context(IPloneSiteRoot)
    grok.layer(ITrustTemplateLayer)
    grok.name('trust-view')
    grok.require('zope2.View')
    grok.template('plone-site-root')
    grok.view(IViewView)

    def update(self):
        plone_portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')
        if plone_portal_state.anonymous():
            url = '{}/login_form'.format(plone_portal_state.portal_url())
            self.request.response.redirect(url)
        else:
            self.template
