from frost_sta_client.dao import base
from frost_sta_client.model.ext.entity_type import EntityTypes


class TaskDao(base.BaseDao):
    def __init__(self, service):
        """
        A data access object for operations with the Task entity
        """
        base.BaseDao.__init__(self, service, EntityTypes['Task'])

