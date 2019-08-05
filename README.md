# MIDAS (Multiple Input Docker Automation System)

-------

MIDAS is a development tool to assist in the automatic creation of docker images.


## Installation

Requirement:
* Python3
* Python YAML

```bash
pip3 install PyYAML

git clone https://github.com/ritua2/DockerImageBuilder
cd DockerImageBuilder
```



## Usage

MIDAS requires an input file, written in either json or yaml, that specifies:

* Base image
* Working directory (optional)
* Setup instructions (optional)
* Files and directories (optional)
* Order of execution (optional)

Run the script *MIDAS.py*

```bash
python3 MIDAS.py
```

Flags:

>	-f, --file: Input file, may be JSON or YAML. Default: midas.yml

>	-o, --output: Output Dockerfile path. Default: Dockerfile

>	--ignore-warnings: Ignore all warnings. 'yes'/'y'/'Y'/'1' for True. Default: False.

>	--ignore-cmd-warnings: Ignore no default command warning. 'yes'/'y'/'Y'/'1' for True.. Default: False.

>	--ignore-copy-warnings: Ignore no added file warnings. 'yes'/'y'/'Y'/'1' for True.. Default: False.

>	--ignore-run-warning: Ignore no provisioning command warnings. 'yes'/'y'/'Y'/'1' for True.. Default: False.

>	--strict: Treat warnings as errors, stop program when one occurs. 'yes'/'y'/'Y'/'1' for True.. Deafult: False.

>	-h, --help: Output Dockerfile path. Default: Dockerfile




To show a list of available flags:
```bash
python3 MIDAS.py --help
# Or
python3 MIDAS.py -h
```


## Examples

The subdirectory [tests](./tests) contains a series of provided input files and the generated Dockerfiles. All common examples share the same filename before
*.midas*. i.e. *sample-input.midas.json* and *sample-input.midas.yml* both can be used to generate the Dockerfile *sample-input-Dockerfile*.


## Acknowledgements

The development and testing for this project was done using the Jetstream \[1\]\[2\] and Chameleon\[3\] systems. We are grateful to XSEDE for providing the allocation required for implementing this project. This project is generously supported through the National Science Foundation (NSF) award \#1664022.  



### References

\[1\] Stewart, C.A., Cockerill, T.M., Foster, I., Hancock, D., Merchant, N., Skidmore, E., Stanzione, D., Taylor, J., Tuecke, S., Turner, G., Vaughn, M., and Gaffney, N.I., Jetstream: a self-provisioned, scalable science and engineering cloud environment. 2015, In Proceedings of the 2015 XSEDE Conference: Scientific Advancements Enabled by Enhanced Cyberinfrastructure. St. Louis, Missouri.  ACM: 2792774.  p. 1-8. http://dx.doi.org/10.1145/2792745.2792774 


\[2\] John Towns, Timothy Cockerill, Maytal Dahan, Ian Foster, Kelly Gaither, Andrew Grimshaw, Victor Hazlewood, Scott Lathrop, Dave Lifka, Gregory D. Peterson, Ralph Roskies, J. Ray Scott, Nancy Wilkins-Diehr, "XSEDE: Accelerating Scientific Discovery", Computing in Science & Engineering, vol.16, no. 5, pp. 62-74, Sept.-Oct. 2014, doi:10.1109/MCSE.2014.80


\[3\] Chameleon: a Scalable Production Testbed for Computer Science Research, K. Keahey, P. Riteau, D. Stanzione, T. Cockerill, J. Mambretti, P. Rad, P. Ruth,	book chapter in "Contemporary High Performance Computing: From Petascale toward Exascale, Volume 3",  Jeffrey Vetter ed., 2017 

