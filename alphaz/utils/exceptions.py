# alfareza


class StopConversation(Exception):
    """ raise if conversation has terminated """


class ProcessCanceled(Exception):
    """ raise if thread has terminated """


class alphazBotNotFound(Exception):
    """ raise if alphaz plugins bot not found """
