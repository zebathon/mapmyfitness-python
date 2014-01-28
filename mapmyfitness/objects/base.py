from ..utils import iso_format_to_datetime


class BaseObject(object):
    def __init__(self, dict_):
        self.original_dict = dict_

        if hasattr(self, 'simple_properties'):
            for property_key, property_name in self.simple_properties.items():
                if property_key in self.original_dict:
                    if property_name is None:
                        property_name = property_key
                    setattr(self, property_name, self.original_dict[property_key])

        if hasattr(self, 'datetime_properties'):
            for property_key, property_name in self.datetime_properties.items():
                if property_key in self.original_dict:
                    if property_name is None:
                        property_name = property_key
                    setattr(self, property_name, iso_format_to_datetime(self.original_dict[property_key]))

    @property
    def _instance(self):
        if not hasattr(self, '_instance_'):
            from mapmyfitness import MapMyFitness
            self._instance_ = MapMyFitness.instance()
        return self._instance_
