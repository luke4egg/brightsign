


# GeoIP Simple REST Interface

This this repository you can find interesting example of implementing API usage in python.    
For the API provider I have used [IPStack API](http://api.ipstack.com).    

The goal here is to have a small, convenient Linux type tool which will provide geolocation information of the provided IP address.


## What is in the repo?

The repository contains two directories:   
- container - where you will find containarized version of the the tool
- shell     - where you will find shell version of the tool


Both versions are independent


## Implementation of the tool
For both versions I've used python3 as an implementation langauge.
Shell version is made with use of "requests" python3 library while container version uses "http.client" common library.

Personally requests version look for me nicer but in standard python container there is no "requests" library implemented and also I wanted to show that it is possible to build the tool two different ways I decided to use "http" library instead of installing additional library to the image.    

This approach makes container smaller therefore better prepared for production use.
Additionally, each additional library increasing the risk of security breach.





## Usage

### Prerequisities

To be able to use this tool you have to create a free account on [IPStack.com](https://ipstack.com)    
Despite of free account you have to provide your personal details, address and credit card during creation of the account
When account is created you should copy "Your API Access Key" generated for you during account creation.




### How to use shell version

You can use any standard Linux or MacBook shell (I used bash as a good example).    

First you need to export your API key as the example:    

`   export IPSTACK="d99d9dd999999dd9dd9d999dd9dd999"

now, you can use the tool.

Basic usage:

./lukipinfo.py 1.2.3.4

this should provide the geo location of IP address 1.2.3.4 in the format:    
  Latitude: 40.5369987487793, Longitude: -82.12859344482422


Sometimes, your next piped tool may require json format as input.
To produce output in json format you need to add second parameter 'json':

./lukipinfo.py 1.2.3.4 json

in this case the output will be in json format as below:

```
{
    "latitude": 40.5369987487793,
    "longitude": -82.12859344482422
}

```
that format can be digested in example by 'jq' or be passed to another API tool




### How to use container version

Containerized version may be easier to use in situations where you do not want to install anything    
in the operating system but you have docker already implemented.
From the other way it require to be built at the target system.


To build the docker image you need to pull this repository.    

Change current directory to "container" subdirectory of the repository

execute (usually as root):
   docker build -t bright .
that will create docker container tagged "bright"

now you can execute the tool in the container:

docker run -e IPSTACK_KEY="d99d9dd999999dd9dd9d999dd9dd999" bright 1.2.3.4 json

which should produce the same output types as shell version.



# Security of the solution

To keep security at higher level you should consider:
- to implement something like AWS-KMS or any other security management system for storing your IPstack key
- not to use IPstack key variable directly in shell execution to avoid storing it in the shell history
- consider to use Docker Secret volume for docker version to provide higher security
- when used within pipelines use CI/CD secret management to provide the Key
- consider to implement https API requests instead of HTTP ones.





