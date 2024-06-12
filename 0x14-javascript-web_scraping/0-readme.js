<<<<<<< HEAD

=======
>>>>>>> a8c5a39231a6f968a1ccb7d15c7cfe4a6d711d9e
#!/usr/bin/node

const file = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: Please provide a file path');
  process.exit(1);
}
file.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('error reading file', err);
  } else {
    console.log(data);
  }
});
