class Learning :

	def __init__(self,name) :
		self.name = name
		self.stack = []
	
	def addStacks(self,topic) :
		self.stack.append(topic)
	
	def setMentororLearner(self,typ) :
		self.typ = typ
		
	def setAvailableTime(self,availableStart,availableEnd) :
		self.available = [(int(availableStart[:2]),int(availableStart[2:4]),availableStart[4:]),(int(availableEnd[:2]),int(availableEnd[2:4]),availableEnd[4:])]
	
	def getMentor(self,stack,users,time) : 
		mentor = []
		h = int(time[:2])
		m = int(time[2:4])
		for user in users :
			if user.typ == 1 :
				for topic in stack :
					if topic in user.stack :
						if time[4:] == user.available[0][2] == user.available[1][2] :
							if (h > user.available[0][0] and h < user.available[1][0]) or (h == user.available[0][0] and m >= user.available[0][1] and (h < user.available[1][0] or m < user.available[1][1])) or (h == user.available[1][0] and m < user.available[1][1] and (h >= user.available[0][1] or m >= user.available[0][1])) :
								mentor.append((user.name,topic))
						elif user.available[0][2] != user.available[1][2] :
							if (h < user.available[1][0] and time[4:] == user.available[1][2]) or (h == user.available[1][0] and m < user.available[1][1] and time[4:] == user.available[1][2]) or (h > user.available[0][0] and time[4:] == user.available[0][2]) or (h == user.available[0][0] and m > user.available[0][1] and time[4:] == user.available[0][2]) :
								mentor.append((user.name,topic))
		return mentor

u1 = Learning("Ajay")
u1.addStacks("Python")
u1.setMentororLearner(1)
u1.setAvailableTime("0700AM","0830AM")

u2 = Learning("Rahul")
u2.addStacks("Python")
u2.addStacks("Java")
u2.setMentororLearner(0)

u3 = Learning("Ranjith")
u3.addStacks("Java")
u3.setMentororLearner(1)
u3.setAvailableTime("0630AM","1000AM")

users = [u1,u2,u3]

mentors = u2.getMentor(u2.stack,users,"0800AM")
if mentors == [] :
	print("No available mentors")
else :
	print("Available Mentors : ")
	for m in mentors :
		print("Mentor",m[0],"who teaches",m[1])
