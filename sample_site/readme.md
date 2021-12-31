# Sample Site

## Running
To run the sample site: `hypercorn -b 0.0.0.0:8000 sample_site.main:app`.

## Endpoints
The sample site includes the following endpoints:
* /success - Returns a 200 with a simple string return value
* /failed - Returns a 500 status code with the FastAPI bundled error message. Throws an exception to provide an example of exception logging.
 