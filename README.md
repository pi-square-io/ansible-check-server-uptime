## Ansible - Check Server Uptime
uptime gives a one line display of the following information.
- The current time
- how long the system has been running
- how many users are currently logged on
## Explanation
1. marks the start and end of a YAML script.
2. marks the member of the list.
3. Key: Value represents a dictionary in YML which defines something.
4. “name:” key defined with value “Get server uptime”
5. “hosts” key defines on what all hosts we want to run below task(s).
6. “all” is a default identifier which contains all hosts defined in the hosts file.
7. “tasks” defines the various tasks we want to perform in this YML script.

##### hosts file:  allows you to access any server you want.

The first script we have created included the ping response of all hosts.

```sh
[mustapha]
vm2 ansible_ssh_host=192.168.40.128

[mustapha:vars]
ansible_ssh_user={{ user }}
ansible_password={{ password }}
```

#### uptime.yaml:  The second YAML script we have created is to get server uptime, and server date/time.

```sh
---
- name: Get server uptime
  hosts: all

  tasks:
   - name: Get uptime first
     shell: uptime
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"

   - name: Get date second
     shell: date
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
```
###### shell command:
```sh
---
ansible-playbook -l all -i hosts utime.yaml 
```