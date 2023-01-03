from dataclasses import dataclass
from .DocType import DocType
from typing import List


@dataclass
class ClassifierResponse:
    """Response of the Document Classifier model

    Args:
        preds (List[DocType]): list of predicted classes sorted by their confidance.
    """

    preds: List[DocType]


    @classmethod
    def from_dict(self, obj: dict):
        return ClassifierResponse(
            preds=[DocType.from_dict(pred) for pred in obj['preds']]
        )