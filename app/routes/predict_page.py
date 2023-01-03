from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import numpy as np
from classifier import doc_classifier
import os
import json
from PIL import Image
from . import base_path, LOGGER
from .utils import clear_dir


predict_page = Blueprint('predict_page', __name__)


@predict_page.route('/predict', methods=['POST'])
def predict():
    """Generate predict page
    """

    # clean buffer directory
    path_to_uploads = os.path.join(base_path, 'static', 'uploads')
    clear_dir(path_to_uploads)

    # recieve a document and its filename
    file = request.files['file']
    file_name, _ = os.path.splitext(secure_filename(file.filename))

    # open the document and store its jpeg image in buffer folder
    image = Image.open(file).convert('RGB')
    jpg_file_path = os.path.join(path_to_uploads, file_name + '.jpg')
    image.save(jpg_file_path, "JPEG", quality=90)

    LOGGER.debug(f'Input image name: {file_name}')
    LOGGER.debug(f'Input image shape: {image.size}')

    try:
        classifier_response = doc_classifier.predict_and_decode(np.asarray(image), top_n=3)
        preds = json.loads(json.dumps(classifier_response.preds, default=vars))

        LOGGER.info(f'Successfully classified: {file_name}')

        return jsonify({
            'state': 'SUCCESS',
            'preds': preds,
            'file_name': file_name
        })

    except Exception as e:
        LOGGER.error(traceback.format_exc())

        return jsonify({
            'state': 'FAILURE',
            'preds': [],
            'file_name': file_name
        })