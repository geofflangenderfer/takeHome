from xml.dom import minidom
from pprint import pprint

class AbodoFeed:
    def __init__(self, xml_file):
        self.feed = minidom.parse(xml_file)
        self.properties = self.get_properties()

    def get_node(self, node_name, pid):
        out = None
        for node in pid.childNodes:
            if type(node).__name__ == "Element" and node.tagName == node_name:
                out = node
                break

        return out

    def get_city(self, pid):
        address = self.get_node("Address", pid)
        city = self.get_node("City", address)

        return city.childNodes[0].nodeValue

    def get_desired_data(self, pid):
        property_id = self                   \
            .get_node("Identification", pid) \
            .getAttribute("IDValue")
        name = self                          \
            .get_node("MarketingName", pid)  \
            .childNodes[0]                   \
            .nodeValue
        email = self                         \
            .get_node("Email",pid)           \
            .childNodes[0]                   \
            .nodeValue

        return {
                "property_id" : property_id,
                "name"        : name,
                "email"       : email
        }

    def get_madison_pids(self, pids):
        out = []
        for pid in pids:
            city = self.get_city(pid)
            if city == "Madison":
                out.append(pid)

        return out

    def get_properties(self):
        property_ids = self.feed.getElementsByTagName('PropertyID')
        madison_pids = self.get_madison_pids(property_ids)
        properties = []
        for pid in madison_pids:
            data = self.get_desired_data(pid)
            properties.append(data)

        return properties

if __name__ == "__main__":
    XML = 'feed.xml'
    feed = AbodoFeed(XML)
    pprint(feed.properties)
