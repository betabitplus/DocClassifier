from flask import Blueprint, render_template


index_page = Blueprint('index_page', __name__)


@index_page.route('/', methods=['GET'])
def index():
    """Render main page
    """

    return render_template('index.html')