# Homework Assignment #2: Functions
"""
Task 1: create functions for song for any 3 attributes (considered as variables in previous assignment)
Task 2: when function is called, the function should return corresponding value for the attribute.
        Example: Artist - AR Rahman
"""
#creating a function Artist
def Artist():
    #print statement of the artist name,
    #the output to be shown
    print("AR Rahman")

#creating a function Song_Name
def Song_Name():
    #print statement of the Song name,
    #the output to be shown
    print("Dil Se")
def Duration_in_secs():
    #print statement of the nos of seconds the song plays for,
    #the output to be shown
    print(390)

#calls Artist Function
Artist()
#calls Song_Name Function
Song_Name()
#calls Duration_in_secs Function
Duration_in_secs()


#trying to use boolean as an extra function for extra credit
Duration_in_mins = 6.5

def song_length():
    if (Duration_in_mins > 4):
        print("This is a long song")
        return True

    else:
        print("This is a short song")
        return False

#calling the function song_length
song_length()
