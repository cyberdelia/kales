from mock import patch
from unittest import TestCase

from kales import Kales

class MockResponse(object):
    content = """{"doc":{"info":{"allowDistribution":"false","allowSearch":"false","calaisRequestID":"4f9e39cb-1c8e-53d5-136c-8fd8edc31aa6","externalID":"0aa35d5a306541ff901514bfa5e24a27","id":"http://id.opencalais.com/FImXEbjqi4Jei0b0vcPQCQ","docId":"http://d.opencalais.com/dochash-1/67379953-4d14-3fbc-8b87-6c23b89a5e5f","document":"Barack Obama","docTitle":"","docDate":"2012-04-19 01:05:22.203"},"meta":{"contentType":"text/raw","emVer":"7.1.1103.5","langIdVer":"DefaultLangId","processingVer":"CalaisJob01","submitionDate":"2012-04-19 01:05:22.140","submitterCode":"5fdfaee7-9ef8-832c-8b2f-11726326fc38","signature":"digestalg-1|jEnTrvvr16OgNDDKmTwSyMA8rs8=|XEnIcf7BKhfDSRd6hA5aiFMbGbcbvdiXJRrpi7S7oqhSgaSpjjBLWA==","language":"InputTextTooShort","messages":[]}},"http://d.opencalais.com/pershash-1/cfcf1aa2-de05-3939-a7d5-10c9c7b3e87b":{"_typeGroup":"entities","_type":"Person","name":"Barack Obama","persontype":"N/A","nationality":"N/A","commonname":"Barack Obama","_typeReference":"http://s.opencalais.com/1/type/em/e/Person","instances":[{"detection":"[]Barack Obama[]","exact":"Barack Obama","offset":0,"length":12}],"relevance":0.857}}"""

    def raise_for_status(self):
        pass


class KalesTest(TestCase):
    def setUp(self):
        self.calais = Kales("123456789")

    @patch.object(Kales, '_request')
    def test_analyze(self, mock):
        mock.return_value = MockResponse()
        data = self.calais.analyze("Barack Obama")
        self.assertTrue("entities" in data)
        self.assertEqual(len(data["entities"]), 1)

    def test_analyze_empty(self):
        data = self.calais.analyze(" ")
        self.assertEqual(data, None)
