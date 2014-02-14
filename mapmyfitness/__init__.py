from .api.config import APIConfig
from .api.route import Route
from .api.user import User, UserProfilePhoto
from .api.workout import Workout
from .api.overall_leaderboard_entry import OverallLeaderboardEntry
from .exceptions import NotInitializedException


class MapMyFitness(object):
    """
    Creating a singleton instance of this class, so that we can easily referr to
    it from anywhere in the code without re-creating the instance and again
    providing the api_key and access_token.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MapMyFitness, cls).__new__(cls)

        return cls._instance

    def __init__(self, api_key, access_token, **kwargs):
        api_config = APIConfig(api_key=api_key, access_token=access_token, **kwargs)
        self.route = Route(api_config=api_config)
        self.workout = Workout(api_config=api_config)
        self.user = User(api_config=api_config)
        self._user_profile_photo = UserProfilePhoto(api_config=api_config)
        api_config.api_root = '{0}/api/0.1'.format(api_config.uri_root)
        self.overall_leaderboard_entry = OverallLeaderboardEntry(api_config=api_config)

    @classmethod
    def instance(cls):
        """
        Returns the singleton instance of MapMyFitness if initializaed.
        If there is no initialized singleton instance, it raises a not initialized exception.

        ::raises:: NotInitializedException
        """
        if cls._instance:
            return cls._instance

        raise NotInitializedException("MapMyFitness has not been initialized")

    @classmethod
    def _drop(cls):
        """
        Drops the instance of the singleton (for testing purposes)
        """
        cls._instance = None
