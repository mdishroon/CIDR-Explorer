import ipaddress

def hex_to_ip(hex_str):
    try:
        parts = hex_str.strip().split('.')
        decimal_parts = [str(int(p, 16)) for p in parts]
        return ".".join(decimal_parts)
    except ValueError:
        return None

def ip_to_binary_string(ip_net):
    return f"{int(ip_net.network_address):032b}"