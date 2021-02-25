import dns.message
import dns.query

ROOT_IP_A = "198.41.0.4"
SITE = "www.cnn.com"

def dns_lookup(site):
    message = dns.message.make_query(site, 'A')
    # contact the root server
    query = dns.query.udp(message, ROOT_IP_A)
    # if there are no answers keep querying
    while len(query.answer) == 0:
        # get the next server to query
        servers = list(query.additional)
        next_location = ""
        for server in servers:
            entry = str(server).split()
            if entry[-2] == 'A':
                next_location = entry[-1]
                break
        if next_location == "":
            return -1
        query = dns.query.udp(message, next_location)
    return query


if __name__ == '__main__':
    import sys
    import time
    if len(sys.argv) > 1:
        site = sys.argv[1]
        start = time.time()
        result = dns_lookup(site)
        end = time.time()
        print(f"QUESTION SECTION: \n{result.question[0]}\n")
        print(f"ANSWER SECTION: \n{result.answer[0]}\n")
        print(f"Query time: {end-start:.2}")
        print(f"WHEN: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")