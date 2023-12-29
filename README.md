# Down Detector

A Monitoring Application that pings a remote IP and notifies the user via email if the site cannot be reached. 

## Table of Contents

- [Down Detector](#down-detector)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Installation](#installation)
    - [Device must have Python3 installed.](#device-must-have-python3-installed)
  - [Usage](#usage)
    - [How to start and stop your Down Detector](#how-to-start-and-stop-your-down-detector)
  - [Contributing](#contributing)

## About

Down Detector is used to monitor a remote site via its public IP address. Its an easy to use and install monitoring tool. Simply clone the repo, edit the config file and run start.sh. Works on Windows & Linux.

## Installation


### Device must have Python3 installed.

For Windows: [Download](https://www.python.org/downloads/)

For Linux: Most Distros have Python3 by default. If yours doesnt. Please use your package manage __apt, dnf, yum__ etc. To install it.

```bash
# Clone the repository
git clone https://github.com/lilrebel17/down-detector.git

# Edit Config File to suit your needs see config section for more info
cd down-detector
nano ./config.cfg
```
## Usage
### How to start and stop your Down Detector

```
#Run the program with start script
#For Linux:
bash start.sh

#For Windows:
./start.bat

#If you need to stop the program. Run the stop script
#For Linux:
bash stop.sh

#For Windows:
./stop.bat
```

## Contributing

Contributions are welcome! Here's how you can contribute:

- Report bugs by opening issues.
- Suggest new features or enhancements through issues.
- Submit pull requests