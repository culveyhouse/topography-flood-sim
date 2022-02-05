# topography-flood-sim

## Table of Contents
[Synopsis](#synopsis)  
[Built With](#built-with)  
[Environment and Methods Used](#environment-and-methods-used)  
[How To Use This Project](#how-to-use-this-project)  
[Express Installation of Python Environment](#express-installation-of-python-environment)  
[Verbose Installation of Python Environment](#verbose-installation-of-python-environment)  
[More Information](#more-information)  
[Troubleshooting and Known Errors](#troubleshooting-and-known-errors)  
[Authors and Acknowledgments](#authors-and-acknowledgments)  

## Synopsis

This simulator built in Python applies water to a 3D topographical grid, then computes the total volume of flood water that pools on that grid. Typically the input is a "chessboard" of height values, or in other words an 8x8 2D array of integers up to a height of 10. However, the simulator has been successfully tested with 2D arrays as large as 200x200 with height values of up to 200. The project was built using Python 3.8.12, however it runs on Python versions as early as 3.6.9.

To run and experiment with the simulation, please start with [How To Use This Project](#how-to-use-this-project), and feel free to enjoy learning more about the simulator in [More Information](#more-information). Then, install it per the steps in either the [express](#express-installation-of-python-environment) or [verbose](#verbose-installation-of-python-environment) instructions. 

## Built With

* [Python 3.8.12](https://www.python.org/downloads/release/python-3812/) - The primary language used, including standard libraries only.

## Environment and Methods Used
* [GitHub](https://github.com/) - Repo and version control
* [AWS Cloud9](https://aws.amazon.com/cloud9/) - Online development IDE which uses its own EC2 server 
* [Ubuntu 18.04.6 LTS](https://releases.ubuntu.com/18.04/) - The Linux OS on the AWS Cloud9 instance

## How To Use This Project

1. Once your Python environment and this code is ready to run (per the instructions in [express](#express-installation-of-python-environment) or [verbose](#verbose-installation-of-python-environment) installation), you may automatically run the entire simulation with a pre-defined chessboard with 
```
python topographyfloodsim.py
```
  * This run will report the total flooding (in cubes) of the chessboard, as well as the maximum water height detected. 

2. You may change the default chessboard to any topography of your choosing by modifying the chessboard 2D array at the end of the [topographyfloodsim.py](topographyfloodsim.py) script around line 495: 
```
        chessboard = [  [0,8,8,7,7,4,4,4],
                        [8,0,0,0,0,0,0,3],
                        [8,0,0,0,0,0,0,3],
                        [4,0,0,0,0,0,0,4],
                        [4,0,0,0,0,0,0,3],
                        [4,0,0,0,0,0,0,4],
                        [4,0,0,0,0,0,0,3],
                        [4,6,6,6,4,4,4,4],
        ]
```

3. If you prefer, you may have the script randomize a topography for you by passing at least one of three arguments through the command line: -l for length, -w for width, and/or --mh for maximum height. If any of these three arguments are passed, then the script ignores the custom chessboard and generates a random one based on your dimensions passed. If you pass at least one argument but not all three, the other dimensions will default to values at the top of the script (DEFAULT_LENGTH, DEFAULT_WIDTH, DEFAULT_MAX_HEIGHT). Here's an example of running the simulation with a randomized topography:
```
python topographyfloodsim.py -l 8 -w 8 --mh 10
```

4. You may verify that the accuracy of the simulation is 100%, by running the unit tests. You may also add additional unit tests by using the same pattern in the [tests.py](tests.py) file, but keep in mind that you must manually compute the correct answer yourself, so that the test may compare that with the simulation. Run the tests like this: 
```
python tests.py
```

5. The topgraphyfloodsim.py main script executes a full simulation automatically by default. To override the behavior of the full simulation (such as to suppress printing the grids), you may locally modify the steps in the full_simulation() function.


## Express Installation of Python Environment

1. On a recent Ubuntu version (preferably 18.04 or more recent), install Python 3.8.12 [Python 3.8.12](https://www.python.org/downloads/release/python-3812/) on your environment. 
2. Check out this code using the current release branch.
3. Create a virtual Python environment inside that project folder and activate it. 
4. Although this simulator uses only the Python standard libraries, it is a common step to run the requirements_dev.txt file to update the pip==21.1.1 and
setuptools==56.0.0 versions. Run this from the project root:
```
pip3 install -r requirements_dev.txt
```

## Verbose Installation of Python Environment

This optional installation process will provide a fully functional Cloud9 environment within a free-tier AWS account. Note that to complete this, you'll need a valid credit card, as AWS requires this just to verify identity for a one year free-tier AWS account. 

1. Create a new [gmail](https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp) account.
2. Use that account to create a new AWS account here: [Sign Up for AWS](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). Note that this will be a free-tier account. 
 * Choose "Personal Account" on the next page and enter your personal information, and then enter your credit card information on the following page. 
 * Follow all instructions to verify your AWS account information, including verifying your gmail address if necessary. 
 * You should now have a root user account for your new AWS free-tier account, which is fine to use for this temporary installation. 
 * Log into AWS using your log in credentials, and then you should be redirected to your ["Console Home"](https://console.aws.amazon.com/console/home)
3. Now set up a Cloud9 development environment, which will automatically create an EC2 instance. The easiest way to find the Cloud9 AWS service is to just type `cloud9` into the search bar at the top of your Console Home. Or, you can find the Cloud9 service under the "Services" button at the top, and in the "Developer Tools" category.
 * Now you should be in the AWS Cloud9 main page. Click "Create Environment".
 * Name it something with an optional description. You can use "Flood Simulator" as the name if you like. Click "Next Step".
 * Allow it to create an EC2 instance, but please choose the "t3.small" size. Although it doesn't state that it is covered in the free-tier, you will not be charged as long as this environment is temporary. 
 * Choose Ubuntu 18.04 LTS as the platform, **not** Amazon Linux 2. 
 * Allow the other defaults and click "Next Step". 
 * On the next page, simply review your request and then click "Create Environment". 
 * After a few minutes, your new Cloud9 IDE should be created, and you'll begin with a bash terminal and a simple directory structure! 
4. 

## More Information

To be added

## Troubleshooting and Known Errors 

1. There are currently no known errors on Python versions of 3.6.9 or greater, when simulating an 8x8 chessboard topography. 
2. Grids as large as 200x200x200 execute fine, albeit slower, so be patient if you're attempting these sizes. 
3. However, a grid of 230x230x230 ran out of memory on a Cloud9 "small" server and froze the EC2 server, so if you are using that same environment, avoid grids over 200x200x200.

## Authors and Acknowledgments

* **Daniel Culveyhouse** (dculvey@gmail.com): Author
* Special thanks to the Cavnue development team for this assignment. 


