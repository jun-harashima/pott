class Option:

    def __init__(self, **args):
        self.start = args.get('start') if args.get('start') else 0
        self.year_low = args.get('year_low')
        self.year_high = args.get('year_high')
        self.every = args.get('every')
