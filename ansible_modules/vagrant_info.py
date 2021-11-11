#!/usr/bin/python
import vagrant
import os
from ansible.module_utils.basic import *

class VagrantVmController:
    def __init__(self, path):
        self.vm = vagrant.Vagrant(os.path.dirname(path))

    def set_state(self, desired_state):
        choice_map = {
            "running": self.vm_set_running,
            "stopped": self.vm_set_stopped,
            "destroyed": self.vm_set_destroyed
        }
        #get link to the necessary function and call it.
        return choice_map.get(desired_state)()

    #get status from Vagrant library.
    def get_vagrant_running_status(self):
        return self.vm.status()[0].state

    #start virtual machine
    def vm_set_running(self):
        has_changed = False
        if self.get_vagrant_running_status() != 'running':
            try:
                self.vm.up()
            except(OSError, IOError, ValueError):
                return (False,{'error:' : 'error creating vm'})
            has_changed = True
        status = self.vm.conf()
        status.update({'ip_adresses': self.vm._run_vagrant_command(['ssh', '-c', "hostname -I"]).split(' ')[0:-1]})
        status.update({'changed': has_changed,'state': 'running'})
        return status

    #stop virtual machine
    def vm_set_stopped(self):
        has_changed = False
        if self.get_vagrant_running_status() == 'running':
            try:
                self.vm.halt()
            except(OSError, IOError, ValueError):
                return (False,{'error:' : 'error stopping vm'})
            has_changed = True
        return {'changed': has_changed,'state': 'stopped'}
    #destroy virtual machine
    def vm_set_destroyed(self):
        has_changed = False
        if self.get_vagrant_running_status() != 'not_created':
            try:
                self.vm.destroy()
            except(OSError, IOError, ValueError):
                return (False,{'error:' : 'error destroying vm'})
            has_changed = True
        return {'changed' : has_changed, "state" : "destroyed"}

def main():
    # Module arguments
    module = AnsibleModule(argument_spec = {
        path  = {'type': 'str', 'required': 'True'},
        state = {'type': 'str', 'required': 'True', 'choices' = ["running", "stopped", 'destroyed']}
     }
    )

    #initialize virtual machine object
    vagrant_vm = VagrantVmController(module.params['path'])

    #set vm state and return result
    result = vagrant_vm.set_state(module.params['state'])
    module.exit_json(**result)

if __name__ == '__main__':
    main()
