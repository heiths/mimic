"""
Canned response for Akamai
"""
import json
import random
import string
import uuid


class AkamaiResponse(object):

    akamai_cache = {}

    def create_policy(self, request_body, customer_id, policy_name):
        """
        Returns PUT policy with response json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for
                 ("/partner-api/v1/network/production/properties/customer_id/'
                  'sub-properties/policy_name/policy'") request.
        """
        self.akamai_cache[policy_name] = json.loads(request_body)
        return self.akamai_cache[policy_name], 200

    def get_policy(self, customer_id, policy_name):
        """Returns policy details json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for Akamai GET policy
                 ("/partner-api/v1/network/production/properties/customer_id/'
                  'sub-properties/policy_name/policy'") request.
        """
        return self.akamai_cache[policy_name]

    def delete_policy(self, customer_id, policy_name):
        """
        Returns DELETE service with response json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for Akamai DELETE policy
                 ("/partner-api/v1/network/production/properties/customer_id/'
                  'sub-properties/policy_name/policy'") request.
        """
        del(self.akamai_cache[policy_name])

        description = 'The policy for property_id {0} and ' \
            'subproperty_id {1} was successfully deleted.'.format(customer_id,
                                                                  policy_name)
        response_body = {
            "message": "Successfully deleted",
            "description": description}

        return response_body

    def create_sub_customer(self, request_body, customer_id, sub_customer_id):
        """
        Returns PUT policy with response json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for
                 ("/partner-api/v1/network/production/properties/'
                  '{customer_id}/customers/{sub_customer_id}'") request.
        """
        self.akamai_cache[sub_customer_id] = json.loads(request_body)
        return self.akamai_cache[sub_customer_id], 200

    def get_sub_customer(self, customer_id, sub_customer_id):
        """
        Returns sub_customer details json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for
                 ("/partner-api/v1/network/production/properties/'
                  '{customer_id}/customers/{sub_customer_id}'") request.
        """
        return self.akamai_cache[sub_customer_id]

    def delete_sub_customer(self, customer_id, sub_customer_id):
        """
        Returns DELETE service with response json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for Akamai DELETE sub_customer
                 ("/partner-api/v1/network/production/properties/'
                  '{customer_id}/customers/{sub_customer_id}'") request.
        """
        del self.akamai_cache[sub_customer_id]

        description = 'The sub_customer for property_id {0} and ' \
            'sub_customer_id {1} was successfully deleted.'.format(
                customer_id,
                sub_customer_id
            )
        response_body = {
            "message": "Successfully deleted",
            "description": description}

        return response_body

    def purge_content(self):
        """Returns service details json.

        :return: a JSON-serializable dictionary matching the format of the JSON
                 response for Akamai CCU API POST
                 ("/ccu/v2/queues/default") request.
        """
        purgeId = uuid.uuid1()
        supportId = ''.join([random.choice(string.ascii_letters + string.digits)
                             for n in xrange(30)]).upper()
        response_body = {
            "estimatedSeconds": 420,
            "progressUri": "/ccu/v2/purges/%s" % str(purgeId),
            "purgeId": str(purgeId),
            "supportId": supportId,
            "httpStatus": 201,
            "detail": "Request accepted.",
            "pingAfterSeconds": 420
        }

        return response_body