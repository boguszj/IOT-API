from direct_controll_module.handlers.preprocessing_status_handlers.PreprocessingStatusHandlingStrategy import \
    PreprocessingStatusHandlingStrategy


class PreprocessingStatusSuccessHandler(PreprocessingStatusHandlingStrategy):
    def __init__(self, handler):
        super().__init__(handler)

    def applies(self, meta_status):
        return meta_status is None

    def handle(self):
        return self.handler.handle()
