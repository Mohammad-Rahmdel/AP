import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project.settings')

import django
# Import settings
django.setup()

import random
from portal.models import AllCourses

course_names = {'AP':2700,
                'DB':2701,
                'BP':2702,
                'Electronic I':2703,
                'Electronic II':2704,
                'Electronic III':2705,
                'Logic Circuit':2706,
                'General Mathematics':2707,
}

TIME = ['07:45-09:15',
        '09:15-10:45',
        '10:45-12:15',
        '13:00-15:00',
        '15:00-17:00',]

DAY = ['SAT',
       'SUN',
       'MON',
       'TUE',
       'WED',
       'SAT-MON',
       'SUN-TUE',]


def populate_course():
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(8):
        cn =list(course_names.keys())[entry]
        id = course_names[cn]
        d = (entry % 3) + 1
        t = (entry % 4) + 1
        name = AllCourses.objects.get_or_create(Name=cn,Day=d,Id=id,Time=t)[0]
        name.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_course()
    print('Populating Complete')
