#!/usr/bin/python
import isi_sdk_8_1_0 as isi_sdk
import urllib3
import json
urllib3.disable_warnings()

username = "root"
password = "a"
url = "https://172.16.10.10:8080"


isi_sdk.configuration.username = username
isi_sdk.configuration.password = password
isi_sdk.configuration.verify_ssl = False

host = url
apiClient = isi_sdk.ApiClient(host)

quotaApi = isi_sdk.QuotaApi(apiClient)
result = quotaApi.list_quota_quotas()
for quota in result.quotas:
    print(json.dumps((quota.to_dict()), indent=4))
