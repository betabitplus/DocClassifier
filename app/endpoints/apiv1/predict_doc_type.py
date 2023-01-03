import traceback
import connexion
from werkzeug.utils import secure_filename
from classifier import doc_classifier
from PIL import Image
import numpy as np
import json
import os
from . import LOGGER


def post(top_n):
    """Perform document type classification

    Args:
        file (str): .tif document file
        top_n (int): top n of the best predicts to show. Defaults to 1.

    Returns:
        List[DocType]: list of predicted classes sorted by their confidance.
    """

    file = connexion.request.files['file']
    file_name, _ = os.path.splitext(secure_filename(file.filename))

    try:
        img = np.asarray(Image.open(file).convert('RGB'))

        LOGGER.debug(f'Input image name: {file_name}')
        LOGGER.debug(f'Input image shape: {img.shape}')

        classifier_response = doc_classifier.predict_and_decode(img, top_n=top_n)

    except Exception as e:
        LOGGER.error(traceback.format_exc())
        return connexion.problem(500, "Internal Server Error", "Failed to classify: " + str(e))

    LOGGER.info(f'Successfully classified: {file_name}')

    return json.loads(json.dumps(classifier_response, default=vars))
