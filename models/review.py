#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in the system"""

    place_id = ""
    user_id = ""
    text = ""
