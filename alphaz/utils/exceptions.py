# alfareza


class StopConversation(Exception):
    """ raise if conversation has terminated """


class ProcessCanceled(Exception):
    """ raise if thread has terminated """


class UsergeBotNotFound(Exception):
    """ raise if alphaz plugins bot not found """
