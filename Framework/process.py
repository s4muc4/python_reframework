from Components.logs import logMessage
from Components.exceptions import BusinessRuleException

def process(transaction, transactionNumber, config):
    logMessage("[process] - Started", "INFO")

    logMessage(f"Processing item {transactionNumber}: {transaction['First Name']} - {transaction['Email']}", "TRACE")

    if 'y' in transaction['First Name']:
        raise Exception("tem Y no nome")
    
    if 'a' in transaction['First Name']:
        raise BusinessRuleException('tem A no nome')
    

    
    logMessage("[process] - Ended", "INFO")