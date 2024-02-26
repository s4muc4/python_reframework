from Components.logs import logMessage
from Framework.takeScreenshot import takeScreenshot
from Components.finalReport import updateReport
from Framework.closeAllApplications import *
from Framework.killAllProcess import *

def setTransactionStatus (transactionNumber, retryNumber, consecutiveSystemExceptions, config, transactionItem, systemException, businessRuleException,startTime, endTime):
    logMessage("[setTransactionStatus] - Started", "INFO")

    if systemException is None and businessRuleException is None:
        successTentative = ''
        if retryNumber>0:
            successTentative = 'Success in tentative number ' + str(retryNumber+1)

        transactionNumber +=1
        retryNumber = 0
        consecutiveSystemExceptions = 0
        
        
        
        updateReport(config['reportPath'], transactionItem.iloc[0], startTime, endTime, 'Successful', successTentative)
    else:
        if businessRuleException is not None:
            logMessage(f"Transaction {transactionNumber} Business Exception", "ERROR")
            transactionNumber +=1
            retryNumber = 0
            consecutiveSystemExceptions = 0
            updateReport(config['reportPath'], transactionItem.iloc[0], startTime, endTime, 'Business Exception', businessRuleException)
        else:
            logMessage(f"Transaction {transactionNumber} System Exception", "ERROR")
            takeScreenshot()
            consecutiveSystemExceptions +=1
            retryNumber, transactionNumber=retryCurrentTransaction(config, retryNumber, transactionNumber, systemException)
            try:
                closeAllApplications()

            except Exception as error:
                logMessage("Error to close Applications.")
                killAllProcess()
            updateReport(config['reportPath'], transactionItem.iloc[0], startTime, endTime, 'System Exception', systemException)

    return transactionNumber, retryNumber, consecutiveSystemExceptions

def retryCurrentTransaction(config, retryNumber, transactionNumber, systemException):

    if int(config["MaxRetryNumber"]) >0:
        if retryNumber >= int(config["MaxRetryNumber"]):
            #max retry
            retryNumber = 0
            transactionNumber +=1
        else:
            #retrying
            retryNumber+=1
    else:
        transactionNumber+=1

    return retryNumber, transactionNumber




