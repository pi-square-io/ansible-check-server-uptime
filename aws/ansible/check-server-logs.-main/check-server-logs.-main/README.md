# check-server-logs.
check server logs gives  display of the following information.
- show all journal entries, which can be fairly long.
- To list the boots of the system
- shows journal messages logged within the last hour.
- To see messages logged in the last two days
- show messages between two dates and times

Explanation
marks the start and end of a YAML script.
marks the member of the list.
Key: Value represents a dictionary in YML which defines something.
“name:” key defined with value “Get server uptime”
“hosts” key defines on what all hosts we want to run below task(s).
“all” is a default identifier which contains all hosts defined in the hosts file.
“tasks” defines the various tasks we want to perform in this YML script.

hosts file:
allows you to access any server you want.

The first script we have created included the ping response of all hosts.
```sh 
[mustapha]
vm2 ansible_ssh_host=192.168.40.128

[mustapha:vars]
ansible_ssh_user={{ user }}
ansible_password={{ password }}
```

logs_server.yaml

- The YAML script we have created is to check server logs
```sh 
---
- name: Get server logs
  hosts: all

  tasks:
   - name: Get logs first5
     shell: journalctl 
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
```
- The YAML script we have created is to list the boots of the system
```sh 
---
- name: Get server logs
  hosts: all
  - name: Get logs first4
     shell: journalctl --list-boots
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
```
- The YAML script we have created is to shows journal messages logged within the last hour.
```sh
---
- name: Get server logs
  hosts: all
  - name: Get logs first2
     shell: journalctl --since "1 hour ago"
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
```
   - The YAML script we have created is to  see messages logged in the last two days
 ```sh
   ---
- name: Get server logs
  hosts: all
  - name: Get logs first3
     shell: journalctl --since "2 days ago"
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
```
  - The YAML script we have created is to  show messages between two dates and times
 ```sh
- name: Get server logs
  hosts: all
   - name: Get logs first1
     shell: journalctl --since "2022-03-11 14:15:00" --until "2022-03-11 14:20:00"
     register: hello
   - debug: msg="{{ hello.stdout }}"
   - debug: msg="{{ hello.stderr }}"
   ```

### shell command:
```sh
---
ansible-playbook -l all -i hosts utime.yaml 
 ```