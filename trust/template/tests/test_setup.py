from trust.template.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_trust_template_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('trust.template'))

    def test_browserlayer(self):
        from trust.template.browser.interfaces import ITrustTemplateLayer
        from plone.browserlayer import utils
        self.failUnless(ITrustTemplateLayer in utils.registered_layers())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-trust.template:default'), u'0')

    def test_setuphandlers__remove_front_page(self):
        self.assertIsNone(self.portal.get('front-page'))

    def test_setuphanders__set_enable_user_folders(self):
        from plone.app.controlpanel.security import ISecuritySchema
        self.assertTrue(ISecuritySchema(self.portal).get_enable_user_folders())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.template'])
        self.failIf(installer.isProductInstalled('trust.template'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.template'])
        from trust.template.browser.interfaces import ITrustTemplateLayer
        from plone.browserlayer import utils
        self.failIf(ITrustTemplateLayer in utils.registered_layers())
