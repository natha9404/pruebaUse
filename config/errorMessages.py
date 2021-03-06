__author__ = 'nbedoya'


class ErrorMsg:
    def __init__(self):
        pass


    _codes = {
        # Simple Codes
        200: "OK",
        201: "Create",
        204: "No Content",
        206: "Partial Content",

        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",

        500: "Internal Server Error",
        503: "Service Unavailable",
        # Application Codes
        2001: "Bad credentials",
        2006: "The user is disabled",
        2007: "You find a load with the same name or unprocessed... File not loaded",
        2008: "Correct file",
        2009: """Alarma de GPS
        Se ha generado un evento de alarma de cambio de estado de GPS para el usuario %s.
        Ubicado en las coordenadas %s.
        Direccion: %s""",
        2010: """Alarma Estado de Bateria
        Se ha generado un evento de alarma de estado de bateria para el usuario %s.
        Ubicado en las coordenadas %s.
        Direccion %s""",
        2011: """Alarma Detencion Prolongada
        Se ha generado un evento de alarma de detencion prolongada para el usuario %s.
        Ubicado en las coordenadas %s.
        Direccion %s""",
        2012: """Alarma Ausencia de Transmicion
        Se ha generado un evento de alarma de ausencia de transmicion para el usuario %s.
        Ubicado en las coordenas %s.
        Direccion %s""",
        2013: """Alarma Entrada a Zona
        Se ha generado un evento de alarma de Entrada a zona para el usuario %s.
        Ubicado en las coordenadas %s.
        Direccion %s""",
        2014: """Alarma Salida de Zona
        Se ha generado un evento de alarma de Salida de zona para el usuario %s.
        Ubicado en las coordenadas %s.
        Direccion %s""",
        4000: "Property not found",
        4001: "Method not supported",
        4002: "User not found",
        4003: "There was a problem authorizing the user, try again",
        4004: "Sorry, it is not possible to change the password, the email assigned to your account is not correct, "
              "is out of order or does not exist",
        4005: "Incorrect code to change password",
        4006: "Can not delete User, User not found or the user to delete is an administrator",
        4007: "User to delete is the user in session",
        4008: "Company not found",
        4009: "Profile not found",
        4010: "Activity not found",
        4011: "Client for user already exists",
        4012: "Group not found",
        4013: "File not permitted, formats ZIP, XLSX or file contain characters not permitted in your name",
        4014: "Format file incorrect, not found ZIP file",
        4015: "Not found some files in zip file",
        4016: "Incorrect category",
        4017: "Upload file not found",
        4018: "Upload file does not have the required minimum columns or column name is empty",
        4019: "date_end must be greater than date_ini",
        4020: "end_hour and init_hour must be greater than time_now",
        4021: "end_date and init_date must be greater than date_now",
        4022: "Upload file does not meet the required sheets",
        4023: "the company from user in session is not equals to id_company sender in the request ",
        4024: "Type Tableau report not found",
        5000: "Current position can not be update",
        5001: "Service can not be consumed",
        5002: "Error, OAUTH2 con not be consumed",
        5003: "Login Failed",
        5004: "Logout Failed",
        5005: "Code to change password failed",
        5006: "Change password failed",
        5007: "Create user failed",
        5008: "List user failed",
        5009: "Update user failed",
        5010: "Delete user failed",
        5011: "Create company failed",
        5012: "List company failed",
        5013: "Update company failed",
        5014: "Delete company failed",
        5015: "Create profile failed",
        5016: "List profile failed",
        5017: "Update profile failed",
        5018: "Delete profile failed",
        5019: "Create activity failed",
        5020: "List activity failed",
        5021: "Update activity failed",
        5022: "Delete activity failed",
        5023: "Create client failed",
        5024: "List Client failed",
        5025: "Client does not exist",
        5026: "Delete client failed",
        5027: "Customer does not exist",
        5028: "Update client failed",
        5029: "Create functionality failed",
        5030: "List functionalities failed",
        5031: "Functionality does not exist",
        5032: "Delete functionality failed",
        5033: "Functionality does not exist",
        5034: "Update functionality failed",
        5035: "Create group failed",
        5036: "List groups failed",
        5037: "Group does not exist",
        5038: "Delete group failed",
        5039: "Update group failed",
        5040: "List current position failed",
        5041: "Create alarm prolonged detention failed",
        5042: "Create alarm zone failed",
        5043: "Create alarm absence of transmission failed",
        5044: "Create alarm GPS failed",
        5045: "Create alarm status battery failed",
        5046: "List alarm prolonged detention failed",
        5047: "List alarm zone failed",
        5048: "List alarm absence of transmission failed",
        5049: "List alarm GPS failed",
        5050: "List alarm status battery failed",
        5051: "Delete alarm prolonged detention failed",
        5052: "Delete alarm zone failed",
        5053: "Delete alarm absence of transmission failed",
        5054: "Delete alarm GPS failed",
        5055: "Delete alarm status battery failed",
        5056: "Update alarm prolonged detention failed",
        5057: "Update alarm zone failed",
        5058: "Update alarm absence of transmission failed",
        5059: "Update alarm GPS failed",
        5060: "Update alarm status battery failed",
        5061: "List alarm type alarm zone failed",
        5062: "Upload file failed",
        5063: "Validate extend file failed",
        5064: "List upload files failed",
        5065: "Delete upload files failed",
        5066: "Create/Update control upload files failed",
        5067: "Delete control upload files failed",
        5068: "List days weekend failed",
        5069: "Create/Update massive upload files failed",
        5070: "Create/Update control alarms failed",
        5071: "Geocoder service failed",
        5072: "GeoInverso service failed",
        5073: "Create/Update tokens scheduler failed",
        5074: "Validate token scheduler failed",
        5075: "List scheduler failed",
        5076: "Create event failed",
        5077: "Cancel event failed",
        5078: "Reschedule event failed",
        5079: "Executed route failed",
        5080: "Create form mobile failed",
        5081: "List status scheduler failed",
        5082: "Change status event failed",
        5083: "Transmission report failed",
        5084: "List city failed",
        5085: "Location report failed",
        5086: "Historic report failed",
        5087: "List statistic failed",
        5088: "Delete structure forms mobile failed",
        5089: "Forms report failed",
        5090: "Count forms failed",
        5091: "Tableau report failed",
        5092: "Preload Cliente Update or Create failed",
        5093: "Preload Cliente Delete failed",
        5094: "Create/Update opcion contacto de formulario failed",
        5095: "List opcion contacto de formulario failed",
        5096: "Delete opcion contacto de formulario failed",
        5097: "Create/Update opcion codigo de gestion de formulario failed",
        5098: "Delete opcion codigo de gestion de formulario failed",
        5099: "Create/Update opcion codigo de causal failed",
        5100: "Delete opcion causal de formulario failed",
        5101: "List opcion causal de formulario failed",
        5102: "List opcion codigo de gestion de formulario failed",
        5103: "List opcion codigo de gestion por contacto de formulario failed",
        5104: "List opcion causal por codigo de gestion de formulario failed",
        5105: "Alarm report failed",
        5106: "List type alarms failed",
        5107: "List scheduler by id failed",
        5108: "Start event failed",
        5109: "ExtraData Cliente Update or Create failed",
        5110: "ExtraData Cliente Delete failed",
        5111: "ExtraData Users Update or Create failed",
        5112: "ExtraData Users Delete failed",
        5113: "List service type form contento failed",
        5114: "List money form contento failed",
        5115: "List layers failed",
        5116: "Report failed",
        5117: "Create firebase failed",
        5118: "List firebase failed",
        5119: "Update firebase failed",
        5120: "Delete firebase failed",
        5121: "FireBase does not exist",
        5122: "List metadata layers failed",
        5123: "List values layer field failed",
        5124: "Program route report failed",
        5125: "Order report failed",
        5126: "Create/Update Licores Cyan",
        5127: "Delete Licores Cyan",
        5128: "Create/Update Encuesta Cyan",
        5129: "Delete Encuesta Cyan",
        5130: "Create/Update Modificacion Cyan",
        5131: "Delete Modificacion Cyan",
        5132: "Create/Update Novedad Cyan",
        5133: "Delete Novedad Cyan",
    }

    @property
    def codes(self):
        return self._codes

    def get_msg(self, code):
        return self._codes.get(code, "message not found")
