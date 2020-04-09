import numpy as np


predicted_classes = ['person', 'person', 'cup', 'laptop', 'clock']
out_boxes = [
    [82, 305, 98, 386],
    [28, 436, 57, 480],
    [94, 316, 114, 393],
    [55, 296, 78, 369],
    [69, 303, 107, 387]
]

indices = np.where(np.array(predicted_classes) == "person")
print(np.array(out_boxes)[indices])
