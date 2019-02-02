from container import IocContainer

if __name__ == '__main__':
    # Configure container:
    container = IocContainer(
        config={
            'database': {
                'mongo_uri': 'mongodb://mongodb:27017/',
            },
        }
    )

    # Run application:
    container.main()

