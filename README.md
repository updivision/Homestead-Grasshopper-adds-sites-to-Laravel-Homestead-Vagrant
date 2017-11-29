# Homestead Grasshopper: A super script that adds sites automatically to Laravel Homestead (Vagrant).
## Description
**Homestead Grasshopper** is a script that automatically adds sites in the Laravel Homestead (Vagrant) environment and “hosts” file. More precisely, it adds the site name and address in the “hosts” file and file paths in Homestead.yaml.   You can just add your site name when running the script and you are done. Or, if you are the control freak type, you can manually configure the site address, hosts file path and more.  

The program was created using Python programming language, so it will work on most used OS. That includes Windows, macOS and Linux (Python is pre-installed on most Linux distributions).

## Requirements
- Python version 2.7+

## How to install  

Quick Installation steps: 
1. Verify you have **Python version 2.7+** installed on your computer.
2. Download [HomesteadGrasshopper.py](https://github.com/updivision/Homestead-Grasshopper-adds-sites-to-Laravel-Homestead-Vagrant/HomesteadGrasshopper.py)
3. Open the terminal and type  ```$sudo python add_site_to_vagrant.py your_site_name```  to veriy if the installation was successfull.
[See instructions for using Homestead Grasshopper](#instructions-for-using-homestead-grasshopper)
---
#### 1. Python install
For using Homestead Grasshopper, you will need Python interpreter version 2.7+ installed on your computer.

Python comes preinstalled on most Linux distributions, and is available as a package on all others. 
- If you need more information, for **Linux** see https://docs.python.org/2/using/unix.html
- For **Mac OS** see https://docs.python.org/2/using/mac.html
- For **Windows** see https://docs.python.org/2/using/windows.html

After you have installed Python interpreter, you are ready to use Homestead Grasshopper.

#### 2. Download [HomesteadGrasshopper.py](https://github.com/updivision/Homestead-Grasshopper-adds-sites-to-Laravel-Homestead-Vagrant/HomesteadGrasshopper.py)
Download the HomesteadGrasshopper.py script from [this link](https://github.com/updivision/Homestead-Grasshopper-adds-sites-to-Laravel-Homestead-Vagrant/HomesteadGrasshopper.py) on your computer in any directory. 

#### 3. Open the terminal and run the script
Open the terminal (on macOS or Linux) or Command Prompt (Windows) and type your first command:
```$sudo python HomesteadGrasshopper.py your_site_name``` (for Linux) or  ```$python HomesteadGrasshopper.py your_site_name``` (for Windows)

*Note: the *sudo* command is needed for modifying the "etc/hosts" file in Linux and macOS*

If the following message appears, the install was successful.

``Are you sure you want to add site your_site_name to Homestead? (in /etc/hosts and Homestead.yaml)``


# Instructions for using Homestead Grasshopper
### To access the script instructions manual, run the command:
```$python HomesteadGrasshopper.py --help```

#### (1) QUICK COMMAND for adding a site to Homestead:

- Linux/macOS:

&nbsp;```$sudo python HomesteadGrasshopper.py your_site_name```

- Windows:

&nbsp;```$python HomesteadGrasshopper.py your_site_name```

**This will do:**
- add the site name and default Homestead address in the “hosts” file
- add file paths and configurations in Homestead.yaml


#### (2) CUSTOMIZATION PARAMETERS. You also have the possibility to use these additional parameters:

- --config.site_address="[your_site_address]"
- --config.hosts_path="[etc_hosts_path]"
- --config.homestead_yaml_path="[yaml_path]
- --config.folder="[folder_name]"
- --config.site_extension="[extension_name]"

**Example:**
   ``` 
  $sudo python HomesteadGrasshopper.py your_site_name
	--config.site_address="192.168.10.10"
	--config.hosts_path="/etc/hosts"
	--config.homestead_yaml_path="Homestead/Homestead.yaml"
	--config.folder="public" --config.site_extension="dev"
```
*Note: If you are using Windows, do not use the "sudo" command, just type ```python HomesteadGrasshopper.py ..... ```*

**Warning! After you run the above commands, do not forget to run ```vagrant reload --provision'``` in the Homestead directory.**

# Screenshots
![screenshot 1](https://github.com/updivision/Homestead-Grasshopper-adds-sites-to-Laravel-Homestead-Vagrant/blob/master/screenshots/HomesteadGrasshopper1.png?raw=true)
![screenshot 2](https://github.com/updivision/Homestead-Grasshopper-adds-sites-to-Laravel-Homestead-Vagrant/blob/master/screenshots/HomesteadGrasshopper2.png?raw=true)
# FAQ
#### Q: The site was not added after running ```$python HomesteadGrasshopper.py your_site_name```. What should I do?

 **A1:** *If you are using Linux or macOS, maybe you forgot to run the script as administrator (using "sudo" command).*
Try ```$sudo python HomesteadGrasshopper.py your_site_name```

 **A2:** *Run ```$vagrant reload --provision``` in Homestead directory after running the HomesteadGrasshopper.py script*

# Contributors
- [Diana Marusic](https://github.com/mdiannna)
