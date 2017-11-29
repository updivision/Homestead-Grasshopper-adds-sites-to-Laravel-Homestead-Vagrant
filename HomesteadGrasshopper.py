import sys
import os
import textwrap


default_config = {
	"site_address": '192.168.10.10',
	"hosts_path": '/etc/hosts',
	"homestead_yaml_path": '/Homestead/Homestead.yaml',
	"folder": 'public',
	"site_extension": 'dev'
}


def add_site_to_hosts(site_name, site_extension, address, hosts_path):
	temp_path = 'temp'

	# Read from hosts, write to temp
	hosts = open(hosts_path, 'r')
	temp = open(temp_path, 'w')

	temp.write(address + " " + site_name + "." + site_extension + "\n")
	temp.write(hosts.read())

	temp.close()
	hosts.close()

	# Read from temp, write to hosts
	temp = open('temp', 'r')
	hosts = open(hosts_path, 'w')
	hosts.write(temp.read())
	os.remove(temp_path)


def add_site_to_homestead_yaml(name, homestead_yaml_path, folder, site_extension):
	absolute_path = os.path.expanduser('~')
	yaml_path = absolute_path +'/' + homestead_yaml_path
	temp_path = 'temp'

	yaml= open(yaml_path, 'r')
	temp = open(temp_path, 'w')

	vagrant_folder_path = '/home/vagrant/Code/'
	line_cnt = 0
	vagrant_folder_path_cnt = -1

	for line in yaml: 
		temp.write(line)
		if 'folders:' in line:
			vagrant_folder_path_cnt = line_cnt+2
		if line_cnt == vagrant_folder_path_cnt:
			vagrant_folder_path = line[line.find("to:")+3:].replace("\n", '')

		if 'sites:' in line:
			temp.write('    - map: ' + name + '.' + site_extension + '\n')
			temp.write('      to: ' + vagrant_folder_path + '/' + name + '/' + folder +'\n')
		line_cnt+=1
	
	temp.close()
	yaml.close()

	# Read from temp, write to Homestead.yaml
	temp = open('temp', 'r')
	yaml = open(yaml_path, 'w')
	yaml.write(temp.read())		 
	os.remove(temp_path)


def read_config_parameters():
	global default_config
	errors = []
	parameters = {}
	console_parameters_cnt = 0

	# Read every parameter specified in default_config_array
	for parameter_name in default_config.keys():
		parameter_array = filter(lambda x: '--config.' + parameter_name in x, sys.argv)
		parameter = default_config[parameter_name]
		if len(parameter_array)>1:
			errors.append(parameter_name.replace('_', ' ').capitalize() + " specified multiple times")
		if len(parameter_array)==1:
			parameter = parameter_array[0].replace('--config.'+parameter_name+'=', '')
			parameter.replace('"', '')
			console_parameters_cnt += 1
		parameters[parameter_name] = parameter

	return errors, parameters, console_parameters_cnt


def print_red(message):
	sys.stdout.write('\x1b[0;31;40m')
	print message
	sys.stdout.write('\x1b[0m')


def print_warning(message):
	sys.stdout.write('\x1b[0;33;40m')
	print message
	sys.stdout.write('\x1b[0m ')


def print_success(message):
	sys.stdout.write('\x1b[0;32;40m')
	print message
	sys.stdout.write('\x1b[0m')


def print_green(message):
	sys.stdout.write('\x1b[0;32;40m')
	print message
	sys.stdout.write('\x1b[0m')


def print_errors(errors):
	for error in errors:
		print_red( error)
	print_red('Site not added to homestead. If you want to add a site to Homestead re-run the script.')


def files_exist(hosts_path, homestead_yaml_path):
	try:
		hosts = open(hosts_path, 'r')
		yaml = open(os.path.expanduser('~') + homestead_yaml_path, 'r')


	except Exception as exception:
		print_red(exception)
		return False

	hosts.close()
	yaml.close()

	return True


def print_help():
	wrapper = textwrap.TextWrapper(subsequent_indent='\t')
	print("\n")
	print("                  ***                   ")
	print("                *******                   ")
	print("                  ***                   ")
	print("\n")
	print("-------------------------------------------------------------")
	print_warning("   INSTRUCTIONS for using Homestead Grasshopper             ")
	print("-------------------------------------------------------------")
	print("Created by UPDIVISION for the open source community.           ")
	print("We also do custom software. Let's talk now about your project.           ")
	print("www.updivision.com           ")
	print("-------------------------------------------------------------")
	print("\n")
	print_green("(1) QUICK COMMAND for adding a site to Homestead:")
	print("\n")
	print('Linux/macOS:')
	print('    $sudo python HomesteadGrasshopper.py your_site_name')
	print('Windows:')
	print('    $python HomesteadGrasshopper.py your_site_name')
	print("\n")
	print("This will do:")
	print('    add the site name and default Homestead address in the "hosts" file')
	print("    add file paths and configurations in Homestead.yaml")
	print("\n")
	print_green("(2) CUSTOMIZATION PARAMETERS. You also have the possibility to use these additional parameters:")
	print('    --config.site_address="[your_site_address]')
	print('    --config.hosts_path="[etc_hosts_path]"')
	print('    --config.homestead_yaml_path="[yaml_path]')
	print('    --config.folder="[folder_name]"')
	print('    --config.site_extension="[extension_name]"')
	print("\n")
	print("EXAMPLE:")
	print(wrapper.fill('    $sudo python HomesteadGrasshopper.py your_site_name --config.site_address="192.168.10.10"' +
		' --config.hosts_path="/etc/.hosts" '+
		' --config.homestead_yaml_path="Homestead/Homestead.yaml"'+
		' --config.folder="public"' +
		' --config.site_extension="dev"'))
	print("\n")
	print_green('Note: If you are using Windows, do not use the "sudo" command, ' 
		+ 'just type $python HomesteadGrasshopper.py your_site_name')
	print("\n")
	print_warning("Warning!!! Do not forget to run '$vagrant reload --provision' in Homestead directory after site added to homestead")
	print("\n")
	print("                  ***                   ")
	print("                *******                   ")
	print("                  ***                   ")
	print("\n")
	
	

if __name__ == "__main__":
   	if len(sys.argv)<2:
	   print_errors(["No site name specified"])
	   print("")
	   exit()

	if "--help" in sys.argv:
		print_help()
		print("")
		exit()

	site_name = sys.argv[1]

	if "--config." in site_name:
		print_errors(["No site name specified"])
		print("")
		exit()


	print("\n")
	print("-------------------------------------------------------------")
	print("             Homestead Grasshopper             ")
	print("-------------------------------------------------------------")
	print("Created by UPDIVISION for the open source community.           ")
	print("We also do custom software. Let's talk now about your project.           ")
	print("www.updivision.com           ")
	print("-------------------------------------------------------------")
	print("\n")



	config_parameters_result = read_config_parameters()
	config_parameters_errors = config_parameters_result[0]
	config_parameters = config_parameters_result[1]
	console_parameters_cnt = config_parameters_result[2]

	hosts_path = config_parameters["hosts_path"]
	site_address = config_parameters["site_address"]
	homestead_yaml_path = config_parameters["homestead_yaml_path"]
	folder = config_parameters["folder"]
	site_extension = config_parameters["site_extension"]

	if len(config_parameters_errors):
		print_errors(config_parameters_errors)
		print("")
		exit()

	if(console_parameters_cnt + 2 < len(sys.argv)):
		print_errors(["Some config parameters are not formatted properly. Try --help command"])
		print("")
		exit()

	print_warning('Grasshopper says: Are you sure you want to add site "' + 
		site_name + '" to Homestead?(in /etc/hosts and Homestead.yaml)')

	print_green('If you need help or want to see additional parameters, type "no" and re-run the script with the --help option')
	option = raw_input("Type yes/no\n") 

	if option == "yes":
		if files_exist(hosts_path, homestead_yaml_path):
			try:
				add_site_to_hosts(site_name, site_extension, site_address, hosts_path)
				add_site_to_homestead_yaml(site_name, homestead_yaml_path, folder, site_extension)

			except Exception as exception:
				print_red(exception)
				print_red('Site not added to Homestead. If you want to add a site to Homestead re-run the script.')
				print_red('If you need help or want to see additional parameters re-run the script with the --help option.')
				print("")
				exit()

			print_success("Site '" + site_name + "' added to Homestead at address " + site_address)
			print_warning("! Do not forget to run '$vagrant reload --provision' in Homestead directory")

		else:
			print_red('Site not added to Homestead. If you want to add a site to Homestead re-run the script.')
			print_red('If you need help or want to see additional parameters re-run the script with the --help option.')

			print("")
			exit()

	if option != "no" and option != "yes":
		print("Wrong option")
		print("Program exited")
		print("")

	if option == "no":
		print_red('Site not added to Homestead. If you want to add a site to Homestead re-run the script.')
		print_red('If you need help or want to see additional parameters re-run the script with the --help option.')
		print("")
