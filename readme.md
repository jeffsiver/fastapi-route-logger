# fastapi-route-logger
Basic middleware to log requests made to routes in FastAPI applications.

## Usage

When creating the FastAPI application, add the middleware with:
```pythonstub
app.add_middleware(RouteLogger)
```

The following additional arguments are supported:
* logger - The Logger instance that should be used. Defaults to the default logger (`logging.getLogger(__name__)`). 
* skip_routes - A list of strings that represent the start of routes that should not be logged. Default is an empty list.

To add this middleware providing all settings, use the following:
```pythonstub
app.add_middleware(RouteLogger, logger=logger, skip_routes=['metrics'])
```

The [sample-site](https://github.com/jeffsiver/fastapi-route-logger/tree/master/sample-site) in the code repository
contains a sample on how to integrate this.