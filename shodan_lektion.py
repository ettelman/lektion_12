import shodan
import os
from dotenv import load_dotenv
import socket


load_dotenv()

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

api = shodan.Shodan(SHODAN_API_KEY)

# try:
#     info = api.info()
#     print(info)
# except shodan.APIError as e:
#     print(f"Error: {e}")

# try:
#     host_info = api.host("89.160.28.168")

#     print(f"Org: {host_info.get('org')}")
#     print(f"OS: {host_info.get('os')}")

#     for i in host_info['data']:
#         print(i)
# except shodan.APIError as e:
#     print(e)

# try:
#     top_services = api.services()

#     print("Services:")
#     for service, description in top_services.items():
#         print(f"Service: {service}, Description: {description}")

# except shodan.APIError as e:
#     print(e)


# try:
#     results = api.search("org:Microsoft")
#     print(f"Antal resultat: {results['total']}")
    
#     for result in results['matches'][:10]:
#         print(f"Port: {result['port']}")
# except shodan.APIError as e:
#     print(e)

try:
    results = api.search("http")

    print(results['total'])

    for result in results['matches'][:10]:
        ip = result['ip_str']
        print(f"IP: {ip}")

        try:
            domain = socket.gethostbyaddr(ip)
            print(f" - Domain: {domain[0]}")
        except socket.herror:
            print(f" - No domain found")
except shodan.APIError as e:
    print(e)