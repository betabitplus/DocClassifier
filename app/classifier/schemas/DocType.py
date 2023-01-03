from dataclasses import dataclass


@dataclass
class DocType:
    """Document Type

    Args:
        label (str): document class
        prob (float): confidence of the prediction. The value should be in range from 0 to 1
    """

    label: str
    prob: float


    @classmethod
    def from_dict(self, obj: dict):
        if obj is None:
            return None

        return DocType(
            label = obj['label'],
            prob = obj['prob']
        )