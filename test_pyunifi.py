from unittest import mock, TestCase
# from pyunifi.controller import APIError, Controller


class testPyUnifi(TestCase):
    @mock.patch('pyunifi.controller.Controller')
    def test_pyunifi_switch_sites(self, MockPyUnifi):
        controller = MockPyUnifi()

        # Test function to switch sites
        controller.switch_site.return_value = [True]
        response = controller.switch_site('test1')
        self.assertIsNotNone(response)
        self.assertIsInstance(True, bool)

    @mock.patch('pyunifi.controller.Controller')
    def test_pyunifi_get_aps(self, MockPyUnifi):
        controller = MockPyUnifi()

        controller.get_aps.return_value = [
            {
                '_id': '11111',
                '_uptime': '30506',
                'adopted': True,
                'ip': '192.168.1.5'
            }
        ]
        response = controller.get_aps()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
