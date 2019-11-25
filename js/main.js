import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';


const myWork = [
  {
    'title': "Work Example",
    'href': "https://github.com/bfraz/kinesis-redshift-pipeline",
    'desc': "example with data ingestion with aws",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "Portfolio Boilerplate",
    'href': "https://github.com/bfraz/nessus-ec2-rhel-ansible",
    'desc': "example with ansible",
    'image': {
      'desc': "A Serverless Portfolio",
      'src': "images/example2.png",
      'comment': ""
    }
  },
  {
    'title': "Work Example",
    'href': "https://github.com/bfraz/go-mvc-web-development",
    'desc': "mvc web development with go",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example3.png",
      'comment': `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
          https://www.flickr.com/photos/37287295@N00/2540855181"`
    }
  }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
