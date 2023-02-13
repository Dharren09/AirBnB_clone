#!/usr/bin/python3
"""
Module that defines all common attributes/methods for all other
classes to inherit from
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Class that contains the common attributes/methods that all other
    classes inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises BaseModel class with default arguments
        """

        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # using key words (deserialize)
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Overides str representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Updates public instance attribute 'updated_at'
        """

        self.updated_at = datetime.now()
        """calling the save(self) method of storage"""
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary with all key/values of the instance's __dict__
        """

        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

    @classmethod
    def all(cls):
        """Retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Create an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id)

    @classmethod
    def destroy(cls, instance_id):
        """Deletes and instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance;
        if args has one elem and its a dict:
            it updates by key value
        else:
            updates by first being key and second being value"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )