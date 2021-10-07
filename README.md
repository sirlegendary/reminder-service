# reminder-service
A simple web service that stores reminders. A reminder consists only of a time (in HH:MM format) and a message which can be any arbitrary string.
```
(base) ➜  ~ curl http://localhost/api/reminders
[]


(base) ➜  ~ curl -H"Content-Type: application/json" \
       -XPOST \
       -d '{"time": "07:30", "message": "hello world"}' \
       http://localhost/api/reminders
Reminder has been created
                                                                                                                                              (base) ➜  ~ curl http://localhost/api/reminders
[
  {
    "message": "hello world", 
    "time": "07:30"
  }
]
```

## Usage

Run the below command. It will build and run the docker image.
```
./start.sh
```

Once the docker image is up, you can list all reminders with: 
```
curl http://localhost/api/reminders
```

To add to the remainder:
```
curl -H"Content-Type: application/json" \
       -XPOST \
       -d '{"time": "07:30", "message": "hello world"}' \
       http://localhost/api/reminders
```

## Notes
You can use [Postman](https://www.postman.com/) for interacting with the reminder API.

If you plan on using kubernetes, I would recommend pushing this image to [Dockerhub](https://hub.docker.com/).

I have implented a delete endpoint but it needs more work since the user has no way of finding out what the record id of the entry that they want to delete.

Since this is a reminder service, it will at some point need to be able to notify/remind users. This could be achieved by using the sleep function and [subprocess](https://docs.python.org/3/library/subprocess.html) for starting a new process.