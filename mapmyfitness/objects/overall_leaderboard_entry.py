from .base import BaseObject
from ..utils import privacy_enum_to_string


class OverallLeaderboardEntryObject(BaseObject):
    simple_properties = {
        'overall_score': None, 'total_distance': None, 'year': None,
        'total_duration': None, 'gender': None,
        'rank': None, 'month': None,
        'average distance': None
    }

    @property
    def id(self):
        return int(self.original_dict['_links']['self'][0]['id'])
