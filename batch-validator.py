import urllib.request
from urllib.error import HTTPError

try:
    request = urllib.request.Request(
        'http://rest.api.domain/batches',
        batch_list_bytes,
        method='POST',
        headers={'Content-Type': 'application/octet-stream'})
    response = urllib.request.urlopen(request)

except HTTPError as e:
    response = e.file