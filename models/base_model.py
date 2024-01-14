#!/usr/bin/python3
"""base class for all models in our project"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Init basemodel"""

        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else :

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at with current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a string representation of the instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """returns instance into dict"""

        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict