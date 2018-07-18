import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project.settings')

import django
# Import settings
django.setup()

import random
from portal.models import Course

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


def populate_course(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        cn = random.choice(list(course_names.keys()))
        id = course_names[cn]
        d = random.choice([i+1 for i in range(7)])
        t = random.choice([i+1 for i in range(5)])
        name = Course.objects.get_or_create(cName=cn,day=d,Id=id,time=t)[0]
        name.save()




if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_course(5)
    print('Populating Complete')
