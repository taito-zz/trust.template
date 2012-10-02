from Products.CMFCore.utils import getToolByName
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
        plone_portal_state = getMultiAdapter((self.context, self.request),
            name='plone_portal_state')
        membership = getToolByName(self.context, 'portal_membership')
        if membership.isAnonymousUser():
            url = '{}/login_form'.format(plone_portal_state.portal_url())
            self.request.response.redirect(url)
        elif membership.getHomeFolder():
            self.request.response.redirect(membership.getHomeUrl())
        else:
            self.template
