import httpretty

from tests import MapMyFitnessTestCase


class RouteTest(MapMyFitnessTestCase):
    def test_single_entry(self):
        overall_lb_entry = self.mmf.overall_leaderboard_entry.find(971924)
        self.assertEqual(overall_lb_entry.id, 971924)

    def test_list(self):
        from nose.tools import set_trace; set_trace()
        overall_lb_entries = self.mmf.overall_leaderboard_entry.search(year=2014, month=1, activity_type=11, user=36142)
        self.assertTrue(len(overall_lb_entries) >  1)