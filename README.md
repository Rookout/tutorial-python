# Rookout official tutorial for using Python

[![CircleCI](https://circleci.com/gh/Rookout/tutorial-python/tree/master.svg?style=svg)](https://circleci.com/gh/Rookout/python/tree/master)
[![License][license-image]][license-url]
[![Docs][docs-image]][docs-url]
[![GitHub version][version-badge]](https://badge.fury.io/gh/rookout%2Ftutorial-python)

This is the official [rookout][rookout-getting-started] Python tutorial

- [Signup][rookout-signup]
- [Documentation][docs-url]
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Prerequisites

1. Python 2.7.14 or newer
1. Optional - Docker - https://www.docker.com/get-docker

## Installation

1. Clone this repo

```bash
git clone https://github.com/Rookout/tutorial-python.git
cd tutorial-python
``` 

1. Set your Rookout token in an ENV variable (replace **export** by **set** if on Windows)

```bash
export ROOKOUT_TOKEN=[Your Rookout Token]
```
     
1. Run the app

- Option 1 - Without Docker:

```bash
pip install -r requirements.txt
python app.py
```

- Option 2 - Running with docker

```bash
docker build . -t tutorial-python
docker run -p 5000:5000 -e ROOKOUT_TOKEN=$ROOKOUT_TOKEN tutorial-python
```

## Usage

- After running the app go to [https://app.rookout.com/][rookout-app-url] and **Log In**
- Add the source code according to the instructions using the left pane **Source View**

    <details>
    <summary>More details</summary>
    <p>
    
    #### Adding source code
    
    1. Click on Add source
    1. Choose source control
        - Github
            - Click on Connect
            - Authorize O-Auth
            - Fill `Repository Owner`
            - Click `Repository` and choose from the dropdown menu
            - Click Next
            - Choose the desired branch
            - Click View Repository
        - Local FileSystem - Server
            - Click on Setup Server
            - Choose a supported HTTP Server
            - Follow the on-screen instructions
    </p>
    </details>
    
    
- Open the file `app.py`
- Add a Dumpframe rule next to line number 74 by clicking next the the line number in the file viewer
- Looking at the right-hand pane **Rules**, you will see the rule you added, on what line you added it and it should be GREEN, meaning everything is communicating correctly.
    - If this is not the case, [click here](#rules-common-issues) to see how to fix that
- Go the the app webpage http://localhost:5000/ and add a todo in order to trigger the rule
- Check the bottom pane **Messages** and you'll see the dumpframe you just added, as it was triggered by the handler of the web api when you added a todo

Go through the [bug list](https://docs.rookout.com/docs/python-getting-started.html#bug-hunt) and follow instructions to see some basic use cases.

## Rules Common Issues

- Rule status is RED -- Hash mismatch. It means the file used in the server is not the same file used from github/local server in app.rookout.com
- Rule status is GRAY -- No rook connected. Make sure you have inserted the token in the right place and that connection is made properly.

## Want to learn more ?

- [Our documentation][docs-url] for more information
- [our deployment examples][deployment-examples] for platform-specific integration examples

## License
[APACHE 2](LICENSE)

[version-badge]: https://badge.fury.io/gh/rookout%2Ftutorial-python.svg
[license-url]: LICENSE
[docs-url]: https://docs.rookout.com/
[rookout-getting-started]: https://docs.rookout.com/docs/introduction.html
[rookout-signup]: https://www.rookout.com/trial/
[docs-image]: https://img.shields.io/badge/docs-latest-blue.svg
[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[rookout-app-url]: https://app.rookout.com/
[deployment-examples]: https://github.com/Rookout/deployment-examples
