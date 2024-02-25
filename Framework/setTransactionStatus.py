from Components.logs import logMessage
from Framework.takeScreenshot import takeScreenshot

def setTransactionStatus (transactionNumber, retryNumber, consecutiveSystemExceptions, config, transactionItem, systemException, businessRuleException):
    logMessage("[setTransactionStatus] - Started", "INFO")

    if systemException is None and businessRuleException is None:
        
        transactionNumber +=1
        retryNumber = 0
        consecutiveSystemExceptions = 0
    else:
        if businessRuleException is not None:
            logMessage(f"Transaction {transactionNumber} Business Exception", "ERROR")
            transactionNumber +=1
            retryNumber = 0
            consecutiveSystemExceptions = 0
        else:
            logMessage(f"Transaction {transactionNumber} System Exception", "ERROR")
            takeScreenshot()
            consecutiveSystemExceptions +=1

    return transactionNumber, retryNumber, consecutiveSystemExceptions



    


    logMessage("[setTransactionStatus] - Ended", "INFO")