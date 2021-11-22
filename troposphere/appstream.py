# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 49.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class S3Location(AWSProperty):
    props = {
        "S3Bucket": (str, True),
        "S3Key": (str, True),
    }


class ScriptDetails(AWSProperty):
    props = {
        "ExecutableParameters": (str, False),
        "ExecutablePath": (str, True),
        "ScriptS3Location": (S3Location, True),
        "TimeoutInSeconds": (integer, True),
    }


class AppBlock(AWSObject):
    resource_type = "AWS::AppStream::AppBlock"

    props = {
        "Description": (str, False),
        "DisplayName": (str, False),
        "Name": (str, True),
        "SetupScriptDetails": (ScriptDetails, True),
        "SourceS3Location": (S3Location, True),
        "Tags": ((Tags, list), False),
    }


class Application(AWSObject):
    resource_type = "AWS::AppStream::Application"

    props = {
        "AppBlockArn": (str, True),
        "AttributesToDelete": ([str], False),
        "Description": (str, False),
        "DisplayName": (str, False),
        "IconS3Location": (S3Location, True),
        "InstanceFamilies": ([str], True),
        "LaunchParameters": (str, False),
        "LaunchPath": (str, True),
        "Name": (str, True),
        "Platforms": ([str], True),
        "Tags": ((Tags, list), False),
        "WorkingDirectory": (str, False),
    }


class ApplicationFleetAssociation(AWSObject):
    resource_type = "AWS::AppStream::ApplicationFleetAssociation"

    props = {
        "ApplicationArn": (str, True),
        "FleetName": (str, True),
    }


class ServiceAccountCredentials(AWSProperty):
    props = {
        "AccountName": (str, True),
        "AccountPassword": (str, True),
    }


class DirectoryConfig(AWSObject):
    resource_type = "AWS::AppStream::DirectoryConfig"

    props = {
        "DirectoryName": (str, True),
        "OrganizationalUnitDistinguishedNames": ([str], True),
        "ServiceAccountCredentials": (ServiceAccountCredentials, True),
    }


class ComputeCapacity(AWSProperty):
    props = {
        "DesiredInstances": (integer, True),
    }


class DomainJoinInfo(AWSProperty):
    props = {
        "DirectoryName": (str, False),
        "OrganizationalUnitDistinguishedName": (str, False),
    }


class VpcConfig(AWSProperty):
    props = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class Fleet(AWSObject):
    resource_type = "AWS::AppStream::Fleet"

    props = {
        "ComputeCapacity": (ComputeCapacity, False),
        "Description": (str, False),
        "DisconnectTimeoutInSeconds": (integer, False),
        "DisplayName": (str, False),
        "DomainJoinInfo": (DomainJoinInfo, False),
        "EnableDefaultInternetAccess": (boolean, False),
        "FleetType": (str, False),
        "IamRoleArn": (str, False),
        "IdleDisconnectTimeoutInSeconds": (integer, False),
        "ImageArn": (str, False),
        "ImageName": (str, False),
        "InstanceType": (str, True),
        "MaxConcurrentSessions": (integer, False),
        "MaxUserDurationInSeconds": (integer, False),
        "Name": (str, True),
        "Platform": (str, False),
        "StreamView": (str, False),
        "Tags": ((Tags, list), False),
        "UsbDeviceFilterStrings": ([str], False),
        "VpcConfig": (VpcConfig, False),
    }


class AccessEndpoint(AWSProperty):
    props = {
        "EndpointType": (str, True),
        "VpceId": (str, True),
    }


class ImageBuilder(AWSObject):
    resource_type = "AWS::AppStream::ImageBuilder"

    props = {
        "AccessEndpoints": ([AccessEndpoint], False),
        "AppstreamAgentVersion": (str, False),
        "Description": (str, False),
        "DisplayName": (str, False),
        "DomainJoinInfo": (DomainJoinInfo, False),
        "EnableDefaultInternetAccess": (boolean, False),
        "IamRoleArn": (str, False),
        "ImageArn": (str, False),
        "ImageName": (str, False),
        "InstanceType": (str, True),
        "Name": (str, True),
        "Tags": ((Tags, list), False),
        "VpcConfig": (VpcConfig, False),
    }


class ApplicationSettings(AWSProperty):
    props = {
        "Enabled": (boolean, True),
        "SettingsGroup": (str, False),
    }


class StorageConnector(AWSProperty):
    props = {
        "ConnectorType": (str, True),
        "Domains": ([str], False),
        "ResourceIdentifier": (str, False),
    }


class UserSetting(AWSProperty):
    props = {
        "Action": (str, True),
        "Permission": (str, True),
    }


class Stack(AWSObject):
    resource_type = "AWS::AppStream::Stack"

    props = {
        "AccessEndpoints": ([AccessEndpoint], False),
        "ApplicationSettings": (ApplicationSettings, False),
        "AttributesToDelete": ([str], False),
        "DeleteStorageConnectors": (boolean, False),
        "Description": (str, False),
        "DisplayName": (str, False),
        "EmbedHostDomains": ([str], False),
        "FeedbackURL": (str, False),
        "Name": (str, False),
        "RedirectURL": (str, False),
        "StorageConnectors": ([StorageConnector], False),
        "Tags": ((Tags, list), False),
        "UserSettings": ([UserSetting], False),
    }


class StackFleetAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackFleetAssociation"

    props = {
        "FleetName": (str, True),
        "StackName": (str, True),
    }


class StackUserAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackUserAssociation"

    props = {
        "AuthenticationType": (str, True),
        "SendEmailNotification": (boolean, False),
        "StackName": (str, True),
        "UserName": (str, True),
    }


class User(AWSObject):
    resource_type = "AWS::AppStream::User"

    props = {
        "AuthenticationType": (str, True),
        "FirstName": (str, False),
        "LastName": (str, False),
        "MessageAction": (str, False),
        "UserName": (str, True),
    }
