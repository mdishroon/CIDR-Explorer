MASTER_QUIZ = [
    {
        "q": "If you have a network address of 192.168.1.0/24, how many usable host addresses are available?",
        "options": ["126", "254", "255", "256"],
        "answer": "254",
        "explanation": "In a /24 network, there are 256 total addresses, but we subtract 2 for the network and broadcast addresses."
    },
    {
        "q": "Which CIDR prefix would you use to aggregate two contiguous /24 networks into a single supernet?",
        "options": ["/16", "/22", "/23", "/25"],
        "answer": "/23",
        "explanation": "Moving the mask one bit to the left doubles the address space, allowing two /24 blocks to be summarized."
    },
    {
        "q": "True or False: Any two /24 networks can be combined into a /23 supernet regardless of their IP range.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Supernetting requires networks to be contiguous and align on a specific binary boundary."
    },
    {
        "q": "What is the 'Magic Number' (the block size increment) for a subnet mask of 255.255.255.192?",
        "options": ["16", "32", "64", "128"],
        "answer": "64",
        "explanation": "The last octet (192) subtracted from 256 gives 64, which is the size of each subnet block."
    },
    {
        "q": "In the IP address 172.16.10.0/20, which octet contains the boundary between the network and host portions?",
        "options": ["First Octet", "Second Octet", "Third Octet", "Fourth Octet"],
        "answer": "Third Octet",
        "explanation": "The first 16 bits cover the first two octets; bits 17-20 fall within the third octet."
    },
    {
        "q": "Which of the following is the valid broadcast address for 192.168.5.0/24?",
        "options": ["192.168.5.0", "192.168.5.1", "192.168.5.254", "192.168.5.255"],
        "answer": "192.168.5.255",
        "explanation": "In a /24, the entire last octet is used for hosts, and the all-ones address (255) is the broadcast."
    },
    {
        "q": "If you collapse 10.0.0.0/24, 10.0.1.0/24, 10.0.2.0/24, and 10.0.3.0/24, what is the resulting supernet?",
        "options": ["10.0.0.0/21", "10.0.0.0/22", "10.0.0.0/23", "10.0.0.0/24"],
        "answer": "10.0.0.0/22",
        "explanation": "These four /24 networks are contiguous and perfectly fit into a /22 block, which is 4 times larger than a /24."
    },
    {
        "q": "What is the binary representation of the decimal value 192 used in subnet masks?",
        "options": ["10000000", "11000000", "11100000", "11110000"],
        "answer": "11000000",
        "explanation": "192 is 128 + 64, which corresponds to the first two bits being set to 1."
    },
    {
        "q": "Why would a network engineer use supernetting (route summarization)?",
        "options": ["To increase the number of available public IPs", "To slow down network traffic for security", "To reduce the size of routing tables", "To prevent subnets from communicating"],
        "answer": "To reduce the size of routing tables",
        "explanation": "By summarizing many routes into one, routers consume less memory and process updates faster."
    },
    {
        "q": "A /30 subnet is commonly used for point-to-point links. How many usable host addresses does it provide?",
        "options": ["1", "2", "4", "6"],
        "answer": "2",
        "explanation": "A /30 has 4 total addresses; subtracting the network and broadcast addresses leaves 2 usable IPs for the routers on each end."
    },
    {
        "q": "A legacy router using classful routing receives a packet with destination IP: 197.28.46.9. Which of the following statements is correct?",
        "options": [
            "It belongs to a Class B network with up to 65,534 hosts.",
            "It belongs to a Class C network with up to 254 hosts.",
            "It belongs to a Class A network with up to 16,777,214 hosts.",
            "It belongs to a Class B network with up to 16,382 hosts."
        ],
        "answer": "It belongs to a Class C network with up to 254 hosts.",
        "explanation": "The first octet (197) falls into the Class C range (192-223). Class C networks use 8 bits for hosts, allowing 2^8 - 2 = 254 usable addresses."
    },
    {
        "q": "Classful addressing caused several inefficiencies in IP allocation. Which correctly identifies a limitation and how CIDR resolves it?",
        "options": [
            "Classful addressing allowed route aggregation, but CIDR removed this to improve routing precision.",
            "Classful addressing caused fixed network boundaries leading to inefficient address utilization, which CIDR mitigates through variable-length subnet masking.",
            "Classful addressing prevented use of private IP ranges, while CIDR introduced them to enable NAT.",
            "Classful addressing limited hosts per network to 65,536, while CIDR expanded this to any arbitrary number."
        ],
        "answer": "Classful addressing caused fixed network boundaries leading to inefficient address utilization, which CIDR mitigates through variable-length subnet masking.",
        "explanation": "CIDR allows the boundary between network and host bits to occur anywhere, stopping the massive waste of IPs caused by rigid Class A, B, and C rules."
    },
    {
        "q": "An ISP owns the address block 192.168.0.0/22. How many Class C (/24) sized networks are summarized in this /22 prefix?",
        "options": ["2", "4", "8", "16"],
        "answer": "4",
        "explanation": "The difference between /24 and /22 is 2 bits. 2^2 = 4, meaning four /24 networks can be summarized into a single /22."
    },
    {
        "q": "You have a Class C network, 192.168.10.0/24, which has 8 equal-sized subnets. What prefix length should you use to aggregate, and what is the subnet mask?",
        "options": [
            "255.255.255.240 -> /28",
            "255.255.255.252 -> /30",
            "255.255.255.248 -> /29",
            "255.255.255.224 -> /27"
        ],
        "answer": "255.255.255.224 -> /27",
        "explanation": "To create 8 subnets, you borrow 3 bits (2^3 = 8). 24 + 3 = 27. The last octet binary is 11100000, which is 224 in decimal."
    },
    {
        "q": "A router has routes to 172.16.0.0/24, 172.16.1.0/24, 172.16.2.0/24, and 172.16.3.0/24. What is the single aggregated prefix that replaces them?",
        "options": [
            "172.16.0.0/23",
            "172.16.0.0/21",
            "172.16.0.0/22",
            "172.16.0.0/20"
        ],
        "answer": "172.16.0.0/22",
        "explanation": "Aggregating 4 networks requires moving the mask left by 2 bits (since 2^2 = 4). /24 minus 2 = /22."
    },
    {
        "q": "Host A (192.168.1.10) wants to send a packet to Host B (192.168.1.20). Host A does not have Host B's MAC address in its ARP cache. What happens next?",
        "options": [
            "Host A sends an ARP request as a unicast frame to Host B.",
            "Host A sends an ARP request as a broadcast frame to all hosts in the LAN.",
            "Host A sends an ICMP echo request to learn Host B's MAC address.",
            "The switch assigns a MAC address dynamically to Host B and updates Host A."
        ],
        "answer": "Host A sends an ARP request as a broadcast frame to all hosts in the LAN.",
        "explanation": "Because Host A doesn't know the destination MAC address, it must broadcast an ARP request asking the entire network, 'Who has this IP address?'"
    }
]