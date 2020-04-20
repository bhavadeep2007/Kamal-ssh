Steps to create custom facts:
1. Create /etc/ansible/facts.d directory on Managed Nodes.
2. Inside of facts.d directory place one or more custom facts files with extension as .fact.
3. Make sure that the output of fact file should be a json.
4. The fact file should have execution permission.


sudo mkdir /etc/ansible/facts.d
sudo chown -R ansible_user:ansible_user !$
cat <<EOF >/etc/ansible/facts.d/git_httpd_version.fact
#!/bin/bash
get_version=$(git --version | awk '{print $3}')
httpd_version=$(httpd -version | awk 'NR==1 {print $3}')

cat <<EOF
{
    "Git_Version" : "$get_version",
    "Httpd_Version": "$httpd_versin"
}
EOF

chmod u+x git_httpd_version.fact


ansible mistaging -m file -a "path=/etc/ansible/facts.d state=directory owner=oncall group=oncall" -b
ansible mistaging -m shell -a "chown oncall:oncall -R /etc/ansible" -b
ansible mistaging -m copy -a "src=/etc/ansible/facts.d/git_httpd_version.fact dest=/etc/ansible/facts.d/git_httpd_version.fact onwer=oncall group=oncall mode=755" -b


Note: Here oncall is the user, which ansbile control node will use to connect and run the script on managed nodes.



