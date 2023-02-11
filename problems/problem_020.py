# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    number_attendees = len(attendees_list)
    number_members = len(members_list) / 2
    if number_attendees >= number_members:
        return True
    else:
        return False
