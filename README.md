# container-orchestration-tool-with-built-in-cli
This is a container orchestration tool through which a user can launch, stop, terminate docker instances from a web interface. Also it contains a console feature through which user can access the command line of the containers from the web application itself. Technologies used to implement this tool are Docker, Ansible, AWS, Python CGI.

Step 1: Setup Controller Node on AWS Instance.

-> Launch AWS EC2 Instance with AMI of RHEL 8.

-> SSH into EC2 instance using security credentials.

-> Install Python3 and Python3-pip in EC2 instance.

-> Install Docker in EC2 instance.

-> Install Ansible in EC2 instance ( Refer to this video for easy installation of ansible on RHEL 8: https://youtu.be/-Y8Oatd49qA )
 
-> Install Apache web server(httpd)

After performing the above steps our controller node is ready to develop our orchestration tool.
