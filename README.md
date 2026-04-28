# CIDR Explorer: Subnets & Supernets

A Streamlit-based interactive educational tool designed to help users master IP addressing, CIDR (Classless Inter-Domain Routing), and networking protocols like ARP and DHCP.

## Features

* **Theory Hub**: Comprehensive lessons on networking fundamentals, including the transition from Classful to Classless addressing and core protocols.
* **Interactive Explorer**: A visual tool to calculate total hosts, IP ranges, and subnet masks based on a user-provided IP and CIDR prefix.
* **Supernet Aggregator**: Automatically summarizes multiple contiguous subnets into the smallest possible route.
* **LPM Simulator**: Explains the "Longest Prefix Match" logic used by routers during packet forwarding.
* **CIDR Mastery Quiz**: A built-in assessment module with detailed explanations for every answer to reinforce learning.

## File Structure

* `cidrExplorer.py`: The main Streamlit application containing the UI logic and module definitions.
* `networkingUtils.py`: Helper functions for binary conversions and IP address processing.
* `quizData.py`: A structured repository of quiz questions, options, and educational explanations.
* `requirements.txt`: List of Python dependencies required to run the application.
* `favicon.png`: The application icon.

## Installation

1.  **Clone the repository** (or download the source files).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    streamlit run cidrExplorer.py
    ```

## Key Concepts Covered

* **Subnetting**: Formula for usable hosts: $2^{(32 - prefix)} - 2$.
* **Supernetting**: Rules for route aggregation (contiguity and power-of-two boundaries).
* **DORA Process**: The four-step handshake for DHCP.
* **ARP**: Layer 2 to Layer 3 address resolution via broadcasting.
* **Magic Number**: Using block sizes to quickly identify subnet increments.

## Dependencies

* `streamlit`: For the web interface.
* `pandas`: For data table rendering.
* `ipaddress`: For robust IP calculation and validation.