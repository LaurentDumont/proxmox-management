from proxmoxer import ProxmoxAPI

PROXMOX_HOST = ''
PROXMOX_USER = ''
USER_PASSWORD = ''
VERIFY_SSL = False

proxmox_api_session = ProxmoxAPI(PROXMOX_HOST, user=PROXMOX_USER, password=USER_PASSWORD, verify_ssl=VERIFY_SSL)

for vm in proxmox_api_session.cluster.resources.get(type='vm'):
    print("{0}. {1} => {2}" .format(vm['vmid'], vm['name'], vm['status']))
