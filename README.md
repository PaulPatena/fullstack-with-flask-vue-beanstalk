## About this project
The aim of this project is demo a full-stack solution using Python  Flask as backend and VueJS as frontend and deployment using AWS Beanstalk.

As this project progresses, I will be using pytest framework for unit testing the backend whilst using Cypress to perform end-to-end tests.

## Deployed in
https://awsbeanstalk.paulpatena.com/#/

## Requirements
1. The user should be able to see his task list, a maximum of 10 entries. Button to "add new card" should be disabled when number of entries reach ten.
2. The text area should automatically grow, the data on a text-area should automatically be saved when it comes out of focus.

## Architectural Decisions
1. When running the UI in debug mode, you need to configure that API requests goes to your debug server port and when in production, api requests should be directed to the actual server. This is done by using the .env files in the Vue project. 
2. When running the backend server in debug mode, its is being served at port 5000 whilst we expect that the debug UI is running at port 8080, we need to enable CORS only during debugging so that in-flight requests from UI won't be blocked by browser.

## Compiling Front End
1. Go to user_interface_in_vue directory
```
npm install
npm run build
``` 

## Deployment Guide on AWS Elastic Beanstalk

### Pre-requisites:
1. Install EB CLI on your PC
2. Amazon Web Services account

### Setting Up on First Setup:
1. Navigate to the root of project, in terminal ```eb init``` and following the prompts
2. In terminal ```eb create``` to setup your application and env in the cloud, this might take 5+ minutes on initial configuration
3. Transpile your VueJS the run ```eb deploy```

### Setting Up SSL/TLS Certificate
1. Pre-requisite that you have your own domain name
2. In ACM, Create a public cert for your domain *.yourdomain.com
3. In EC2, Add a HTTPS listener in your load balancer and attach your certificate (from ACM)
4. In the DNS settings of your domain registrar, add a CNAME that points to Elastic Beanstalk applications DNS name

