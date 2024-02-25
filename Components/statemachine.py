from transitions import Machine

class StateMachine:
    def __init__(self):
        states = ['init', 'get_transaction', 'process', 'end']
        transitions = [
            {'trigger': 'init_sucessfull', 'source': 'init', 'dest': 'get_transaction'},
            {'trigger': 'init_se', 'source': 'init', 'dest': 'end'},
            {'trigger': 'get_transaction_new', 'source': 'get_transaction', 'dest': 'process'},
            {'trigger': 'get_transaction_no_data', 'source': 'get_transaction', 'dest': 'end'},
            {'trigger': 'process_success', 'source': 'process', 'dest': 'get_transaction'},
            {'trigger': 'process_be', 'source': 'process', 'dest': 'get_transaction'},
            {'trigger': 'process_se', 'source': 'process', 'dest': 'init'}
        ]

        self.machine = Machine(model=self, states=states, transitions=transitions, initial='init')

