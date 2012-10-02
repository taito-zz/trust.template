from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest


class TrustTemplateLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        # Setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')

        # Load ZCML
        import trust.template
        self.loadZCML(package=trust.template)

    def setUpPloneSite(self, portal):
        """Set up Plone."""

        # Setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')

        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'trust.template:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'Products.PythonScripts')


FIXTURE = TrustTemplateLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="TrustTemplateLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="TrustTemplateLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
