## Base goals app file
from project import Project
from places import Place
from total import Total
import sys 

if __name__ == "__main__":
    print ""
    print "2015 Goals"
    
    print "Goal 1: Ship 48 projects"
    proj = Project()
    print "Projects Shipped", ", ".join(proj.projects)
    print "Projects Remaining", 48-len(proj.projects)
    print ""
    
    place = Place()
    print "Goal 2: Visit 48 projects"
    print "Places Visited", ", ".join(place.places)
    print "Places Remaining", 48-len(place.places)
    print ""
    
    print "Goal 3: Minimize my Belongings"
    print ""
    
    print "Goal 4: Do Yoga / Airtone weekly"
    print ""
    
    print "Goal 5: Be 100% nomadic"
    print ""
    
    print "Goal 6: Pay off all Debt and save 10K"
    budget={
    'rent':9600,
    'health':1200,
    'phone':660,
    'car':1440,
    'travel':8400,
    'priorities':18000,
    'business':8660,
    'personal':10800
    }
    t = Total(budget)
    year = sys.argv[1] if len(sys.argv) > 1 else 1
    t.year_report(year)
    print ""
    
    