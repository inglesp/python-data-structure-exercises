# This program knows about the schedule for a conference that runs over the
# course of a day, with sessions in different tracks in different rooms.  Given
# a room and a time, it can tell you which session starts at that time.
#
# Usage:
#
# $ python conference_schedule.py [room] [time]
#
# For instance:
#
# $ python conference_schedule.py "Main Hall" 13:30
# 


schedule = {
    'Main Hall': {
        '10:00': 'Django REST framework',
        '11:00': 'Lessons learned from PHP',
        '12:00': "Tech interviews that don't suck",
        '14:00': 'Taking control of your Bluetooth devices',
        '15:00': "Fast Python? Don't Bother!",
        '16:00': 'Test-Driven Data Analysis',
    },
    'Seminar Room': {
        '10:00': 'Python in my Science Classroom',
        '11:00': 'My journey from wxPython tp PyQt',
        '12:00': 'Easy solutions to hard problems',
        '14:00': 'Taking control of your Bluetooth devices',
        '15:00': "Euler's Key to Cryptography",
        '16:00': 'Build your Microservices with ZeroMQ',
    },
    'Assembly Hall': {
        '10:00': 'Distributed systems from scratch',
        '11:00': 'Python in Medicine: ventilator data',
        '12:00': 'Neurodiversity in Technology',
        '14:00': 'Chat bots: What is AI?',
        '15:00': 'Pygame Zero',
        '16:00': 'The state of PyPy',
    },
}

print('There are talks scheduled in {} rooms'.format(len(schedule)))


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that that it can tell you what session is running in
#   a room at a given time, even if a session doesn't start at that time.
# * Change the program so that if called with a single argument, the title of a
#   session, it displays the room and the time of the session.
