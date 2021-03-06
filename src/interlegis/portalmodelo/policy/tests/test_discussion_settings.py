# -*- coding: utf-8 -*-
from interlegis.portalmodelo.policy.testing import INTEGRATION_TESTING
from plone.app.discussion.interfaces import IDiscussionSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class DiscussionTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_configuration(self):
        settings = getUtility(IRegistry).forInterface(IDiscussionSettings)
        self.assertTrue(settings.anonymous_comments)
        self.assertTrue(settings.anonymous_email_enabled)
        self.assertFalse(settings.moderation_enabled)
        self.assertEqual(settings.captcha, u'recaptcha')
        self.assertTrue(settings.globally_enabled)
        self.assertTrue(settings.show_commenter_image)
        self.assertTrue(settings.user_notification_enabled)
        self.assertEqual(settings.text_transform, u'text/x-web-intelligent')

    def test_news_items_have_discussion_enabled(self):
        news_item = self.portal['portal_types']['News Item']
        self.assertTrue(news_item.allow_discussion)
