# -*- coding:utf-8 -*-
from interlegis.portalmodelo.policy.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile
from plone import api

import logging

PROFILE_ID = 'interlegis.portalmodelo.policy:default'

def apply_configurations(context):
    """Atualiza perfil para versao 4."""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-interlegis.portalmodelo.policy.upgrades.v4:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 4')


