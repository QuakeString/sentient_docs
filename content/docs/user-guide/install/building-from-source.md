+++
title = "Building from sources"
description = "Building SENTIENT IoT platform from sources"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/building-from-source.md"
+++
This guide will help you to download and build SENTIENT from source code.

Instructions listed below are tested on Ubuntu 24.04 LTS and CentOS 8/9.

<hr>

## Required tools

This section contains installation instructions for build tools.

<b><font size="4">Java</font></b>   
SENTIENT is built using **Java 17**.

Install Java 17 using these instructions:

- [Install Java 17 on Ubuntu](/docs/user-guide/install/ubuntu/#step-1-install-java-17-openjdk)

Verify the installation:

```bash
java -version
```


<b><font size="4">Maven</font></b>   
SENTIENT requires Maven 3.1.0 or newer.


<div class="st-tabs">

<div class="st-tab" data-label="Ubuntu">


```bash
sudo apt-get install maven
```


</div>

<div class="st-tab" data-label="CentOS">


```bash
sudo yum install maven
```


</div>

</div>


> Note: On certain Linux machines, Maven installation may set Java 7 as the default JVM. If this happens, reconfigure your system to use Java 17.

<hr>

## Source code


<div class="st-callout info">


**Important:** Building Docker images on Windows requires **LF** line endings.   

To build Docker image, certain scripts, configuration files and sources that will be a part of the Docker image must have **LF** line endings.   

So before cloning the repo set to _input_ the Git [core.autocrlf](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreautocrlf) configuration option. 

For example, to set *core.autocrlf* globally:

`git config --global core.autocrlf input`

Failing to do so may cause runtime errors when running Docker images.


</div>


Clone the [SENTIENT repository](https://github.com/sentient/sentient) from GitHub:

```bash
# checkout latest release branch
git clone -b  https://github.com/sentient/sentient.git --depth 1
cd sentient
```


<hr>

## Build the Project

From the project root directory, run:

```bash
mvn clean install -DskipTests
```


This command:
- build the project:
- skips unit and integration tests
- produces installation artifacts

## Build local Docker images (Optional)


<div class="st-callout info">


**Important:** Building Docker images on Windows requires **LF** line endings.   

To build Docker image, certain scripts, configuration files and sources that will be a part of the Docker image must have **LF** line endings.   

So before cloning the repo set to _input_ the Git [core.autocrlf](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreautocrlf) configuration option. 

For example, to set *core.autocrlf* globally:

`git config --global core.autocrlf input`

Failing to do so may cause runtime errors when running Docker images.


</div>


To build local Docker images for SENTIENT services, ensure [Docker](https://docs.docker.com/engine/install/) is installed.

Then run:
```bash
mvn clean install -DskipTests -Ddockerfile.skip=false
```


Docker images can be listed using:

```bash
docker images
```


## Build artifacts

After a successful build, installation packages are available in:
 
```bash
application/target
```


This directory contains:
- <span class="code-light">.deb</span> packages for Debian/Ubuntu
- <span class="code-light">.rpm</span> packages for CentOS/RHEL
- Windows installation packages

## Running tests (Optional)

This requires [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/). Make sure [Docker is configured to run as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

> **Note:** Master and release branches are already tested, so you can skip tests and avoid installing Docker as well.

<b><font size="4">Unit and integration tests</font></b>

Run all unit and integration tests:
```bash
mvn clean install
```


<b><font size="4">Black-box tests</font></b>

Black-box tests are located in [https://github.com/sentient/sentient/tree/master/msa/black-box-tests](https://github.com/sentient/sentient/tree/master/msa/black-box-tests)

Follow the instructions in the corresponding [README](https://github.com/sentient/sentient/blob/master/msa/black-box-tests/README.md) to execute them.

> Estimated runtime is approximately 1 hour, depending on hardware performance.

## Tips and tricks

SENTIENT is quite easy to build from sources on a brand-new clear environment.

Here are some tips and tricks to boost build experience: 

- [clean maven cache](https://www.baeldung.com/maven-clear-cache)
  ```bash
  rm -rf ~/.m2/repository
  ```
  

- clean gradle cache
  ```bash
  rm -rf ~/.gradle/caches/
  ```
  

- clean node modules
  ```bash
  rm -rf ui-ngx/node_modules
  ```
  

- build in parallel, format headers, build Docker images
  ```bash
  mvn -T 0.8C license:format clean install -DskipTests -Ddockerfile.skip=false
  ```
  

## Common build and runtime errors

<b><font size="4">Docker runtime error</font></b>

If you see the following error when running a locally built Docker image:

```bash
Standard_init_linux.go:175 exec user process caused no such file
```

This usually indicates incorrect [line endings](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreautocrlf).

<b><font size="3">Solution:</font></b>   
- Reconfigure Git to use LF line endings
- Re-clone the repository
- Rebuild the Docker images

Refer to the [Source code](#source-code) section above for details.
