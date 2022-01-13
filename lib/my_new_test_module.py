#!/usr/bin/python3

ANSIBLE_METADATA = {
        'metadata+version': '1.1',
        'status': ['preview'],
        'supported_by': 'rzfeeser'
}

DOCUMENTATION = '''
---
module: testmod
short_description: This module is being designed so we can observe the minimum required config for an Ansible module.
version_added: "2.8"
description:
    - This module is being designed so we can observe the minimum required config for an Ansible module.
    - user passes a parameter called "name: " <str> <required>
    - user passes a parameter called "augment: " <bool> <required>
    - if augment: true then ansible returns name + additional string as well as indicates YELLOW CHANGE on PLAY RECAP
    - if augment: false then ansible returns name string and indicates GREEN OK on PLAY RECAP
    - if "name: fail me" then ansible returns FAILED in PLAY RECAP
author:
    - RZFeeser@alta3.com
'''

EXAMPLE = '''
# Pass in a name
- name: Requesting GREEN OK from our new module
  testmod:
    name: Zach
    augment: false
- name: Requesting YELLOW CHANGE from our new module
  testmod:
    name: Zach
    augment: true
- name: Requesting FAILED from our new module
  testmod:
    augment: fail me
'''

RETURN = '''
original_message:
    description: The name parameter that was passed by our user
    type: str
message:
    description: The name parameter returned the same way or in an augmented fashion depending on how change: is set
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    """module logic"""
    
    ## define the parameters that a user may pass in
    module_args = dict(
            name=dict(type='str', required=True),
            augment=dict(type='bool', default=False)
        )

    ## seed the result diction in the object
    ## we primarily care about the change and state
    ## change is if this module effectively modified the target
    ## this is what is sometimes called idempotency (don't use this term)
    ## state will include any data that you want your module to pass back
    ## for consumption, for example, in another task
    result = dict(
            changed=False,
            original_message='',
            message=''
        )


    ## the AnsibleModule object will be our abstraction working with Ansible
    ## this includes instantiation, a couple of common attr would be the
    ## args / params passed to the execution, as well as if the module
    ## supports check mode
    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )

    ## give the user the ability to run the module but not make any changes
    ## to the target hosts or our environment, just return the current state
    ## as we have described thus far
    if module.check_mode:
        return result

    ## result is what is returned
    ## we always want to return the original messaged as delivered by the user
    result['original_message'] = module.params['name']

    ## here is where we test if the user passed TRUE or FALSE for the param change:
    if module.params['augment'] == False:
        result['message'] = module.params['name']
    else:
        result['message'] = module.params['name'] + " is a wild and crazy guy!!! -- or so says Dan Akroyd."

    if module.params['name'] == 'fail me':
        module.fail_json(msg="You requested this to fail...", **result)


    ## in the event that the module successfully executes, you will find yourself here
    ## and you will be wanting to return your result
    module.exit_json(**result)
    

def main():
    run_module()

if __name__ == "__main__":
    main()

