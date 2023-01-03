# Doc Classifier

Create a docker image:

      $ make build

Run container (or skip the first command and simply):

      $ make run

Open in the browser:

      $ make open

The app looks like the following.

![step 1](assets/readme/step1.png)

Once the document was chosen press the 'Classify the document!' button.

![step 2](assets/readme/step2.png)

The result will be similar to this.

![step 3](assets/readme/step3.png)

Also, there are REST API to be easily integrated with. OpenAPI page looks like the following.

![step 4](assets/readme/swagger1.png)

Example of the request on the `/doc_type/predict` endpoint looks like:

![step 5](assets/readme/swagger2.png)