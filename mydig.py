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
            # can't find a IPv4 address in additional
            server = str(query.authority[0]).split()
            _, address = dns_lookup(server[-1])
            next_location = str(address[0]).split()[-1]
        query = dns.query.udp(message, next_location)
        
    answers = query.answer
    answer = str(query.answer[0]).split()
    if answer[-2] != 'A':
        _, additional_answers = dns_lookup(answer[-1])
        answers += additional_answers # list

    return message.question[0], answers


if __name__ == '__main__':
    import sys
    import time
    if len(sys.argv) > 1:
        site = sys.argv[1]
        start = time.time()
        question, answers = dns_lookup(site)
        end = time.time()
        answers = '\n'.join([str(entry) for entry in answers])
        print(f"QUESTION SECTION: \n{question}\n")
        print(f"ANSWER SECTION: \n{answers}\n")
        print(f"Query time: {int(1000*(end-start))} msec")
        print(f"WHEN: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")