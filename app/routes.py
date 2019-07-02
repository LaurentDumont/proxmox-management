#Flask imports
from app import app
from flask import render_template

#Application specific imports.
from proxmoxer import ProxmoxAPI
import requests

@app.route('/')
def get_dh_vm():

    def sort_dict(dict):
      sorted_vm_dict = {}
      for key in sorted(dict.keys()):
        sorted_vm_dict[key] = dict[key]
      return sorted_vm_dict
    
    PROXMOX_HOST = ''
    PROXMOX_USER = ''
    USER_PASSWORD = ''
    VERIFY_SSL = False
    try:
      proxmox_response = requests.get("https://"+PROXMOX_HOST, timeout=5, verify=False)
    except Exception as e:
      return render_template('error.html', error_message=str(e), title="Error page")
    proxmox_api_session = ProxmoxAPI(PROXMOX_HOST, user=PROXMOX_USER, password=USER_PASSWORD, verify_ssl=VERIFY_SSL)
    #vm_dict_dh1 = {"dh1": "online", "dh2": "online", "dh3": "offline", "dh4": "online"}
    vm_dict_dh1 = {}
    vm_dict_dh2 = {}
    vm_dict_dh3 = {}
    
    vm_pool = proxmox_api_session.pools.get("DH-LAB-1")
    for vm in vm_pool["members"]:
      vm_dict_dh1[vm["name"]] = vm["status"]
    sorted_vm_dict_dh1 = sort_dict(vm_dict_dh1)

    vm_pool = proxmox_api_session.pools.get("DH-LAB-2")
    for vm in vm_pool["members"]:
      vm_dict_dh2[vm["name"]] = vm["status"]
    sorted_vm_dict_dh2 = sort_dict(vm_dict_dh2)

    vm_pool = proxmox_api_session.pools.get("DH-LAB-3")
    for vm in vm_pool["members"]:
      vm_dict_dh3[vm["name"]] = vm["status"]
    sorted_vm_dict_dh3 = sort_dict(vm_dict_dh3)

    return render_template('proxmox.html', dh1_vms=sorted_vm_dict_dh1, dh2_vms=sorted_vm_dict_dh2, dh3_vms=sorted_vm_dict_dh3, title="Dreamhack Lab Status")
