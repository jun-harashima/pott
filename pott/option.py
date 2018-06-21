class Option:

    def __init__(self, **args):
        self.start = args.get('start')
        self.year_low = args.get('year_low')
        self.year_high = args.get('year_high')
        self.every = args.get('every')
