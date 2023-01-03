import os
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename
import numpy as np
import cv2
from . import base_path, LOGGER
from .schemas import ClassifierResponse, DocType


class DocClassifier():
    def __init__(self,
                 state_path: str,
                 labels_path: str) -> None:
        """Load and Inference a Document Classification Model

        Args:
            state_path (str): path to .h5 file to load model's state
            label_path (str): location of .txt file with labels encoding
        """

        self.label_encoder = self.load_labels(labels_path) # Labels encoding
        self.model = load_model(os.path.join(base_path, state_path))

        model_name, _ = os.path.splitext(secure_filename(state_path))
        LOGGER.info(f'Model loaded [name: {model_name}].')


    @staticmethod
    def load_labels(path: str):
        """Read label encodings

        Args:
            path (str): path to file

        Returns:
            np.array[str]: labels encodings
        """

        data = list()

        with open(os.path.join(base_path, path), 'r') as f:
            for line in f:
                data.append(line.split('. ')[1].strip())

        return np.sort(data)


    def preprocess(self, img: np.array) -> np.array:
        """Preprocessing the image

        Args:
            img (np.array): input image

        Returns:
            np.array: preprocessed image
        """

        LOGGER.debug(f'Before preprocessing image shape: {img.shape}')

        if len(img.shape) == 2:
            LOGGER.warning('Input image should be in RGB format. It is converted from GRAY to RGB.')
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        x = cv2.resize(img, (224, 224))
        x = np.true_divide(x, 255)
        x = np.expand_dims(x, axis=0)

        return x


    def predict(self, img: np.array) -> np.array:
        """Inference model

        Args:
            img (np.array): input image

        Returns:
            np.array: prediction probabilities
        """

        x = self.preprocess(img)
        probs = self.model.predict(x)[0]

        LOGGER.debug(f'Predicted probabilities: {probs}')

        return probs


    def predict_and_decode(self, img: np.array, top_n: int=1) -> ClassifierResponse:
        """Perform Infarence and decode the result

        Args:
            img (np.array): input image
            top_n (int, optional): top n of the best predicts to show. Defaults to 1.

        Returns:
            ClassifierResponse: list of label names and prediction probabilities
        """

        pred = self.predict(img)
        inds = np.argsort(pred)[::-1][:top_n]

        labels, probs = self.label_encoder[inds], pred[inds]

        preds = [DocType(label=label, prob=float(prob)) for label, prob in zip(labels, probs)]
        res = ClassifierResponse(preds=preds)

        return res