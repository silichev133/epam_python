#!/usr/bin/python3

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
'''
EXAMPLES = r'''
'''
RETURN = r'''
'''
from ansible.module_utils.basic import AnsibleModule
import os
import re
def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        url=dict(type='str', required=True),
        war=dict(type='str', required=True),
        username=dict(type='str', required=False),
        password=dict(type='str', required=False),
    )
    result = dict(
        changed=False,
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    os.popen(#todo update deploy-info )

def main():
    run_module()

if __name__ == '__main__':
    main()
