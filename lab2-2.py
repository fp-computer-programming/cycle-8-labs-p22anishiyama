# Author: ATN 12/1/21

def invite(invitees):
    '''Takes a list parameter and returns an invite for each attendee.'''
    for name in invitees:
        print("Hi {0}, \nYou're invited to my party on Friday!".format(name))


invite(["Aiden", "Mr. Mesquita"])
