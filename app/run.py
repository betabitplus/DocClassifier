import os
import json
import argparse
import connexion
import logging.config


if __name__ == '__main__':
    # parse input args
    parser = argparse.ArgumentParser(description='Document Classification Model REST Web Server.')
    parser.add_argument('--port', type=int, default=5000, metavar='p',
                        help='Define server port (default: 5000)')
    args = parser.parse_args()

    # setup logging configuration
    base_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_path, 'resources', 'logging.json'), 'r') as logs:
        logging.config.dictConfig(json.load(logs))

    logging.info(f'Running on http://localhost: {args.port}')


    # Run app
    from routes.index_page import index_page
    from routes.predict_page import predict_page

    app = connexion.FlaskApp(__name__, specification_dir="resources/", server='tornado')
    app.add_api('swagger.yaml')

    app.app.register_blueprint(index_page)
    app.app.register_blueprint(predict_page)

    app.run(port=args.port)
