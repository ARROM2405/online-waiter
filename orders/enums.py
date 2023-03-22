from enum import IntEnum


class OrderPreparationSatus(IntEnum):
    NEW = 1
    PREPARING = 2
    SERVED = 3
    FINISHED = 4


class OrderPaymentStatus(IntEnum):
    PAID = 1
    NOT_PAID = 2


class OrderingType(IntEnum):
    ONLINE = 1
    OFFLINE = 2
