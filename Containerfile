FROM registry.access.redhat.com/ubi8/python-39
LABEL maintainer="Osca Mwongera <oscamwongera@gmail.com>"

# Add application source code with correct permissions for OpenShift
USER 0
ADD . .
RUN chown -R 1001:0 ./
USER 1001

# Install project dependencies
RUN pip install -r requirements.txt

# Run the application
CMD gunicorn fenster.wsgi
