class Monument:
    def __init__(self, nom: str, cout: int)->None:
        self._nom = nom
        self._cout = cout
        self._construit = False #car le joueur ne possede pas encore ce monument
    
    @property
    def nom(self)->str:
        return self._nom

    @property
    def cout(self)->int:
        return self._cout

    @property
    def construit(self)->bool:
        return self._construit

    def construire(self)->None: #pour changer son etat
        self._construit = True