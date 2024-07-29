class DataFetcher:
    def __init__(self, data_source):
        self.data_source = data_source

    def _get(self, key):
        return self.data_source.get(key, None)

# Usage
data_source = {'user_id': 12345, 'name': 'Alice'}
fetcher = DataFetcher(data_source)
user_id = fetcher._get('user_id')
print(user_id)  # Output: 12345
