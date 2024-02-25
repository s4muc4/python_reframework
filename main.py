from Components.statemachine import StateMachine
from Components.exceptions import BusinessRuleException
from Components.logs import *
from Components.screenInfo import get_screen_resolution
from Framework.initAllSettings import initAllSettings
from Framework.killAllProcess import killAllProcess
from Framework.initAllApplications import initAllApplications
from Framework.getTransactionData import getTransactionData
from Framework.process import process
from Framework.closeAllApplications import closeAllApplications
from Framework.setTransactionStatus import setTransactionStatus
import pandas as pd 
from Project.getInputData import getInputData


hashCodeProject = generateHashCodeProject()
clear_logs_output()

logMessage('#####---AUTOMATION STARTED---#####', "INFO")

# Create an instance of SimpleMachine
stateMachine = StateMachine()

# Initialize variables
transactions = pd.DataFrame()
systemException = Exception
businessRuleException = BusinessRuleException
transactionNumber = 1
config = {}
retryNumber = 0
consecutiveSystemExceptions = 0
transactionItem = {}

finalizeAutomation = False

while finalizeAutomation == False:

    logMessage(stateMachine.state, "STATE")

    if stateMachine.state == 'init':
        try:
            systemException = None

            if len(config) == 0:
                logMessage(get_screen_resolution(),'TRACE')
                config = initAllSettings("Data/Config.xlsx")
                killAllProcess()
                transactions = getInputData(config['InputData_Path'], config['InputData_Sheet'])

            if int(config['MaxConsecutiveSystemExceptions'])>0 and consecutiveSystemExceptions >= int(config['MaxConsecutiveSystemExceptions']):
                raise Exception(config['ExceptionMessage_ConsecutiveErrors'] + 'Consecutive retry number: ' + str(consecutiveSystemExceptions+1))
            
            initAllApplications()

            stateMachine.init_sucessfull()

        except Exception as error:
            logMessage(str(error) , "ERROR")
            stateMachine.init_se()

        finally:
            continue

    if stateMachine.state == 'get_transaction':
        transactionItem = getTransactionData(transactionNumber, transactions, config)
        if transactionItem is not None:
            stateMachine.get_transaction_new()
        else:
            stateMachine.get_transaction_no_data()     

        continue

    if stateMachine.state == 'process':
        try:
            businessRuleException = None
            process(transactionItem, config)

            stateMachine.process_success()

        except BusinessRuleException as error:
            businessRuleException = error
            stateMachine.process_be()
        
        except Exception as error:
            systemException = error
            stateMachine.process_se()

        finally:
            transactionNumber, retryNumber, consecutiveSystemExceptions = setTransactionStatus(transactionNumber, retryNumber, consecutiveSystemExceptions, config, transactionItem, systemException, businessRuleException)
            continue

    if stateMachine.state == 'end':
        try:
            closeAllApplications()

        except Exception as error:
            logMessage("Error to close Applications.")
            killAllProcess()

        finally:
            finalizeAutomation = True


        
        
logMessage('#####---AUTOMATION ENDED---#####', "INFO")
