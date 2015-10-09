import random
from .models import article

def all_objects(request):
	total = article.objects.all()	
	cn = random.sample(total,0)
	rows = {'box':cn}
	return rows

