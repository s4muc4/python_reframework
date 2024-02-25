from Components.logs import logMessage
from Components.exceptions import BusinessRuleException

def process(transaction, config):
    logMessage("[process] - Started", "INFO")

    logMessage(f"Processing item: {transaction['First Name']} - {transaction['Email']}", "TRACE")

    #raise Exception("Erro de System")
    
    logMessage("[process] - Ended", "INFO")