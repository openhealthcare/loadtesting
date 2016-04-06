"""
Benchmarking script for elCID@UCH
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class elCID(FunkLoadTestCase):

    def setUp(self):
        self.server_url = self.conf_get('main', 'url')

    def url(self, path):
        return self.server_url + path

    def api_url(self, name):
        return self.url( '/api/v0.1' + name)

    def login(self):
        res = self.get( self.url('/accounts/login/'), description = 'Get url' ).cookies.itervalues ( ).next ( )
        morsel_str = res [ '/' ] [ 'XSRF-TOKEN' ]
        csrftoken = morsel_str.value
        # Once Cookie found include it in params
        params = [
            [ 'csrfmiddlewaretoken', csrftoken ],
            [ 'username', 'super' ],
            [ 'password', 'super1' ] ]
        self.post(self.url('/accounts/login/?next=/'), params, description = "Post /login/" )

    def list_page(self, slug):
        self.get(self.api_url('/patientlist/' + slug + '/'))
        self.get(self.url('/templates/patient_list.html/'+slug))
        return

    def test_daily(self):
        self.login()
        self.get(self.api_url('/userprofile/'))
        self.get(self.api_url('/record/'))
        self.get(self.api_url('/options/'))
        self.list_page('hiv-immune_inpatients')
        self.list_page('walkin-walkin_triage')
        self.list_page('walkin-walkin_doctor')
        self.list_page('infectious_diseases-id_inpatients')
        self.list_page('opat-opat_current')
        return

if __name__ in ('main', '__main__'):
    unittest.main()
