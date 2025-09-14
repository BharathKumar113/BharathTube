# BharathTube

## Overview

**BharathTube** is a lightweight, self-hosted file sharing and streaming tool built with Python and Flask. It allows users to share, stream, and download media directly over a local network without relying on third-party cloud services. This makes it a simple and effective alternative to cloud storage when working in the same Wi-Fi/LAN environment.

## Why This Project?

Cloud storage platforms (Google Drive, Dropbox, etc.) often require internet access, account logins, and storage limits. BharathTube solves this by enabling direct peer-to-peer sharing over a local network:

* No cloud dependency
* Unlimited file sharing (restricted only by your device storage)
* Faster transfers since files don’t leave the local network
* Simple setup using only Python

## How It Works

1. The project runs a **Flask web server** on your machine.
2. Files inside the `uploads/` directory (or those you add via the interface) are made available through the server.
3. The server’s IP and port are displayed so others on the same Wi-Fi/LAN can access your files.
4. Users can **stream videos, preview media, or download files** directly through their browser.

## Features

* Upload and share files easily
* Stream media (like a local YouTube alternative)
* Direct download links
* QR code for quick mobile access
* Works entirely offline in a local network

## Installation

### Prerequisites

* Python 3.8+
* pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/BharathTube.git
cd BharathTube

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

## How to Use

1. Run the Flask server using the command above.
2. Note the local IP address and port shown in the terminal (e.g., `http://192.168.1.100:5000`).
3. On any other device connected to the **same Wi-Fi/LAN**, open a browser and visit the displayed link.
4. Upload, stream, or download files directly.

### Connecting from Other Devices

* Find the IP address of your hosting machine using:

  ```bash
  ipconfig   # on Windows
  ifconfig   # on Linux/Mac
  ```
* Replace `127.0.0.1` in the URL with your local IP so others can connect.
* Example: `http://192.168.1.100:5000`

## Alternative to Cloud

* No internet required → Perfect for offline environments
* Instant sharing in classrooms, offices, or home networks
* Your data never leaves your device → Full privacy
* Unlimited storage (limited only by your hard drive)

## Example Use Cases

* Share movies, songs, or documents with friends on the same Wi-Fi
* Stream videos on your phone hosted from your laptop
* Quickly send large files without USB drives or third-party services

## Future Improvements

* User authentication
* File organization and search
* Mobile-friendly UI
* Encrypted transfer option
