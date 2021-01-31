import jimi
from plugins.unshorten.includes import unshorten

class _unshortenURL(jimi.action._action):
    url = str()
    
    def run(self,data,persistentData,actionResult):
        url = jimi.helpers.evalString(self.url,{"data" : data})
        
        result, statusCode = unshorten._unshorten().unshortenURL(url)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from unshorten API"
        return actionResult 
