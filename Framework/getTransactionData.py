from Components.logs import logMessage

def getTransactionData(transactionNumber, transactions, config):
    logMessage("[getTransactionData] - Started", "INFO")
    if transactionNumber <= len(transactions):
        logMessage("Getting data", "TRACE")
        logMessage("[getTransactionData] - Ended", "INFO")
        return transactions.loc[transactionNumber-1]
    else:
        logMessage("No data", "INFO")
        logMessage("[getTransactionData] - Ended", "INFO")
        return None
    






    