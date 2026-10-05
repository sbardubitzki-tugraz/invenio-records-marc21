# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2026 Graz University of Technology.
#
# Invenio-Records-Marc21 is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Jobs."""

from invenio_jobs.jobs import JobType, PredefinedArgsSchema

from .tasks import validate_marc21_dois

class Marc21PredefinedArgsSchema(PredefinedArgsSchema):
    """Marc21 Predefined Args Schema."""
    # to be completed
    pass

class ValidateMarc21DOIsJob(JobType):
    """Validate DOIs in Marc 21 records."""
    
    id = "validate_marc21_dois"
    title = "Validate DOIs (Publications)"
    description = "Validate DOIs of publication records."

    task = validate_marc21_dois

    arguments_schema = Marc21PredefinedArgsSchema