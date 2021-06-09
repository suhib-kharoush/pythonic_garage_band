from abc import abstractmethod

class Band:
      
      instances = []
      def __init__(self, name, members):
          self.name = name
          self.members = members
          Band.instances.append(self.name)
        
      def play_solos(self):
          solos = []
          for member in self.members:
              solos.append(member.play_solo())
          return solos

      @classmethod

      def to_list(cls):
          return cls.instances     



class Musician:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is {} and I play {}".format(self.name, self.instrument)

    def __repr__(self):
        return f"{self.__class__.name} instance. Name = {self.name}"
        

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"

class Guitarist(Musician):

    def __init__(self, name):

        super().__init__(name)
        self.instrument = "guitar"
        self.solo = "face melting guitar solo"



class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "bass"
        self.solo = "bom bom buh bom"

  

class Drummer(Musician):
    
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "drums"
        self.solo = "rattle boom crash"

if __name__ == "__main__":
    Joan = Guitarist('Joan Jett')
    Sheila = Drummer('Sheila E.')
    Meshell = Bassist('Meshell Ndegeocello')

    print(Joan)
    print(Sheila)
    print(Meshell)