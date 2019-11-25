import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';


const myWork = [
  {
    'title': "Data Lake Ingestion on AWS",
    'href': "https://github.com/bfraz/kinesis-redshift-pipeline",
    'desc': "An Automated data ingestion solution on AWS using Apache Nifi to manipulate data and send to Redshift",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "System Administration",
    'href': "https://github.com/bfraz/nessus-ec2-rhel-ansible",
    'desc': "Example leveraging Ansible to for System Administration",
    'image': {
      'desc': "A Serverless Portfolio",
      'src': "images/example2.png",
      'comment': ""
    }
  },
  {
    'title': "Web Development",
    'href': "https://github.com/bfraz/go-mvc-web-development",
    'desc': "An example of a website built in Go, leveraging MVC architecture",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example3.png",
      'comment': `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
          https://www.flickr.com/photos/37287295@N00/2540855181"`
    }
  }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
