# Virtual Machine Testbed for *ita_navigation*

> This folder contains the files to support simulation of the repo *ita_navigation*

### The VM configuration (testbed - guest machine)

- Ubuntu 14.04
- ROS Kinetic

## Pre-requisites (host machine)

This testbed was tested in a host machine with the following configuration:

- Ubuntu 18.04 (bionic)
- Vagrant 2.2.7 
- Oracle VirtualBox 6.1

Vagrant and VirtualBox are **mandatory** to use this testbed.

More info:
[Oracle VirtualBox](https://virtualbox.org/wiki/Downloads)

[Vagrant](https://www.vagrantup.com/downloads.html)

## Reproducing this testbed

```
$ git clone https://github.com/carlospotter/ita_navigation.git
$ cd ita_navigation/testbed/
$ vagrant up
```
