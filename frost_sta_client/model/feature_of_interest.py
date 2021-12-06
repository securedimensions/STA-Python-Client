from . import entity

import frost_sta_client.dao.features_of_interest

from .ext import entity_list

import json


class FeatureOfInterest(entity.Entity):
    def __init__(self,
                 name='',
                 description='',
                 encoding_type='',
                 feature='',
                 properties=None,
                 observations=None):
        super().__init__()
        if properties is None:
            properties = {}
        self.name = name
        self.description = description
        self.encoding_type = encoding_type
        self.feature = feature
        self.properties = properties
        self.observations = observations

    def __new__(cls, *args, **kwargs):
        new_foi = super().__new__(cls)
        attributes = {'_id': None, '_name': '', '_description': '', '_properties': {}, '_encoding_type': '',
                      '_feature': '', '_observations': [], '_self_link': '', '_service': None}
        for key, value in attributes.items():
            new_foi.__dict__[key] = value
        return new_foi

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            self._name = None
            return
        if type(value) != str:
            raise ValueError('name should be of type str!')
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None:
            self._description = None
            return
        if type(value) != str:
            raise ValueError('description should be of type str!')
        self._description = value

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if value is None:
            self._properties = None
            return
        if type(value) != dict:
            raise ValueError('properties should be of type dict!')
        self._properties = value

    @property
    def encoding_type(self):
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, value):
        if value is None:
            self._encoding_type = None
            return
        if type(value) != str:
            raise ValueError('encodingType should be of type str!')
        self._encoding_type = value

    @property
    def observations(self):
        return self._observations

    @observations.setter
    def observations(self, values):
        if values is None:
            self._observations = None
            return
        if type(values) == entity_list.EntityList and \
                all((isinstance(ob, frost_sta_client.model.observation.Observation)) for ob in values.entities):
            self._observations = values
            return
        raise ValueError('Observations should be a list of Observations')

    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        if value is None:
            self._feature = None
            return
        try:
            json.dumps(value)
        except TypeError:
            raise TypeError('feature should be json serializable')
        self._feature = value

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, type(self)):
            return False
        if id(self) == id(other):
            return True
        if self.name != other.name:
            return False
        if self.properties != other.properties:
            return False
        if self.description != other.description:
            return False
        if self.encoding_type != other.encoding_type:
            return False
        if self.feature != other.feature:
            return False
        return True

    def ensure_service_on_children(self, service):
        if self.observations is not None:
            self.observations.set_service(service)

    def __ne__(self, other):
        return not self == other

    def __getstate__(self):
        data = super().__getstate__()
        data['name'] = self.name
        data['description'] = self.description
        data['properties'] = self.properties
        data['encodingType'] = self.encoding_type
        if self.feature is not None:
            data['feature'] = self.feature
        if self.observations is not None and len(self.observations.entities) > 0:
            data['Observations'] = self.observations.__gestate__()
        return data

    def __setstate__(self, state):
        super().__setstate__(state)
        self.name = state.get("name", None)
        self.description = state.get("description", None)
        self.properties = state.get("properties", None)
        self.encoding_type = state.get("encodingType", None)
        if state.get("Observations", None) is not None and type(state["Observations"]) == list:
            self.observation = []
            for value in state["Observation"]:
                obs = frost_sta_client.model.observation.Observation()
                obs.__setstate__(value)
                self.observation.append(obs)

    def get_dao(self, service):
        return frost_sta_client.dao.features_of_interest.FeaturesOfInterestDao(service)
