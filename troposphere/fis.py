# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.1.0


from . import AWSObject, AWSProperty


class ExperimentTemplateStopCondition(AWSProperty):
    props = {
        "source": (str, True),
        "value": (str, False),
    }


class ExperimentTemplate(AWSObject):
    resource_type = "AWS::FIS::ExperimentTemplate"

    props = {
        "actions": (dict, False),
        "description": (str, True),
        "roleArn": (str, True),
        "stopConditions": ([ExperimentTemplateStopCondition], True),
        "tags": (dict, True),
        "targets": (dict, True),
    }