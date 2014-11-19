"""
Canned response for Akamai
"""
import json


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

    def get_policy(self, policy_name):
        """Returns service details json.

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
