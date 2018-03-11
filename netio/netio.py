from sense_hat import SenseHat
from time import sleep
import requests
import xml.etree.ElementTree as ET

r = requests.get('http://192.168.212.76/netio.xml')
#print(type(r))
print(r.status_code)
#print(r.headers)
#print(r.headers['content-type'])
xmlString = r.text
root = ET.fromstring(xmlString)
outputs = root.find("Outputs")
output1 = outputs.find("Output")
    
#else:
    #print (output1)
    
action = output1.find("Action")

action.text = 0
print (action.text)

data = ET.tostring(root)
print (data)
#https://stackoverflow.com/questions/47020470/how-do-i-send-an-xml-elementtree-with-python-requests

headers = {'Content-Type': '/xml'} # set what your server accepts
requests.post('http://192.168.212.76/netio.xml', data=data, headers=headers).text

#https://stackoverflow.com/questions/12509888/how-can-i-send-an-xml-body-using-requests-library/12510559



"""
200
0
<ns0:Root xmlns:ns0="http://www.netio-products.com/XMLSchema/NETIO.xsd"><Agent><Model>NETIO 4</Model><Version>3.0.3</Version><XmlVer>2.0</XmlVer><DeviceName>myNetio</DeviceName><VendorID>0</VendorID><OemID>0</OemID><SerialNumber>24:A4:2C:39:02:BC</SerialNumber><Uptime>4913</Uptime><Time>2018-03-01T19:14:22+01:00</Time><NumOutputs>4</NumOutputs></Agent><Outputs><Output><ID>1</ID><Name>output_1</Name><State>1</State><Action /><Delay>5000</Delay></Output><Output><ID>2</ID><Name>output_2</Name><State>1</State><Action>6</Action><Delay>5000</Delay></Output><Output><ID>3</ID><Name>output_3</Name><State>1</State><Action>6</Action><Delay>5000</Delay></Output><Output><ID>4</ID><Name>output_4</Name><State>1</State><Action>6</Action><Delay>5000</Delay></Output></Outputs></ns0:Root>
^CTraceback (most recent call last):
  File "netio.py", line 29, in <module>
    requests.post('http://192.168.212.76/netio.xml', data=data, headers=headers).text
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 94, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 49, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 457, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 569, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/adapters.py", line 362, in send
    timeout=timeout
  File "/usr/lib/python2.7/dist-packages/urllib3/connectionpool.py", line 516, in urlopen
    body=body, headers=headers)
  File "/usr/lib/python2.7/dist-packages/urllib3/connectionpool.py", line 331, in _make_request
    httplib_response = conn.getresponse(buffering=True)
  File "/usr/lib/python2.7/httplib.py", line 1111, in getresponse
    response.begin()
  File "/usr/lib/python2.7/httplib.py", line 444, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python2.7/httplib.py", line 400, in _read_status
    line = self.fp.readline(_MAXLINE + 1)
  File "/usr/lib/python2.7/socket.py", line 476, in readline
    data = self._sock.recv(self._rbufsize)
KeyboardInterrupt
"""