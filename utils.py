class Utils:
    @staticmethod
    def parse_context(data):
        from strategy import Cycle
        return Cycle(data)