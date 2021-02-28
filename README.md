# Rookout tutorial for debugging Python applications

[![CircleCI](https://circleci.com/gh/Rookout/tutorial-python/tree/master.svg?style=svg)](https://circleci.com/gh/Rookout/python/tree/master)
[![License][license-image]][license-url]
[![Docs][docs-image]][docs-url]
[![GitHub version][version-badge]](https://badge.fury.io/gh/rookout%2Ftutorial-python)

A sample app for debugging Python using [Rookout][rookout-getting-started].

## Helpful links:

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Sign up to Rookout][rookout-signup]
- [Online Documentation][docs-url]


## Prerequisites

1. Python 3.5 - 3.8
2. pip
3. Optional - Docker - https://www.docker.com/get-docker

## Setup

3. Clone the sample app from this repository:

```bash
git clone https://github.com/Rookout/tutorial-python.git
cd tutorial-python
``` 

4. Set your Rookout token as an environment variable (for Windows, use ***set*** instead of **export**)

```bash
export ROOKOUT_TOKEN=[Your Rookout Token]
```
     
5. Run the app:

```bash
pip install -r requirements.txt
python app.py
```

- Optional - Run the app using Docker:

```bash
docker run -p 5000:5000 -e ROOKOUT_TOKEN=$ROOKOUT_TOKEN rookout/tutorial-python
```

## Usage

- Log in to [the Rookout IDE][rookout-app-url].
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
- Add a Breakpoint next to line number 84 by clicking next the the line number in the file viewer
- The Breakpoint should turn solid purple, indicating that it has been set successfully and that it is active.
    - If this is not the case, [click here](https://docs.rookout.com/docs/breakpoints-status.html) to see how to fix that
- Go the the app webpage http://localhost:5000/ and add a todo in order to trigger the Breakpoint
- Check the bottom pane **Messages** and you'll see the snapshot you just added, as it was triggered by the handler of the web api when you added a todo

Go through the [bug list](https://docs.rookout.com/docs/sample-applications.html#bug-hunt) and follow instructions to see some basic use cases.

## Common Pitfalls

- Breakpoint status is pending (hollow with purple outline) -- Connection to the app was not able to be established. Make sure that you inserted the Rookout Token in the right place and that the SDK was properly installed.
- Breakpoing status is disabled (hollow with gray outline) -- The breakpoint was disabled from collecting more data due to the limits being hit.
- Brekapoint error -- something went wrong. Check the breakpoint status to get more information on the error type, and for more information go to our [breakpoint status guide][https://docs.rookout.com/docs/breakpoints-status/].

## Want to learn more ?

- [Our documentation][docs-url] for more information
- [our deployment examples][deployment-examples] for platform-specific integration examples

## License
[APACHE 2](LICENSE)

[version-badge]: https://badge.fury.io/gh/rookout%2Ftutorial-python.svg
[license-url]: LICENSE
[docs-url]: https://docs.rookout.com/
[rookout-getting-started]: https://docs.rookout.com/docs/welcome.html
[rookout-signup]: https://www.rookout.com/trial/
[docs-image]: https://img.shields.io/badge/docs-latest-blue.svg
[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[rookout-app-url]: https://app.rookout.com/
[deployment-examples]: https://github.com/Rookout/deployment-examples
