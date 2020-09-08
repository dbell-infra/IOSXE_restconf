import requests


class IosXe_RestConf():
    def __init__(self, config):
        self.config = config

    def get_request(self, endpoint):
        url = f"https://{self.config['host']}:{self.config['port']}/restconf/data/{endpoint}"

        headers = {
            "Accept": "application/yang-data+json",
            "Content-type": "application/yang-data+json"
        }

        response = requests.get(url=url,
                                headers=headers,
                                auth=(self.config['user'], self.config['password']),
                                verify=False)

        return response


    def get_capabilities(self):
        capabilities = self.get_request('netconf-state/capabilities').json()

        for cap in capabilities['ietf-netconf-monitoring:capabilities']['capability']:
            print(cap)

    def get_routing(self):
        request = self.get_request('ietf-routing:routing-state').json()

        data = request['ietf-routing:routing-state']['routing-instance'][0]['ribs']['rib']

        for table in data:
            table_name = table['name']
            address_family = table['address-family']
            print(f"Table Name: {table_name} \n"
                  f"Address Family: {address_family} \n")
            try:
                table_routes = table['routes']['route']
                print(f"Routes: \n")

                for route in table_routes:
                    destination_prefix = route['destination-prefix']
                    metric = str(route['metric'])
                    outbound_int = route['next-hop']['outgoing-interface']
                    next_hop = route['next-hop']['next-hop-address']
                    source_protocol = route['source-protocol']
                    print(f"  Desintation Prefix: {destination_prefix} \n"
                          f"    Next Hop: {next_hop} \n"
                          f"    Outbound Interface: {outbound_int} \n"
                          f"    Source: {source_protocol} \n"
                          f"    Metric: {metric} \n")

            except:
                pass
                print("  No routes found for this Address Family")

    def get_interfaces(self):
        request = self.get_request('ietf-interfaces:interfaces').json()
        print("Interfaces:")
        for interface in request['ietf-interfaces:interfaces']['interface']:
            name = interface['name']
            if "description" in interface.keys():
                description = interface['description']
            else:
                description = "None"

            if interface['enabled']:
                status = "Enabled"
            else:
                status = "Disabled"

            if interface['ietf-ip:ipv4'] != {}:
                ipv4_address = interface['ietf-ip:ipv4']['address'][0]['ip']
                ipv4_address_mask = interface['ietf-ip:ipv4']['address'][0]['netmask']
            else:
                ipv4_address = "Not"
                ipv4_address_mask = "configured"

            print(f"  Name: {name} \n"
                  f"    Description: {description} \n"
                  f"    Status: {status} \n"
                  f"    Address: {ipv4_address} {ipv4_address_mask} \n")
