import datetime

class Score:
    def __init__(self, identifier, name, score, time=str(datetime.datetime.now())):
        if type(identifier) is not int or identifier == 0:
            return ValueError("Wrong identifier")

        if not isinstance(name, str) or not name:
            return ValueError("Invalid name") 

        if type(score) is not int:
            return ValueError("Score must be an integer")
        
        self._identifier = identifier
        self._name = name
        self._score = score
        self._time = time
  

    @property
    def identifier(self):
        return self._identifier

    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score

    @property
    def time(self):
        return self._time

    def to_json(self):
        """ returns a JSON-serializable version of the class  """
        return {"identifier": self._identifier, "name": self._name, "score": self._score, "time": self._time}

    @classmethod
    def from_json(cls, data):
        """ Deserialization method """
        if "name" not in data or "score" not in data:
            return ValueError("name or score missing in data")

        # Creates an instance of the same class
        return cls(identifier=data["identifier"], name=data["name"], score=data["score"], time=data["time"])


