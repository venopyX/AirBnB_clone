import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class from which all other classes will inherit."""

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at to the current datetime & saves."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
