import math
def predict_age(*ages):
    return math.floor(math.sqrt(sum(i for i in ages))/2)