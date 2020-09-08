from IOSXE_restconf import restconfxe


# CREATE A DICTIONARY THAT SPECIFIES HOST, CREDENTIALS AND PORT
config = {
    'host': 'ios-xe-mgmt-latest.cisco.com',
    'port': '9443',
    'user': 'developer',
    'password': 'C1sco12345',
}

# INITIALIZE IOSXE_RESTONCONF OBJECT AS ROUTER
router = restconfxe.IosXe_RestConf(config)

# Three custom methods are provided in restconfxe.py
# as examples for how to programmatically interact with
# the RESTCONF API, the fourth method can be used to execute
# HTTP GET requests against any endpoint.
# To test new endpoints head to:
# https://github.com/YangModels/yang/tree/master/vendor/cisco/xe
# and cross reference the data models that you can retrieve
# from get_capabilities, look inside the data models at the names of containers
# to try and find endpoints to test. Not all models work with RESTCONF
# or have clear structure at this time for how to build your endpoints.


#GET NETCONF/RESTONF CAPABILITIES (available yang data models)

router.get_capabilities()

#VIEW THE ROUTING TABLE

router.get_routing()

#VIEW THE INTERRFACES

router.get_interfaces()

#EXECUTE A GET REQUEST AGAINST AN ARBITRARY ENDPOINT

request = router.get_request("Cisco-IOS-XE-arp-oper:arp-data")

# Get_request returns a Requests object that can be worked with using
# normal requests methods like .text and .json

print(request.text)