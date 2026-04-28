import streamlit as st
import ipaddress
import pandas as pd
from networkingUtils import hex_to_ip, ip_to_binary_string
from quizData import MASTER_QUIZ

st.set_page_config(page_title="CIDR Explorer", page_icon="favicon.png", layout="wide")

# APP NAVIGATION
st.title("CIDR Explorer: Subnets & Supernets")
mode = st.sidebar.selectbox("Select a Module", 
    ["Theory Hub", "Interactive Explorer", "Supernet Aggregator", "Longest Prefix Match (LPM)", "Quiz Zone"])

# tabs

# 1. THEORY HUB 
if mode == "Theory Hub":
    st.header("Networking Theory Hub")
    
    # Create tabs for different study topics
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Subnets & Supernets", "Classful vs. CIDR", "ARP & DHCP", "Exam Prep", "External Resources"])
    
    with tab1:
        st.subheader("Subnetting & Supernetting")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**What is Subnetting?**")
            st.write("""
            Subnetting is the process of stealing bits from the Host portion of an IP address 
            to create smaller sub-networks.
            
            * Goal: Reduce broadcast traffic and improve security.
            * The Math: Every bit you steal doubles the number of networks and halves the number of hosts.
            """)
            st.latex(r"Hosts = 2^{(32 - prefix)} - 2")
            
        with col2:
            st.markdown("**What is Supernetting?**")
            st.write("""
            Also called Route Summarization, this combines multiple contiguous networks 
            into one single advertisement.
            
            * Goal: Minimize router CPU usage and routing table size.
            * The Rule: Networks must be adjacent and start on a proper binary boundary.
            """)

        with st.expander("See the Binary Secret"):
            st.write("IP addresses are just 32 bits. The CIDR /number tells the router exactly where the 'cut' is.")
            st.code("Example /24: [11111111.11111111.11111111] . [00000000]\n"
                    "                  Network (24 bits)        Host (8 bits)")

    with tab2:
        st.subheader("The Evolution of IP Allocation")
        
        st.markdown("#### The Legacy: Classful Addressing")
        st.write("""
        Originally, IP addresses were divided into rigid classes based on the first few bits. 
        This determined the default subnet mask and the maximum number of hosts.
        """)
        
        class_data = {
            "Class": ["A", "B", "C"],
            "First Octet Range": ["1 - 126", "128 - 191", "192 - 223"],
            "Default Mask": ["255.0.0.0 (/8)", "255.255.0.0 (/16)", "255.255.255.0 (/24)"],
            "Max Hosts": ["16,777,214", "65,534", "254"]
        }
        st.table(pd.DataFrame(class_data))
        
        st.error("**The Problem:** Classful boundaries were inefficient. If a company needed 500 IPs, a Class C was too small, so they were given a Class B, wasting over 65,000 addresses.")
        
        st.markdown("#### The Solution: CIDR")
        st.success("""
        **Classless Inter-Domain Routing (CIDR)** abolished the rigid A/B/C classes. It introduced 
        Variable-Length Subnet Masking (VLSM), allowing engineers to place the network/host boundary 
        anywhere using a prefix length (e.g., /22 or /27), drastically improving IP allocation efficiency.
        """)
        st.subheader("CIDR Notation & Binary Conversion")
        st.write("""
        In CIDR, subnet masks are denoted by /X. For example, a subnet of 255.255.255.0 is denoted by /24. 
        To calculate a subnet mask in CIDR, convert each octet into its binary value and count the 1s:
        """)
        
        st.code("""
        Subnet Mask: 255.255.255.0
        
        First Octet:  255 -> 11111111 (8 ones)
        Second Octet: 255 -> 11111111 (8 ones)
        Third Octet:  255 -> 11111111 (8 ones)
        Fourth Octet: 0   -> 00000000 (0 ones)
        
        Total = 24 binary 1s -> /24
        """)
        
        st.info("""
        **The Contiguous Rule:** When creating a network in CIDR, the masks must be contiguous 1s from left to right. A mask like `10111111.X.X.X` cannot exist. 
        
        With CIDR, we can use Variable Length Subnet Masks (VLSM), drastically reducing IP address waste. The divider between the network and host portions does not have to sit on an 8-bit octet boundary. For example, a mask like `255.224.0.0` (`11111111.11100000.00000000.00000000`) is perfectly valid.
        """)

        st.markdown("---")
        st.subheader("Classful vs. Classless Addressing Comparison")
        st.write("A definitive breakdown of legacy class-based routing versus modern CIDR implementation.")
        
        # GeeksforGeeks Comparison Table
        comparison_data = {
            "Parameter": [
                "Basics", 
                "Network ID & Host ID", 
                "VLSM", 
                "Bandwidth", 
                "CIDR", 
                "Routing Updates", 
                "Troubleshooting", 
                "Division of Address"
            ],
            "Classful Addressing": [
                "IP addresses are allocated according to strict classes (A to E).",
                "The boundary between Network ID and Host ID depends entirely on the class.",
                "Does not support Variable Length Subnet Mask (VLSM).",
                "Requires more bandwidth; becomes slower and more expensive.",
                "Does not support Classless Inter-Domain Routing (CIDR).",
                "Relies on regular or periodic routing updates.",
                "Easier to detect problems due to the rigid division of network and host parts.",
                "Network, Host"
            ],
            "Classless Addressing": [
                "Replaced classful addressing to prevent the exhaustion of IPv4 addresses.",
                "There is no restriction of class; the boundary can sit anywhere.",
                "Fully supports Variable Length Subnet Mask (VLSM).",
                "Requires less bandwidth; faster and less expensive routing overhead.",
                "Built entirely around Classless Inter-Domain Routing (CIDR).",
                "Utilizes triggered routing updates.",
                "More complex to troubleshoot due to fluid and variable boundaries.",
                "Subnet, Host"
            ]
        }
        
        st.table(pd.DataFrame(comparison_data))

    with tab3:
        st.subheader("Essential Core Protocols")
        
        col_arp, col_dhcp = st.columns(2)
        
        with col_arp:
            st.markdown("#### ARP (Address Resolution Protocol)")
            st.write("""
            ARP bridges Layer 3 (Network) to Layer 2 (Data Link). It maps a known IP address to an unknown MAC address.
            """)
            st.info("""
            **How it works:**
            If Host A wants to talk to Host B on the same LAN but doesn't have Host B's MAC address in its ARP cache, 
            Host A sends an ARP Request as a **broadcast frame** (FF:FF:FF:FF:FF:FF) asking: 
            'Who has this IP? Tell Host A.'
            """)
            
        with col_dhcp:
            st.markdown("#### DHCP (Dynamic Host Configuration Protocol)")
            st.write("""
            DHCP automates the assignment of IP addresses, subnet masks, default gateways, and DNS servers to devices on a network.
            """)
            st.info("""
            **The DORA Process:**
            1. **Discover:** Client broadcasts seeking a DHCP server.
            2. **Offer:** Server offers an IP address.
            3. **Request:** Client requests the offered IP.
            4. **Acknowledge:** Server confirms the lease.
            """)

    with tab4:
        st.subheader("Exam Prep: How to Solve It")
        st.write("A guide for the core calculations found in the Quiz Zone.")

        with st.expander("1. Calculating Usable Hosts"):
            st.write("Whenever asked for the number of usable hosts, use this formula:")
            st.latex(r"Usable\ Hosts = 2^{(32 - prefix)} - 2")
            st.markdown("""
            **Why subtract 2?**
            * The first address (all 0s in the host portion) is reserved for the **Network ID**.
            * The last address (all 1s in the host portion) is reserved for the **Broadcast Address**.
            
            **Example:** A /30 network has $32 - 30 = 2$ host bits. 
            $2^2 - 2 = 2$ usable hosts. (Perfect for point-to-point router links).
            """)

        with st.expander("2. Finding the Magic Number (Block Size)"):
            st.write("The Magic Number tells you exactly how subnets increment. To find it, subtract the 'interesting' octet of the subnet mask from 256.")
            st.markdown("""
            **Example:** Subnet mask 255.255.255.192.
            * The interesting octet is 192.
            * $256 - 192 = 64$.
            * The subnets will increment by 64: .0, .64, .128, .192.
            """)

        with st.expander("3. Creating Equal-Sized Subnets (Borrowing Bits)"):
            st.write("If you are given a prefix (like /24) and need to create a specific number of smaller subnets, find out how many bits to borrow using powers of 2.")
            st.latex(r"2^{borrowed\_bits} \ge required\_subnets")
            st.markdown("""
            **Example:** You have a /24 and need 8 subnets.
            * $2^3 = 8$. You must borrow 3 bits.
            * New Prefix: $24 + 3 = 27$.
            * The new mask (/27) turns on 3 bits in the last octet (`11100000`), which equals 224.
            """)

        with st.expander("4. Route Aggregation (Supernetting) Rules"):
            st.write("To summarize multiple networks into one routing table entry, you move the prefix to the left (make the number smaller).")
            st.markdown("""
            **The Process:**
            1. Count the number of networks you are summarizing (must be a power of 2, like 2, 4, 8, 16).
            2. Determine the power of 2. (e.g., 4 networks = $2^2$).
            3. Subtract that exponent from the prefix length.
            
            **Example:** Summarize four /24 networks.
            * 4 networks = $2^2$.
            * $24 - 2 = 22$.
            * The summary prefix is /22.
            
            **Strict Rule:** Networks must be contiguous and align on a shared binary boundary. You cannot summarize 192.168.1.0/24 and 10.0.0.0/24.
            """)

        with st.expander("5. Identifying Classful IP Ranges"):
            st.write("Before CIDR, IP addresses were categorized by their first octet value.")
            st.markdown("""
            * **Class A (1-126):** /8 default mask. Used for massive networks.
            * **Class B (128-191):** /16 default mask. Used for medium/large networks.
            * **Class C (192-223):** /24 default mask. Used for small networks (max 254 hosts).
            """)

        with st.expander("6. Binary Mask Conversions"):
            st.write("You must know the decimal values of bits turned on from left to right in an octet.")
            st.markdown("""
            * 1 bit  (`10000000`) = 128
            * 2 bits (`11000000`) = 192
            * 3 bits (`11100000`) = 224
            * 4 bits (`11110000`) = 240
            * 5 bits (`11111000`) = 248
            * 6 bits (`11111100`) = 252
            """)

    with tab5:
        st.subheader("External Resources")
        st.write("Here are some useful links to learn more about CIDR and subnetting:")
        st.markdown("- [Flackbox CIDR Tutorial](https://www.flackbox.com/cisco-cidr-classless-inter-domain-routing)")
        st.markdown("- [Subnetting Practice Problems](https://www.subnetting.net/Subnetting.aspx?mode=practice)")
        st.markdown("- [GeeksforGeeks - Classful vs. Classless](https://www.geeksforgeeks.org/computer-networks/classful-vs-classless-addressing/)")
        st.markdown("- [Subnetting Mastery Playlist](https://www.youtube.com/playlist?list=PLIFyRwBY_4bQUE4IB5c4VPRyDoLgOdExE)")

# 2. INTERACTIVE EXPLORER
elif mode == "Interactive Explorer":
    st.header("Subnet Explorer")
    c1, c2 = st.columns([1, 2])
    with c1:
        ip_in = st.text_input("Base IP", "172.16.0.0")
        cid_in = st.slider("Prefix", 8, 30, 24)
    
    try:
        net = ipaddress.ip_network(f"{ip_in}/{cid_in}", strict=False)
        with c2:
            st.metric("Total Hosts", net.num_addresses)
            st.write(f"Range: {net[0]} to {net[-1]}")
            st.write(f"Mask: {net.netmask}")
    except ValueError as e:
        st.error(f"Invalid Input: {e}")

# 3. SUPERNET AGGREGATOR
# may remove this
elif mode == "Supernet Aggregator":
    st.header("Route Aggregator")
    st.write("Enter multiple contiguous subnets. The aggregator will find the smallest possible summary address that covers all of them.")
    
    nets_in = st.text_area("Paste subnets here:", "10.0.0.0/24\n10.0.1.0/24\n10.0.2.0/24\n10.0.3.0/24", height=150)
    
    if st.button("Summarize"):
        try:
            n_list = sorted([ipaddress.ip_network(n.strip()) for n in nets_in.split('\n') if n.strip()])
            collapsed = list(ipaddress.collapse_addresses(n_list))
            
            st.subheader("Results")
            for c in collapsed:
                st.success(f"Summary Route: {c}")
                
            st.markdown("---")
            st.subheader("How Routes are Aggregated")
            st.write("""
            Supernetting works by finding the **Longest Common Matching Bits** from left to right. 
            To successfully summarize networks, they must meet two rules:
            1. They must be contiguous (adjacent to one another).
            2. The total number of addresses must be a power of two (2, 4, 8, 16, etc.) so they fit into a new binary boundary.
            """)
            
            st.write("**Binary Breakdown:**")
            st.write("Look at the binary representation of your networks below. The new summary mask is drawn exactly where the bits stop matching.")
            
            binary_data = []
            for net in n_list:
                full_bin = ip_to_binary_string(net)
                formatted_bin = f"{full_bin[0:8]}.{full_bin[8:16]}.{full_bin[16:24]}.{full_bin[24:32]}"
                binary_data.append({
                    "Original Network": str(net),
                    "Binary Representation": formatted_bin
                })
                
            st.table(pd.DataFrame(binary_data))
            
            if len(collapsed) == 1:
                summary_prefix = collapsed[0].prefixlen
                st.info(f"Notice how the first **{summary_prefix}** bits are identical across all the networks above. That is why the summary route is a /{summary_prefix}.")
            else:
                st.warning("Because your inputted networks were either not contiguous or not a power of two, they could not be summarized into a single route. The router must keep multiple entries.")

        except Exception as e:
            st.error(f"Invalid input: {e}")

# 4. LONGEST PREFIX MATCH (LPM)
elif mode == "Longest Prefix Match (LPM)":
    st.header("Longest Prefix Match (LPM)")
    st.write("When a router receives a packet, it must decide where to send it by comparing the destination IP address against its routing table. To do this, the router uses a mathematical operation called a Bitwise AND.")

    st.subheader("The Secret: The Bitwise AND Operation")
    st.write("When a router evaluates an IP address against a Subnet Mask, it compares them in binary bit-by-bit.")
    st.markdown("""
    * If both bits are `1`, the result is `1`.
    * Otherwise, the result is `0`.
    """)
    
    st.write("**The Human Shortcut:**")
    st.markdown("""
    * Any octet matched against `255` stays exactly the same.
    * Any octet matched against `0` becomes `0`.
    * You only need to do binary math on the 'interesting octet' (the one that is not 255 or 0).
    """)

    st.subheader("Subnet Mask Conversion Chart (3rd Octet Focus)")
    st.write("To understand which mask is the Longest Prefix, you look at how many 1s are in the subnet mask. The mask with the most consecutive 1s is the most specific route.")
    
    chart_data = {
        "Decimal Mask": ["255.255.255.0", "255.255.254.0", "255.255.252.0", "255.255.248.0", "255.255.240.0"],
        "Binary Equivalent": ["11111111", "11111110", "11111100", "11111000", "11110000"],
        "CIDR Notation": ["/24", "/23", "/22", "/21", "/20"],
        "Block Size": [1, 2, 4, 8, 16]
    }
    st.table(pd.DataFrame(chart_data))

    st.subheader("Step-by-Step Breakdown")

    st.markdown("#### Example A: Single Match")
    st.write("**Destination IP:** 128.96.171.92")
    st.code("Test against 255.255.254.0 mask:\n171 in binary: 10101011\n254 in binary: 11111110\nAND Result:    10101010 (170 in decimal)")
    st.write("**Result:** 128.96.170.0. Matches the routing table. Forwards to Interface 0.")

    st.markdown("#### Example B: Multiple Matches")
    st.write("**Destination IP:** 128.96.167.151")
    st.code("Test 1: Against mask 255.255.254.0 (/23)\nResult: 128.96.166.0 (Match for Router 2)")
    st.code("Test 2: Against mask 255.255.252.0 (/22)\nResult: 128.96.164.0 (Match for Router 3)")
    st.write("**Decision:** Both match, but /23 is a longer prefix than /22. Forwards to Router 2.")

# 5. QUIZ ZONE
else:
    st.header("The CIDR Mastery Quiz")
    st.write("Test your networking knowledge. Select an answer and submit to see the detailed explanation.")

    # Initialize session state variables for the quiz
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.session_state.selected_option = None

    if st.session_state.quiz_index < len(MASTER_QUIZ):
        current_q = MASTER_QUIZ[st.session_state.quiz_index]
        st.subheader(f"Question {st.session_state.quiz_index + 1} of {len(MASTER_QUIZ)}")
        st.write(current_q["q"])
        
        user_choice = st.radio("Select an answer:", current_q["options"], index=None, key=f"q_{st.session_state.quiz_index}")
        
        if not st.session_state.submitted:
            if st.button("Submit Answer"):
                if user_choice is not None:
                    st.session_state.selected_option = user_choice
                    st.session_state.submitted = True
                    if user_choice == current_q["answer"]:
                        st.session_state.score += 1
                    st.rerun()
                else:
                    st.warning("Please select an answer before submitting.")
        else:
            if st.session_state.selected_option == current_q["answer"]:
                st.success("Correct")
            else:
                st.error(f"Incorrect. The correct answer was: {current_q['answer']}")
            
            st.info(f"Explanation: {current_q['explanation']}")
            
            if st.button("Next Question"):
                st.session_state.quiz_index += 1
                st.session_state.submitted = False
                st.session_state.selected_option = None
                st.rerun()
    else:
        st.subheader("Quiz Complete")
        st.write(f"Your final score is {st.session_state.score} out of {len(MASTER_QUIZ)}.")
        
        # Calculate grade
        percentage = (st.session_state.score / len(MASTER_QUIZ)) * 100
        if percentage >= 80:
            st.success("Excellent work. You have a strong grasp of CIDR concepts.")
        elif percentage >= 60:
            st.warning("Good job, but a quick review of the Theory Hub might help solidify some concepts.")
        else:
            st.error("Keep practicing. Use the Interactive Explorer to visualize how these boundaries work.")
            
        if st.button("Retake Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            st.session_state.submitted = False
            st.session_state.selected_option = None
            st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Tip: Use the slider in Explorer mode to see how masks change in real-time.")