# fastapi-route-logger
Basic middleware to log requests made to routes in FastAPI applications.

## Installation
```
pip install fastapi-route-logger-middleware
```
## Usage
The component is FastAPI middleware. 
```pythonstub
app.add_middleware(RouteLoggerMiddleware)
```

Additional arguments can be provided, when needed:
* logger - The Logger instance to use. Defaults to the default logger (`logging.getLogger(__name__)`). 
* skip_routes - A list of strings that represent the start of routes that should not be logged. Default is an empty 
list. This is a "begins with" type match so an entry of "/health" will block the routes /health/check and /healthcheck.

The [sample-site](https://github.com/jeffsiver/fastapi-route-logger/tree/master/sample-site) in the code repository
contains a sample FastAPI site with this middleware integrated.