"""pexpect"""
import pexpect as pe# pip install pexpect
def main():
    """pexpect"""
    promt = '#'
    ip = '172.31.106.1'
    username = 'admin'
    password = 'cisco'
    command = 'show ip int brief'
    
    child = pe.spawn('telnet ' + ip, timeout=100)
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(promt)
    child.sendline(command)
    child.expect(promt)
    result = child.before
    print(result)
    print()
    print(result.decode('utf-8'))
    child.sendline('exit')
main()