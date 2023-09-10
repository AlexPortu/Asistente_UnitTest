
class SelectorsValues(object):

    def __init__(self):
        """ ------ Variables de traducción/selección mantenidas por el usuario ------ """ 

        # swimlane
        self.swimlanes_ids = {
            "forfait": "'interes3'",
            "hotel": "'interes2'",
            "clases": "'interes4'",
            "alquiler": "'interes5'",
            "restauracion": "'interes8'",
            "actividades": "'interes1'"
        }
        # Atributo @for de la clase
        self.clases_selectors = {
            "colectivas": "clase_209", 
            "particulares": "clase_237"
            }
        # Necita un número al final del - que indique el tipo de clase. La operación se realiza en el metodo de la page.py
        self.estilos_selectors = {
            "esqui":"edit-checkoption-1-",
            "snow":"edit-checkoption-2-",
        }
        # Sectores
        self.sectores_selectors = {
            "grau": "14",
            "pas": "13",
            "soldeu": "15",
            "tarter": "16",
            "canillo": "17",
            "encamp": "18"
        }
        



        
        