# Citrix ADC & Citrix ADM Ansible modules

This repository provides [Ansible](https://www.ansible.com)  modules for configuring [Citrix NetScaler](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix NetScaler are supported.

The code here should be considered alpha quality and may be broken at times due to experiments and refactoring. Tagged releases should be stable. The most stable version will be availble with Ansible automatically.

## Module renaming

Note that as of this [commit](https://github.com/citrix/netscaler-ansible-modules/commit/b53935432646741d9af27d9617480517a28aa86d)
all modules were renamed to match the new Citrix product names.

See [here](https://www.citrix.com/about/citrix-product-guide) for reference.

All modules which previously started with the `netscaler_` prefix have been renamed to
to start with the `citrix_adc_` prefix.

All new modules will follow this convention as well.

Until these changes are integrated into the Ansible distribution the Citrix ADC
module names will differ depending on where they were installed from.

## Documentation

Documentation is hosted at [readthedocs](http://netscaler-ansible.readthedocs.io/).

Currently the following modules are implemented

* citrix\_adc\_appfw\_confidfield - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_fieldtype - Configuration for application firewall form field type resource
* citrix\_adc\_appfw\_global\_bindings - Define global bindings for AppFW
* citrix\_adc\_appfw\_htmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_jsoncontenttype - Configuration for JSON content type resource
* citrix\_adc\_appfw\_learningsettings - Configuration for learning settings resource
* citrix\_adc\_appfw\_policy - Manage Netscaler Web Application Firewall policies
* citrix\_adc\_appfw\_policylabel - Manage Netscaler Web Application Firewall policy labels
* citrix\_adc\_appfw\_profile - Manage Netscaler Web Application Firewall profiles
* citrix\_adc\_appfw\_settings - Manage Netscaler Web Application Firewall settings
* citrix\_adc\_appfw\_signatures - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_wsdl - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlcontenttype - Configuration for XML Content type resource
* citrix\_adc\_appfw\_xmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlschema - Configuration for configured confidential form fields resource
* citrix\_adc\_cs\_action - Manage content switching actions
* citrix\_adc\_cs\_policy - Manage content switching policy
* citrix\_adc\_cs\_vserver - Manage content switching vserver
* citrix\_adc\_gslb\_service - Manage gslb service entities in Netscaler
* citrix\_adc\_gslb\_site - Manage gslb site entities in Netscaler
* citrix\_adc\_gslb\_vserver - Configure gslb vserver entities in Netscaler
* citrix\_adc\_lb\_monitor - Manage load balancing monitors
* citrix\_adc\_lb\_vserver - Manage load balancing vserver configuration
* citrix\_adc\_nitro\_request - Issue Nitro API requests to a Netscaler instance
* citrix\_adc\_save\_config - Save Netscaler configuration
* citrix\_adc\_server - Manage server configuration
* citrix\_adc\_service - Manage service configuration in Netscaler
* citrix\_adc\_servicegroup - Manage service group configuration in Netscaler
* citrix\_adc\_ssl\_certkey - Manage ssl cerificate keys
* citrix\_adm\_application - Manage applications on Citrix ADM
* citrix\_adm\_dns\_domain\_entry - Manage Citrix ADM domain names
* citrix\_adm\_login - Login to a Citrix ADM instance
* citrix\_adm\_mpsgroup - Manage Citrix ADM user groups
* citrix\_adm\_mpsuser - Manage Citrix ADM users
* citrix\_adm\_ns\_facts - Retrieve facts about Citrix ADM managed instances
* citrix\_adm\_poll\_instances - Force the poll instances network function on the target Citrix ADM
* citrix\_adm\_rba\_policy - Manage Citrix ADM rba policies
* citrix\_adm\_rba\_role - Manage Citrix ADM rba roles
* citrix\_adm\_stylebook - Create or delete Citrix ADM stylebooks
* citrix\_adm\_tenant\_facts - Retrieve facts about Citrix ADM tenants



## Pre-requisites

* NITRO Python SDK (available from https://www.citrix.com/downloads/netscaler-adc or from the "Downloads" tab of the Netscaler GUI)
* Ansible       
* Python 2.7 or 3.x

## Installation

### Using `virtualenv` (recommended)
Use of a python virtualenv during installation is recommended.

* Activate the virtualenv (`source bin/activate`)
* Install all dependencies by running ```pip install -r requirements.test.txt``` from the project checkout.
* Install the netscaler modules using ```python install.py```

### Global install
* Install Ansible (`sudo pip install ansible`)
* Install NetScaler SDK (`pip install deps/nitro-python-1.0_kamet.tar.gz`)
* Install NetScaler modules (`sudo python install.py`). It tries to find the ansible installation directory and then copies the module files to the appropriate places.

If the ansible installation is on a dirctory that requires root access, the install script should be run with root privileges.
If the isntallation script fails and you know where ansible is located on your system you can do a manual installation.
Just copy the contents of the ansible-modules directory to the extras module directory and the netscaler.py file to the module_utils directory of ansible.

### Backport for Ansible 2.4.x

The modules are developed against the latest development version of ansible.

Some changes made by the core ansible developers caused the modules to lose backwards portability to ansible 2.4.

If you need the latest version of the modules present in this repository and are restricted to using ansible 2.4 you can use
the backport branch [backport_2.4](https://github.com/citrix/netscaler-ansible-modules/tree/backport_2.4) which
contains the fixes needed for the modules to run under ansible 2.4 while also containing the latest changes.

This branch will be kept up to date with the master branch.

## Usage

All modules are intended to be run on the ansible control machine or a jumpserver with access to the Citrix NetScaler appliance.
To do this you need to use the `local_action` or the `delegate_to` options in your playbooks.

There are sample playbooks in the `samples` directory.

Detailed documentation for each module can be found in the htmldoc directory.

Documentation regarding the Citrix NetScaler appliance configuration in general can be found at the following link, http://docs.citrix.com/en-us/netscaler/11-1.html

### MAS proxied calls

There is also the ability to proxy module NITRO calls through a MAS to a target Netscaler.

In order to do that you need a NITRO Python SDK that has the MAS proxy calls capability and also follow these 2 steps.

1. First acquire a nitro authentication token with the use of the ```netscaler_nitro_request```  ```mas_login``` operation.
2. Next all subsequent module invocations should have the ```mas_proxy_call``` option set to ```true``` , replace the ```nitro_user``` and ```nitro_pass``` authentication options with the ```nitro_auth_token``` acquired from the previous step and finally include the ```instance_ip``` option to instruct MAS to which netscaler to proxy the calls.

A  sample playbook is provided in the samples directory. [mas_proxied_server.yaml](https://github.com/citrix/netscaler-ansible-modules/blob/master/samples/mas_proxied_server.yaml)

## Citrix ADC connection plugin

The Citrix ADC connection plugin allows the use of standard Ansible modules, such as `shell` and `fetch`, with Citrix ADC.

### Installation

The installation script provided here `install.py` will install the plugin to the ansible path inside the standard Ansible connection plugin directory.

You can also manually copy the connection plugin source file located in `ansible-plugin/ssh\_citrix\_adc.py` to a custom location that Ansible will search for it. Refer to the Ansible documentation for details.

### Usage

In order for a standard Ansible module to work properly with the Citrix ADC connection plugin the following conditions must hold true.

* Modify the playbook so that it uses the connection plugin (`connection: ssh_citrix_adc`).
* Citrix ADC does not have the python interpreter path defined, so one should pass this path when defining the host group (`ansible_python_interpreter: /var/python/bin/python`).
* The plugin works only with ssh key based authentication. The remote Citrix ADC must have the public ssh key of the controlling machine in their authorized_keys file (`/flash/nsconfig/ssh/authorized_keys`).
* In the local ansible.cfg file make sure the following lines exist:
```
[defaults]
host_key_checking = False

[ssh_connection]
scp_if_ssh = True
```

You can find usage samples in this [folder](samples/citrix_adc_connection_plugin).

### Citrix ADC and standard Ansible modules in a single playbook

There are some conflicting configuration options when using a standard Ansible module with a Citrix ADC specific module in the same playbook.

To have such a playbook execute correctly the following solutions are proposed.

* Have a single playbook with multiple plays ( [sample](samples/citrix_adc_connection_plugin/multiple_plays.yaml) ).
* Have a single play configured for standard Ansible modules and define the neeeded overrides in the Citrix ADC specific tasks ( [sample](samples/citrix_adc_connection_plugin/override_citrix_adc_tasks.yaml) ).
* Have a single play configured for Citrix ADC specific modules and define the needed overrides for the generic Ansible tasks ( [sample](samples/citrix_adc_connection_plugin/override_generic_tasks.yaml) ).


## What if there is no module for your configuration?

When there is no module that covers the ADC configuration you want to apply there are
a few options that will allow you to still apply the configuration through an ansible playbook.

### Use the citrix\_adc\_nitro\_request module.

This a module that is a thin wrapper around the NITRO REST API.
It provides a number of operations which it then translates into HTTP requests
and provides the resulting NITRO API response in a well defined return value.

You can find examples of using the module in this [folder](samples/nitro_request)

### Use the roles leveraging citrix\_adc\_nitro\_request module

Using the citrix\_adc\_nitro\_request module is quite barebones as all workflow
must be handled by the user.

A step up in functionality are the roles that leverage this module to provide
a more complex workflow that resembles that of a fully fledged module.

Roles invoke the citrix\_adc\_nitro\_request module multiple times and
also have logic programmed into them to apply the correct operation
under the current configuration state.

Using a role to create a configuration entity is different from calling
the generic citrix\_adc\_nitro\_request module, since the role will
search for the configuration item and if it exists it will compare it
to the configuration input.

Depending on the processing result it will either create, update, recreate, delete or simply
do a noop for the configuration passed. It will also populate an output variable
that will contain information for the processing that took place and the user
can test these values to see what actually happened.

Additionally roles provide a `dry_run` option during which no actual change is made
but the output variables are populated just as in a normal run. This is useful to verify
that given a configuration the operations performed will be what the user expects.

Examples can be found in this [folder](samples/recipes)


### Use the connection plugin with the `shell` Ansible module

As a last resort the user can user the `shell` Ansible module
along with the Citrix ADC connection plugin to issue `nscli` commands
to the target ADC.

This provides the least feedback but it is useful for one off
configuration steps or when nothing else is applicable.

Examples can be found in this [folder](samples/citrix_adc_connection_plugin)



## Directory structure

* `ansible-modules.` Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* `ansible-plugins.` Contains all the ansible plugins available.

* `tests.` Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* `samples.` Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* `htmldoc.` Contains the html documentation for each module.

* `utils.` Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* `documentation_fragments.` Contains the Citrix NetScaler specific documentation files for ansible.

* `run_tests.py`. Top level script to run all the tests.

## LICENSE
**GPL V3**
See [LICENSE](./LICENSE)

## COPYRIGHT

**COPYRIGHT 2017 CITRIX Systems Inc**

## Contributions
Pull requests and issues are welcome. 
