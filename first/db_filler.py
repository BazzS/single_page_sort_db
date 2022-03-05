from django.utils import timezone
import random

from first.models import Mat

match_country = ['Spain','Italy','France','Germany','Russia']
home_team = ['Real','Spartak','Barcelona','Arsenal','Milan','Bayer','Inter','Dinamo']

for match in match_country:
    for home in home_team:
        Mat.objects.create(match_date = timezone.localdate + timezone.timedelta(random.randint(10,150)),
        match_name = f"{match}{home}",
        match_count = random.randint(20,10000),
        match_distance = random.randrange(500,3000,5))
