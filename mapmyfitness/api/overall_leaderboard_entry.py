from .base import BaseAPI
from ..inflators import OverallLeaderboardEntryInflator
from ..validators.overall_leaderboard_entry import OverallLeaderboardEntryValidator
from ..serializers import OverallLeaderboardEntrySerializer
from .mixins import Searchable, Findable

class OverallLeaderboardEntry(BaseAPI, Searchable, Findable):
    __name__ = 'OverallLeaderboardEntry'
    path = '/overall_leaderboard_entry'
    validator_class = OverallLeaderboardEntryValidator
    inflator_class = OverallLeaderboardEntryInflator
    serializer_class = OverallLeaderboardEntrySerializer
    embedded_name = 'overall_leaderboard_entries'
