import swagger_client
import jwt
import datetime

apiClient = swagger_client.ApiClient()
holdingsApi = swagger_client.HoldingsApi(apiClient)
accountsApi = swagger_client.AccountsApi(apiClient)

apiClient.configuration.host = "https://sandbox.api.yodlee.com/ysl"
apiClient.set_default_header("Content-Type", "application/json")
apiClient.set_default_header("Cobrand-Name", "restserver")
apiClient.set_default_header("Api-Version", "1.1")

f = open('devSandbox.key', 'r')
privateKey = f.read()
f.close()
issuer = '0098bef0-7b74c69c-0e12-4209-8e83-4455ccc3fa10'

""" Get list of holdings. """
payload = {'iss': issuer,
           'exp': datetime.datetime.utcnow() +
                  datetime.timedelta(days=0, seconds=30),
           'iat': datetime.datetime.utcnow()}
token = jwt.encode(payload, privateKey, 'RS512')
apiClient.set_default_header('Authorization', 'Bearer ' + token.decode())
holdingsResponse = holdingsApi.get_holding_type_list()
print(holdingsResponse)

""" Get all accounts. """
payload = {'account_id':'12006187',
           'sub': 'sbMemZHuBmwrwdcvYe1',
           'iss': issuer,
           'exp': datetime.datetime.utcnow() +
                  datetime.timedelta(days=0, seconds=30),
           'iat': datetime.datetime.utcnow()}
token = jwt.encode(payload, privateKey, 'RS512')
apiClient.set_default_header('Authorization', 'Bearer ' + token.decode())
accountsResponse = accountsApi.get_all_accounts()
print(accountsResponse)

""" Get historical balances. """
payload = {'account_id': 12006181,
	   'interval': 'D',
	   'to_date': '2015-09-02',
	   'from_date': '2015-09-01',
           'include_cf': 'True'}
token = jwt.encode(payload, privateKey, 'RS512')
apiClient.set_default_header('Authorization', 'Bearer ' + token.decode())
accountsResponse = accountsApi.get_historical_balances()
print(accountsResponse)
        
