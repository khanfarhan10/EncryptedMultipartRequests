import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("data.XXXX.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=batchSize;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("1"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('FileName-1.json')))

fileType = mimetypes.guess_type('FileName-1.json')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('FileName-1.json', 'rb') as f:
  dataList.append(f.read())
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
  'Cookie': 'XXXXXXXXXXX',
  'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/fileupload/uri/XXXX", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# copied from https://stackoverflow.com/a/67628574/12464709
