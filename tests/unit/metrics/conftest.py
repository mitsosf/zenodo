# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2022 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Pytest configuration."""

import pytest
from flask import current_app

from zenodo.modules.metrics.api import ZenodoMetric


@pytest.fixture
def use_metrics_config(app):
    """Activate webhooks config."""
    old_value = current_app.config.pop('ZENODO_METRICS_DATA', None)
    current_app.config['ZENODO_METRICS_DATA'] = {
        'openaire-nexus': [
            {
                'name': 'zenodo_unique_visitors_web_total',
                'help': 'Number of unique visitors in total on Zenodo '
                        'portal',
                'type': 'gauge',
                'value': ZenodoMetric.get_visitors
            },
            {
                'name': 'zenodo_researchers_total',
                'help': 'Number of researchers registered on Zenodo',
                'type': 'gauge',
                'value': ZenodoMetric.get_researchers
            },
            {
                'name': 'zenodo_files_total',
                'help': 'Number of files hosted on Zenodo',
                'type': 'gauge',
                'value': ZenodoMetric.get_files
            },
            {
                'name': 'zenodo_communities_total',
                'help': 'Number of Zenodo communities created',
                'type': 'gauge',
                'value': ZenodoMetric.get_communities
            },
        ]
    }
    yield
    current_app.config['ZENODO_METRICS_DATA'] = old_value
