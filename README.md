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

This simulator applies water to a 3D topographical grid, then computes the total volume of flood water that pools on that grid. Typically the input is a "chessboard" of height values, or in other words an 8x8 2D array of integers up to a height of 10. However, the simulator has been successfully tested with 2D arrays as large as 200x200 with height values of up to 200. The project was built using Python 3.8.12, however it runs on Python versions as early as 3.6.9.

The simulator was assigned to me as a project by the Cavnue development team, and the original request was quite simple: "Imagine a chess board where each square has a height, forming a topology. Water is poured over the entire board and collects in 'valleys'.  What volume of water does a given board hold?" This simulation solves this challenge and works with 100% accuracy. 

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
python3 topographyfloodsim.py
```
  * This method will report the total flooding of the chessboard (in number of cubes), as well as the maximum water height detected. 

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
python3 topographyfloodsim.py -l 8 -w 8 --mh 10
```

4. You may verify that the accuracy of the simulation is 100%, by running the unit tests. You may also add additional unit tests by using the same pattern in the [tests.py](tests.py) file, but keep in mind that you must manually compute the correct answer yourself, so that the test may compare that with the simulation. Run the tests like this: 
```
python3 tests.py
```

5. The topgraphyfloodsim.py main script executes a full simulation automatically by default. To override the behavior of the full simulation (such as to suppress printing the grids), you may locally modify the steps in the full_simulation() function.


## Express Installation of Python Environment

1. On a recent Ubuntu version (preferably 18.04 or more recent), install [Python 3.8.12](https://www.python.org/downloads/release/python-3812/) on your environment. 
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
3. Now set up a Cloud9 development environment, which will automatically create an EC2 instance. The easiest way to find the Cloud9 AWS service is to just type `cloud9` into the search bar at the top of your Console Home. Or, you can find the Cloud9 service under the "Services" button at the top, and in the "Developer Tools" category. Or, just click here: [AWS Cloud9 Environments](https://console.aws.amazon.com/cloud9/)
 * Now you should be in the AWS Cloud9 main page. Click "Create Environment".
 * Name it something with an optional description. You can use "Flood Simulator" as the name if you like. Click "Next Step".
 * Allow it to create an EC2 instance, but please choose the "t3.small" size. Although it doesn't state that it is covered in the free-tier, you will not be charged as long as this environment is temporary. 
 * Choose Ubuntu 18.04 LTS as the platform, **not** Amazon Linux 2. 
 * Allow the other defaults and click "Next Step". 
 * On the next page, simply review your request and then click "Create Environment". 
 * After a few minutes, your new Cloud9 IDE should be created, and you'll begin with a bash terminal and a simple directory structure! 
4. Now we'll prepare Ubuntu and Python before installing and running the script. 
 * Firstly, udpate Ubuntu with any of the latest packages with these three commands, one at a time: 
```
sudo -su root
apt update && apt upgrade -y
exit
```
 * Update the Python package installer (PIP). Note: You should no longer be the root user, so make sure you use the "exit" above: 
```
pip install --upgrade pip
```
* Update important Ubuntu libraries with these two commands. After each command, you will need to confirm with an *uppercase* "Y": 
```
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
```
5. Now we'll check out this repository. 
 * Use the default git to check out the repository's current release: 
```
git clone https://github.com/culveyhouse/topography-flood-sim.git
cd topography-flood-sim/
```
6. Create a Python virtual environment within that new repo directory and activate it:
``` 
python3 -m venv env
source ./env/bin/activate
```
 * Note: You'll need to use the `python3` command for all Python requests in this particular environment, as Amazon provides both Python 2 & 3 in this installation. This repo will not work in Python 2.x. 

7. Now, switch to the `release-0.1` branch: 
```
git checkout release-0.1
```
 * Your command prompt should now look decorated like: 
```
(env) ubuntu:~/environment/topography-flood-sim (release-0.1) $ 
```

8. You may now run the simulation as per the instructions in [How To Use This Project](#how-to-use-this-project). You may try the default simulation:
```
python3 topographyfloodsim.py
```
 * Or you may customize it: 
```
python3 topographyfloodsim.py -l 8 -w 8 -mh 10
```

## More Information

1. To write this simulation, I immediately noticed I would need to build a pathfinding algorithm. Several pathfinding examples exist and are widely used, and at first I attempted a recursive pathfinder. However, I abandoned this as it was too resource-heavy and very time-consuming to troubleshoot and debug. I also wanted this simulator to function perfectly on a lightweight server with low memory. I settled on a simpler while loop with a 4-directonal pathfinder, similar to [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). 
2. I decided to use an OOP system to represent the 3D cubes as objects, so that each object may store its own information, namely its content (0=board, 1=air, 2=water). By using this structure, the simulation may be expanded in the future with more materials, behaviors, etc.
3. The simulation functions contrary to the physics of pouring water over a topology, but rather it simulates flooding the topology upwards, producing the same end result. Water drains or pools based on the topology and uses pathfinding to attempt drainage. Water will typically pool in multiple areas at multiple heights, and I included a few visuals here to depict the tests that are availalbe in `tests.py`:

   a. The first test is a small control grid which fully drains with a total flooding of zero (0) cubes: 
   
 <img src="https://user-images.githubusercontent.com/14173083/152660186-fdd50ea6-c43a-47a3-91ae-9dcdbf518ad5.png" width="300" />

   b. The second test is a chessboard with full containment and walls on all sides, which floods 3 layers deep: 
     
 <img src="https://user-images.githubusercontent.com/14173083/152660184-36eba653-269b-442a-ad2d-a096013b2030.png" width="300" />
 
   c. The third test is a chessboard maze where water drains through the maze, but pools in just one place: 
   
 <img src="https://user-images.githubusercontent.com/14173083/152660188-54407599-5107-4181-b998-dec59aefe1ad.png" width="300" /> 
 
   d. The last test is a tiered waterfall, where some water pools at each terrace:
   
 <img src="https://user-images.githubusercontent.com/14173083/152660187-77ad1640-6998-4cdc-85c8-b33af1e9df35.png" width="300" /> 

4. Potential upcoming features: Because of the object-oriented approach I used in the 3D grid, this simulation may be extended to support other materials, including sand, mud, concrete, lava, and others. Additionally, it can support erosion, pothole, and sinkhole physics, and can support cavitation (pathfinding through caves) which could also calculate air pockets in the cave systems. It would also be very curious to run several thousand randomized simulations with different X, Y, Z grid sizes, keep track of each result, then report on the mean & average pooling for each grid size.

## Troubleshooting and Known Errors 

1. There are currently no known errors on Python versions of 3.6.9 or greater, when simulating an 8x8 chessboard topography. 
2. Grids as large as 200x200x200 execute fine, albeit slower (8,000,000 Python objects), so be patient if you're attempting these sizes. 
3. However, a grid of 230x230x230 ran out of memory on a Cloud9 "small" server and froze the EC2 server with over 12.1 million Python objects, so if you are using that same environment, avoid grids over 200x200x200.

## Authors and Acknowledgments

* **Daniel Culveyhouse** (dculvey@gmail.com): Author
* Special thanks to the Cavnue development team for this assignment. 


