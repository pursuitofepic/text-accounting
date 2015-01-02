
import re
import sys 

class Total(object):

    def __init__(self,budget=None,filename="accounting15.taskpaper"):
        if not budget:
            self.bud={
                'rent':9600,
                'health':1200,
                'phone':660,
                'car':1440,
                'travel':8400,
                'priorities':18000,
                'business':8660,
                'personal':10800
            }
        else:
            self.bud = budget
        #print "in init"
        self.filename = filename
        self.file = open(filename, 'r')
        self.data = []
        week = ''
        month = ''
        for line in self.file:
            line = line.strip('\t\n ')
            if line and line[0] == '-': # line is a task
                #print line
                s = line.split(":")
                s[0] = s[0][2:]
                s[1] = s[1].split(' ')
                alist = []
                alist.append(s[0])
                alist.append(s[1][1])
                alist.append([])
                for item in s[1][2:]:
                    item = item.strip('@')
                    alist[2].append(item.replace(' ','_'))
                if week:
                    alist[2].append(week.replace(' ','_'))
                if month:
                    alist[2].append(month.replace(' ','_'))
                self.data.append(alist)
            elif line and line[-1] == ':': #line is a project
                
                line = line.strip(':')
                if line in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]:
                    month = line
                else:
                    week = line
                
        #print self.data
                
    def run(self):
        """
        Runs the function with the same name as sys.argv[1]
        """
        print "in run"
        try:
            doreport = False
            month = None
            if len(sys.argv) > 1 and sys.argv[1] == "report":
                doreport = True
                if len(sys.argv) > 2:
                	month = sys.argv[2]
            else:
                if len(sys.argv) == 2:
                    print sys.argv[1]
                    tag = sys.argv[1].split(' ')
                    #print tag
                elif len(sys.argv) > 2:
                    print 'to have multiple search terms, put the whole search string in quotes.'
                else:
                    tag = None
            
            if doreport:
            	#print month
                self.report(month=month)
            else:
                self.calc(tag)
            
        except Exception as e: 
            print 'There has been an error:', e
            
    def report_numbers(self, month=None):
        verbose = False
        details = {}
        details['income'] = self.calc(self.get_tag(['in'],month),verbose=verbose) #incoming after tax
        details['tax'] = self.calc(self.get_tag(['tax'],month),verbose=verbose) #income marked for Taxes
        details['essential'] = self.calc(self.get_tag(['essential'],month),verbose=verbose)
        details['rent'] = self.calc(self.get_tag(['rent'],month),verbose=verbose)
        details['health'] = self.calc(self.get_tag(['health'],month),verbose=verbose)
        details['phone'] = self.calc(self.get_tag(['phone'],month),verbose=verbose)
        details['grocery'] = self.calc(self.get_tag(['grocery'],month),verbose=verbose)
        details['gas'] = self.calc(self.get_tag(['gas'],month),verbose=verbose)
        details['car'] = self.calc(self.get_tag(['car'],month),verbose=verbose)
        details['onithotel'] = self.calc(self.get_tag(['onithotel'],month),verbose=verbose)
        details['travel'] = self.calc(self.get_tag(['travel'],month),verbose=verbose)
        details['priorities'] = self.calc(self.get_tag(['priorities'],month),verbose=verbose)
        details['savings'] = self.calc(self.get_tag(['savings'],month),verbose=verbose)
        details['loan'] = self.calc(self.get_tag(['loan'],month),verbose=verbose)
        details['business'] = self.calc(self.get_tag(['business'],month),verbose=verbose)
        details['contractor'] = self.calc(self.get_tag(['contractor'],month),verbose=verbose)
        details['training'] = self.calc(self.get_tag(['training'],month),verbose=verbose)
        details['supplies'] = self.calc(self.get_tag(['supplies'],month),verbose=verbose)
        details['software'] = self.calc(self.get_tag(['software'],month),verbose=verbose)
        details['personal'] = self.calc(self.get_tag(['personal'],month),verbose=verbose)
        details['food'] = self.calc(self.get_tag(['food'],month),verbose=verbose)
        details['planner'] = self.calc(self.get_tag(['planner'],month),verbose=verbose)
        details['other'] = self.calc(self.get_tag(['other',],month),verbose=verbose)
        return details
            
    def report(self, month=None):
        print "in report"
    	
    	details = report_numbers(month)
    	net = 0
    	print ""
        print "Income: ", details['income']
        net += details['income']
        print ""
        print "Essential: ", details['essential']
        net += details['essential']
        print "    Rent: ", details['rent']
        print "    Health: ", details['health']
        print "    Phone: ", details['phone']
        print "    Groceries: ", details['grocery']
        print "    Gas: ", details['gas']
        print "    Other Car: ", details['car']
        print "    Onit Travel: ", details['onithotel']
        print "    Travel: ", details['travel']
        print ""
        print "Priorities: ", details['priorities']
        net += details['priorities']
        print "    Savings: ", details['savings']
        print "    Loan: ", details['loan']
        print ""
        print "Business: ", details['business']
        net += details['business']
        print "    Contractors: ", details['contractor']
        print "    Training: ", details['training']
        print "    Supplies: ", details['supplies']
        print "    Software: ", details['software']
        print ""
        print "Personal: ", details['personal']
        net += details['personal']
        print "    Food: ", details['food']
        print "    Planners: ", details['planner']
        print "    Other: ", details['other']
        print ""
        print "NET: ", net
        total = details['personal'] + details['essential'] + details['business'] + details['priorities']
        print "Essential: ", details['essential']/total*100
        print "Business: ", details['business']/total*100
        print "Personal: ", details['personal']/total*100
        print "Priorities: ", details['priorities']/total*100
        print ""
        
                
    def get_tag(self,tag,month=None):
    	if month:
    		tag.append(month)
    	return tag
   
    def calc(self, tagname=None, verbose=True):
        total = 0
        for item in self.data:  
            if self.match(item,tagname):
                if verbose:
                    print item
                total = total + float(item[1])
        if verbose:
            print 'total: '+ str(total)
        return total
        
    def match(self, item, tagline=None):
        ''' returns True if tagline is None or if all items in tagline match the tags of item'''
        if tagline:
            for each in tagline:
                if each[0] == '#':
                    if each[1:] in item[2]:
                        return False
                else:
                    if each not in item[2]:
                        return False
        return True
        
        
    def year_report(self,month_num=1):
        budget = [self.bud['rent'],self.bud['health'],self.bud['phone'],self.bud['car'],self.bud['travel'],self.bud['priorities'],self.bud['business'],self.bud['personal']]
        details = self.report_numbers()
        print "Total Needed After Tax Income:", sum(budget)
        print "Current After Tax Income:", details['income']
        print "Needed After Tax Income:", sum(budget)-details['income']
        print ""
        print "Category\tYear Budget\tYear TD Budget\tYear TD Actual\tYear Extra\tYear Remaining"

        print "Rent\t\t "+str(budget[0])+"\t\t"+str(budget[0]/12.0*int(month_num))+"\t\t"+str(details['rent']*-1)+"\t\t"+str(budget[0]/12.0*int(month_num)-details['rent']*-1)+"\t\t"+str(budget[0]-details['rent']*-1)
        print "Health\t\t "+str(budget[1])+" \t\t"+str(budget[1]/12.0*int(month_num))+"\t\t"+str(details['health']*-1)+"\t\t"+str(budget[1]/12.0*int(month_num)-details['health']*-1)+"\t\t"+str(budget[1]-details['health']*-1)
        print "Phone\t\t "+str(budget[2])+" \t\t"+str(budget[2]/12.0*int(month_num))+"\t\t"+str(details['phone']*-1)+"\t\t"+str(budget[2]/12.0*int(month_num)-details['phone']*-1)+"\t\t"+str(budget[2]-details['phone']*-1)
        print "Car\t\t "+str(budget[3])+" \t\t"+str(budget[3]/12.0*int(month_num))+"\t\t"+str((details['car']+details['gas'])*-1)+"\t\t"+str(budget[3]/12.0*int(month_num)-(details['car']+details['gas'])*-1)+"\t\t"+str(budget[3]-(details['car']+details['gas'])*-1)
        print "Travel\t\t "+str(budget[4])+" \t\t"+str(budget[4]/12.0*int(month_num))+"\t\t"+str((details['travel']+details['onithotel'])*-1)+"\t\t"+str(budget[4]/12.0*int(month_num)-(details['travel']+details['onithotel'])*-1)+"\t\t"+str(budget[4]-(details['travel']+details['onithotel'])*-1)
        print "Priorities\t "+str(budget[5])+" \t\t"+str(budget[5]/12.0*int(month_num))+"\t\t"+str(details['priorities']*-1)+"\t\t"+str(budget[5]/12.0*int(month_num)-details['priorities']*-1)+"\t\t"+str(budget[5]-details['priorities']*-1)
        print "Business\t "+str(budget[6])+" \t\t"+str(budget[6]/12.0*int(month_num))+"\t\t"+str(details['business']*-1)+"\t\t"+str(budget[6]/12.0*int(month_num)-details['business']*-1)+"\t\t"+str(budget[6]-details['business']*-1)
        print "Personal\t "+str(budget[7])+" \t\t"+str(budget[7]/12.0*int(month_num))+"\t\t"+str((details['personal']+details['grocery'])*-1)+"\t\t"+str(budget[7]/12.0*int(month_num)-(details['personal']+details['grocery'])*-1)+"\t\t"+str(budget[7]-(details['personal']+details['grocery'])*-1)

        total = details['personal'] + details['essential'] + details['business'] + details['priorities']
        #TOTAL
        print "TOTAL\t\t"+str(sum(budget))+"\t\t"+str(sum(budget)/12.0*int(month_num))+"\t\t"+str(total*-1)+"\t\t"+str(sum(budget)/12.0*int(month_num)-total*-1)+"\t\t"+str(sum(budget)-total*-1)
            
if __name__ == "__main__":
    t = Total('accounting15.taskpaper')
    t.run()
