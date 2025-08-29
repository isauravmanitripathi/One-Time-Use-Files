# **Chapter 2. Python Infrastructure**

In building a house, there is the problem of the selection of wood. It is essential that the carpenter's aim be to carry equipment that will cut well and, when he has time, to sharpen that equipment. Miyamoto Musashi (*The Book of Five Rings*)

For someone new to Python, Python deployment might seem all but straightforward. The same holds true for the wealth of libraries and packages that can be installed optionally. First of all, there is not only *one* Python. Python comes in many different flavors, like CPython, Jython, IronPython, and PyPy. Then there is the divide between Python 2.7 and the 3.x world. 1

Even after you've decided on a version, deployment is difficult for a number of additional reasons:

- The interpreter (a standard CPython installation) only comes with the socalled *standard library* (e.g., covering typical mathematical functions)
- Optional Python packages need to be installed separately and there are hundreds of them
- Compiling/building such nonstandard packages on your own can be tricky due to dependencies and operating system–specific requirements
- Taking care of these dependencies and of version consistency over time (i.e., maintenance) is often tedious and time consuming
- Updates and upgrades for certain packages might necessitate recompiling a multitude of other packages
- Changing or replacing one package might cause trouble in (many) other places

Fortunately, there are tools and strategies available that can help. This chapter covers the following types of technologies that help with Python deployment:

#### *Package managers*

Package managers like [pip](https://pypi.python.org/pypi/pip) and [conda](http://conda.pydata.org/docs/intro.html) help with the installing, updating, and removing of Python packages; they also help with version consistency of different packages.

### *Virtual environment managers*

A virtual environment manager like [virtualenv](https://pypi.python.org/pypi/virtualenv) or conda allows you to manage multiple Python installations in parallel (e.g., to have both a Python 2.7 and 3.7 install on a single machine or to test the most recent development version of a fancy Python package without risk). 2

### *Containers*

[Docker](http://docker.com) containers represent complete filesystems containing all the pieces of a system needed to run certain software, like code, runtime, or system tools. For example, you can run an Ubuntu 18.04 operating system with a Python 3.7 install and the respective Python code in a Docker container hosted on a machine running macOS or Windows 10.

### *Cloud instances*

Deploying Python code for financial applications generally requires high availability, security, and also performance; these requirements can typically only be met by the use of professional compute and storage infrastructure that is nowadays available at attractive conditions in the form of fairly small to really large and powerful cloud instances. One benefit of a cloud instance (i.e., a virtual server) compared to a dedicated server rented longer-term is that users generally get charged only for the hours of actual usage; another advantage is that such cloud instances are available literally in a minute or two if needed, which helps with agile development and also with scalability.

The structure of this chapter is as follows:

*"conda as a Package Manager"*

This section introduces conda as a package manager for Python.

*"conda as a Virtual Environment Manager"*

This section focuses on conda's capabilities as a virtual environment manager.

This section gives a brief overview of Docker as a containerization

*"Using Docker Containers"*

This section gives a brief overview of Docker as a containerization technology and focuses on the building of an Ubuntu-based container with a Python 3.7 installation.

### *"Using Cloud Instances"*

The section shows how to deploy Python and Jupyter Notebook — a powerful, browser-based tool suite for Python development — in the cloud.

The goal of this chapter is to set up a proper Python installation with the most important tools as well as numerical, data analysis, and visualization packages on a professional infrastructure. This combination then serves as the backbone for implementing and deploying the Python code in later chapters, be it interactive financial analytics code or code in the form of scripts and modules.

# **conda as a Package Manager**

Although conda can be installed standalone, an efficient way of doing it is via Miniconda, a minimal Python distribution including conda as a package and virtual environment manager.

### **Installing Miniconda**

Miniconda is available for Windows, macOS, and Linux. You can download the different versions from the [Miniconda](https://conda.io/miniconda.html) webpage. In what follows, the Python 3.7 64-bit version is assumed. The main example in this section is a session in an Ubuntu-based Docker container which downloads the Linux 64-bit installer via wget and then installs Miniconda. The code as shown should work — perhaps with minor modifications — on any other Linux-or macOS-based machine as well: \$ **docker run -ti -h py4fi -p 11111:11111 ubuntu:latest** *bin***bash**

root@py4fi:/# **apt-get update; apt-get upgrade -y** ...

root@py4fi:/# **apt-get install -y bzip2 gcc wget** ...

root@py4fi:/# **cd root** root@py4fi:~# **wget \** > **https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86\_64.sh \** > **-O miniconda.sh** ...

HTTP request sent, awaiting response... 200 OK

Length: 62574861 (60M) [application/x-sh]

Saving to: 'miniconda.sh'

miniconda.sh 100%[====================>] 59.68M 5.97MB/s in 11s

2018-09-15 09:44:28 (5.42 MB/s) - 'miniconda.sh' saved [62574861/62574861]

root@py4fi:~# **bash miniconda.sh**

Welcome to Miniconda3 4.5.11

In order to continue the installation process, please review the license agreement.

Please, press ENTER to continue

>>>

Simply pressing the Enter key starts the installation process. After reviewing the license agreement, approve the terms by answering yes: ...

Do you accept the license terms? [yes|no]

```
[no] >>> yes
```

Miniconda3 will now be installed into this location: *root*miniconda3

- Press ENTER to confirm the location

- Press CTRL-C to abort the installation - Or specify a different location below

[*root*miniconda3] >>>

PREFIX=*root*miniconda3

installing: python-3.7. ...

...

installing: requests-2.19.1-py37\_0 ...

installing: conda-4.5.11-py37\_0 ...

installation finished.

After you have agreed to the licensing terms and have confirmed the install location you should allow Miniconda to prepend the new Miniconda install location to the PATH environment variable by answering yes once again: Do you wish the installer to prepend the Miniconda3 install location to PATH in your *root*.bashrc ? [yes|no]

[no] >>> **yes**

Appending source *root*miniconda3*bin*activate to *root*.bashrc A backup will be made to: *root*.bashrc-miniconda3.bak

For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!

root@py4fi:~#

After that, you might want to upgrade conda as well as Python: 3

```
root@py4fi:~# export PATH="rootminiconda3bin:$PATH"
root@py4fi:~# conda update -y conda python
...
root@py4fi:~# echo ". rootminiconda3/etc/profile.d/conda.sh" >> ~/.bashrc
root@py4fi:~# bash
```

After this rather simple installation procedure, you'll have a basic Python install as well as conda available. The basic Python install comes with some nice batteries included, like the SQLite3 [database](https://sqlite.org) engine. You might try out whether you can start Python in a new shell instance after appending the relevant path to the respective environment variable (as done previously): root@py4fi:~# **python** Python 3.7.0 (default, Jun 28 2018, 13:15:42) [GCC 7.2.0] :: Anaconda, Inc. on linux

Type "help", "copyright", "credits" or "license" for more information.

>>> **print('Hello Python for Finance World.')** Hello Python for Finance World.

>>> **exit()** root@py4fi:~#

### **Basic Operations with conda**

conda can be used to efficiently handle, among other things, the installing, updating, and removing of Python packages. The following list provides an overview of the major functions:

*Installing Python x.x* conda install python=*x.x*

*Updating Python* conda update python

*Installing a package* conda install \$PACKAGE\_NAME

*Updating a package* conda update \$PACKAGE\_NAME

*Removing a package* conda remove \$PACKAGE\_NAME

*Updating conda itself* conda update conda

*Searching for packages* conda search \$SEARCH\_TERM

*Listing installed packages* conda list

Given these capabilities, installing, for example, NumPy — one of the most important libraries of the so-called scientific stack — requires a single command only. When the installation takes place on a machine with an Intel processor, the procedure automatically installs the Intel Math Kernel [Library](https://docs.continuum.io/mkl-optimizations/) (mkl), which speeds up numerical operations not only for NumPy but also for a few other scientific Python packages: 4

root@py4fi:~# **conda install numpy** Solving environment: done ## Package Plan ##

```
environment location: rootminiconda3
```

```
added updated specs:
  - numpy
```

*The following packages will be downloaded:*

| package<br>                                                                                                                                                                                                                             | build                                                                                                   |                                                            |               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------|---------------|
| --------------------------- -----------------<br>mkl-2019.0<br> <br>intel-openmp-2019.0<br> <br>mkl_random-1.0.1<br> <br>libgfortran-ng-7.3.0<br> <br>numpy-1.15.1<br> <br>numpy-base-1.15.1<br> <br>blas-1.0<br> <br>mkl_fft-1.0.4<br> | 117<br>117<br>py37h4414c95_1<br>hdf63c60_0<br>py37h1d66e8a_0<br>py37h81de0dd_0<br>mkl<br>py37h4414c95_1 | 204.4 MB<br>721 KB<br>372 KB<br>1.3 MB<br>4.2 MB<br>149 KB | 37 KB<br>6 KB |
| ------------------------------------------------------------                                                                                                                                                                            | Total:                                                                                                  | 211.1 MB                                                   |               |

*The following NEW packages will be INSTALLED:*

```
blas: 1.0-mkl
   intel-openmp: 2019.0-117
   libgfortran-ng: 7.3.0-hdf63c60_0
   mkl: 2019.0-117
   mkl_fft: 1.0.4-py37h4414c95_1
   mkl_random: 1.0.1-py37h4414c95_1
   numpy: 1.15.1-py37h1d66e8a_0
   numpy-base: 1.15.1-py37h81de0dd_0
Proceed ([y]n)? y
Downloading and Extracting Packages
mkl-2019.0 | 204.4 MB | ####################################### | 100%
...
numpy-1.15.1 | 37 KB | ####################################### | 100%
numpy-base-1.15.1 | 4.2 MB | ####################################### | 100%
...
root@py4fi:~#
```

Multiple packages can also be installed at once. The -y flag indicates that all (potential) questions shall be answered with yes:

```
root@py4fi:/# conda install -y ipython matplotlib pandas pytables scikit-learn \
> scipy
...
pytables-3.4.4 | 1.5 MB | ####################################### | 100%
kiwisolver-1.0.1 | 83 KB | ####################################### | 100%
icu-58.2 | 22.5 MB | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
root@py4fi:~#
```

After the resulting installation procedure, some of the most important libraries

for financial analytics are available in addition to the standard ones. These include:

#### *[IPython](http://ipython.org)*

An improved interactive Python shell

#### *[matplotlib](http://matplotlib.org)*

The standard plotting library in Python

*[NumPy](http://numpy.org)*

For efficient handling of numerical arrays

#### *[pandas](http://pandas.pydata.org)*

For management of tabular data, like financial time series data

#### *[PyTables](http://pytables.org)*

A Python wrapper for the HDF5 [library](http://hdfgroup.org)

#### *[scikit-learn](http://scikit-learn.org)*

A package for machine learning and related tasks

#### *[SciPy](http://scipy.org)*

A collection of scientific classes and functions (installed as a dependency)

This provides a basic tool set for data analysis in general and financial analytics in particular. The next example uses IPython and draws a set of pseudo-random numbers with NumPy:

```
root@py4fi:~# ipython
Python 3.7.0 (default, Jun 28 2018, 13:15:42)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import numpy as np
In [2]: np.random.seed(100)
In [3]: np.random.standard_normal((5, 4))
Out[3]:
array([[-1.74976547, 0.3426804 , 1.1530358 , -0.25243604],
      [ 0.98132079, 0.51421884, 0.22117967, -1.07004333],
      [-0.18949583, 0.25500144, -0.45802699, 0.43516349],
      [-0.58359505, 0.81684707, 0.67272081, -0.10441114],
      [-0.53128038, 1.02973269, -0.43813562, -1.11831825]])
In [4]: exit
root@py4fi:~#
```

Executing conda list shows which packages are installed:

| root@py4fi:~# conda list                     |         |            |         |
|----------------------------------------------|---------|------------|---------|
| # packages in environment at rootminiconda3: |         |            |         |
| #                                            |         |            |         |
| # Name                                       | Version | Build      | Channel |
| asn1crypto                                   | 0.24.0  | py37_0     |         |
| backcall                                     | 0.1.0   | py37_0     |         |
| blas                                         | 1.0     | mkl        |         |
| blosc                                        | 1.14.4  | hdbcaa40_0 |         |
| bzip2                                        | 1.0.6   | h14c3975_5 |         |
|                                              |         |            |         |
| python                                       | 3.7.0   | hc3d631a_0 |         |
|                                              |         |            |         |
| wheel                                        | 0.31.1  | py37_0     |         |
| xz                                           | 5.2.4   | h14c3975_4 |         |
| yaml                                         | 0.1.7   | had09818_2 |         |
| zlib                                         | 1.2.11  | ha838bed_2 |         |
| root@py4fi:~#                                |         |            |         |

If a package is not needed anymore, it is efficiently removed with conda remove:

```
root@py4fi:~# conda remove scikit-learn
Solving environment: done
## Package Plan ##
  environment location: rootminiconda3
  removed specs:
    - scikit-learn
The following packages will be REMOVED:
    scikit-learn: 0.19.1-py37hedc7406_0
Proceed ([y]/n)? y
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
root@py4fi:~#
```

conda as a package manager is already quite useful. However, its full power only becomes evident when adding virtual environment management to the mix.

### **EASY PACKAGE MANAGEMENT**

Using conda as a package manager makes installing, updating, and removing Python packages a pleasant experience. There is no need to take care of building and compiling packages on your own — which can be tricky sometimes, given the list of dependencies a package specifies and the specifics to be considered on different operating systems.

## **conda as a Virtual Environment Manager**

Depending on the version of the installer you choose, Miniconda provides a default Python 2.7 or 3.7 installation. The virtual environment management capabilities of conda allow one, for example, to add to a Python 3.7 default installation a completely separate installation of Python 2.7.x. To this end, conda offers the following functionality:

*Creating a virtual environment* conda create --name \$ENVIRONMENT\_NAME *Activating an environment* conda activate \$ENVIRONMENT\_NAME *Deactivating an environment* conda deactivate \$ENVIRONMENT\_NAME *Removing an environment* conda env remove --name \$ENVIRONMENT\_NAME *Exporting to an environment file* conda env export > \$FILE\_NAME *Creating an environment from a file* conda env create -f \$FILE\_NAME *Listing all environments* conda info --envs As a simple illustration, the example code that follows creates an environment called py27, installs IPython, and executes a line of Python 2.7.x code:

```
root@py4fi:~# conda create --name py27 python=2.7
Solving environment: done
## Package Plan ##
  environment location: rootminiconda3/envs/py27
  added updated specs:
    - python=2.7
```

*The following NEW packages will be INSTALLED:*

```
ca-certificates: 2018.03.07-0
...
   python: 2.7.15-h1571d57_0
...
   zlib: 1.2.11-ha838bed_2
Proceed ([y]n)? y
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use:
# > conda activate py27
#
# To deactivate an active environment, use:
# > conda deactivate
#
root@py4fi:~#
```

Notice how the prompt changes to include (py27) after the activation of the environment:

```
root@py4fi:~# conda activate py27
(py27) root@py4fi:~# conda install ipython
Solving environment: done
...
Executing transaction: done
(py27) root@py4fi:~#
```

Finally, this allows you to use IPython with Python 2.7 syntax:

```
(py27) root@py4fi:~# ipython
Python 2.7.15 |Anaconda, Inc.| (default, May 1 2018, 23:32:55)
Type "copyright", "credits" or "license" for more information.
IPython 5.8.0 -- An enhanced Interactive Python.
? -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help -> Python's own help system.
object? -> Details about 'object', use 'object??' for extra details.
In [1]: print "Hello Python for Finance World!"
Hello Python for Finance World!
In [2]: exit
(py27) root@py4fi:~#
```

As this example demonstrates, using conda as a virtual environment manager allows you to install different Python versions alongside each other. It also allows you to install different versions of certain packages. The default Python install is not influenced by such a procedure, nor are other environments which

might exist on the same machine. All available environments can be shown via conda env list:

```
(py27) root@py4fi:~# conda env list
# conda environments:
#
base rootminiconda3
py27 * rootminiconda3/envs/py27
(py27) root@py4fi:~#
```

Sometimes it is necessary to share environment information with others or to use environment information on multiple machines. To this end, one can export the installed packages list to a file with conda env export. This only works properly by default if the machines use the same operating system, since the build versions are specified in the resulting YAML file, but they can be deleted to only specify the package version:

```
(py27) root@py4fi:~# conda env export --no-builds > py27env.yml
(py27) root@py4fi:~# cat py27env.yml
name: py27
channels:
  - defaults
dependencies:
  - backports=1.0
...
  - python=2.7.15
...
  - zlib=1.2.11
prefix: rootminiconda3/envs/py27
(py27) root@py4fi:~#
```

Often a virtual environment, which is technically not that much more than a certain (sub)folder structure, is created to do some quick tests. 5 In such a case, the environment is easily removed after deactivation via conda env remove:

```
(py27) root@py4fi:/# conda deactivate
root@py4fi:~# conda env remove -y --name py27
Remove all packages in environment rootminiconda3/envs/py27:
## Package Plan ##
 environment location: rootminiconda3/envs/py27
The following packages will be REMOVED:
   backports: 1.0-py27_1
```

```
...
root@py4fi:~#
```

zlib: 1.2.11-ha838bed\_2

This concludes the overview of conda as a virtual environment manager.

### **EASY ENVIRONMENT MANAGEMENT**

conda does not only help with managing packages; it is also a virtual environment manager for Python. It simplifies the creation of different Python environments, allowing you to have multiple versions of Python and optional packages available on the same machine without them influencing each other in any way. conda also allows you to export environment information so you can easily replicate it on multiple machines or share it with others.

# **Using Docker Containers**

Docker [containers](http://docker.com) have taken the IT world by storm. Although the technology is still relatively young, it has established itself as one of the benchmarks for the efficient development and deployment of almost any kind of software application.

For the purposes of this book it suffices to think of a Docker container as a separate ("containerized") filesystem that includes an operating system (e.g., Ubuntu Server 18.04), a (Python) runtime, additional system and development tools, as well as further (Python) libraries and packages as needed. Such a Docker container might run on a local machine with Windows 10 or on a cloud instance with a Linux operating system, for instance.

This section does not go into all the exciting details of Docker containers. It is rather a concise illustration of what the Docker technology can do in the context of Python deployment. 6

### **Docker Images and Containers**

However, before moving on to the illustration, two fundamental concepts need to be distinguished when talking about Docker. The first is a *Docker image*, which can be compared to a Python class. The second is a *Docker container*, which can be compared to an instance of the respective Python class. 7

On a more technical level, you find the following definition for an *image* in the Docker [glossary:](https://docs.docker.com/engine/reference/glossary/)

Docker images are the basis of containers. An Image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime. An image typically contains a union of layered filesystems stacked on top of each other. An image does not have state and it never changes.

Similarly, you find the following definition for a *container* in the Docker glossary, which makes the analogy to Python classes and instances of such classes transparent:

A container is a runtime instance of a Docker image. A Docker container consists of: a Docker image, an execution environment, and a standard set of instructions.

Depending on the operating system, the installation of Docker is somewhat different. That is why this section does not go into the details. More information and further links are found on the About [Docker](https://docs.docker.com/install/) CE page.

### **Building an Ubuntu and Python Docker Image**

This section illustrates the building of a Docker image based on the latest version of Ubuntu, which includes Miniconda as well as a few important Python packages. In addition, it does some Linux housekeeping by updating the Linux packages index, upgrading packages if required, and installing certain additional system tools. To this end, two scripts are needed. One is a bash script that does all the work on the Linux level. <sup>8</sup> The other is a so-called *Dockerfile*, which controls the building procedure for the image itself.

The bash script in [Example](#page-19-0) 2-1 that does the installing consists of three major parts. The first part handles the Linux housekeeping. The second part installs Miniconda, while the third part installs optional Python packages. There are also more detailed comments inline.

<span id="page-19-0"></span>*Example 2-1. Script installing Python and optional packages*

```
#!binbash
#
# Script to Install
# Linux System Tools and
# Basic Python Components
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
# GENERAL LINUX
apt-get update # updates the package index cache
apt-get upgrade -y # updates packages
# installs system tools
apt-get install -y bzip2 gcc git htop screen vim wget
apt-get upgrade -y bash # upgrades bash if necessary
apt-get clean # cleans up the package index cache
# INSTALL MINICONDA
# downloads Miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O \
  Miniconda.sh
bash Miniconda.sh -b # installs it
rm -rf Miniconda.sh # removes the installer
export PATH="rootminiconda3/bin:$PATH" # prepends the new path
# INSTALL PYTHON LIBRARIES
conda update -y conda python # updates conda & Python (if required)
conda install -y pandas # installs pandas
conda install -y ipython # installs IPython shell
```

The *Dockerfile* in Example 2-2 uses the bash script in [Example](#page-19-0) 2-1 to build a new Docker image. It also has its major parts commented inline.

*Example 2-2. Dockerfile to build the image*

```
#
# Building a Docker Image with
# the Latest Ubuntu Version and
# Basic Python Install
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
# latest Ubuntu version
FROM ubuntu:latest
# information about maintainer
MAINTAINER yves
# add the bash script
ADD install.sh /
# change rights for the script
RUN chmod u+x /install.sh
# run the bash script
RUN /install.sh
# prepend the new path
ENV PATH rootminiconda3/bin:$PATH
# execute IPython when container is run
```

CMD ["ipython"]

If these two files are in a single folder and Docker is installed, then the building of the new Docker image is straightforward. Here, the tag ubuntupython is used for the image. This tag is needed to reference the image, for example when running a container based on it:

```
~/Docker$ docker build -t py4fi:basic .
...
Removing intermediate container 5fec0c9b2239
 ---> accee128d9e9
Step 6/7 : ENV PATH rootminiconda3/bin:$PATH
 ---> Running in a2bb97686255
Removing intermediate container a2bb97686255
 ---> 73b00c215351
Step 7/7 : CMD ["ipython"]
 ---> Running in ec7acd90c991
Removing intermediate container ec7acd90c991
 ---> 6c36b9117cd2
Successfully built 6c36b9117cd2
Successfully tagged py4fi:basic
~/Docker$
```

Existing Docker images can be listed via docker images. The new image should be at the top of the list:

|                    | (py4fi) ~/Docker\$ docker images |              |                    |        |
|--------------------|----------------------------------|--------------|--------------------|--------|
| REPOSITORY         | TAG                              | IMAGE ID     | CREATED            | SIZE   |
| py4fi              | basic                            | f789dd230d6f | About a minute ago | 1.79GB |
| ubuntu             | latest                           | cd6d8154f1e1 | 9 days ago         | 84.1MB |
| (py4fi) ~/Docker\$ |                                  |              |                    |        |

Successfully building the py4fi:basic allows you to run the respective Docker container with docker run. The parameter combination -ti is needed for interactive processes running within a Docker container, like a shell process (see the docker run [reference](https://docs.docker.com/engine/reference/run/) page):

```
~/Docker$ docker run -ti py4fi:basic
Python 3.7.0 (default, Jun 28 2018, 13:15:42)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import numpy as np
In [2]: a = np.random.standard_normal((5, 3))
In [3]: import pandas as pd
In [4]: df = pd.DataFrame(a, columns=['a', 'b', 'c'])
In [5]: df
Out[5]:
         a b c
0 -1.412661 -0.881592 1.704623
1 -1.294977 0.546676 1.027046
2 1.156361 1.979057 0.989772
3 0.546736 -0.479821 0.693907
4 -1.972943 -0.193964 0.769500
In [6]:
```

Exiting IPython will exit the container as well since it is the only application running within the container. However, you can *detach* from a container by typing Ctrl-P+Ctrl-Q.

The docker ps command will still show the running container (and any other currently running containers) after you've detached from it:

| ~/Docker\$ docker ps       |               |           |                    |                   |
|----------------------------|---------------|-----------|--------------------|-------------------|
| CONTAINER ID               | IMAGE         | COMMAND   | CREATED            | STATUS            |
| e815df8f0f4d               | py4fi:basic   | "ipython" | About a minute ago | Up About a minute |
| 4518917de7dc               | ubuntu:latest | "binbash" | About an hour ago  | Up About an hour  |
| d081b5c7add0<br>~/Docker\$ | ubuntu:latest | "binbash" | 21 hours ago       | Up 21 hours       |

Attaching to a Docker container is accomplished with the command docker attach \$CONTAINER\_ID (notice that a few letters of the \$CONTAINER\_ID are

enough):

```
~/Docker$ docker attach e815d
In [6]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
a 5 non-null float64
b 5 non-null float64
c 5 non-null float64
dtypes: float64(3)
memory usage: 200.0 bytes
In [7]: exit
~/Docker$
```

The exit command terminates IPython and stops the Docker container. It can be removed with docker rm:

~/Docker\$ **docker rm e815d** e815d ~/Docker\$

Similarly, the Docker image py4fi:basic can be removed via docker rmi if not needed any longer. While containers are relatively lightweight, single images might consume quite a bit of storage. In the case of the py4fi:basic image, the size is close to 2 GB. That is why you might want to regularly clean up the list of Docker images:

```
~/Docker$ docker rmi 6c36b9117cd2
```

Of course, there is much more to say about Docker containers and their benefits in certain application scenarios. But for the purposes of this book, it's enough to know that they provide a modern approach to deploy Python, to do Python development in a completely separate (containerized) environment, and to ship codes for algorithmic trading.

### **BENEFITS OF DOCKER CONTAINERS**

If you are not yet using Docker containers, you should consider doing so. They provide a number of benefits when it comes to Python deployment and development efforts, not only when working locally but in particular when working with remote cloud instances and servers deploying code for algorithmic trading.

# **Using Cloud Instances**

This section shows how to set up a full-fledged Python infrastructure on a [DigitalOcean](http://digitalocean.com) cloud instance. There are many other cloud providers out there, among them the leading provider, [Amazon](http://aws.amazon.com) Web Services (AWS). However, DigitalOcean is well known for its simplicity and also its relatively low rates for its smaller cloud instances, called *Droplets*. The smallest Droplet, which is generally sufficient for exploration and development purposes, only costs 5 USD per month or 0.007 USD per hour. Usage is charged by the hour so that one can easily spin up a Droplet for 2 hours, say, destroy it afterward, and get charged just 0.014 USD. 9

The goal of this section is to set up a Droplet on DigitalOcean that has a Python 3.7 installation plus typically needed packages (e.g., NumPy, pandas) in combination with a password-protected and Secure Sockets Layer (SSL)– encrypted Jupyter [Notebook](http://jupyter.org) server installation. This server installation will provide three major tools that can be used via a regular browser:

### *Jupyter Notebook*

*Server setup script*

A popular interactive development environment that features a selection of different language kernels (e.g., for Python, R, and Julia).

### *Terminal*

A system shell implementation accessible via the browser that allows for all typical system administration tasks and for usage of helpful tools like [Vim](http://www.vim.org/download.php) and [git](https://git-scm.com/).

### *Editor*

A browser-based file editor with syntax highlighting for many different programming languages and file types as well as typical text/code editing capabilities.

Having Jupyter Notebook installed on a Droplet allows you to do Python development and deployment via the browser, circumventing the need to log in to the cloud instance via Secure Shell (SSH) access.

To accomplish the goal of this section, a number of files are needed:

*Server setup script*

This script orchestrates all the steps necessary, like, for instance, copying other files to the Droplet and running them on the Droplet.

*Python and Jupyter installation script*

This installs Python, additional packages, and Jupyter Notebook, and starts the Jupyter Notebook server.

### *Jupyter Notebook configuration file*

This file is for the configuration of the Jupyter Notebook server, e.g., with respect to password protection.

### *RSA public and private key files*

These two files are needed for the SSL encryption of the Jupyter Notebook server.

The following subsections work backward through this list of files.

### **RSA Public and Private Keys**

In order to create a secure connection to the Jupyter Notebook server via an arbitrary browser, an SSL certificate consisting of RSA public and [private](http://bit.ly/2ONvjvw) keys is needed. In general, one would expect such a certificate to come from a socalled Certificate Authority (CA). For the purposes of this book, however, a selfgenerated certificate is "good enough." <sup>10</sup> A popular tool to generate RSA key pairs is [OpenSSL.](http://openssl.org) The brief interactive session that follows shows how to generate a certificate appropriate for use with a Jupyter Notebook server (insert your own values for the country name and other fields after the prompts):

```
~/cloud$ openssl req -x509 -nodes -days 365 -newkey \
> rsa:1024 -out cert.pem -keyout cert.key
Generating a 1024 bit RSA private key
..++++++
.......++++++
writing new private key to 'cert.key'
```

You are about to be asked to enter information that will be incorporated into your certificate request. What you are about to enter is what is called a Distinguished Name or a DN. There are quite a few fields, but you can leave some blank and others will have a default value. If you enter *.*, the field will be left blank.

```
Country Name (2 letter code) [AU]:DE
State or Province Name (full name) [Some-State]:Saarland
Locality Name (eg, city) []:Voelklingen
Organization Name (eg, company) [Internet Widgits Pty Ltd]:TPQ GmbH
Organizational Unit Name (eg, section) []:Python for Finance
Common Name (e.g. server FQDN or YOUR name) []:Jupyter
Email Address []:team@tpq.io
~/cloud$ ls
cert.key cert.pem
~/cloud$
```

The two files *cert.key* and *cert.pem* need to be copied to the Droplet and need to be referenced by the Jupyter Notebook configuration file. This file is presented next.

### **Jupyter Notebook Configuration File**

A public Jupyter Notebook server can be deployed securely as explained in the [documentation.](http://bit.ly/2Ka0tfI) Among other features, Jupyter Notebook can be password protected. To this end, there is a password hash code–generating function called passwd() available in the notebook.auth subpackage. The following code generates a password hash code with jupyter being the password itself: ~/cloud\$ **ipython** Python 3.7.0 (default, Jun 28 2018, 13:15:42) Type 'copyright', 'credits' or 'license' for more information IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help. In [1]: from notebook.auth import passwd In [2]: passwd('jupyter') Out[2]:

'sha1:d4d34232ac3a:55ea0ffd78cc3299e3e5e6ecc0d36be0935d424b' In [3]: exit

This hash code needs to be placed in the Jupyter Notebook configuration file as presented in [Example](#page-27-0) 2-3. The configuration file assumes that the RSA key files have been copied on the Droplet to the *root.jupyter/* folder.

<span id="page-27-0"></span>*Example 2-3. Jupyter Notebook configuration file*

```
#
# Jupyter Notebook Configuration File
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
# SSL ENCRYPTION
# replace the following filenames (and files used) with your choice/files
c.NotebookApp.certfile = u'root.jupyter/cert.pem'
c.NotebookApp.keyfile = u'root.jupyter/cert.key'
# IP ADDRESS AND PORT
# set ip to '*' to bind on all IP addresses of the cloud instance
c.NotebookApp.ip = '*'
# it is a good idea to set a known, fixed default port for server access
c.NotebookApp.port = 8888
# PASSWORD PROTECTION
# here: 'jupyter' as password
# replace the hash code with the one for your strong password
c.NotebookApp.password = 'sha1:d4d34232ac3a:55ea0ffd78cc3299e3e5e6ecc0d36be0935d424b'
# NO BROWSER OPTION
# prevent Jupyter from trying to open a browser
c.NotebookApp.open_browser = False
```

### **JUPYTER AND SECURITY**

Deploying Jupyter Notebook in the cloud principally leads to a number of security issues since it is a full-fledged development environment accessible via a web browser. It is therefore of paramount importance to use the security measures that a Jupyter Notebook server provides by default, like password protection and SSL encryption. But this is just the beginning; further security measures might be advisable depending on what exactly is done on the cloud instance.

The next step is to make sure that Python and Jupyter Notebook get installed on the Droplet.

### **Installation Script for Python and Jupyter Notebook**

The bash script to install Python and Jupyter Notebook is similar to the one presented in "Using Docker Containers" to install Python via Miniconda in a Docker container. However, the script in [Example](#page-29-0) 2-4 needs to start the Jupyter Notebook server as well. All major parts and lines of code are commented inline.

<span id="page-29-0"></span>*Example 2-4. Bash script to install Python and to run the Jupyter Notebook server*

```
#!/bin/bash
#
# Script to Install
# Linux System Tools,
# Basic Python Packages and
# Jupyter Notebook Server
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
# GENERAL LINUX
apt-get update # updates the package index cache
apt-get upgrade -y # updates packages
apt-get install -y bzip2 gcc git htop screen vim wget # installs system tools
apt-get upgrade -y bash # upgrades bash if necessary
apt-get clean # cleans up the package index cache
# INSTALLING MINICONDA
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O \
  Miniconda.sh
bash Miniconda.sh -b # installs Miniconda
rm Miniconda.sh # removes the installer
# prepends the new path for current session
export PATH="rootminiconda3/bin:$PATH"
# prepends the new path in the shell configuration
echo ". rootminiconda3/etc/profile.d/conda.sh" >> ~/.bashrc echo "conda activate" >>
~/.bashrc
# INSTALLING PYTHON LIBRARIES
# More packages can/must be added
# depending on the use case.
conda update -y conda # updates conda if required
conda create -y -n py4fi python=3.7 # creates an environment
source activate py4fi # activates the new environment
```

conda install -y jupyter *# interactive data analytics in the browser*

conda install -y pytables *# wrapper for HDF5 binary storage*

conda install -y matplotlib *# standard plotting library* conda install -y scikit-learn *# machine learning library* conda install -y openpyxl *# library for Excel interaction* conda install -y pyyaml *# library to manage YAML files*

conda install -y pandas *# data analysis package*

pip install --upgrade pip *# upgrades the package manager* pip install cufflinks *# combining plotly with pandas*

*# COPYING FILES AND CREATING DIRECTORIES* mkdir *root*.jupyter

mv *root*jupyter\_notebook\_config.py *root*.jupyter/

mv *root*cert.\* *root*.jupyter

mkdir *root*notebook

cd *root*notebook

*# STARTING JUPYTER NOTEBOOK* jupyter notebook --allow-root

*# STARTING JUPYTER NOTEBOOK # as background process: # jupyter notebook --allow-root &*

This script needs to be copied to the Droplet and needs to be started by the orchestration script as described in the next subsection.

### **Script to Orchestrate the Droplet Setup**

The second bash script, which sets up the Droplet, is the shortest one ([Example](#page-31-0) 2-5). It mainly copies all the other files to the Droplet, whose IP address is expected as a parameter. In the final line it starts the *install.sh* bash script, which in turn does the installation itself and starts the Jupyter Notebook server.

<span id="page-31-0"></span>*Example 2-5. Bash script to set up the Droplet*

```
#!/bin/bash
#
# Setting up a DigitalOcean Droplet
# with Basic Python Stack
# and Jupyter Notebook
#
# Python for Finance, 2nd ed.
# (c) Dr Yves J Hilpisch
#
# IP ADDRESS FROM PARAMETER
MASTER_IP=$1
# COPYING THE FILES
scp install.sh root@${MASTER_IP}:
scp cert.* jupyter_notebook_config.py root@${MASTER_IP}:
# EXECUTING THE INSTALLATION SCRIPT
ssh root@${MASTER_IP} bash rootinstall.sh
```

Everything is now in place to give the setup code a try. On DigitalOcean, create a new Droplet with options similar to these:

### *Operating system*

Ubuntu 18.10 x64 (the newest version available at the time of this writing)

*Size*

1 core, 1 GB, 25 GB SSD (the smallest Droplet)

*Data center region*

Frankfurt (since your author lives in Germany)

*SSH key*

Add a (new) SSH key for password-less login 11

*Droplet name*

You can go with the prespecified name or can choose something like py4fi

Clicking the Create button initiates the Droplet creation process, which generally takes about one minute. The major outcome of the setup procedure is the IP address, which might be, for instance, 46.101.156.199 if you chose Frankfurt as your data center location. Setting up the Droplet now is as easy as follows: (py3) ~/cloud\$ **bash setup.sh 46.101.156.199**

The resulting process might take a couple of minutes. It is finished when there is a message from the Jupyter Notebook server saying something like:

```
The Jupyter Notebook is running at: https://[all ip addresses on your
system]:8888/
```

In any current browser, visiting the following address accesses the running Jupyter Notebook server (note the https protocol):

https://46.101.156.199:8888

After perhaps requesting that you add a security exception, the Jupyter Notebook login screen prompting for a password (in our case, jupyter) should appear. You are now ready to start Python development in the browser via Jupyter Notebook, IPython via a terminal window, or the text file editor. Other file management capabilities, such as file upload, deletion of files, and creation of folders, are also available.

#### **BENEFITS OF THE CLOUD**

Cloud instances like those from DigitalOcean and Jupyter Notebook are a powerful combination, allowing the Python developer and quant to work on and make use of professional compute and storage infrastructure. Professional cloud and data center providers make sure that your (virtual) machines are physically secure and highly available. Using cloud instances also keeps the cost of the exploration and development phase rather low, since usage generally gets charged by the hour without the need to enter into a long-term agreement.

# **Conclusion**

Python is the programming language and technology platform of choice, not only for this book but for almost every leading financial institution. However, Python deployment can be tricky at best and sometimes even tedious and nervewracking. Fortunately, several technologies that help with the deployment issue have become available in recent years. The open source conda helps with both Python package and virtual environment management. Docker containers go even further, in that complete filesystems and runtime environments can be easily created in a technically shielded "sandbox" (i.e., the container). Going even one step further, cloud providers like DigitalOcean offer compute and storage capacity in professionally managed and secured data centers within minutes, billed by the hour. This in combination with a Python 3.7 installation and a secure Jupyter Notebook server installation provides a professional environment for Python development and deployment in the context of Pythonfor-finance projects.