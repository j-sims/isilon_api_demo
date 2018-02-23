# Isilon API Demo

The following is a quick start repo for using the Isilon APIs (PAPI & RAN) to automate.

# Reference Documentation
API Guide - https://support.emc.com/docu84279_OneFS-8.1.0-API-Reference.pdf
Tech Specs - https://support.emc.com/docu84267_Isilon-OneFS-8.1.0-and-IsilonSD-Edge:-Technical-Specifications-Guide.pdf
Code Samples - https://support.emc.com/docu53714_OneFS_API_Code_Samples.zip

# Step 1 - Authentication - Create Local user on Isilon CLI
```bash
isi auth users create user1 --password user1 --home-directory /ifs/home/user1 --password-expires no
```

# Step 2 - Create namespace access point
```python
import requests
encoded_data = '{ "path" : "/ifs/data/Shares" }'
headers = {'Content-Type': 'application/json'}
response = requests.put("https://172.16.10.10:8080/namespace/Shares", auth=('root', 'a'), data=encoded_data, headers=headers, verify=False)
response.status_code
response.text
response.close()
```

# Step 3 - Check to see namespace was Created
```python
import requests
response = requests.get("https://172.16.10.10:8080/namespace", auth=('root', 'a'), verify=False)
response.status_code
response.text
```

# Step 4 - Set ACL on the Shares namespace
```python
import requests
encoded_data = '{"acl":[{"accessrights":["file_read","file_write"],"accesstype":"allow","inherit_flags":[],"trustee":{"id":"UID:2000","name":"user1","type":"user"}}],"authoritative":"acl","group":{"id":"GID:0","name":"wheel","type":"group"},"mode":"0060","owner":{"id":"UID:0","name":"root","type":"user"}}'
headers = {'Content-Type': 'application/json'}
response = requests.put("https://172.16.10.10:8080/namespace/Shares?acl&nsaccess=true", auth=('root', 'a'), data=encoded_data, headers=headers, verify=False)
response.status_code
response.text
response.close()
```

# Step 5 - Get ACL on the Shares namespace
```python
import requests
response = requests.get("https://172.16.10.10:8080/namespace/Shares?acl&nsaccess=true", auth=('root', 'a'), verify=False)
response.status_code
response.text
response.close()
```

# Step 6 - Create the Directory
```python
import requests
headers = {'x-isi-ifs-target-type': 'container'}
response = requests.put("https://172.16.10.10:8080/namespace/Shares/folder1", auth=('user1', 'user1'), headers=headers, verify=False)
response.status_code
response.text
response.close()
```

# Step 7 - Add/List/Delete a quota - CLI Method First
```bash
isi quota create /ifs/data/Shares directory --advisory-threshold=10G
isi quota list
isi debug quota delete /ifs/data/Shares --type directory
```

# Step 8 - Create/List/Delete API Calls from CLI commands
```bash
isi --debug quota create /ifs/data/Shares directory --advisory-threshold=10G
isi --debug debug quota delete /ifs/data/Shares --type directory
isi --debug quota list
```
# Step 9 - Create Quota via Python REST API
```python
import requests
encoded_data = '{"enforced": false, "include_snapshots": false, "thresholds": {"advisory": 10737418240}, "thresholds_include_overhead": false, "path": "/ifs/data/Shares", "type": "directory"}'
headers = {'Content-Type': 'application/json'}
response = requests.post("https://172.16.10.10:8080/platform/1/quota/quotas", auth=('root', 'a'), data=encoded_data, headers=headers, verify=False)
response.status_code
response.text
response.close()
```

# Step 10 List Quotas via api
```python
import requests
response = requests.get("https://172.16.10.10:8080/platform/1/quota/quotas", auth=('root', 'a'), verify=False)
response.status_code
response.text
a = json.loads(response.text)
response.close()
```

# Step 11 Delete Quota
```python
import requests
encoded_data = '{"path": "/ifs/data/Shares", "type": "directory"}'
headers = {'Content-Type': 'application/json'}
response = requests.delete("https://172.16.10.10:8080/platform/1/quota/quotas", auth=('root', 'a'), data=encoded_data, headers=headers, verify=False)
response.status_code
response.text
response.close()
```
