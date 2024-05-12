class macAddrFormat:

    def __init__(self, mac):
        mac = None

    def MacFile(self, mac):
        mac_list = ['0','1','-']
        for i in str(mac):
            if i % 2 == 0:
                mac_list.append(i)
                mac_list.append('-')
            elif i % 2 != 0:
                mac_list.append(i)
        mac_true = ''.join(mac_list)[:20]
        return mac_true