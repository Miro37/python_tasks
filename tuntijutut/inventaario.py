class inventaario:
    def __init__(self, potioni, miekka, yrtti):
        self.potioni=potioni
        self.miekka=miekka
        self.yrtti=yrtti
        
        pass
    def tulosta_tavarat(self, invi):
      invi=[]
      invi.append(self.potioni)
      invi.append(self.miekka)
      invi.append(self.yrtti)
      print(invi)
      return
   