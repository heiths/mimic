# -*- test-case-name: mimic.test.test_auth -*-
"""
Defines get current customer
"""

import json

from twisted.web.server import Request

from mimic.rest.mimicapp import MimicApp
from mimic.canned_responses import akamai

Request.defaultContentType = 'application/json'


class AkamaiApi(object):
    """
    Rest endpoints for mocked Akamai api.
    """

    app = MimicApp()

    def __init__(self, core):
        """
        :param MimicCore core: The core to which this AkamaiApi will be
            communicating.
        """
        self.core = core
        self.services = {}
        self.akamai_response = akamai.AkamaiResponse()

    @app.route('/partner-api/v1/network/production/properties/'
               '<string:customer_id>/sub-properties/'
               '<string:policy_name>/policy',
               methods=['PUT'])
    def create_policy(self, request, customer_id, policy_name):
        """
        Returns PUT policy.
        """
        data = request.content.read()
        response = self.akamai_response.create_policy(data,
                                                      customer_id, policy_name)
        return json.dumps(response[0])

    @app.route('/partner-api/v1/network/production/properties/'
               '<string:customer_id>/sub-properties/'
               '<string:policy_name>/policy',
               methods=['GET'])
    def get_policy(self, request, customer_id, policy_name):
        """
        Returns POST Service.
        """
        response = self.akamai_response.get_policy(policy_name)
        return json.dumps(response)

    @app.route('/partner-api/v1/network/production/properties/'
               '<string:customer_id>/sub-properties/'
               '<string:policy_name>/policy',
               methods=['DELETE'])
    def delete_policy(self, request, customer_id, policy_name):
        """
        Returns DELETE Policy.
        """
        response = self.akamai_response.delete_policy(customer_id, policy_name)
        return json.dumps(response)
    
    
    @app.route('/ccu/v2/queues/default',
               methods=['POST'])
    def purge_content(self, request):
        """
        Returns DELETE Policy.
        """
        request.setResponseCode(201)
        response = self.akamai_response.purge_content()
        return json.dumps(response)
      
    @app.route('/config-secure-provisioning-service/v1'
               '/sps-requests/',
               methods=['POST'])
    def sps_post(self, request):
        """
        Akamai Secure Provisioning Service endpoint.
        """
        request.setResponseCode(201)
        response = json.dumps({
            "requestList":
                [{"resourceUrl": "/config-secure-provisioning-service/"
                                 "v1/sps-requests/1849",
                 "lastStatusChange": "2015-03-19T21:47:10Z",
                    "spsId": 1789,
                    "status": "SUCCESS",
                    "jobId": 44306}]})
        return json.dumps(response)
    
    @app.route('/config-secure-provisioning-service/v1'
               '/sps-requests/<string:spsId>',
               methods=['GET'])
    def sps_get(self, request, spsId):
        """
        Akamai Secure Provisioning Service endpoint.
        """
        return "Hello World"