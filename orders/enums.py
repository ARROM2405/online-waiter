from utils.utils import EnhancedIntEnum


class OrderPreparationSatus(EnhancedIntEnum):
    NEW = 1
    PREPARING = 2
    SERVED = 3
    FINISHED = 4


class OrderPaymentStatus(EnhancedIntEnum):
    PAID = 1
    NOT_PAID = 2


class OrderingType(EnhancedIntEnum):
    ONLINE = 1
    OFFLINE = 2


class TableStatus(EnhancedIntEnum):
    FREE = 1
    OCCUPIED = 2
    RESERVED = 3
