from utils.utils import EnhancedIntEnum


class BeverageType(EnhancedIntEnum):
    COLD = 1
    HOT = 2


class DishType(EnhancedIntEnum):
    APPETIZER = 1
    MAIN_DISH = 2
    DESERT = 3
