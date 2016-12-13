# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-snapshot
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V2alpha1JobStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, completion_time=None, conditions=None, failed=None, start_time=None, succeeded=None):
        """
        V2alpha1JobStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'int',
            'completion_time': 'UnversionedTime',
            'conditions': 'list[V2alpha1JobCondition]',
            'failed': 'int',
            'start_time': 'UnversionedTime',
            'succeeded': 'int'
        }

        self.attribute_map = {
            'active': 'active',
            'completion_time': 'completionTime',
            'conditions': 'conditions',
            'failed': 'failed',
            'start_time': 'startTime',
            'succeeded': 'succeeded'
        }

        self._active = active
        self._completion_time = completion_time
        self._conditions = conditions
        self._failed = failed
        self._start_time = start_time
        self._succeeded = succeeded


    @property
    def active(self):
        """
        Gets the active of this V2alpha1JobStatus.
        Active is the number of actively running pods.

        :return: The active of this V2alpha1JobStatus.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this V2alpha1JobStatus.
        Active is the number of actively running pods.

        :param active: The active of this V2alpha1JobStatus.
        :type: int
        """

        self._active = active

    @property
    def completion_time(self):
        """
        Gets the completion_time of this V2alpha1JobStatus.
        CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :return: The completion_time of this V2alpha1JobStatus.
        :rtype: UnversionedTime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """
        Sets the completion_time of this V2alpha1JobStatus.
        CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :param completion_time: The completion_time of this V2alpha1JobStatus.
        :type: UnversionedTime
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """
        Gets the conditions of this V2alpha1JobStatus.
        Conditions represent the latest available observations of an object's current state. More info: http://kubernetes.io/docs/user-guide/jobs

        :return: The conditions of this V2alpha1JobStatus.
        :rtype: list[V2alpha1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V2alpha1JobStatus.
        Conditions represent the latest available observations of an object's current state. More info: http://kubernetes.io/docs/user-guide/jobs

        :param conditions: The conditions of this V2alpha1JobStatus.
        :type: list[V2alpha1JobCondition]
        """

        self._conditions = conditions

    @property
    def failed(self):
        """
        Gets the failed of this V2alpha1JobStatus.
        Failed is the number of pods which reached Phase Failed.

        :return: The failed of this V2alpha1JobStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this V2alpha1JobStatus.
        Failed is the number of pods which reached Phase Failed.

        :param failed: The failed of this V2alpha1JobStatus.
        :type: int
        """

        self._failed = failed

    @property
    def start_time(self):
        """
        Gets the start_time of this V2alpha1JobStatus.
        StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :return: The start_time of this V2alpha1JobStatus.
        :rtype: UnversionedTime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this V2alpha1JobStatus.
        StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :param start_time: The start_time of this V2alpha1JobStatus.
        :type: UnversionedTime
        """

        self._start_time = start_time

    @property
    def succeeded(self):
        """
        Gets the succeeded of this V2alpha1JobStatus.
        Succeeded is the number of pods which reached Phase Succeeded.

        :return: The succeeded of this V2alpha1JobStatus.
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """
        Sets the succeeded of this V2alpha1JobStatus.
        Succeeded is the number of pods which reached Phase Succeeded.

        :param succeeded: The succeeded of this V2alpha1JobStatus.
        :type: int
        """

        self._succeeded = succeeded

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
