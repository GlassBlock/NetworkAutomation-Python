from SSHAutomation import SSHAutomation


def main():
    SSHAutomation.initiate_connections('./HostFiles/hosts.yaml')


if __name__ == '__main__':
    main()
