from enum import Enum


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class BaseChannels(NoValue):
    pass

class Channels(BaseChannels):
    # Trollbox chat
    chat = 1

    # Statistics of connected users/bots
    connected = 2

    # Daily Insurance Fund updates
    insurance = 3

    # Liquidation orders as they're entered into the book
    liquidation = 4

    # System-wide notifications
    publicNotifications = 5


class SecureChannels(BaseChannels):
    # Affiliate status, such as total referred users & payout %
    affiliate = 6

    # Updates on your current account balance and margin requirements
    margin = 7

    # Individual notifications - currently not used
    privateNotifications = 8

    # Bitcoin address balance data, including total deposits & withdrawals
    wallet = 9

    # Deposit/Withdrawal updates
    transact = 10


class InstrumentChannels(BaseChannels):
    # Instrument updates including turnover and bid/ask
    instrument = 11

    # Top 10 levels using traditional full book push
    orderBook10 = 12

    # Full level 2 orderBook
    orderBookL2 = 13

    # Top level of the book
    quote = 14

    # 1-minute quote bins
    quoteBin1m = 15

    # Settlements
    settlement = 16

    # Live trades
    trade = 17

    # 1-minute ticker bins
    tradeBin1m = 18


class SecureInstrumentChannels(BaseChannels):
    # Individual executions; can be multiple per order
    execution = 19

    # Live updates on your orders
    order = 20

    # Updates on your positions
    position = 21


class Action(NoValue):
    partial = 22

    insert = 23

    update = 24

    delete = 25

# Don't grow a table larger than this amount. Helps cap memory usage.
MAX_TABLE_LEN = 200
