from plone.app.controlpanel.security import ISecuritySchema

import logging


logger = logging.getLogger(__name__)


def remove_front_page(context):
    portal = context.getSite()
    portal.manage_delObjects(['front-page'])


def setupVarious(context):

    if context.readDataFile('trust.template_various.txt') is None:
        return

    remove_front_page(context)
    ISecuritySchema(context.getSite()).set_enable_user_folders(True)
