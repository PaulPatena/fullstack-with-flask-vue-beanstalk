## Deployment Guide on AWS Elastic Beanstalk

### Pre-requisites:
1. Install EB CLI on your PC
2. Amazon Web Services account

### Setting Up on First Setup:
1. Navigate to the root of project, in terminal ```eb init``` and following the prompts
2. In terminal ```eb create``` to setup your application and env in the cloud, this might take 5+ minutes on initial configuration
3. Edit your code manually and when you are ready to deploy, in terminal ```eb deploy```

### Setting Up SSL/TLS Certificate
1. Pre-requisite that you have your own domain name
2. In ACM, Create a public cert for your domain *.yourdomain.com
3. In EC2, Add a HTTPS listener in your load balancer and attach your certificate (from ACM)
4. In the DNS settings of your domain registrar, add a CNAME that points to Elastic Beanstalk applications DNS name

