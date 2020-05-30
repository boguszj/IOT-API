class PreprocessingStatusHandlingStrategy:

    def __init__(self, handler):
        self.handler = handler

    def applies(self, status):
        pass

    def handle(self):
        pass

    def handle_startegy(self, status, strategies):
        print(list(filter(lambda strategy: strategy.applies(status), strategies))[0].handle())
        return list(filter(lambda strategy: strategy.applies(status), strategies))[0].handle()
