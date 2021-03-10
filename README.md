# flask_ssl
Generate self-signed certificates and enable https protocol in a flask server

## Usage
```shell
# Generate CA and signed cert for the client
./generate_certs.sh

# Prepare the environment
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements

# Run the SSL tests
python test
```
